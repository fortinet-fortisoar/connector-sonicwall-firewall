
## About the connector

SonicWall's advanced firewall appliances with various network and security systems. This connector facilitates seamless communication and data exchange between the SonicWall Firewall and other network elements, providing enhanced security, management, and monitoring capabilities

This document provides information about the SonicWall Firewall connector, which facilitates automated interactions, with a SonicWall Firewall server using FortiSOAR™ playbooks. Add the SonicWall Firewall connector as a step in FortiSOAR™ playbooks and perform automated operations with SonicWall Firewall.

### Version information

Connector Version: 1.1.0

Authored By: Fortinet

Certified: No

## Release Notes for version 1.1.0

Following enhancements have been made to the SonicWall Firewall connector in version 1.1.0:

#### What's Fix

-   Fixed an issue where an Unauthorized error occurred while executing connector actions.
-   Renamed the action *Get Address Object Configuration* to **Get Address Object**
-   Renamed the action *Create Address Object Configuration* to **Create Address Object**
-   Renamed the action *Update Address Object Configuration* to **Update Address Object**
-   Renamed the action *Delete Address Object Configuration* to **Delete Address Object**
-   Added the following new actions and corresponding playbooks:
    -   Create Address Group
    -   Get Address Group
    -   Update Address in Group
    -   Delete Address From Group
    -   Add Address Object to Group
    -   Remove Address Object from Group

## Installing the connector

Use the **Content Hub** to install the connector. For the detailed procedure to install a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector).

## Prerequisites to configuring the connector

-   You must have the credentials of SonicWall Firewall server to which you will connect and perform automated operations.
-   The FortiSOAR™ server should have outbound connectivity to port 443 on the SonicWall Firewall server.

## Minimum Permissions Required

-   Not applicable

## Configuring the connector

For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)

### Configuration parameters

In FortiSOAR™, on the Connectors page, click the **SonicWall Firewall** connector row (if you are in the **Grid** view on the Connectors page) and in the **Configurations** tab enter the required configuration details:

| Parameter  | Description                                                                                                                            |
|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Server URL | Specify the Rest API endpoint URL of the SonicWall server to connect and perform automated operations.                                 |
| Port       | Specify the port of the SonicWall server to connect and perform automated operations.                                                  |
| Username   | Specify the username to access the SonicWall Rest API endpoint to which you will connect and perform the automated operations.         |
| Password   | Specify the username to access the SonicWall Rest API endpoint to which you will connect and perform the automated operations.         |
| Verify SSL | Specifies whether the SSL certificate for the server is to be verified.<br />By default, this option is selected, i.e., set to `true`. |

## Actions supported by the connector

You can use the following automated operations in playbooks and also use the annotations to access operations:

| Function                         | Description                                                                                                                         | Annotation and Category                                |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| Create Address Object            | Creates a new address object on the SonicWall firewall.                                                                             | create_address_object_configuration<br />Investigation |
| Get Address Object               | Retrieves one or all address object details within the SonicWall firewall.                                                           | get_address_object_configuration<br />Investigation    |
| Update Address Object            | Updates an existing address object on the SonicWall firewall.                                                                       | update_address_object_configuration<br />Investigation |
| Delete Address Object            | Deletes the a specific address object based on specified input parameters.                                                           | delete_address_object_configuration<br />Investigation |
| Create Address Group             | Creates a new Address Group Object Configuration on a SonicWall Firewall.                                                            | create_address_group<br />Investigation                |
| Get Address Group                | Retrieves details for one or all address groups from the SonicWall firewall.                                                        | get_address_group<br />Investigation                   |
| Update Address in Group          | Updates the configuration of an existing address object on a SonicWall firewall to reflect current network requirements or policies. | update_address_group<br />Investigation                |
| Delete Address From Group        | Deletes the a specific address group based on specified input parameters.                                                            | delete_address_group<br />Investigation                |
| Add Address Object to Group      | Adds an existing address object to a specified address group.                                                                       | add_address_object_to_group<br />Investigation         |
| Remove Address Object from Group | Removes an address object from an address group.                                                                                    | remove_address_object_from_group<br />Investigation    |

### operation: Create Address Object

#### Input parameters

| Parameter   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name        | Specify the name of the address object to create.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Zone        | Security zone for the address object (e.g., WAN, LAN, DMZ).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Object Type | Select one of the following object types to create the address object configuration:<br /><br />**IPV4**<br />- **Address Object**: Select the type of IPv4 address object you wish to create: a single IPv4 address for a host, a range of IPv4 addresses, or a network address for defining a subnet.<br /><br />**Host IP Address**<br />- **IP Address**: Specify the IPv4 address of the host to create the IPv4 Address Object<br /><br />**IP Range**<br />- **Starting Range of IP Address**: Specify the starting IP address of the range for the IPv4 Address Object.<br />- **Ending Range of IP Address**: Specify the ending IP address of the range for the IPv4 Address Object.<br /><br />**Network IP Address**<br />- **Subnet**: Subnet mask (required for network type), e.g., 255.255.255.0<br />- **Mask**: Specify the masking value of the IP address<br /><br />**IPV6**<br />- **Address Object**: Select the type of IPv6 address object you wish to create: a single IPv6 address for a host, a range of IPv6 addresses, or a network address for defining a subnet.<br /><br />**Host IP Address**<br />- **IP Address**: Specify the IPv6 address of the host to create the IPv6 Address Object<br /><br />**IP Range**<br />- **Starting Range of IP Address**: Specify the starting IP address of the range for the IPv6 Address Object.<br />- **Ending Range of IP Address**: Specify the ending IP address of the range for the IPv6 Address Object.<br /><br />**Network IP Address**<br />- **Subnet**: Specify the subdivision of an IP network.<br />- **Mask**: Specify the masking value of the IP address<br /><br />**FQDN**<br />- **Domain**: Specify the Fully Qualified Domain Name (for fqdn type) |

#### Output

The output contains the following populated JSON schema:

```
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

| Parameter                | Description                                                                                                                                                                                                                                                                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Object Type              | Select the object type to retrieve address object configuration details based on the selected object type: IPv4, IPv6, or FQDN                                                                                                                                                                                                                  |
| Filter Address Object By | (Optional) Select filter parameters to retrieve address object configurations details by UUID or Name.<br /><br />- **UUID**: Specify the universally unique identifier (UUID) of the address object, in the **UUID** field, to retrieve its information by UUID.<br />- **Name**: Specify the name of the Address Object, in the **Name** field, to retrieve its information by name. |

#### Output

The output contains the following populated JSON schema:

```
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

| Parameter                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Update Type              | Select the type of update operation the user wants to perform. If the user selects **Partial Update**, only the provided fields will be updated. Any fields not included will remain unchanged. If the user selects **Full Replace**, the entire existing record will be replaced with the new data provided. Any fields not included in the request may be removed or reset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Update Address Object By | Select the input option (name or UUID) to update the address object configuration.<br /><br />- **UUID**: Specify the universally unique identifier (UUID) of the address object, in the **UUID** field, to update its information by UUID.<br />- **Name**: Specify the name of the Address Object, in the **Name** field, to update its information by name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Object Type              | Select one of the following object types to update the address object configuration:<br /><br />**IPV4**<br />- **Address Object**: Select the type of IPv4 address object you wish to update: a single IPv4 address for a host, a range of IPv4 addresses, or a network address for defining a subnet.<br /><br />**Host IP Address**<br />- **IP Address**: Specify the IPv4 address of the host to update the IPv4 Address Object<br /><br />**IP Range**<br />- **Starting Range of IP Address**: Specify the starting IP address of the range for the IPv4 Address Object.<br />- **Ending Range of IP Address**: Specify the ending IP address of the range for the IPv4 Address Object.<br /><br />**Network IP Address**<br />- **Subnet**: Subnet mask (required for network type), e.g., 255.255.255.0<br />- **Mask**: Specify the masking value of the IP address<br /><br />**IPV6**<br />- **Address Object**: Select the type of IPv6 address object you wish to update: a single IPv6 address for a host, a range of IPv6 addresses, or a network address for defining a subnet.<br /><br />**Host IP Address**<br />- **IP Address**: Specify the IPv6 address of the host to update the IPv6 Address Object<br /><br />**IP Range**<br />- **Starting Range of IP Address**: Specify the starting IP address of the range for the IPv6 Address Object.<br />- **Ending Range of IP Address**: Specify the ending IP address of the range for the IPv6 Address Object.<br /><br />**Network IP Address**<br />- **Subnet**: Specify the subdivision of an IP network.<br />- **Mask**: Specify the masking value of the IP address<br /><br />**FQDN**<br />- **Domain**: Specify the Fully Qualified Domain Name (for fqdn type) |
| Zone                     | Specify the specific zone within the domain, IPv4 or IPv6 that you wish to update in the address object configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

#### Output

The output contains the following populated JSON schema:

```
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

| Parameter                | Description                                                                                                                                                                                                                                                                                    |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Object Type              | Choose the object type parameters to delete the address object configuration dbased on the specified input type: IPv4, IPv6, or FQDN                                                                                                                                                           |
| Delete Address Object By | Select filter parameters to delete IPV4 Address Object configurations by UUID or Name.<br /><br />- **UUID**: Specify the universally unique identifier (UUID) of the address object, in the **UUID** field, to delete it by UUID.<br />- **Name**: Specify the name of the Address Object, in the **Name** field, to delete it by name. |

#### Output

The output contains the following populated JSON schema:

```
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

| Parameter           | Description                                                                               |
|---------------------|-------------------------------------------------------------------------------------------|
| Object Type         | Select the object type to create the address object configuration: IPv4, IPv6, or FQDN.   |
| Address Group Name  | Specify the name for the address group object you want to create.                         |
| Address Object Name | Specify the name of the address object you want to use to create an address object group. |

#### Output

The output contains the following populated JSON schema:

```
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

| Parameter               | Description                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Object Type             | Select the object type to retrieve address object configuration details based on the selected object type: IPv4, IPv6, or FQDN                                                                                                                                                                                                                            |
| Filter Address Group By | (Optional) Select filter parameters to retrieve address groups configurations details by UUID or name.<br /><br />- **UUID**: Specify the universally unique identifier (UUID) of the address group, in the **UUID** field, to retrieve the address group's configurations details by UUID.<br />- **Name**: Specify the name of the address group, in the **Name** field, to retrieve the address group's configurations details by name. |

#### Output

The output contains the following populated JSON schema:

```
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

| Parameter   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Update Type | Select the type of update operation the user wants to perform. If the user selects Partial Update, only the provided fields will be updated. Any fields not included will remain unchanged. If the user selects Full Replace, the entire existing record will be replaced with the new data provided. Any fields not included in the request may be removed or reset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Object Type | Choose the object type parameters to update address object configuration based on the specified input type: IPv4, IPv6, or FQDN  <br />**IPV4**<br /><br />*   Update Address Object By: Select filter parameters based on the address object configurations you want to update by UUID or name.<br />**UUID**<br /><br />*   Group Name: Specify the name of the address object you want to update.<br /><br />**Name**<br /><br />*   Group Name: Specify the name of the address object based on the following field you want to update.<br /><br />*   Address Object: Select the type of IPv4 address object you wish to update: a single IPv4 address for a host, a range of IPv4 addresses, or a network address for defining a subnet.<br />**Host IP Address**<br /><br />*   IP Address: Specify the IPv4 address of the host to update the IPv4 Address Object<br /><br />**IP Range**<br /><br />*   Starting Range of IP Address: Specify the starting IP address of the range for the IPv4 Address Object.<br />*   Ending Range of IP Address: Specify the ending IP address of the range for the IPv4 Address Object.<br /><br />**Network IP Address**<br /><br />*   Subnet: Specify the subdivision of an IP network.<br />*   Mask: Specify the masking value of the IP address<br /><br />**IPV6**<br /><br />*   Update Address Object By: Select filter parameters to update Address Object configurations by UUID or Name.<br />**UUID**<br /><br />*   UUID: Specify the universally unique identifier (UUID) of the Address Object which you want to update<br /><br />**Name**<br /><br />*   Name: Specify the name of the Address Object of the Address Object which you want to update<br /><br />*   Address Object: Select the type of IPv6 address object you wish to update: a single IPv6 address for a host, a range of IPv6 addresses, or a network address for defining a subnet.<br />**Host IP Address**<br /><br />*   IP Address: Specify the IPv6 address of the host to update the IPv6 Address Object<br /><br />**IP Range**<br /><br />*   Starting Range of IP Address: Specify the starting IP address of the range for the IPv6 Address Object.<br />*   Ending Range of IP Address: Specify the ending IP address of the range for the IPv6 Address Object.<br /><br />**Network IP Address**<br /><br />*   Subnet: Specify the subdivision of an IP network.<br />*   Mask: Specify the masking value of the IP address<br /><br />**FQDN**<br /><br />*   Update Address Object By: Select filter parameters based on the address object configurations you want to update by UUID or name.<br />**UUID**<br /><br />*   UUID: Specify the universally unique identifier (UUID) of the address object based on the following field you want to update.<br /><br />**Name**<br /><br />*   Name: Specify the name of the address object based on the following field you want to update.<br /><br />*   Domain: Specify the domain you wish to update within the current address object configuration. |
| Zone        | Specify the specific zone within the domain, ipv4 or ipv6 that you wish to update in the address object configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

#### Output

The output contains the following populated JSON schema:

```
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

| Parameter                | Description                                                                                                                                                                                                                                                                    |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Object Type              | Choose the object type parameters to delete the address object configuration based on the specified input type: IPv4, IPv6, or FQDN                                                                                                                                            |
| Delete Address Object By | Select filter parameters to delete IPV4 Address Object configurations by UUID or Name.<br /><br />- **UUID**: Specify the universally unique identifier (UUID) of the address object, in the **UUID** field, to delete it by UUID.<br />- **Name**: Specify the name of the Address Object, in the **Name** field, to delete it by name. |

#### Output

The output contains the following populated JSON schema:

```
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

| Parameter               | Description                                                                                                                                                                                                                                                                                                                                |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Object Type             | Select the object type to add the address object to the specified group.                                                                                                                                                                                                                                                                   |
| Filter Address Group By | (Optional) Select filter parameters to fetch the address group configurations details by UUID or name.<br /><br />- **UUID**: Specify the universally unique identifier (UUID) of the address object, in the **UUID** field, to delete it by UUID.<br />- **Name**: Specify the name of the Address Object, in the **Name** field, to delete it by name. |
| Address Object Name     | Name of the address object to add to the specified group.                                                                                                                                                                                                                                                                                  |

#### Output

The output contains the following populated JSON schema:

```
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

| Parameter               | Description                                                                                                                                                                                                                                                                                                                                |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Object Type             | Select the object type to create the address object configuration: IPv4, IPv6, or FQDN.                                                                                                                                                                                                                                                    |
| Filter Address Group By | (Optional) Select filter parameters to fetch the address group configurations details by UUID or name.  <br>**UUID**<br><br>*   UUID: Specify the universally unique identifier (UUID) of the group object to retrieve its information.<br><br>**Name**<br><br>*   Name: Specify the name of the address group to retrieve its information |
| Address Object Name     | Name of the address object to add to the group.                                                                                                                                                                                                                                                                                            |

#### Output

The output contains a non-dictionary value.

## Included playbooks

The *`Sample - SonicWall Firewall - 1.1.0`* playbook collection comes bundled with the SonicWall Firewall connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR™ after importing the SonicWall Firewall connector.

- Add Address Object to Group
- Create Address Group
- Create Address Object
- Delete Address From Group
- Delete Address Object
- Get Address Group
- Get Address Object
- Remove Address Object from Group
- Update Address Object
- Update Address in Group

>[!Note]
>
>If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
