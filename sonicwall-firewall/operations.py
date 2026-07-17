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
    endpoint = endpoint_path
    if object_type:
        endpoint = f'/{endpoint}/{object_type}'
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
    resp = client.make_api_call(endpoint, method='POST', payload=json.dumps(payload))
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
    endpoint = get_endpoint(params, endpoint_path='address-groups')
    if not start_firewall_management_session(client):
        raise ConnectorError('Failed to start firewall management session')

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")
    return client.make_api_call(endpoint, method='GET')


def create_address_group(client, params):
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


def _build_uri_list_object_body(params, outer_key=None, inner_key=None):
    raw_payload = params.pop("raw_payload", None)
    if raw_payload:
        return raw_payload
    entry_type = params.pop("entry_type", "domain").lower()
    params['type'] = entry_type
    entries = params.pop("entries", [])
    entries = _convert_str_to_list(entries)
    params[entry_type] = [{entry_type: entry.strip()} for entry in _convert_str_to_list(entries)]
    payload = {outer_key: {inner_key: [params]}}
    return payload


def _get_uri_object_data(client, params):
    if not start_firewall_management_session(client):
        raise ConnectorError("Failed to start firewall management session")

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")

    entry_type = params.get("entry_type", "").lower()
    entries = params.get("entries") or []
    entries = _convert_str_to_list(entries)
    endpoint = get_endpoint(params, endpoint_path="/content-filter/uri-list-objects")
    uri_object = client.make_api_call(endpoint, method="GET")
    uri_list = uri_object.get("content_filter", {}).get("uri_list_object", [{}])
    uri_data = uri_list[0] if uri_list else {}
    return endpoint, uri_object, uri_data, entry_type, entries


def add_entries_to_uri_object_list(client, params):
    """Adding entries into provided uri object and entry type."""
    endpoint, uri_object, uri_data, entry_type, entries = _get_uri_object_data(client, params)
    existing_members = uri_data.get(entry_type, [])

    # Get existing entries from the URI object
    existing_entries = {member.get(entry_type) for member in existing_members if isinstance(member, dict)}

    # If the entry is not present in the existing_members list, add it.
    existing_members.extend({entry_type: entry} for entry in entries if entry not in existing_entries)

    uri_data[entry_type] = existing_members
    resp = client.make_api_call(endpoint, method="PUT", payload=json.dumps(uri_object))
    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")
    return resp


def remove_entries_from_uri_object_list(client, params):
    """Removing entries from provided uri object and entry type."""
    endpoint, uri_object, uri_data, entry_type, entries = _get_uri_object_data(client, params)
    entries_to_remove = set(entries)
    # removed entries from existing uri object
    uri_data[entry_type] = [member for member in uri_data.get(entry_type, []) if
                            member.get(entry_type) not in entries_to_remove]
    return client.make_api_call(endpoint, method="PUT", payload=json.dumps(uri_object))


def _convert_str_to_list(members):
    if members and isinstance(members, str):
        members = members.replace("\n", ",")
        return [member.strip() for member in members.split(",") if member.strip()]
    return members or []


def _build_uri_list_group_body(params):
    raw_payload = params.get("raw_payload")
    if raw_payload:
        return raw_payload
    object_members = _convert_str_to_list(params.get("object_members"))
    group_members = _convert_str_to_list(params.get("group_members"))
    payload = {"content_filter": {"uri_list_group": [{"name": params.get("name"), **(
        {"uri_list_object": [{"name": m} for m in object_members]} if object_members else {}), **(
        {"uri_list_group": [{"name": m} for m in group_members]} if group_members else {}), }]}}
    return payload


def _update_members(existing_members, members, add=True):
    """Adding or removing members from provided existing_members."""
    if add:
        existing_names = {member.get("name") for member in existing_members if isinstance(member, dict)}
        existing_members.extend({"name": member} for member in members if member not in existing_names)
        return existing_members

    members_to_remove = set(members)
    return [member for member in existing_members if member.get("name") not in members_to_remove]


def _build_cfs_profile_body(params):
    profile_name = params.get("name")
    allowed_list = _convert_str_to_list(params.get("allowed_uri_list")) or []
    forbidden_list = _convert_str_to_list(params.get("forbidden_uri_list")) or []
    additional_json = params.get("settings") or {}

    profile = {
        "name": profile_name,
        "uri_list": {
            "allowed": [{"name": item} for item in allowed_list],
            "forbidden": [{"name": item} for item in forbidden_list],
        },
    }
    if isinstance(additional_json, dict):
        profile.update(additional_json)

    return {
        "content_filter": {
            "profile": [profile]
        }
    }


def _cfs_profile_request(client, params, method, endpoint):
    """Execute a CFS profile API request."""
    if not start_firewall_management_session(client):
        raise ConnectorError("Failed to start firewall management session")

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")

    payload = _build_cfs_profile_body(params)

    resp = client.make_api_call(
        endpoint,
        method=method,
        payload=json.dumps(payload)
    )

    if not commit_changes(client):
        raise ConnectorError("Failed to commit changes")

    return resp


def create_cfs_profile(client, params):
    """Create a new content filter profile."""
    return _cfs_profile_request(client=client, params=params, method="POST", endpoint="/content-filter/profiles")


def update_cfs_profile(client, params):
    """Patch a content filter profile configuration."""
    return _cfs_profile_request(client=client, params=params, method="PATCH",
                                endpoint=get_endpoint(params, endpoint_path="/content-filter/profiles"))


def _execute_get_delete_request(client, params, endpoint_path, method, commit=False):
    """Execute a Content Filter API request."""
    if not start_firewall_management_session(client):
        raise ConnectorError("Failed to start firewall management session")

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")

    endpoint = get_endpoint(params, endpoint_path=endpoint_path)
    resp = client.make_api_call(endpoint, method=method)
    if commit:
        if not commit_changes(client):
            raise ConnectorError("Failed to commit changes")

    return resp


def get_uri_object_list(client, params):
    """Retrieve one or all URI list objects."""
    return _execute_get_delete_request(client, params, "/content-filter/uri-list-objects", "GET")


def delete_uri_object_list(client, params):
    """Deleting the provided uri object."""
    return _execute_get_delete_request(client, params, "/content-filter/uri-list-objects", "DELETE", commit=True)


def get_uri_list_group(client, params):
    """Retrieve content filter URI list group object configuration"""
    return _execute_get_delete_request(client, params, "/content-filter/uri-list-groups", "GET")


def delete_uri_list_group(client, params):
    """Deleting the provided uri object."""
    return _execute_get_delete_request(client, params, "/content-filter/uri-list-groups", method='DELETE', commit=True)


def get_cfs_action(client, params):
    """Retrieve content filter action object configuration"""
    return _execute_get_delete_request(client, params, "/content-filter/actions", "GET")


def delete_cfs_action(client, params):
    """Delete a content filter action object"""
    return _execute_get_delete_request(client, params, "/content-filter/actions", "DELETE", commit=True)


def get_cfs_profile(client, params):
    """Retrieve content filter profile object configuration"""
    return _execute_get_delete_request(client, params, "/content-filter/profiles", "GET")


def delete_cfs_profile(client, params):
    """Delete a content filter profile object"""
    return _execute_get_delete_request(client, params, "/content-filter/profiles", "DELETE", commit=True)


def _execute_request(client, endpoint, method, payload=None, commit=False):
    """Execute a Content Filter API request."""
    if not start_firewall_management_session(client):
        raise ConnectorError("Failed to start firewall management session")

    if not change_config_mode(client):
        raise ConnectorError("Failed to switch config mode")

    resp = client.make_api_call(
        endpoint,
        method=method,
        payload=json.dumps(payload) if payload is not None else None,
    )
    if commit and not commit_changes(client):
        raise ConnectorError("Failed to commit changes")

    return resp


def _build_content_filter_action_payload(params):
    """Build payload for Content Filter Action APIs."""
    settings = params.get("settings")
    if isinstance(settings, dict):
        return {"content_filter": {"action": [{"name": params.get("name"), **settings}]}}
    if isinstance(settings, list):
        return {"content_filter": {"action": settings}}
    return {}


def create_uri_object_list(client, params):
    """Create a new content filter URI list object"""
    return _execute_request(
        client=client,
        endpoint="/content-filter/uri-list-objects",
        method="POST",
        payload=_build_uri_list_object_body(params, "content_filter", inner_key='uri_list_object'),
        commit=True
    )


def create_uri_group(client, params):
    """Create a new content filter URI list group object"""
    return _execute_request(
        client=client,
        endpoint="/content-filter/uri-list-groups",
        method="POST",
        payload=_build_uri_list_group_body(params),
        commit=True
    )


def _build_update_uri_list_group_payload(client, endpoint, params):
    """Build payload for Content Filter Update URIList Group APIs."""
    payload = params.get("raw_payload")
    if not payload:
        uri_group = _execute_request(
            client=client,
            endpoint=endpoint,
            method="GET"

        )
        content_filter = uri_group.get("content_filter", {})
        add = params.get("action") == "Add Entries to Group List"
        object_members = (_convert_str_to_list(params.get("object_members")) or [])
        group_members = (_convert_str_to_list(params.get("group_members")) or [])
        if content_filter and content_filter.get("uri_list_group", []):
            list_object = content_filter["uri_list_group"][0]
            list_object['uri_list_object'] = _update_members(list_object['uri_list_object'], object_members, add)
        if content_filter and content_filter["uri_list_group"]:
            list_group = content_filter["uri_list_group"][0]
            list_group['uri_list_group'] = _update_members(list_group['uri_list_group'], group_members, add)
        payload = {"content_filter": content_filter}
    return payload


def update_uri_list_group(client, params):
    """Update content filter URI list group object configuration."""
    endpoint = get_endpoint(params, endpoint_path="/content-filter/uri-list-groups")
    return _execute_request(
        client=client,
        endpoint=endpoint,
        method="PUT",
        payload=_build_update_uri_list_group_payload(client, endpoint, params),
        commit=True
    )


def create_cfs_action(client, params):
    """Create a new content filter action object"""
    return _execute_request(
        client=client,
        endpoint="/content-filter/actions",
        method="POST",
        payload=_build_content_filter_action_payload(params),
        commit=True
    )


def update_cfs_action(client, params):
    """Patch content filter action object configuration"""
    return _execute_request(
        client=client,
        endpoint=get_endpoint(params, endpoint_path="/content-filter/actions"),
        method="PATCH",
        payload=_build_content_filter_action_payload(params),
        commit=True
    )


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
    # URL Related operations
    'create_uri_object_list': create_uri_object_list,
    'get_uri_object_list': get_uri_object_list,
    'add_entries_to_uri_object_list': add_entries_to_uri_object_list,
    'remove_entries_from_uri_object_list': remove_entries_from_uri_object_list,
    'delete_uri_object_list': delete_uri_object_list,
    'create_uri_group': create_uri_group,
    'get_uri_list_group': get_uri_list_group,
    'update_uri_list_group': update_uri_list_group,
    'delete_uri_list_group': delete_uri_list_group,
    'create_cfs_action': create_cfs_action,
    'get_cfs_action': get_cfs_action,
    'update_cfs_action': update_cfs_action,
    'delete_cfs_action': delete_cfs_action,
    'create_cfs_profile': create_cfs_profile,
    'get_cfs_profile': get_cfs_profile,
    'update_cfs_profile': update_cfs_profile,
    'delete_cfs_profile': delete_cfs_profile
}
