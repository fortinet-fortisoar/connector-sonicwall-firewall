"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

import time
import json
from requests.auth import HTTPBasicAuth
import requests
from connectors.core.connector import get_logger, ConnectorError
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
        self.session.auth = HTTPBasicAuth(self.username, self.password)
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.login_user()

    def make_api_call(self, endpoint, method='POST', payload=None, params=None):
        service_endpoint = self.server_url + endpoint
        try:
            logger.debug(f'API Service Endpoint: {service_endpoint}')
            logger.debug(f'API Method: {method}')
            logger.debug(f'API Payload: {payload}')
            logger.debug(f'Session Auth: {self.session.auth}')
            logger.debug(f'Session Headers: {self.session.headers}')
            response = self.session.request(
                method,
                service_endpoint,
                data=payload,
                params=params,
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
        # Authentication based on "RFC-2617 HTTP Basic Authentication"
        # This authentication method needs to be enabled on the firewall
        # The respective interface associated to the IP address also needs to have HTTPS user access enabled
        try:
            api_endpoint = self.server_url + '/auth'

            resp = self.session.post(
                api_endpoint,
                verify=self.verify_ssl
            )

            if not resp.ok:
                raise ConnectorError(f"Login failed: {resp.status_code} {resp.text}")

            logger.debug("Login successful. Cookies: {}".format(self.session.cookies.get_dict()))

        except Exception as err:
            logger.error(err)
            raise ConnectorError('Failed to login to SonicWall: {}'.format(err))

    def logout_user(self):
        endpoint = "/auth"
        resp = self.make_api_call(endpoint, method='DELETE')
        logger.debug("User successfully logout.")
        logger.debug("Logout Response: {}".format(resp))
        return resp

    def start_management(self):
        # This is a required step
        resp = None
        try:
            endpoint = "/start-management"
            logger.debug("Starting management session")
            resp = self.make_api_call(endpoint, method='POST')
            start_management_status = bool(resp and resp.get('status', {}).get('success', False))
            if not start_management_status:
                logger.debug("Starting management session response: {}".format(resp))
            return start_management_status
        except Exception:
            logger.error("Failed to start management session: {}".format(resp))
            return False

    def switch_config_mode(self):
        # This is required to be able to make changes on the firewall
        resp = None
        try:
            endpoint = "/config-mode"
            logger.debug("Switching to config mode")
            resp = self.make_api_call(endpoint, method='POST')
            logger.debug("switch_config_mode resp: {}".format(resp))
            config_mode_status = bool(resp and resp.get('status', {}).get('success', False))
            if not config_mode_status:
                logger.debug("switch_config_mode resp: {}".format(resp))
            return config_mode_status
        except Exception as err:
            logger.error(err)
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


def start_firewall_management_session(client):
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
    """
           Commits pending all pending (unsaved) configuration changes to SonicWall.
           Required after POST/PUT/DELETE operations.
           """
    endpoint = "/config/pending"
    resp = client.make_api_call(endpoint, method='POST')
    status = resp.get('status', {}).get('success')
    logger.info('Commiting changes to SonicWall: {}'.format(resp))
    commit_status = bool(resp and resp.get('status', {}).get('success', False))
    if commit_status:
        if resp.get('status', {}).get('info'):
            message = resp.get('status', {}).get('info')[0].get('message')
            logger.info("All pending (unsaved) configuration changes successfully committed")
            logger.debug(f"{message}: {status}")
        return commit_status
    else:
        error_message = "Failed to commit all pending (unsaved) configuration changes to SonicWall, Resp: {}".format(
            resp)
        logger.error(error_message)
        raise ConnectorError(error_message)


def get_endpoint(params, endpoint_path):
    object_type = params.get('object_type', '').lower()
    endpoint = f'/{endpoint_path}/{object_type}'
    name = params.get('name')
    uuid = params.get('uuid')
    if uuid:
        endpoint = f'{endpoint}/uuid/{uuid}'
    elif name:
        endpoint = f'{endpoint}/name/{name}'
    return endpoint


def get_address_object_configuration(client, params):
    """Retrieves one or all address objects."""
    endpoint = get_endpoint(params, endpoint_path='address-objects')
    if not start_firewall_management_session(client):
        raise ConnectorError('Failed to start firewall management session')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")
    return client.make_api_call(endpoint, method='GET')


def create_address_object_configuration(client, params):
    # Create a new IPv4 address object.
    # Rest API endpoint: https://sonicos-api.sonicwall.com/#/address-object-ipv4/post_address_objects_ipv4

    if not start_firewall_management_session(client):
        raise ConnectorError('Failed to start firewall management session')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")
    payload = get_payload(params)
    object_type = params.get('object_type', '').lower()
    endpoint = f'/address-objects/{object_type}'
    resp = client.make_api_call(endpoint, method='POST', payload= json.dumps(payload))
    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")
    return resp


def update_address_object_configuration(client, params):
    if not start_firewall_management_session(client):
        raise ConnectorError('Failed to start firewall management session')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")
    endpoint = get_endpoint(params, endpoint_path='address-objects')
    payload = get_payload(params)
    update_type = params.get('update_type', '')
    method = 'PATCH' if update_type == 'Partial Update' else 'PUT'
    resp = client.make_api_call(endpoint, method=method, payload=json.dumps(payload))
    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")
    return resp


def delete_address_object_configuration(client, params):
    if not start_firewall_management_session(client):
        raise ConnectorError('Failed to start firewall management session')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")

    endpoint = get_endpoint(params, endpoint_path='address-objects')
    resp = client.make_api_call(endpoint, method='DELETE')
    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")
    return resp


def get_address_group(client, params):
    """Retrieves one or all address groups."""
    logger.info("Invoking get_address_group action")
    endpoint = get_endpoint(params, endpoint_path='address-groups')
    if not start_firewall_management_session(client):
        raise ConnectorError('Failed to start firewall management session')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")
    return client.make_api_call(endpoint, method='GET')


def create_address_group(client, params):
    logger.info("Invoking create_address_group action")
    if not start_firewall_management_session(client):
        raise ConnectorError('Failed to start firewall management session')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")
    payload = get_address_group_payload(params)
    object_type = params.get('object_type', '').lower()
    endpoint = f'/address-groups/{object_type}'
    resp = client.make_api_call(endpoint, method='POST', payload=json.dumps(payload))
    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")
    return resp


def update_address_group(client, params):
    logger.info("Invoking update_address_group action")
    if not start_firewall_management_session(client):
        raise ConnectorError('Failed to start firewall management session')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")
    update_type = params.get('update_type', '')
    method = 'PATCH' if update_type == 'Partial Update' else 'PUT'
    endpoint = get_endpoint(params, endpoint_path='address-groups')
    payload = get_address_group_payload(params)
    resp = client.make_api_call(endpoint, method=method, payload=json.dumps(payload))
    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")
    return resp


def delete_address_group(client, params):
    logger.info("Invoking delete_address_group action")
    if not start_firewall_management_session(client):
        raise ConnectorError('Failed to start firewall management session')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")

    endpoint = get_endpoint(params, endpoint_path='address-objects')
    resp = client.make_api_call(endpoint, method='DELETE')
    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")
    return resp


def add_address_object_to_group(client, params):
    """Adds an existing address object to an address group."""
    logger.info("Invoking add_address_object_to_group action")
    if not start_firewall_management_session(client):
        raise ConnectorError('Failed to start firewall management session')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")
    object_name = params.get('address_object_name')
    object_type = params.get('object_type', '').lower()
    group_name = params.get('name')
    # First, get the current group to preserve existing members
    endpoint = get_endpoint(params, endpoint_path='address-groups')
    current_group_resp = client.make_api_call(endpoint, method='GET')
    # Parse current members
    existing_members = []
    try:
        groups = current_group_resp.get('address_groups', [])
        if groups:
            existing_members = groups[0].get(object_type, {}).get('address_object', {}).get(object_type, [])
            if not isinstance(existing_members, list):
                existing_members = [existing_members] if existing_members else []
    except (KeyError, IndexError, TypeError):
        existing_members = []

    # Check if member already exists
    member_names = [m.get('name') for m in existing_members]
    if object_name in member_names:
        return {
            "status": "skipped",
            "message": f"Address object '{object_name}' is already a member of group '{group_name}'."
        }

    # Add new member
    existing_members.append({"name": object_name})

    payload = {
        "address_groups": [{
            f"{object_type}": {
                "name": group_name,
                "address_object": {
                    f"{object_type}": existing_members
                }
            }
        }]
    }
    endpoint = f'/address-groups/{object_type}/name/{group_name}'
    current_group_resp = client.make_api_call(endpoint, method='PUT', payload=json.dumps(payload))
    logger.info(f"Address object '{object_name}' added to group '{group_name}'.")
    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")
    return {
        "status": "success",
        "message": f"Address object '{object_name}' added to group '{group_name}' successfully.",
        "data": current_group_resp
    }


def remove_address_object_from_group(client, params):
    """Removes an address object from an address group."""
    logger.info("Invoking remove_address_object_from_group action")
    if not start_firewall_management_session(client):
        raise ConnectorError('Failed to start firewall management session')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")
    object_name = params.get('address_object_name')
    object_type = params.get('object_type', '').lower()
    group_name = params.get('name')
    # First, get the current group to preserve existing members
    endpoint = get_endpoint(params, endpoint_path='address-groups')
    current_group_resp = client.make_api_call(endpoint, method='GET')
    existing_members = []
    try:
        groups = current_group_resp.get('address_groups', [])
        if groups:
            existing_members = groups[0].get(f'{object_type}', {}).get('address_object', {}).get(f'{object_type}', [])
            if not isinstance(existing_members, list):
                existing_members = [existing_members] if existing_members else []
    except (KeyError, IndexError, TypeError):
        existing_members = []

    # Filter out the target object
    updated_members = [m for m in existing_members if m.get('name') != object_name]

    if len(updated_members) == len(existing_members):
        return {
            "status": "skipped",
            "message": f"Address object '{object_name}' was not found in group '{group_name}'."
        }

    payload = {
        "address_groups": [{
            f"{object_type}": {
                "name": group_name,
                "address_object": {
                    f"{object_type}": updated_members
                }
            }
        }]
    }

    endpoint = f'/address-groups/{object_type}/name/{group_name}'
    current_group_resp = client.make_api_call(endpoint, method='PUT', payload=json.dumps(payload))
    logger.info(f"Address object '{object_name}' removed from group '{group_name}'.")
    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")
    return {
        "status": "success",
        "message": f"Address object '{object_name}' removed from group '{group_name}' successfully.",
        "data": current_group_resp
    }


operations = {
    'get_address_object_configuration': get_address_object_configuration,
    'create_address_object_configuration': create_address_object_configuration,
    'update_address_object_configuration': update_address_object_configuration,
    'delete_address_object_configuration': delete_address_object_configuration,
    'get_address_group': get_address_group,
    'create_address_group': create_address_group,
    'update_address_group': update_address_group,
    'delete_address_group': delete_address_group,
    'add_address_object_to_group': add_address_object_to_group,
    'remove_address_object_from_group': remove_address_object_from_group,
}
