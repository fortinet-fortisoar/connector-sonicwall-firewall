"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import time
from collections import OrderedDict
import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import ADDRESS_OBJECT_MAP, HTTPstatusCodes

logger = get_logger('sonicwall-firewall')


class SonicWallFirewall(object):

    def __init__(self, config):
        self.server_url = config.get('server_url', '').strip('/')
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = 'https://' + self.server_url
        self.port = config.get('port')
        if self.port:
            self.server_url = f'{self.server_url}:{str(self.port)}'
        self.server_url = self.server_url + '/api/sonicos'
        self.verify_ssl = config.get('verify_ssl', False)
        self.basic_auth = (config.get('username'), config.get('password'))
        self.username = config.get('username')
        self.headers = OrderedDict([
            ('Accept', 'application/json'),
            ('Content-Type', 'application/json'),
            ('Accept-Encoding', 'application/json'),
            ('Charset', 'UTF-8')])
        self.login_user()

    def make_api_call(self, endpoint, method='POST', payload=None, params=None):
        service_endpoint = self.server_url + endpoint
        try:
            response = requests.request(method, service_endpoint, auth=self.basic_auth, json=payload,
                                        headers=self.headers, params=params,
                                        verify=self.verify_ssl)
            logger.debug('API Service Endpoint: {0}'.format(service_endpoint))
            logger.debug('API Payload: {0}'.format(payload))
            logger.debug('API Response Status code: {0}'.format(response.status_code))
            logger.debug('API Response: {0}'.format(response.text))
            if response.ok:
                return response.json()
            else:
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code),
                     '{}'.format(HTTPstatusCodes.get(response.status_code, response.status_code)): '{}'.format(
                         response.text)})
        except requests.exceptions.SSLError as err:
            logger.error(err)
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout as err:
            logger.error(err)
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout as err:
            logger.error(err)
            raise ConnectorError('The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError as err:
            logger.error(err)
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            logger.error(err)
            raise ConnectorError(str(err))

    def login_user(self):
        resp = self.make_api_call('/auth', method='POST')
        logger.debug("User successfully login.")
        logger.debug("Login Response: {}".format(resp))

    def logout_user(self):
        endpoint = "/user/session/name/" + self.username
        resp = self.make_api_call(endpoint, method='DELETE')
        logger.debug("User successfully logout.")
        logger.debug("Logout Response: {}".format(resp))

    def start_management(self):
        try:
            endpoint = "/start-management"
            logger.debug("Starting firewall management")
            resp = self.make_api_call(endpoint, method='POST')
            logger.debug("start_management resp: {}".format(resp))
            return True
        except Exception:
            return False

    def switch_config_mode(self):
        try:
            endpoint = "/config-mode"
            logger.debug("Starting firewall management")
            resp = self.make_api_call(endpoint, method='POST')
            logger.debug("switch_config_mode resp: {}".format(resp))
            return True
        except Exception:
            return False


def get_payload(params):
    object_type = params.get('object_type', '')
    address_object = params.get('address_object', '')
    address_object = ADDRESS_OBJECT_MAP.get(address_object, '') or ADDRESS_OBJECT_MAP.get(object_type, '')
    name = params.get('name')
    zone = params.get('zone')
    object_type = object_type.lower()
    if address_object == "host":
        ip_address = params.get('ip_address')
        payload = {
            "address_objects": [
                {
                    f"{object_type}": {
                        "name": name,
                        "zone": zone,
                        "host": {
                            "ip": ip_address
                        }
                    }
                }
            ]
        }
        return payload
    elif address_object == "range":
        start_ip_range = params.get('begin')
        end_ip_range = params.get('end')
        payload = {
            "address_objects": [
                {
                    f"{object_type}": {
                        "name": name,
                        "zone": zone,
                        "range": {
                            "begin": start_ip_range,
                            "end": end_ip_range
                        }
                    }
                }
            ]
        }
        return payload
    elif address_object == "network":
        subnet = params.get('subnet')
        mask = params.get('mask')
        payload = {
            "address_objects": [
                {
                    f"{object_type}": {
                        "name": name,
                        "zone": zone,
                        "network": {
                            "subnet": subnet,
                            "mask": mask
                        }
                    }
                }
            ]
        }
        return payload
    elif address_object == "fqdn":
        domain = params.get('domain')
        payload = {
            "address_objects": [
                {
                    "fqdn": {
                        "name": name,
                        "domain": domain,
                        "zone": zone
                    }
                }
            ]
        }
        return payload
    else:
        logger.error("Invalid Object type")


def start_firewall_management(client):
    retry_limit = 3
    while retry_limit > 0:
        is_successfully_start = client.start_management()
        if not is_successfully_start:
            logger.error("Starting firewall management failed. Trying again in 5 secs!")
            retry_limit -= 1
            time.sleep(5)
        else:
            retry_limit = 0
    logger.debug("Starting firewall management")


def change_confi_mode(client):
    retry_limit = 3
    while retry_limit > 0:
        config_mode_status = client.switch_config_mode()
        if not config_mode_status:
            logger.error("Changing to Config Mode failed. Trying again in 5 secs!")
            retry_limit -= 1
            time.sleep(5)
        else:
            retry_limit = 0
    logger.debug("Changing to Config Mode")


def commit_changes(client):
    endpoint = "/config/pending"
    resp = client.make_api_call(endpoint, method='POST')
    status = resp.get('status', {}).get('success')
    if resp.get('status', {}).get('info'):
        message = resp.get('status', {}).get('info')[0].get('message')
        logger.info("All changes successfully committed")
        logger.error(f"{status}: {message}")
    else:
        logger.error("failed to commit changes")


def get_endpoint(params):
    object_type = params.get('object_type', '').lower()
    endpoint = f'/address-objects/{object_type}'
    name = params.get('name')
    uuid = params.get('uuid')
    if uuid:
        endpoint = f'{endpoint}/uuid/{uuid}'
    elif name:
        endpoint = f'{endpoint}/name/{name}'
    return endpoint


def get_address_object_configuration(config, params):
    client = SonicWallFirewall(config)
    endpoint = get_endpoint(params)
    return client.make_api_call(endpoint, method='GET')


def create_address_object_configuration(config, params):
    client = SonicWallFirewall(config)
    start_firewall_management(client)
    change_confi_mode(client)
    payload = get_payload(params)
    object_type = params.get('object_type', '').lower()
    endpoint = f'/address-objects/{object_type}'
    resp = client.make_api_call(endpoint, method='POST', payload=payload)
    commit_changes(client)
    client.logout_user()
    return resp


def update_address_object_configuration(config, params):
    client = SonicWallFirewall(config)
    start_firewall_management(client)
    change_confi_mode(client)
    endpoint = get_endpoint(params)
    payload = get_payload(params)
    resp = client.make_api_call(endpoint, method='PATCH', payload=payload)
    commit_changes(client)
    client.logout_user()
    return resp


def delete_address_object_configuration(config, params):
    client = SonicWallFirewall(config)
    start_firewall_management(client)
    change_confi_mode(client)
    endpoint = get_endpoint(params)
    resp = client.make_api_call(endpoint, method='DELETE')
    commit_changes(client)
    client.logout_user()
    return resp


def _check_health(config):
    client = SonicWallFirewall(config)
    client.logout_user()


operations = {
    'get_address_object_configuration': get_address_object_configuration,
    'create_address_object_configuration': create_address_object_configuration,
    'update_address_object_configuration': update_address_object_configuration,
    'delete_address_object_configuration': delete_address_object_configuration
}
