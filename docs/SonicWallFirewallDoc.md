
<h2>About the connector</h2>

<p>SonicWall's advanced firewall appliances with various network and security systems. This connector facilitates seamless communication and data exchange between the SonicWall Firewall and other network elements, providing enhanced security, management, and monitoring capabilities</p>

<p>This document provides information about the SonicWall Firewall connector, which facilitates automated interactions, with a SonicWall Firewall server using FortiSOAR&trade; playbooks. Add the SonicWall Firewall connector as a step in FortiSOAR&trade; playbooks and perform automated operations with SonicWall Firewall.</p>

<h3>Version information</h3>

<p>Connector Version: 1.2.0</p>

<p>Authored By: Fortinet</p>

<p>Certified: No</p>

<h2>Release Notes for version 1.2.0</h2>

<p>Following enhancements have been made to the SonicWall Firewall connector in version 1.2.0:</p>

<h4>What's Improved</h4>

<ul>

<li><p>Added the following new actions and corresponding playbooks:</p>

<ul>
<li>Create URI Object List</li>
<li>Get URI Object List</li>
<li>Add Entries to URI Object List</li>
<li>Remove Entries from URI Object List</li>
<li>Delete URI Object List</li>
<li>Create URI List Group</li>
<li>Get URI Group List</li>
<li>Update URI Group List</li>
<li>Delete URI Group List</li>
<li>Create CFS Action Object</li>
<li>Get CFS Action Object</li>
<li>Update CFS Action Object</li>
<li>Delete CFS Action Object</li>
<li>Create CFS Profile Object</li>
<li>Get CFS Profile Object</li>
<li>Update CFS Profile Object</li>
<li>Delete CFS Profile Object</li>
</ul></li>
</ul>

<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-sonicwall-firewall</pre>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the credentials of SonicWall Firewall server to which you will connect and perform automated operations.</li>
<li>The FortiSOAR&trade; server should have outbound connectivity to port 443 on the SonicWall Firewall server.</li>
</ul>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>SonicWall Firewall</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the Rest API endpoint URL of the SonicWall server to connect and perform automated operations.</td></tr>
<tr><td>Port</td><td>Specify the port of the SonicWall server to connect and perform automated operations.</td></tr>
<tr><td>Username</td><td>Specify the username to access the SonicWall Rest API endpoint to which you will connect and perform the automated operations.</td></tr>
<tr><td>Password</td><td>Specify the username to access the SonicWall Rest API endpoint to which you will connect and perform the automated operations.</td></tr>
<tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified. <br/>By default, this option is selected, i.e., set to <code>true</code>.</td></tr>
</tbody></table>

<h2>Actions supported by the connector</h2>

<p>You can use the following automated operations in playbooks and also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Create Address Object</td><td>Creates a new address object on the SonicWall firewall.</td><td>create_address_object_configuration <br/>Investigation</td></tr>
<tr><td>Get Address Object</td><td>Retrieves one or all address object details within the SonicWall firewall.</td><td>get_address_object_configuration <br/>Investigation</td></tr>
<tr><td>Update Address Object</td><td>Updates an existing address object on the SonicWall firewall.</td><td>update_address_object_configuration <br/>Investigation</td></tr>
<tr><td>Delete Address Object</td><td>Deletes the a specific address object based on specified input parameters.</td><td>delete_address_object_configuration <br/>Investigation</td></tr>
<tr><td>Create Address Group</td><td>Creates a new Address Group Object Configuration on a SonicWall Firewall.</td><td>create_address_group <br/>Investigation</td></tr>
<tr><td>Get Address Group</td><td>Retrieves details for one or all address groups from the SonicWall firewall.</td><td>get_address_group <br/>Investigation</td></tr>
<tr><td>Update Address in Group</td><td>Updates the configuration of an existing address object on a SonicWall firewall to reflect current network requirements or policies.</td><td>update_address_group <br/>Investigation</td></tr>
<tr><td>Delete Address From Group</td><td>Deletes the a specific address group based on specified input parameters.</td><td>delete_address_group <br/>Investigation</td></tr>
<tr><td>Add Address Object to Group</td><td>Adds an existing address object to a specified address group.</td><td>add_address_object_to_group <br/>Investigation</td></tr>
<tr><td>Remove Address Object from Group</td><td>Removes an address object from an address group.</td><td>remove_address_object_from_group <br/>Investigation</td></tr>
<tr><td>Create URI Object List</td><td>Create a new content filter URI list object containing domain, URI, or keyword entries.</td><td>create_uri_object_list <br/>Investigation</td></tr>
<tr><td>Get URI Object List</td><td>Retrieve a content filter URI list object by name or UUID. Leave the name or UUID blank to list all URI list objects.</td><td>get_uri_list_object <br/>Investigation</td></tr>
<tr><td>Add Entries to URI Object List</td><td>Add entries to the configuration of the existing URI list object</td><td>add_entries_to_uri_object_list <br/>Investigation</td></tr>
<tr><td>Remove Entries from URI Object List</td><td>Remove entries from the specified URI list object's configuration.</td><td>remove_entries_from_uri_object_list <br/>Investigation</td></tr>
<tr><td>Delete URI Object List</td><td>Delete the specified URI list object's configuration.</td><td>delete_uri_object_list <br/>Investigation</td></tr>
<tr><td>Create URI List Group</td><td>Create a new content filter URI list group object.</td><td>create_uri_list_group <br/>Investigation</td></tr>
<tr><td>Get URI Group List</td><td>Retrieve a URI List Group by name. Leave name or uuid blank to list all URI List Groups.</td><td>get_uri_list_group <br/>Investigation</td></tr>
<tr><td>Update URI Group List</td><td>Update a membership(Add/Remove) of an existing URI List Group.</td><td>update_uri_list_group <br/>Investigation</td></tr>
<tr><td>Delete URI Group List</td><td>Delete a specified content filter URI list group object.</td><td>delete_uri_list_group <br/>Investigation</td></tr>
<tr><td>Create CFS Action Object</td><td>Create a Content Filter (CFS) Action Object defining what happens when a policy match occurs (block/confirm/passphrase/BWM). Provide the full object body as JSON since action objects have many optional nested settings.</td><td>create_cfs_action <br/>Investigation</td></tr>
<tr><td>Get CFS Action Object</td><td>Retrieve a CFS Action Object by name. Leave name blank to list all CFS Action Objects.</td><td>get_cfs_action <br/>Investigation</td></tr>
<tr><td>Update CFS Action Object</td><td>Update the specified CFS Action Object configuration based on the provided input parameters.</td><td>update_cfs_action <br/>Investigation</td></tr>
<tr><td>Delete CFS Action Object</td><td>Delete a CFS Action Object by name</td><td>delete_cfs_action <br/>Investigation</td></tr>
<tr><td>Create CFS Profile Object</td><td>Create a Content Filter (CFS) Profile Object. At minimum lets you bind Allowed/Forbidden URI Lists; pass additional category/advanced settings via JSON.</td><td>create_cfs_profile <br/>Investigation</td></tr>
<tr><td>Get CFS Profile Object</td><td>Retrieve a CFS Profile Object by name. Leave name blank to list all CFS Profile Objects.</td><td>get_cfs_profile <br/>Investigation</td></tr>
<tr><td>Update CFS Profile Object</td><td>Updates a Content Filter (CFS) Profile Object. At minimum lets you bind Allowed/Forbidden URI Lists; pass additional category/advanced settings via JSON.</td><td>update_cfs_profile <br/>Investigation</td></tr>
<tr><td>Delete CFS Profile Object</td><td>Deletes a CFS Profile Object by name.</td><td>delete_cfs_profile <br/>Investigation</td></tr>
</tbody></table>

<h3>operation: Create Address Object</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Specify the name of the address object to create.</td></tr>
<tr><td>Zone</td><td>Security zone for the address object (e.g., WAN, LAN, DMZ).</td></tr>
<tr><td>Object Type</td><td>Select one of the following object types to create the address object configuration: IPV4, IPV6, FQDN<br><strong>If you choose 'IPV4'</strong><ul><li>Address Object: Select the type of IPv4 address object you wish to create: a single IPv4 address for a host, a range of IPv4 addresses, or a network address for defining a subnet.</li><strong>If you choose 'Host IP Address'</strong><ul><li>IP Address: Specify the IPv4 address of the host to create the IPv4 Address Object</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Starting Range of IP Address: Specify the starting IP address of the range for the IPv4 Address Object.</li><li>Ending Range of IP Address: Specify the ending IP address of the range for the IPv4 Address Object.</li></ul><strong>If you choose 'Network IP Address'</strong><ul><li>Subnet: Subnet mask (required for network type), e.g., 255.255.255.0</li><li>Mask: Specify the masking value of the IP address</li></ul></ul><strong>If you choose 'IPV6'</strong><ul><li>Address Object: Select the type of IPv6 address object you wish to create: a single IPv6 address for a host, a range of IPv6 addresses, or a network address for defining a subnet.</li><strong>If you choose 'Host IP Address'</strong><ul><li>IP Address: Specify the IPv6 address of the host to create the IPv6 Address Object</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Starting Range of IP Address: Specify the starting IP address of the range for the IPv6 Address Object.</li><li>Ending Range of IP Address: Specify the ending IP address of the range for the IPv6 Address Object.</li></ul><strong>If you choose 'Network IP Address'</strong><ul><li>Subnet: Specify the subdivision of an IP network.</li><li>Mask: Specify the masking value of the IP address</li></ul></ul><strong>If you choose 'FQDN'</strong><ul><li>Domain: Specify the Fully Qualified Domain Name (for fqdn type)</li></ul></td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Get Address Object</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Object Type</td><td>Select the object type to retrieve address object configuration details based on the selected object type: IPv4, IPv6, or FQDN</td></tr>
<tr><td>Filter Address Object By</td><td>(Optional) Select filter parameters to retrieve address object configurations details by UUID or Name.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the address object, in the UUID field, to retrieve its information by UUID.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the Address Object, in the Name field, to retrieve its information by name.</li></ul></td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "address_objects": [
        {
            "ipv4": {
                "name": "",
                "uuid": "",
                "zone": ""
            }
        }
    ]
}</pre>

<h3>operation: Update Address Object</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Update Type</td><td>Select the type of update operation the user wants to perform. If the user selects Partial Update, only the provided fields will be updated. Any fields not included will remain unchanged. If the user selects Full Replace, the entire existing record will be replaced with the new data provided. Any fields not included in the request may be removed or reset.</td></tr>
<tr><td>Update Address Object By</td><td>Select one of the following object types to update the address object configuration: UUID or Name<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the address object, in the UUID field, to update its information by UUID.</li></ul><strong>If you choose 'Name'</strong><ul><li>Address Object Name: Specify the name of the Address Object, in the Name field, to update its information by name.</li></ul></td></tr>
<tr><td>Object Type</td><td>Select one of the following object types to update the address object configuration: IPv4, IPv6, or FQDN<br><strong>If you choose 'IPV4'</strong><ul><li>Address Object: Select the type of IPv4 address object you wish to update: a single IPv4 address for a host, a range of IPv4 addresses, or a network address for defining a subnet.</li><strong>If you choose 'Host IP Address'</strong><ul><li>IP Address: Specify the IPv4 address of the host to update the IPv4 Address Object</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Starting Range of IP Address: Specify the starting IP address of the range for the IPv4 Address Object.</li><li>Ending Range of IP Address: Specify the ending IP address of the range for the IPv4 Address Object.</li></ul><strong>If you choose 'Network IP Address'</strong><ul><li>Subnet: Subnet mask (required for network type), e.g., 255.255.255.0</li><li>Mask: Specify the masking value of the IP address</li></ul></ul><strong>If you choose 'IPV6'</strong><ul><li>Address Object: Select the type of IPv6 address object you wish to update: a single IPv6 address for a host, a range of IPv6 addresses, or a network address for defining a subnet.</li><strong>If you choose 'Host IP Address'</strong><ul><li>IP Address: Specify the IPv6 address of the host to update the IPv6 Address Object</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Starting Range of IP Address: Specify the starting IP address of the range for the IPv6 Address Object.</li><li>Ending Range of IP Address: Specify the ending IP address of the range for the IPv6 Address Object.</li></ul><strong>If you choose 'Network IP Address'</strong><ul><li>Subnet: Specify the subdivision of an IP network.</li><li>Mask: Specify the subdivision of an IP network.</li></ul></ul><strong>If you choose 'FQDN'</strong><ul><li>Domain: Specify the Fully Qualified Domain Name (for fqdn type)</li></ul></td></tr>
<tr><td>Zone</td><td>Specify the specific zone within the domain, IPv4 or IPv6 that you wish to update in the address object configuration</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Delete Address Object</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Object Type</td><td>Choose the object type parameters to delete the address object configuration dbased on the specified input type: IPv4, IPv6, or FQDN</td></tr>
<tr><td>Delete Address Object By</td><td>Select filter parameters to delete IPV4 Address Object configurations by UUID or Name.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the address object, in the UUID field, to delete it by UUID.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the Address Object, in the Name field, to delete it by name.</li></ul></td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Create Address Group</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Object Type</td><td>Select the object type to create the address object configuration: IPv4, IPv6, or FQDN.</td></tr>
<tr><td>Address Group Name</td><td>Specify the name for the address group object you want to create.</td></tr>
<tr><td>Address Object Name</td><td>Specify the name of the address object you want to use to create an address object group.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Get Address Group</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Object Type</td><td>Select the object type to retrieve address object configuration details based on the selected object type: IPv4, IPv6, or FQDN</td></tr>
<tr><td>Filter Address Group By</td><td>(Optional) Select filter parameters to retrieve address groups configurations details by UUID or name.<br><strong>If you choose 'UUID'</strong><ul><li>Group UUID: Specify the universally unique identifier (UUID) of the address group, in the UUID field, to retrieve the address group's configurations details by UUID.</li></ul><strong>If you choose 'Name'</strong><ul><li>Group Name: Specify the name of the address group, in the Name field, to retrieve the address group's configurations details by name.</li></ul></td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "address_objects": [
        {
            "ipv4": {
                "name": "",
                "uuid": "",
                "zone": ""
            }
        }
    ]
}</pre>

<h3>operation: Update Address in Group</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Update Type</td><td>Select the type of update operation the user wants to perform. If the user selects Partial Update, only the provided fields will be updated. Any fields not included will remain unchanged. If the user selects Full Replace, the entire existing record will be replaced with the new data provided. Any fields not included in the request may be removed or reset.</td></tr>
<tr><td>Object Type</td><td>Choose the object type parameters to update address object configuration based on the specified input type: IPv4, IPv6, or FQDN<br><strong>If you choose 'IPV4'</strong><ul><li>Update Address Object By: Select filter parameters based on the address object configurations you want to update by UUID or name.</li><strong>If you choose 'UUID'</strong><ul><li>Group Name: Specify the name of the address object you want to update.</li></ul><strong>If you choose 'Name'</strong><ul><li>Group Name: Specify the name of the address object based on the following field you want to update.</li></ul><li>Address Object: Select the type of IPv4 address object you wish to update: a single IPv4 address for a host, a range of IPv4 addresses, or a network address for defining a subnet.</li><strong>If you choose 'Host IP Address'</strong><ul><li>IP Address: Specify the IPv4 address of the host to update the IPv4 Address Object</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Starting Range of IP Address: Specify the starting IP address of the range for the IPv4 Address Object.</li><li>Ending Range of IP Address: Specify the ending IP address of the range for the IPv4 Address Object.</li></ul><strong>If you choose 'Network IP Address'</strong><ul><li>Subnet: Specify the subdivision of an IP network.</li><li>Mask: Specify the masking value of the IP address</li></ul></ul><strong>If you choose 'IPV6'</strong><ul><li>Update Address Object By: Select filter parameters to update Address Object configurations by UUID or Name.</li><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the Address Object which you want to update</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the Address Object of the Address Object which you want to update</li></ul><li>Address Object: Select the type of IPv6 address object you wish to update: a single IPv6 address for a host, a range of IPv6 addresses, or a network address for defining a subnet.</li><strong>If you choose 'Host IP Address'</strong><ul><li>IP Address: Specify the IPv6 address of the host to update the IPv6 Address Object</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Starting Range of IP Address: Specify the starting IP address of the range for the IPv6 Address Object.</li><li>Ending Range of IP Address: Specify the ending IP address of the range for the IPv6 Address Object.</li></ul><strong>If you choose 'Network IP Address'</strong><ul><li>Subnet: Specify the subdivision of an IP network.</li><li>Mask: Specify the masking value of the IP address</li></ul></ul><strong>If you choose 'FQDN'</strong><ul><li>Update Address Object By: Select filter parameters based on the address object configurations you want to update by UUID or name.</li><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the address object based on the following field you want to update.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the address object based on the following field you want to update.</li></ul><li>Domain: Specify the domain you wish to update within the current address object configuration.</li></ul></td></tr>
<tr><td>Zone</td><td>Specify the specific zone within the domain, ipv4 or ipv6 that you wish to update in the address object configuration</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Delete Address From Group</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Object Type</td><td>Choose the object type parameters to delete the address object configuration based on the specified input type: IPv4, IPv6, or FQDN</td></tr>
<tr><td>Delete Address Object By</td><td>Select filter parameters to delete IPV4 Address Object configurations by UUID or Name.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the address object, in the UUID field, to delete it by UUID.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the Address Object, in the Name field, to delete it by name.</li></ul></td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Add Address Object to Group</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Object Type</td><td>Select the object type to add the address object to the specified group.</td></tr>
<tr><td>Filter Address Group By</td><td>(Optional) Select filter parameters to fetch the address group configurations details by UUID or name.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the group object to retrieve its information.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the address group to retrieve its information</li></ul></td></tr>
<tr><td>Address Object Name</td><td>Name of the address object to add to the specified group.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Remove Address Object from Group</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Object Type</td><td>Select the object type to create the address object configuration: IPv4, IPv6, or FQDN.</td></tr>
<tr><td>Filter Address Group By</td><td>(Optional) Select filter parameters to fetch the address group configurations details by UUID or name.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the group object to retrieve its information.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the address group to retrieve its information</li></ul></td></tr>
<tr><td>Address Object Name</td><td>Name of the address object to add to the group.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Create URI Object List</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Specify a unique name for the URI List object that you want to create.</td></tr>
<tr><td>Entry Type</td><td>Select the type of entries you want to store.</td></tr>
<tr><td>Entries</td><td>Specify a comma-separated list of entries that you want to store in this URI List object at the time of creation. For example, domains such as example.com and *.example.com.</td></tr>
<tr><td>Raw Payload Override</td><td>(Optional) If user want to provide any custom payload request body. full JSON body to send as-is instead of auto-building one.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Get URI Object List</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter URI Object By</td><td>(Optional) Select filter parameters to retrieve URI object configurations details by UUID or Name.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the URI object configuration to retrieve its information.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the URI object configuration to retrieve its information.</li></ul></td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Add Entries to URI Object List</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Entry Type</td><td>Select the type of entry you want to update</td></tr>
<tr><td>Update URI Object By</td><td>Update the URI object list configurations based on the provided input parameter, either name or UUID.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the URI object configuration that you want to update.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the URI object configuration that you want to update.</li></ul></td></tr>
<tr><td>Entries</td><td>Provide a CSV list of entries which you want to add to existing URI list Object's configuration.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Remove Entries from URI Object List</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Entry Type</td><td>Select the type of entry you want to update.</td></tr>
<tr><td>Update URI Object By</td><td>Update the URI object list configurations based on the provided input parameter, either name or UUID.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the URI object configuration that you want to update.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the URI object configuration that you want to update.</li></ul></td></tr>
<tr><td>Entries</td><td>Provide a CSV list of entries which you want to remove from existing URI list Object's configuration.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Delete URI Object List</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Delete URI Object By</td><td>Delete URI object configuration details by UUID or name.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the URI object configuration that you want to delete.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the URI object configuration that you want to delete.</li></ul></td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Create URI List Group</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Specify the name of the URI List Group you want to create.</td></tr>
<tr><td>URI List Object Members</td><td>Provide a CSV list of URI object names that you want to add when creating a URI List Group.</td></tr>
<tr><td>URI List Group Members</td><td>Provide a CSV list of URI List Group names that you want to add when creating a URI List Group.</td></tr>
<tr><td>Raw Payload Override</td><td>(Optional) If user want to provide any custom payload request body. full JSON body to send as-is instead of auto-building one.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Get URI Group List</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter URI Group By</td><td>(Optional) Select filter parameters to retrieve URI List Group details by UUID or name.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) to retrieve the URI List Group details.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the URL List Group to retrieve its details.</li></ul></td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Update URI Group List</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Update URI Group By</td><td>(Optional) Select the UUID parameter name of the group list that you want to update.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the group list that you want to update.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the group list that you want to update.</li></ul></td></tr>
<tr><td>Perform Action</td><td>Specify the URI list object member in the group list that you want to update.</td></tr>
<tr><td>URI List Object Members</td><td>(Optional) Specify the URI list object member in the group list that you want to update.</td></tr>
<tr><td>URI List Group Members</td><td>(Optional) Specify the URI list Group member in the group list that you want to update.</td></tr>
<tr><td>Raw Payload Override</td><td>(Optional) If user want to provide any custom payload request body. full JSON body to send as-is instead of auto-building one.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Delete URI Group List</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Delete URI Group By</td><td>Select the UUID or name of the group list you want to delete.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the group list you want to delete.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the group list that you want to delete.</li></ul></td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Create CFS Action Object</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Specify the name of the CFS action object you want to create.</td></tr>
<tr><td>Action Settings (JSON)</td><td>Specify the CFS action settings (block page, passphrase, confirmation, bandwidth management, etc.) in JSON format, matching your firmware's schema.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Get CFS Action Object</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>(Optional) Specify the name of the CFS action object whose information you want to retrieve. Leave name blank to list all CFS Action Objects.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Update CFS Action Object</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Specify the name of the CFS action object you want to update.</td></tr>
<tr><td>Action Settings (JSON)</td><td>Specify the CFS action settings object schema (block page, passphrase, confirmation, bandwidth management, etc.) in JSON format to update its fields.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Delete CFS Action Object</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Specify the name of the CFS action object you want to delete.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Create CFS Profile Object</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Profile Name</td><td>Specify the name of the CFS Profile Object that you want to create.</td></tr>
<tr><td>Allowed URI List Object/Group</td><td>(Optional) Specify the name of an existing URI List Object or Group to use as the Allowed list.</td></tr>
<tr><td>Forbidden URI List Object/Group</td><td>(Optional) Specify the name of an existing URI List Object or Group to use as the Forbidden list.</td></tr>
<tr><td>Additional Settings (JSON)</td><td>(Optional) Specify additional profile settings in JSON format (category actions, search order, consent, etc.) that are required to create a CFS profile object.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Get CFS Profile Object</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>(Optional) Specify the name of the CFS Profile Object for which you want to retrieve detailed information.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Update CFS Profile Object</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Specify the name of the CFS Profile object that you want to update.</td></tr>
<tr><td>Allowed URI List Object/Group</td><td>(Optional) Specify the name of a URI List Object or Group to update in the Allowed list.</td></tr>
<tr><td>Forbidden URI List Object/Group</td><td>(Optional) Specify the name of a URI List Object or Group to update in the Forbidden URI list.</td></tr>
<tr><td>Additional Settings (JSON)</td><td>(Optional) Specify additional profile settings in JSON format (category actions, search order, consent, etc.) that are required to update a CFS profile object.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h3>operation: Delete CFS Profile Object</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Specify the name of the CFS profile object you want to delete.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
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
}</pre>

<h2>Included playbooks</h2>

<p>The <code>Sample - SonicWall Firewall - 1.2.0</code> playbook collection comes bundled with the SonicWall Firewall connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the SonicWall Firewall connector.</p>

<ul>
<li>Add Address Object to Group</li>
<li>Add Entries to URI Object List</li>
<li>Create Address Group</li>
<li>Create Address Object</li>
<li>Create CFS Action Object</li>
<li>Create CFS Profile Object</li>
<li>Create URI List Group</li>
<li>Create URI Object List</li>
<li>Delete Address From Group</li>
<li>Delete Address Object</li>
<li>Delete CFS Action Object</li>
<li>Delete CFS Profile Object</li>
<li>Delete URI Group List</li>
<li>Delete URI Object List</li>
<li>Get Address Group</li>
<li>Get Address Object</li>
<li>Get CFS Action Object</li>
<li>Get CFS Profile Object</li>
<li>Get URI Group List</li>
<li>Get URI Object List</li>
<li>Remove Address Object from Group</li>
<li>Remove Entries from URI Object List</li>
<li>Update Address Object</li>
<li>Update Address in Group</li>
<li>Update CFS Action Object</li>
<li>Update CFS Profile Object</li>
<li>Update URI Group List</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>
