## About the connector

SonicWall firewall appliances provide advanced network and security services. The SonicWall Firewall connector facilitates communication and data exchange between a SonicWall firewall and other network elements, providing enhanced security, management, and monitoring capabilities.

This document provides information about the SonicWall Firewall connector, which facilitates automated interactions with a SonicWall Firewall server using FortiSOAR playbooks. Add the SonicWall Firewall connector as a step in FortiSOAR playbooks and perform automated operations with SonicWall Firewall.

### Version information

Connector Version: 1.2.0

Publisher: Fortinet

Certified: No

## Release Notes for version 1.2.0

The following enhancements have been made to the SonicWall Firewall connector in version 1.2.0:

#### What's Improved

-   Added the following new actions and corresponding playbooks:
    -   Create URI Object List
    -   Get URI Object List
    -   Add Entries to URI Object List
    -   Remove Entries from URI Object List
    -   Delete URI Object List
    -   Create URI List Group
    -   Get URI List Group
    -   Update URI List Group
    -   Delete URI List Group
    -   Create CFS Action Object
    -   Get CFS Action Object
    -   Update CFS Action Object
    -   Delete CFS Action Object
    -   Create CFS Profile Object
    -   Get CFS Profile Object
    -   Update CFS Profile Object
    -   Delete CFS Profile Object

## Installing the connector

Use the **Content Hub** to install the connector. For the detailed procedure to install a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector).

## Prerequisites to configuring the connector

-   You must have the credentials of the SonicWall Firewall server to which you will connect and perform automated operations.
-   The FortiSOAR server should have outbound connectivity to the management port of the SonicWall Firewall server, which is port 443 by default.

## Minimum Permissions Required

-   Not applicable

## Configuring the connector

For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)

### Configuration parameters

In FortiSOAR, on the Connectors page, click the **SonicWall Firewall** connector row (if you are in the **Grid** view on the Connectors page) and in the **Configurations** tab enter the required configuration details:

| Parameter | Description |
| --- | --- |
| Server URL | Specify the REST API endpoint URL of the SonicWall server to which you will connect and perform the automated operations. |
| Port | (Optional) Specify the port of the SonicWall server to which you will connect and perform the automated operations. |
| Username | Specify the username used to access the SonicWall REST API endpoint to which you will connect and perform the automated operations. |
| Password | Specify the password used to access the SonicWall REST API endpoint to which you will connect and perform the automated operations. |
| Verify SSL | Specifies whether the SSL certificate for the server is to be verified. <br/>By default, this option is selected, i.e., set to `true`. |

## Actions supported by the connector

You can use the following automated operations in playbooks and also use the annotations to access operations:

| Function | Description | Annotation and Category |
| --- | --- | --- |
| Create Address Object | Creates an address object on the SonicWall firewall based on the name, zone, and object type that you have specified. | create_address_object_configuration <br/>Remediation |
| Get Address Object | Retrieves the details of one or all address objects from the SonicWall firewall based on the object type and filter that you have specified. | get_address_object_configuration <br/>Investigation |
| Update Address Object | Updates an existing address object on the SonicWall firewall based on the update type, object identifier, and object type that you have specified. | update_address_object_configuration <br/>Remediation |
| Delete Address Object | Deletes a specific address object from the SonicWall firewall based on the object type and object identifier that you have specified. | delete_address_object_configuration <br/>Remediation |
| Create Address Group | Creates an address group object on the SonicWall firewall based on the object type, address group name, and address object name that you have specified. | create_address_group <br/>Remediation |
| Get Address Group | Retrieves the details of one or all address groups from the SonicWall firewall based on the object type and filter that you have specified. | get_address_group <br/>Investigation |
| Update Address in Group | Updates the configuration of an existing address object on the SonicWall firewall based on the update type, object type, and zone that you have specified. | update_address_group <br/>Remediation |
| Delete Address From Group | Deletes a specific address object from the SonicWall firewall based on the object type and object identifier that you have specified. | delete_address_group <br/>Remediation |
| Add Address Object to Group | Adds an existing address object to an address group based on the object type, address group, and address object name that you have specified. | add_address_object_to_group <br/>Containment |
| Remove Address Object from Group | Removes an address object from an address group based on the object type, address group, and address object name that you have specified. | remove_address_object_from_group <br/>Remediation |
| Create URI Object List | Creates a content filter URI list object that contains domain, URI, or keyword entries, based on the name, entry type, and entries that you have specified. | create_uri_object_list <br/>Remediation |
| Get URI Object List | Retrieves a content filter URI list object based on the filter that you have specified. If you do not specify a filter, this operation returns all URI list objects. | get_uri_object_list <br/>Investigation |
| Add Entries to URI Object List | Adds entries to the configuration of an existing URI list object based on the entry type, object identifier, and entries that you have specified. | add_entries_to_uri_object_list <br/>Containment |
| Remove Entries from URI Object List | Removes entries from the configuration of an existing URI list object based on the entry type, object identifier, and entries that you have specified. | remove_entries_from_uri_object_list <br/>Remediation |
| Delete URI Object List | Deletes the configuration of a URI list object based on the object identifier that you have specified. | delete_uri_object_list <br/>Remediation |
| Create URI List Group | Creates a content filter URI list group object based on the name and members that you have specified. | create_uri_list_group <br/>Remediation |
| Get URI List Group | Retrieves a URI list group based on the filter that you have specified. If you do not specify a filter, this operation returns all URI list groups. | get_uri_list_group <br/>Investigation |
| Update URI List Group | Adds members to, or removes members from, an existing URI list group based on the group identifier, action, and members that you have specified. | update_uri_list_group <br/>Remediation |
| Delete URI List Group | Deletes a content filter URI list group object based on the group identifier that you have specified. | delete_uri_list_group <br/>Remediation |
| Create CFS Action Object | Creates a Content Filter (CFS) action object that defines what happens when a policy match occurs, based on the name and action settings that you have specified. Provide the full object body as JSON, since action objects have many optional nested settings. | create_cfs_action <br/>Remediation |
| Get CFS Action Object | Retrieves a CFS action object based on the name that you have specified. If you do not specify a name, this operation returns all CFS action objects. | get_cfs_action <br/>Investigation |
| Update CFS Action Object | Updates the configuration of a CFS action object based on the name and action settings that you have specified. | update_cfs_action <br/>Remediation |
| Delete CFS Action Object | Deletes a CFS action object based on the name that you have specified. | delete_cfs_action <br/>Remediation |
| Create CFS Profile Object | Creates a Content Filter (CFS) profile object based on the profile name, URI lists, and additional settings that you have specified. | create_cfs_profile <br/>Remediation |
| Get CFS Profile Object | Retrieves a CFS profile object based on the name that you have specified. If you do not specify a name, this operation returns all CFS profile objects. | get_cfs_profile <br/>Investigation |
| Update CFS Profile Object | Updates a CFS profile object based on the name, URI lists, and additional settings that you have specified. | update_cfs_profile <br/>Remediation |
| Delete CFS Profile Object | Deletes a CFS profile object based on the name that you have specified. | delete_cfs_profile <br/>Remediation |

### operation: Create Address Object

#### Input parameters

| Parameter | Description |
| --- | --- |
| Name | Specify the name of the address object that you want to create. |
| Zone | Specify the security zone for the address object, for example `WAN`, `LAN`, or `DMZ`. |
| Object Type | Select the type of object for which you want to create the address object configuration. You can choose from the following options: `IPV4`, `IPV6`, or `FQDN`. By default, this is set to `IPV4`.<br>**If you choose 'IPV4' or 'IPV6'**<br>• **Address Object**: Select the type of address object that you want to create: a single address for a host, a range of addresses, or a network address that defines a subnet. By default, this is set to `Host IP Address`.<br>**If you choose 'Host IP Address'**<br>• **IP Address**: Specify the IP address of the host for which you want to create the address object.<br>**If you choose 'IP Range'**<br>• **Starting Range of IP Address**: Specify the starting IP address of the range for the address object.<br>• **Ending Range of IP Address**: Specify the ending IP address of the range for the address object.<br>**If you choose 'Network IP Address'**<br>• **Subnet**: Specify the network address of the subnet.<br>• **Mask**: Specify the subnet mask of the IP address, for example `255.255.255.0`.<br>**If you choose 'FQDN'**<br>• **Domain**: Specify the fully qualified domain name of the address object. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "cli": {
            "mode": "",
            "depth": "",
            "configuring": "",
            "pending_config": "",
            "restart_required": ""
        },
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Get Address Object

#### Input parameters

| Parameter | Description |
| --- | --- |
| Object Type | Select the type of object whose address object configuration details you want to retrieve. You can choose from the following options: `IPV4`, `IPV6`, or `FQDN`. By default, this is set to `IPV4`. |
| Filter Address Object By | (Optional) Select the parameter by which you want to filter the address object configurations. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the address object whose information you want to retrieve.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the address object whose information you want to retrieve. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "address_objects": [
        {
            "ipv4": {
                "name": "",
                "uuid": "",
                "zone": ""
            }
        }
    ]
}
```

### operation: Update Address Object

#### Input parameters

| Parameter | Description |
| --- | --- |
| Update Type | Select the type of update operation that you want to perform. You can choose from the following options: `Partial Update` or `Full Replace`. If you choose Partial Update, only the fields that you provide are updated, and any fields that you do not include remain unchanged. If you choose Full Replace, the entire existing record is replaced with the new data that you provide, and any fields that you do not include in the request might be removed or reset. By default, this is set to `Partial Update`. |
| Update Address Object By | Select the parameter by which you want to identify the address object that you want to update. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the address object that you want to update.<br>**If you choose 'Name'**<br>• **Address Object Name**: Specify the name of the address object that you want to update. |
| Object Type | Select the type of object whose address object configuration you want to update. You can choose from the following options: `IPV4`, `IPV6`, or `FQDN`. By default, this is set to `IPV4`.<br>**If you choose 'IPV4' or 'IPV6'**<br>• **Address Object**: Select the type of address object that you want to update: a single address for a host, a range of addresses, or a network address that defines a subnet. By default, this is set to `Host IP Address`.<br>**If you choose 'Host IP Address'**<br>• **IP Address**: Specify the IP address of the host for which you want to update the address object.<br>**If you choose 'IP Range'**<br>• **Starting Range of IP Address**: Specify the starting IP address of the range for the address object.<br>• **Ending Range of IP Address**: Specify the ending IP address of the range for the address object.<br>**If you choose 'Network IP Address'**<br>• **Subnet**: Specify the network address of the subnet.<br>• **Mask**: Specify the subnet mask of the IP address, for example `255.255.255.0`.<br>**If you choose 'FQDN'**<br>• **Domain**: Specify the fully qualified domain name of the address object. |
| Zone | Specify the security zone, within the domain, IPv4, or IPv6, that you want to update in the address object configuration. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Delete Address Object

#### Input parameters

| Parameter | Description |
| --- | --- |
| Object Type | Select the type of object whose address object configuration you want to delete. You can choose from the following options: `IPV4`, `IPV6`, or `FQDN`. By default, this is set to `IPV4`. |
| Delete Address Object By | Select the parameter by which you want to identify the address object that you want to delete. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the address object that you want to delete.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the address object that you want to delete. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Create Address Group

#### Input parameters

| Parameter | Description |
| --- | --- |
| Object Type | Select the type of object for which you want to create the address group configuration. You can choose from the following options: `IPV4`, `IPV6`, or `FQDN`. By default, this is set to `IPV4`. |
| Address Group Name | Specify the name of the address group object that you want to create. |
| Address Object Name | Specify the name of the address object that you want to use to create the address group. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "cli": {
            "mode": "",
            "depth": "",
            "configuring": "",
            "pending_config": "",
            "restart_required": ""
        },
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Get Address Group

#### Input parameters

| Parameter | Description |
| --- | --- |
| Object Type | Select the type of object whose address group configuration details you want to retrieve. You can choose from the following options: `IPV4`, `IPV6`, or `FQDN`. By default, this is set to `IPV4`. |
| Filter Address Group By | (Optional) Select the parameter by which you want to filter the address group configurations. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **Group UUID**: Specify the universally unique identifier (UUID) of the address group whose configuration details you want to retrieve.<br>**If you choose 'Name'**<br>• **Group Name**: Specify the name of the address group whose configuration details you want to retrieve. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "address_objects": [
        {
            "ipv4": {
                "name": "",
                "uuid": "",
                "zone": ""
            }
        }
    ]
}
```

### operation: Update Address in Group

#### Input parameters

| Parameter | Description |
| --- | --- |
| Update Type | Select the type of update operation that you want to perform. You can choose from the following options: `Partial Update` or `Full Replace`. If you choose Partial Update, only the fields that you provide are updated, and any fields that you do not include remain unchanged. If you choose Full Replace, the entire existing record is replaced with the new data that you provide, and any fields that you do not include in the request might be removed or reset. By default, this is set to `Partial Update`. |
| Object Type | Select the type of object whose address object configuration you want to update. You can choose from the following options: `IPV4`, `IPV6`, or `FQDN`. By default, this is set to `IPV4`.<br>**If you choose 'IPV4' or 'IPV6'**<br>• **Update Address Object By**: Select the parameter by which you want to identify the address object that you want to update: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the address object that you want to update.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the address object that you want to update.<br>• **Address Object**: Select the type of address object that you want to update: a single address for a host, a range of addresses, or a network address that defines a subnet. By default, this is set to `Host IP Address`.<br>**If you choose 'Host IP Address'**<br>• **IP Address**: Specify the IP address of the host for which you want to update the address object.<br>**If you choose 'IP Range'**<br>• **Starting Range of IP Address**: Specify the starting IP address of the range for the address object.<br>• **Ending Range of IP Address**: Specify the ending IP address of the range for the address object.<br>**If you choose 'Network IP Address'**<br>• **Subnet**: Specify the network address of the subnet.<br>• **Mask**: Specify the subnet mask of the IP address.<br>**If you choose 'FQDN'**<br>• **Update Address Object By**: Select the parameter by which you want to identify the address object that you want to update: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the address object that you want to update.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the address object that you want to update.<br>• **Domain**: Specify the domain that you want to update within the current address object configuration. |
| Zone | Specify the security zone, within the domain, IPv4, or IPv6, that you want to update in the address object configuration. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Delete Address From Group

#### Input parameters

| Parameter | Description |
| --- | --- |
| Object Type | Select the type of object whose address object configuration you want to delete. You can choose from the following options: `IPV4`, `IPV6`, or `FQDN`. By default, this is set to `IPV4`. |
| Delete Address Object By | Select the parameter by which you want to identify the address object that you want to delete. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the address object that you want to delete.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the address object that you want to delete. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Add Address Object to Group

#### Input parameters

| Parameter | Description |
| --- | --- |
| Object Type | Select the type of object that you want to add to the specified address group. You can choose from the following options: `IPV4`, `IPV6`, or `FQDN`. By default, this is set to `IPV4`. |
| Filter Address Group By | (Optional) Select the parameter by which you want to identify the address group. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the address group whose information you want to retrieve.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the address group whose information you want to retrieve. |
| Address Object Name | Specify the name of the address object that you want to add to the specified group. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "cli": {
            "mode": "",
            "depth": "",
            "configuring": "",
            "pending_config": "",
            "restart_required": ""
        },
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Remove Address Object from Group

#### Input parameters

| Parameter | Description |
| --- | --- |
| Object Type | Select the type of object that you want to remove from the specified address group. You can choose from the following options: `IPV4`, `IPV6`, or `FQDN`. By default, this is set to `IPV4`. |
| Filter Address Group By | (Optional) Select the parameter by which you want to identify the address group. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the address group whose information you want to retrieve.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the address group whose information you want to retrieve. |
| Address Object Name | Specify the name of the address object that you want to remove from the specified group. |

#### Output

The output contains a non-dictionary value.

### operation: Create URI Object List

#### Input parameters

| Parameter | Description |
| --- | --- |
| Name | Specify a unique name for the URI list object that you want to create. |
| Entry Type | Select the type of entries that you want to store. You can choose from the following options: `Domain`, `URI`, or `Keyword`. By default, this is set to `Domain`. |
| Entries | Specify a comma-separated list of entries that you want to store in this URI list object at the time of creation, for example domains such as `example.com` and `*.example.com`. |
| Raw Payload Override | (Optional) Specify a custom request body, in JSON format, to send as-is instead of the body that the connector builds automatically. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Get URI Object List

#### Input parameters

| Parameter | Description |
| --- | --- |
| Filter URI Object By | (Optional) Select the parameter by which you want to filter the URI object configurations. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the URI object configuration whose information you want to retrieve.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the URI object configuration whose information you want to retrieve. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "content_filter": {
        "uri_list_object": [
            {
                "name": "",
                "uuid": "",
                "type": "",
                "uri": [
                    {
                        "uri": ""
                    }
                ],
                "domain": [
                    {
                        "domain": ""
                    }
                ],
                "keyword": [
                    {
                        "keyword": ""
                    }
                ]
            }
        ]
    }
}
```

### operation: Add Entries to URI Object List

#### Input parameters

| Parameter | Description |
| --- | --- |
| Entry Type | Select the type of entry that you want to add. You can choose from the following options: `Domain`, `URI`, or `Keyword`. By default, this is set to `Domain`. |
| Update URI Object By | Select the parameter by which you want to identify the URI object list that you want to update. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the URI object configuration that you want to update.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the URI object configuration that you want to update. |
| Entries | Specify a comma-separated list of entries that you want to add to the configuration of the existing URI list object. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Remove Entries from URI Object List

#### Input parameters

| Parameter | Description |
| --- | --- |
| Entry Type | Select the type of entry that you want to remove. You can choose from the following options: `Domain`, `URI`, or `Keyword`. By default, this is set to `Domain`. |
| Update URI Object By | Select the parameter by which you want to identify the URI object list that you want to update. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the URI object configuration that you want to update.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the URI object configuration that you want to update. |
| Entries | Specify a comma-separated list of entries that you want to remove from the configuration of the existing URI list object. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Delete URI Object List

#### Input parameters

| Parameter | Description |
| --- | --- |
| Delete URI Object By | Select the parameter by which you want to identify the URI object configuration that you want to delete. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the URI object configuration that you want to delete.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the URI object configuration that you want to delete. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Create URI List Group

#### Input parameters

| Parameter | Description |
| --- | --- |
| Name | Specify the name of the URI list group that you want to create. |
| URI List Object Members | Specify a comma-separated list of URI object names that you want to add to the URI list group. |
| URI List Group Members | Specify a comma-separated list of URI list group names that you want to add to the URI list group. |
| Raw Payload Override | (Optional) Specify a custom request body, in JSON format, to send as-is instead of the body that the connector builds automatically. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Get URI List Group

#### Input parameters

| Parameter | Description |
| --- | --- |
| Filter URI Group By | (Optional) Select the parameter by which you want to filter the URI list groups. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the URI list group whose details you want to retrieve.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the URI list group whose details you want to retrieve. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "content_filter": {
        "uri_list_group": [
            {
                "name": "",
                "uuid": "",
                "uri_list_object": [
                    {
                        "name": ""
                    }
                ],
                "uri_list_group": [
                    {
                        "name": ""
                    }
                ]
            }
        ]
    }
}
```

### operation: Update URI List Group

#### Input parameters

| Parameter | Description |
| --- | --- |
| Update URI Group By | (Optional) Select the parameter by which you want to identify the URI list group that you want to update. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the URI list group that you want to update.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the URI list group that you want to update. |
| Perform Action | Select the action that you want to perform on the URI list group. You can choose from the following options: `Add Entries to Group List` or `Remove Entries from Group List`. |
| URI List Object Members | (Optional) Specify a comma-separated list of URI list object members that you want to add to, or remove from, the URI list group. |
| URI List Group Members | (Optional) Specify a comma-separated list of URI list group members that you want to add to, or remove from, the URI list group. |
| Raw Payload Override | (Optional) Specify a custom request body, in JSON format, to send as-is instead of the body that the connector builds automatically. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Delete URI List Group

#### Input parameters

| Parameter | Description |
| --- | --- |
| Delete URI Group By | Select the parameter by which you want to identify the URI list group that you want to delete. You can choose from the following options: `UUID` or `Name`. By default, this is set to `Name`.<br>**If you choose 'UUID'**<br>• **UUID**: Specify the universally unique identifier (UUID) of the URI list group that you want to delete.<br>**If you choose 'Name'**<br>• **Name**: Specify the name of the URI list group that you want to delete. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Create CFS Action Object

#### Input parameters

| Parameter | Description |
| --- | --- |
| Name | Specify the name of the CFS action object that you want to create. |
| Action Settings (JSON) | Specify the CFS action settings, such as the block page, passphrase, confirmation, and bandwidth management settings, in JSON format, matching the schema of your firmware. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Get CFS Action Object

#### Input parameters

| Parameter | Description |
| --- | --- |
| Name | (Optional) Specify the name of the CFS action object whose information you want to retrieve. If you do not specify a name, this operation returns all CFS action objects. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "content_filter": {
        "action": [
            {
                "name": "",
                "uuid": "",
                "wipe_cookies": "",
                "flow_reporting": "",
                "block": {
                    "page": {}
                },
                "passphrase": {
                    "page": {},
                    "password": "",
                    "active_time": ""
                },
                "confirm": {
                    "page": {},
                    "active_time": ""
                },
                "bandwidth_management": {
                    "aggregation_method": "",
                    "egress": {
                        "name": ""
                    },
                    "ingress": {
                        "name": ""
                    },
                    "usage_tracking": ""
                }
            }
        ]
    }
}
```

### operation: Update CFS Action Object

#### Input parameters

| Parameter | Description |
| --- | --- |
| Name | Specify the name of the CFS action object that you want to update. |
| Action Settings (JSON) | Specify the CFS action settings, such as the block page, passphrase, confirmation, and bandwidth management settings, in JSON format, to update its fields. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Delete CFS Action Object

#### Input parameters

| Parameter | Description |
| --- | --- |
| Name | Specify the name of the CFS action object that you want to delete. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Create CFS Profile Object

#### Input parameters

| Parameter | Description |
| --- | --- |
| Profile Name | Specify the name of the CFS profile object that you want to create. |
| Allowed URI List Object/Group | (Optional) Specify the name of an existing URI list object or group to use as the Allowed list. |
| Forbidden URI List Object/Group | (Optional) Specify the name of an existing URI list object or group to use as the Forbidden list. |
| Additional Settings (JSON) | (Optional) Specify any additional profile settings, such as the category actions, search order, and consent settings, in JSON format. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Get CFS Profile Object

#### Input parameters

| Parameter | Description |
| --- | --- |
| Name | (Optional) Specify the name of the CFS profile object whose detailed information you want to retrieve. If you do not specify a name, this operation returns all CFS profile objects. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "content_filter": {
        "profile": [
            {
                "name": "",
                "uuid": "",
                "uri_list": {
                    "allowed": [
                        {
                            "name": ""
                        }
                    ],
                    "forbidden": [
                        {
                            "name": ""
                        }
                    ],
                    "search_order": "",
                    "forbidden_operation": ""
                },
                "category": [
                    {
                        "name": "",
                        "operation": ""
                    }
                ],
                "categories": "",
                "https_filtering": "",
                "smart_filter": "",
                "safe_search": "",
                "threat_api": "",
                "google_force_safe_search": "",
                "youtube_restrict_mode": "",
                "bing_force_safe_search": "",
                "consent": {
                    "required": "",
                    "user_idle_timeout": "",
                    "optional": {
                        "page_url": ""
                    },
                    "mandatory": {
                        "page_url": "",
                        "address": {}
                    }
                },
                "custom_header": {
                    "insertion": "",
                    "entry": [
                        {
                            "domain": "",
                            "key": "",
                            "value": ""
                        }
                    ]
                }
            }
        ]
    }
}
```

### operation: Update CFS Profile Object

#### Input parameters

| Parameter | Description |
| --- | --- |
| Name | Specify the name of the CFS profile object that you want to update. |
| Allowed URI List Object/Group | (Optional) Specify the name of a URI list object or group to update in the Allowed list. |
| Forbidden URI List Object/Group | (Optional) Specify the name of a URI list object or group to update in the Forbidden list. |
| Additional Settings (JSON) | (Optional) Specify any additional profile settings, such as the category actions, search order, and consent settings, in JSON format. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

### operation: Delete CFS Profile Object

#### Input parameters

| Parameter | Description |
| --- | --- |
| Name | Specify the name of the CFS profile object that you want to delete. |

#### Output

The output contains the following populated JSON schema:

```json
{
    "status": {
        "success": "",
        "info": [
            {
                "level": "",
                "code": "",
                "message": ""
            }
        ]
    }
}
```

## Included playbooks

The *`Sample - SonicWall Firewall - 1.2.0`* playbook collection comes bundled with the SonicWall Firewall connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR after importing the SonicWall Firewall connector.

-   Add Address Object to Group
-   Add Entries to URI Object List
-   Create Address Group
-   Create Address Object
-   Create CFS Action Object
-   Create CFS Profile Object
-   Create URI List Group
-   Create URI Object List
-   Delete Address From Group
-   Delete Address Object
-   Delete CFS Action Object
-   Delete CFS Profile Object
-   Delete URI List Group
-   Delete URI Object List
-   Get Address Group
-   Get Address Object
-   Get CFS Action Object
-   Get CFS Profile Object
-   Get URI List Group
-   Get URI Object List
-   Remove Address Object from Group
-   Remove Entries from URI Object List
-   Update Address Object
-   Update Address in Group
-   Update CFS Action Object
-   Update CFS Profile Object
-   Update URI List Group

> [!Note]
> 
> If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
>