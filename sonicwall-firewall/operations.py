"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

import time
import json
from collections import OrderedDict
from requests.auth import HTTPBasicAuth
import requests
from connectors.core.connector import get_logger, ConnectorError
from requests.auth import HTTPDigestAuth
from .constants import ADDRESS_OBJECT_MAP, HTTPstatusCodes

logger = get_logger('sonicwall-firewall')


class SonicWallFirewall(object):

    def __init__(self, config):
        self.server_url = config.get('server_url', '').strip('/')
        if not self.server_url.startswith(('https://', 'http://')):
            self.server_url = 'https://' + self.server_url
        self.port = config.get('port')
        if self.port:
            self.server_url = f'{self.server_url}:{str(self.port)}'
        if not self.server_url.endswith('/api/sonicos'):
            self.server_url = self.server_url + '/api/sonicos'
        self.verify_ssl = config.get('verify_ssl', False)
        self.username = config.get('username')
        self.password = config.get('password')
        self.session = requests.Session()
        self.headers = OrderedDict([
            ('Accept', 'application/json'),
            ('Content-Type', 'application/json'),
            ('Accept-Encoding', 'application/json'),
            ('Charset', 'UTF-8')
        ])
        self.login_user()

    def make_api_call(self, endpoint, method='POST', payload=None, params=None):
        service_endpoint = self.server_url + endpoint
        try:
            logger.debug(f'API Service Endpoint: {service_endpoint}')
            logger.debug(f'API Method: {payload}')
            logger.debug(f'API Payload: {payload}')
            response = self.session.request(
                method,
                service_endpoint,
                data=payload,
                params=params,
                headers=self.headers,
                verify=self.verify_ssl
            )

            logger.debug(f'API Response Status code: {response.status_code}')
            logger.debug(f'API Response: {response.text}')
            if response.ok:
                return response.json() if response.text else response.text
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
        """Authenticate and store session cookies"""
        try:
            payload = json.dumps({"override": True})
            api_endpoint = self.server_url + '/auth'
            #logger.info(f'API Endpoint: {api_endpoint}')
            resp = self.session.post(
                api_endpoint,
                data=payload,
                headers=self.headers,
                auth=HTTPDigestAuth(self.username, self.password),
                #auth=HTTPBasicAuth(self.username, self.password),
                verify=self.verify_ssl
            )
            if not resp.ok:
                raise ConnectorError(f"Login failed: {resp.text}")

            logger.debug("Login Response: {}".format(resp))

        except ConnectorError as err:
            logger.error(err)
            raise ConnectorError('Failed to login to SonicWall: {}'.format(err))

    def logout_user(self):
        endpoint = "/auth"
        resp = self.make_api_call(endpoint, method='DELETE')
        logger.debug("User successfully logout.")
        logger.debug("Logout Response: {}".format(resp))
        return resp

    def start_management(self):
        resp = None
        try:
            endpoint = "/start-management"
            logger.debug("Starting firewall management")
            resp = self.make_api_call(endpoint, method='POST')
            logger.debug("start_management resp: {}".format(resp))
            start_management_status = bool(resp and resp.get('status', {}).get('success', False))
            if not start_management_status:
                logger.debug("start_management resp: {}".format(resp))
            return start_management_status

        except Exception:
            logger.error("Failed to start management: {}".format(resp))
            return False

    def switch_config_mode(self):
        resp = None
        try:
            endpoint = "/config-mode"
            logger.debug("Starting firewall management")
            resp = self.make_api_call(endpoint, method='POST')
            logger.debug("switch_config_mode resp: {}".format(resp))
            config_mode_status = bool(resp and resp.get('status', {}).get('success', False))
            if not config_mode_status:
                logger.debug("switch_config_mode resp: {}".format(resp))
            return config_mode_status
        except Exception:
            logger.error("Failed to commit changes: {}".format(resp))
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
        raise ConnectorError("Unknown address object: {}".format(address_object))


def get_address_group_payload(params):
    object_type = params.get('object_type', '').lower()
    address_group_name = params.get('address_group_name')
    address_object_name = params.get('address_object_name')
    payload = {
        "address_groups": [
            {
                f"{object_type}": {
                    "name": address_group_name,
                    "address_object": {
                        f"{object_type}": [
                            {
                                "name": address_object_name
                            }
                        ]
                    }
                }
            }
        ]
    }
    return payload

def start_firewall_management(client):
    retry_limit = 3
    while retry_limit > 0:
        is_successfully_start = client.start_management()
        if is_successfully_start:
            return is_successfully_start
        else:
            logger.error("Starting firewall management failed. Trying again in 5 secs!")
            retry_limit -= 1
            time.sleep(5)
    raise ConnectorError('Failed to start firewall management')


def change_config_mode(client):
    retry_limit = 3
    while retry_limit > 0:
        config_mode_status = client.switch_config_mode()
        if config_mode_status:
            return config_mode_status
        else:
            logger.error("Changing to Config Mode failed. Trying again in 5 secs!")
            retry_limit -= 1
            time.sleep(5)
    raise ConnectorError('Failed to change Config Mode')


def commit_changes(client):
    endpoint = "/config/pending"
    resp = client.make_api_call(endpoint, method='POST')
    status = resp.get('status', {}).get('success')
    commit_status = bool(resp and resp.get('status', {}).get('success', False))
    if commit_status:
        if resp.get('status', {}).get('info'):
            message = resp.get('status', {}).get('info')[0].get('message')
            logger.info("All changes successfully committed")
            logger.debug(f"{message}: {status}")
        return commit_status
    else:
        logger.error("Failed to commit changes, Resp: {}".format(resp))
        raise ConnectorError("failed to commit changes")


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


def get_address_object_configuration(client, params):
    endpoint = get_endpoint(params)
    return client.make_api_call(endpoint, method='GET')


def create_address_object_configuration(client, params):
    if not start_firewall_management(client):
        raise ConnectorError('Failed to start firewall management')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")
    payload = get_payload(params)
    object_type = params.get('object_type', '').lower()
    endpoint = f'/address-objects/{object_type}'
    payload = json.dumps(payload)
    resp = client.make_api_call(endpoint, method='POST', payload=payload)
    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")
    return resp


def create_address_group_object_configuration(client, params):
    if not start_firewall_management(client):
        raise ConnectorError('Failed to start firewall management')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")
    payload = get_address_group_payload(params)
    payload = json.dumps(payload)
    object_type = params.get('object_type', '').lower()
    endpoint = f'/address-groups/{object_type}'
    resp = client.make_api_call(endpoint, method='POST', payload=payload)
    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")
    return resp


def update_address_object_configuration(client, params):
    if not start_firewall_management(client):
        raise ConnectorError('Failed to start firewall management')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")
    endpoint = get_endpoint(params)
    payload = get_payload(params)
    resp = client.make_api_call(endpoint, method='PATCH', payload=payload)
    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")
    return resp


def delete_address_object_configuration(client, params):
    if not start_firewall_management(client):
        raise ConnectorError('Failed to start firewall management')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")

    endpoint = get_endpoint(params)
    resp = client.make_api_call(endpoint, method='DELETE')
    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")
    return resp


operations = {
    'get_address_object_configuration': get_address_object_configuration,
    'create_address_object_configuration': create_address_object_configuration,
    'create_address_group_object_configuration': create_address_group_object_configuration,
    'update_address_object_configuration': update_address_object_configuration,
    'delete_address_object_configuration': delete_address_object_configuration
}
