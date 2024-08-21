
<h2>About the connector</h2>

<p>SonicWall's advanced firewall appliances with various network and security systems. This connector facilitates seamless communication and data exchange between the SonicWall Firewall and other network elements, providing enhanced security, management, and monitoring capabilities</p>

<p>This document provides information about the SonicWall Firewall connector, which facilitates automated interactions, with a SonicWall Firewall server using FortiSOAR&trade; playbooks. Add the SonicWall Firewall connector as a step in FortiSOAR&trade; playbooks and perform automated operations with SonicWall Firewall.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>Authored By: Fortinet</p>

<p>Certified: No</p>

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

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Address Object Configuration</td><td>Retrieve the configuration details for a specific address object within the SonicWall firewall.</td><td>get_address_object_configuration <br/>Investigation</td></tr>
<tr><td>Create Address Object Configuration</td><td>Create a new Address Object Configuration on a SonicWall Firewall.</td><td>create_address_object_configuration <br/>Investigation</td></tr>
<tr><td>Update Address Object Configuration</td><td>Update the configuration of an existing address object on a SonicWall firewall to reflect current network requirements or policies.</td><td>update_address_object_configuration <br/>Investigation</td></tr>
<tr><td>Delete Address Object Configuration</td><td>Delete the a specific address object based on specified input parameters.</td><td>delete_address_object_configuration <br/>Investigation</td></tr>
</tbody></table>

<h3>operation: Get Address Object Configuration</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Object Type</td><td>Select the object type to retrieve address object configuration details based on the selected object type: IPv4, IPv6, or FQDN</td></tr>
<tr><td>Filter Address Object By</td><td>Select filter parameters to retrieve address object configurations details by UUID or name.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the address object to retrieve its information.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the Address Object to retrieve its information</li></ul></td></tr>
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

<h3>operation: Create Address Object Configuration</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Specify the name for the address object you wish to create.</td></tr>
<tr><td>Zone</td><td>Specify the specific zone within the domain, ipv4 or ipv6 that you wish to create a address object configuration</td></tr>
<tr><td>Object Type</td><td>Select the object type to create the address object configuration: IPv4, IPv6, or FQDN.<br><strong>If you choose 'IPV4'</strong><ul><li>Address Object: Select the type of IPv4 address object you wish to create: a single IPv4 address for a host, a range of IPv4 addresses, or a network address for defining a subnet.</li><strong>If you choose 'Host IP Address'</strong><ul><li>IP Address: Specify the IPv4 address of the host to create the IPv4 Address Object</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Starting Range of IP Address: Specify the starting IP address of the range for the IPv4 Address Object.</li><li>Ending Range of IP Address: Specify the ending IP address of the range for the IPv4 Address Object.</li></ul><strong>If you choose 'Network IP Address'</strong><ul><li>Subnet: Specify the subdivision of an IP network.</li><li>Mask: Specify the masking value of the IP address</li></ul></ul><strong>If you choose 'IPV6'</strong><ul><li>Address Object: Select the type of IPv6 address object you wish to create: a single IPv6 address for a host, a range of IPv6 addresses, or a network address for defining a subnet.</li><strong>If you choose 'Host IP Address'</strong><ul><li>IP Address: Specify the IPv6 address of the host to create the IPv6 Address Object</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Starting Range of IP Address: Specify the starting IP address of the range for the IPv6 Address Object.</li><li>Ending Range of IP Address: Specify the ending IP address of the range for the IPv6 Address Object.</li></ul><strong>If you choose 'Network IP Address'</strong><ul><li>Subnet: Specify the subdivision of an IP network.</li><li>Mask: Specify the masking value of the IP address</li></ul></ul><strong>If you choose 'FQDN'</strong><ul><li>Domain: Specify the domain to create the IPv6 Address Object</li></ul></td></tr>
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

<h3>operation: Update Address Object Configuration</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Object Type</td><td>Choose the object type parameters to update address object configuration based on the specified input type: IPv4, IPv6, or FQDN<br><strong>If you choose 'IPV4'</strong><ul><li>Update Address Object By: Select filter parameters based on the address object configurations you want to update by UUID or name.</li><strong>If you choose 'UUID'</strong><ul><li>Name: Specify the name of the address object you want to update.</li><li>UUID: Specify the universally unique identifier (UUID) of the address object based on the following field you want to update.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the address object based on the following field you want to update.</li></ul><li>Address Object: Select the type of IPv4 address object you wish to update: a single IPv4 address for a host, a range of IPv4 addresses, or a network address for defining a subnet.</li><strong>If you choose 'Host IP Address'</strong><ul><li>IP Address: Specify the IPv4 address of the host to update the IPv4 Address Object</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Starting Range of IP Address: Specify the starting IP address of the range for the IPv4 Address Object.</li><li>Ending Range of IP Address: Specify the ending IP address of the range for the IPv4 Address Object.</li></ul><strong>If you choose 'Network IP Address'</strong><ul><li>Subnet: Specify the subdivision of an IP network.</li><li>Mask: Specify the masking value of the IP address</li></ul></ul><strong>If you choose 'IPV6'</strong><ul><li>Update Address Object By: Select filter parameters to update Address Object configurations by UUID or Name.</li><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the Address Object which you want to update</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the Address Object of the Address Object which you want to update</li></ul><li>Address Object: Select the type of IPv6 address object you wish to update: a single IPv6 address for a host, a range of IPv6 addresses, or a network address for defining a subnet.</li><strong>If you choose 'Host IP Address'</strong><ul><li>IP Address: Specify the IPv6 address of the host to update the IPv6 Address Object</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Starting Range of IP Address: Specify the starting IP address of the range for the IPv6 Address Object.</li><li>Ending Range of IP Address: Specify the ending IP address of the range for the IPv6 Address Object.</li></ul><strong>If you choose 'Network IP Address'</strong><ul><li>Subnet: Specify the subdivision of an IP network.</li><li>Mask: Specify the masking value of the IP address</li></ul></ul><strong>If you choose 'FQDN'</strong><ul><li>Update Address Object By: Select filter parameters based on the address object configurations you want to update by UUID or name.</li><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the address object based on the following field you want to update.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the address object based on the following field you want to update.</li></ul><li>Domain: Specify the domain you wish to update within the current address object configuration.</li></ul></td></tr>
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

<h3>operation: Delete Address Object Configuration</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Object Type</td><td>Choose the object type parameters to delete the address object configuration dbased on the specified input type: IPv4, IPv6, or FQDN</td></tr>
<tr><td>Delete Address Object By</td><td>Select filter parameters to delete IPV4 Address Object configurations by UUID or Name.<br><strong>If you choose 'UUID'</strong><ul><li>UUID: Specify the universally unique identifier (UUID) of the IPv4 Address Object</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the name of the IPv4 Address Object</li></ul></td></tr>
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

<p>The <code>Sample - SonicWall Firewall - 1.0.0</code> playbook collection comes bundled with the SonicWall Firewall connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the SonicWall Firewall connector.</p>

<ul>
<li>Create Address Object Configuration</li>
<li>Delete Address Object Configuration</li>
<li>Get Address Object Configuration</li>
<li>Update Address Object Configuration</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>
