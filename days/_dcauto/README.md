## :calendar: Day DCAUTO 1: 5/2/2021-5/14/2021

---

## Topics:

:clipboard: ACI COBRA SDK

:clipboard: ACI Ansible

---

## Resources:

#### ACI

:desktop_computer: [DevNet Always-On APIC](https://sandboxapicdc.cisco.com)

:snake: [COBRA Documentation](https://cobra.readthedocs.io/en/latest/)

:octocat: [DCAUTO COBRA Challenge GitHub Repo](https://github.com/wwt/cisco-aci-sdk)

:notebook: [ACI MIT Reference Image](https://www.cisco.com/c/dam/en/us/td/i/500001-600000/500001-510000/501001-502000/501289.jpg)

:octocat: [DCAUTO Ansible Challenge GitHub Repo](https://github.com/wwt/cisco-aci-ansible)

:milky_way: [Cisco ACI on Ansible Galaxy](https://galaxy.ansible.com/cisco/aci)



#### UCS

:snake: [**ucsmsdk** Documentation](https://ciscoucs.github.io/ucsmsdk_docs/ucsmsdk_ug.html#management-information-model)

:computer: [UCS DevNet Programmability Learning Labs](https://developer.cisco.com/learning/tracks/ucs-compute-prog)

:cloud: [dCloud UCS Programmability and Automation Lab](https://dcloud2-sjc.cisco.com/content/demo/4158)

:notebook_with_decorative_cover: [Intersight API Documentation](https://intersight.com/apidocs/introduction/overview/)

:milky_way: [Ansible Galaxy UCSM Collection](https://galaxy.ansible.com/cisco/ucs)

:milky_way: [Ansible Galaxy Intersight Collection](https://galaxy.ansible.com/cisco/ucs)

:computer: [Docker Image for UCS PowerTool](https://hub.docker.com/r/ciscodevnet/ucs-powertool-core-ms)

```shell
docker run -it --rm ciscodevnet/ucs-powertool-core:latest
```

:computer: UCSPE VM Connection Information:

- 192.168.72.4

:computer: UCS Director (UCSD) Guides:

- [REST API - Getting Started](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-director/rest-api-getting-started-guide/6-5/cisco-ucs-director-REST-API-getting-started-65.html)
- [REST API - Cookbook](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-director/rest-api-cookbook/6-5/cisco-ucs-director-REST-API-cookbook-65.html)
- [Orchestration Guide](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/ucs-director/orchestration-guide/6-8/cisco-ucs-director-orchestration-68.html)



#### Nexus 9000

:notebook: [Best Practics and Useful Scripts for EEM](https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-xe-16/216091-best-practices-and-useful-scripts-for-ee.html)

:computer: ATC CML Nexus 9000:

- 10.255.70.238
- admin/admin

---

## Tasks:

:white_check_mark: Create and complete ACI COBRA SDK challenge Jupyter notebook - **5/2/21**

:white_check_mark: Review Ansible study group recording - **5/2/21**

:white_check_mark: Retake COBRA SDK exercise - **5/3/21**

:white_check_mark: Start UCS study - **5/4/21**

:white_check_mark: DevNet UCS PowerTool Beginning Learning Labs - **5/5/21**

:white_check_mark: DevNet UCS Director Learning Labs - **5/6/21**

:white_check_mark: DevNet Python SDK Learning Labs - **5/6/21**

:white_check_mark: DevNet Python SDK Learning Labs - **5/7/21**

:white_check_mark: DevNet UCS PowerTool & Python SDK Intermediate Learning Labs - **5/7/21**

:white_large_square: UCS Ansible - just 5/8/21

:white_large_square: Retake ACI exercises - **5/8/21**

:white_large_square: Intersight UCS Learning Labs - **5/8/21**

:white_large_square: DCNM - **5/12/21**

---

## Notes:

#### :notebook: 5/2/21

:telescope: [REST API Challenge](apic_cobra_sdk_exercises.ipynb)

- :green_book: [Solution](solutions/apic_cobra_sdk_exercise_solution.ipynb)

:telescope: [COBRA SDK Challenge](apic_rest_exercises.ipynb)

- :green_book: [Solution](solutions/apic_rest_exercise_solution.ipynb)

:notebook: [Ansible Configuration File Reference](https://docs.ansible.com/ansible/latest/installation_guide/intro_configuration.html)

:notebook: [Ansible Inventory File Reference](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html)



---



#### :notebook: 5/3/21

:book: Work through COBRA SDK challenge again

- Augment challenge with **vz** prefix objects (Filter, Entry, Subject, Contract, etc.)

:book: Complete [Cisco Ansible DevNet learning lab](https://developer.cisco.com/learning/tracks/aci-programmability/ansible-aci-intro/aci_ansible_part2/step/1)

- Augment Ansible playbook with additional modules (Filter, Entry, Subject, Contract, etc)



---



#### :notebook: 5/4/21

:computer: Watch DCAUTO UCS/Intersight video

- Write sample code with the Python `uscmsdk` to manage **blade** objects.
- Write sample code with the Python `ucsmsdk` to setup a UCSM environment.



---



#### :notebook: 5/5/21

- [UCS PowerTool Introduction](https://developer.cisco.com/learning/modules/ucs-powertool-introduction)

:computer: DevNet UCS Manager PowerTool Part I

```powershell
# Connect to UCS
Connect-Ucs -Name 192.168.72.4

# Get the UCS PowerShell session
Get-UcsPSSession

# Disconnect from UCS
Disconnect-Ucs

# Get UCS Blades (class computeBlade)
Get-UcsBlade

# Get UCS Blade DNs (only)
Get-UcsBlade | Select-Object Dn

# Get UCS Rack Servers (class computeRackUnit)
Get-UcsRackUnit

# Get UCS Rack Server DNs (only)
Get-UcsRackUnit | Select-Object dn

# Get all UCS servers by abstract class (computePhysical)
Get-UcsServer | Select-Object dn

# Retreive UCS blade and rack servers by DN, with a parameter query
Get-UcsBlade -Dn sys/chassis-3/blade-7
Get-UcsRackUnit -Dn sys/rack-unit-8

# Get UCS blades and display select attributes
Get-UcsBlade | Select-Object Dn, TotalMemory, NumOfCpus, Serial

# Add the SlotId parameter to the previous command and notice the output format change
Get-UcsBlade | Select-Object Dn, TotalMemory, NumOfCpus, Serial, SlotId

# Preserver the table output view with the previous command
Get-UcsBlade | Select-Object Dn, TotalMemory, NumOfCpus, Serial, SlotId | Format-Table

# Display format graphically (requires Windows desktop)
Get-UcsBlad | Select-Object Dn, TotalMemory, NumOfCpus, Serial, Slot-Id | Out-GridView

# Use a paramater to filter, display only servers with 4 CPUs
Get-UcsBlade -NumOfCpus 4 | Select-Object Dn, TotalMemory, NumOfCpus, Serial, SlotId | Format-Table

# Filter with a Where-Object expression
Get-UcsBlade | Where-Object {$_.NumOfCpus -eq 4} | Select-Object Dn, TotalMemory, NumOfCpus, Serial, SlotId | Format-Table

### PowerShell Shortcuts ###
# Select = Select-Object
# ? - Where-Object
# ft = Format-Table
# ogv - Output-GridView
# % = foreach

```



---



:computer: DevNet UCS Manager PowerTool Part II

```powershell
# List all PowerTool Cmdlets
Get-Command -Module Cisco.UCSManager | more

# Get a total count of all PowerTool Cmdlets
Get-Command -Module Cisco.UCSManager | Measure-Object

# Display an alphabetical list of PowerTool verbs (only)
Get-Command -Module Cisco.UCSManager | ?{$_.Name -match '-'} | %{$_.Name.Substring(0, ($_.Name.IndexOf('-')))} | Sort-Object -Unique

# Connect to UCS without HTTPS (using HTTP)
Connect-Ucs -Name 192.168.72.4 -NoSsl

# Display the HTTP session details and notice the 'RedirectState parameter'
Get-UcsHttp

# Disable HTTPS redirection
Get-UcsHttp | Set-UcsHttp -RedirectState disabled -Force

# Get the UCS Lan Cloud VLANs
Get-UcsLanCloud | Get-UcsVlan -SwitchId dual | Select Dn, Id, Name

# Create a single VLAN
Get-UcsLanCloud | Add-UcsVlan -Name vlan100 -Id 100

# Add a range of VLANs
## Create an object for the Lan Cloud (parent object of VLANs)
$lanCloud = Get-UcsLanCloud

## Use a PowerShell range object to specify a numeric range and loop over the range
## to create new VLANs
120..129 | ForEach-Object {Add-UcsVlan -LanCloud $lanCloud -Name vlan$_ -Id $_}

# View properties for a specific VLAN
Get-UcsVlan -Id 100

# Get the 'Sharing' parameter for a VLAN
Get-UcsVlan -Id 100 | Select Sharing

# Update the 'Sharing' parameter for many VLANs
120..129 | %{Get-UcsVlan -Id $_ | Set-UcsVlan -Sharing community -Force}

# Perform a "whatIf" delete for many VLANs
## There will be output only for objects that the delete would apply to
120..129 | %{Get-UcsVlan -id $_ | Remove-UcsVlan -WhatIf}

# Perform a delete of many VLANs
120..129 | %{Get-UcsVlan -Id $_ | Remove-UcsVlan -Force}

```

```xml
// 'Copy XML' output from the default VLAN (1) in the UCS LAN Cloud'
// The XML tag name is the class ID (fabricVlan)
<fabricVlan
            assocPrimaryVlanState="ok"
            assocPrimaryVlanSwitchId="NONE"
            childAction="deleteNonPresent"
            cloud="ethlan"
            compressionType="included"
            configIssues=""
            configOverlap="ok"
            defaultNet="yes"
            dn="fabric/lan/net-default"
            epDn=""
            fltAggr="0"
            global="0"
            id="1"
            ifRole="network"
            ifType="virtual"
            local="0"
            locale="external"
            mcastPolicyName=""
            name="default"
            operMcastPolicyName="org-root/mc-policy-default"
            operState="ok"
            overlapStateForA="active"
            overlapStateForB="active"
            peerDn=""
            policyOwner="local"
            pubNwDn=""
            pubNwId="1"
            pubNwName=""
            sharing="none"
            switchId="dual"
            transport="ether"
            type="lan"
/>
```

```powershell
# Create a multi-object transaction
# This is an atomic transaction which does not allow objects to have any dependencies
# on other objects within the transaction

# Determine if there are any transactions in progress
Get-UcsPsSession | Select NumPendingConfigs, TransactionInProgress

# Start a multi-object transaction and re-check the UCS PS Session status
Start-UcsTransaction
Get-UcsPsSession | Select NumPendingConfigs, TransactionInProgress

# Create two new VLANs and check the UCS PS Session status
$lanCloud = Get-UcsLanCloud
Add-UcsVlan -LanCloud $lanCloud -Name vlan100 -Id 100
Add-UcsVlan -LanCloud $lanCloud -Name vlan101 -Id 101
Get-UcsPsSession | Select NumPendingConfigs, TransactionInProgress

# Complete the UCS multi-object transaction and re-check the UCS PS session status
Complete-UcsTransaction
Get-UcsPsSession | Select NumPendingConfigs, TransactionInProgress

# Remove the VLANs with a multi-object transaction and re-check the UCS PS session status
Start-UcsTransaction
Get-UcsVlan -Id 100 | Remove-UcsVlan
Get-UcsVlan -Id 101 | Remove-UcsVlan
Complete-UcsTransaction -Force
Get-UcsPsSession | Select NumPendingConfigs, TransactionInProgress
```



:computer: DevNet UCS Manager PowerTool Part Ii

```powershell
# Export credentials from a Connect-Ucs session

$UCSM = '10.10.20.113'
Connect-Ucs -Name $UCSM

# Create a new local directory
New-Item -ItemType Directory ucs-sessions

# Export the current UCS PowerShell session
## The key is 'password'
Export-UcsPsSession -Path ./ucs-sessions/ucspe.xml
```

```xml
// UCS session export contents
<basehandles>
  <ucshandles>
    <ucs name="10.10.20.113" username="admin" password="/kcAoRX5Uc0tuioq+vlapA==" />
  </ucshandles>
  <imchandles />
  <ucscentralhandles />
</basehandles>
```

```powershell
# Connect to UCS with the stored session credentials
Connect-Ucs -Path ./ucs-sessions/ucspe.xml

# Create a System.Security.SecureString object to pass the key paramater to Connect-Ucs
$Key = $(ConvertTo-SecureString 'password' -AsPlainText -Force)

# Connect to UCS using the Key parameter
Connect-Ucs -Path ./ucs-sessions/ucspe.xml -Key $Key

# Create a Microsoft PowerShell Credential object with the username and the
# SecureString password
$UCS_PW = ConvertTo-SecureString 'password' -AsPlainText -Force
$UCS_CREDS = New-Object System.Management.Automation.PSCredential ('admin', $UCS_PW)

# Connect to UCS with the PowerShell Credential object
Connect-Ucs -Name $UCSM -Credential $UCS_CREDS
```



```raw
# Create a Boot Policy in UCS Manager HTML GUI

Add a Boot Policy with the Name LocalBoot_01_PS
Add a Local Lun from "Local Devices"
Add a Local CD/DVD from "Local Devices"

Right-Click "Boot Policies" in the "Policies" Group under the "root" Organization
Click "Create Boot Policy"
Enter "LocalBoot_01_PS" in the Name field
Click "Local Devices" to expand the section
Click "Add Local Lun" under "Add Local Disk"
Select "Any"
Click "OK"
Click "Add Local CD/DVD" under "Add CD/DVD"
Click "OK" 
```

```powershell
# Use UCS PowerTool to retreive the Boot Policy and generate the UCS PowerTool code
# which would also create the boot policy
Get-UcsBootPolicy -Name LocalBoot_01_PS -Hierarchy | ConvertTo-UcsCmdlet > New-BootPolicy.ps1

# Generated PowerShell commands
######
Start-UcsTransaction
$mo = Get-UcsOrg -Level root  | Add-UcsBootPolicy -ModifyPresent  -BootMode "legacy" -Descr "" -EnforceVnicName "yes" -Name "LocalBoot_01_PS" -PolicyOwner "local" -RebootOnUpdate "no"
$mo_1 = $mo | Add-UcsLsbootVirtualMedia -ModifyPresent -Access "read-only-local" -LunId "0" -MappingName "" -Order 2
$mo_2 = $mo | Add-UcsLsbootStorage -ModifyPresent -Order 1
$mo_2_1 = $mo_2 | Add-UcsLsbootLocalStorage -ModifyPresent
$mo_2_1_1 = $mo_2_1 | Add-UcsLsbootLocalHddImage -ModifyPresent -Order 1
Complete-UcsTransaction
######
```



```xml
// Use the UCS Manager GUI to capture UCS XML API log entries as a source to generate
// UCS PowerTool commands
// In the GUI, press ctrl-alt-q and click the link at the top of the screen to 'Record XML'
// Stop recording after creating objects and download the XML file (sample below)

[------------- Sending Request to Server ------------

<configResolveDn
dn="sys"
cookie="1620268133/3e13cce4-65d9-4548-9714-5ecacc035fd3"
inHierarchical="false">
</configResolveDn>

<configEstimateImpact
cookie="1620268133/3e13cce4-65d9-4548-9714-5ecacc035fd3">
    <inConfigs>
<pair key="org-root/mac-pool-MAC_POOL_PS">
    <macpoolPool
    name="MAC_POOL_PS"
    dn="org-root/mac-pool-MAC_POOL_PS"
    
    status="created"
    
    sacl="addchild,del,mod">
        <macpoolBlock
        from="00:25:B5:00:00:00"
        to="00:25:B5:00:00:7F"
        
        rn="block-00:25:B5:00:00:00-00:25:B5:00:00:7F"
        status="created"
        
        sacl="addchild,del,mod">
        </macpoolBlock>
    </macpoolPool>
</pair>
    </inConfigs>
</configEstimateImpact>

<configConfMos
cookie="1620268133/3e13cce4-65d9-4548-9714-5ecacc035fd3"
inHierarchical="false">
    <inConfigs>
<pair key="org-root/mac-pool-MAC_POOL_PS">
    <macpoolPool
    name="MAC_POOL_PS"
    dn="org-root/mac-pool-MAC_POOL_PS"
    
    status="created"
    
    sacl="addchild,del,mod">
        <macpoolBlock
        from="00:25:B5:00:00:00"
        to="00:25:B5:00:00:7F"
        
        rn="block-00:25:B5:00:00:00-00:25:B5:00:00:7F"
        status="created"
        
        sacl="addchild,del,mod">
        </macpoolBlock>
    </macpoolPool>
</pair>
    </inConfigs>
</configConfMos>

<configResolveChildren
cookie="1620268133/3e13cce4-65d9-4548-9714-5ecacc035fd3"
classId="macpoolBlock"
inDn="org-root/mac-pool-MAC_POOL_PS"
inHierarchical="false">
    <inFilter>
    </inFilter>
</configResolveChildren>

<configResolveDn
dn="sys"
cookie="1620268133/3e13cce4-65d9-4548-9714-5ecacc035fd3"
inHierarchical="false">
</configResolveDn>

<configEstimateImpact
cookie="1620268133/3e13cce4-65d9-4548-9714-5ecacc035fd3">
    <inConfigs>
<pair key="org-root/mac-pool-MAC_POOL_PS/block-00:25:B5:00:00:80-00:25:B5:00:00:FF">
    <macpoolBlock
    from="00:25:B5:00:00:80"
    to="00:25:B5:00:00:FF"
    dn="org-root/mac-pool-MAC_POOL_PS/block-00:25:B5:00:00:80-00:25:B5:00:00:FF"
    
    status="created"
    
    sacl="addchild,del,mod">
    </macpoolBlock>
</pair>
    </inConfigs>
</configEstimateImpact>

<configConfMos
cookie="1620268133/3e13cce4-65d9-4548-9714-5ecacc035fd3"
inHierarchical="false">
    <inConfigs>
<pair key="org-root/mac-pool-MAC_POOL_PS/block-00:25:B5:00:00:80-00:25:B5:00:00:FF">
    <macpoolBlock
    from="00:25:B5:00:00:80"
    to="00:25:B5:00:00:FF"
    dn="org-root/mac-pool-MAC_POOL_PS/block-00:25:B5:00:00:80-00:25:B5:00:00:FF"
    
    status="created"
    
    sacl="addchild,del,mod">
    </macpoolBlock>
</pair>
    </inConfigs>
</configConfMos>

<configEstimateImpact
cookie="1620268133/3e13cce4-65d9-4548-9714-5ecacc035fd3">
    <inConfigs>
<pair key="org-root/mac-pool-MAC_POOL_PS">
    <macpoolPool
    dn="org-root/mac-pool-MAC_POOL_PS"
    
    status="deleted,modified"
    
    sacl="addchild,del,mod">
    </macpoolPool>
</pair>
    </inConfigs>
</configEstimateImpact>

<configConfMos
cookie="1620268133/3e13cce4-65d9-4548-9714-5ecacc035fd3"
inHierarchical="false">
    <inConfigs>
<pair key="org-root">
    <orgOrg
    name="root"
    dn="org-root"
    
    status="created,modified"
    
    sacl="addchild,del,mod">
        <macpoolPool
        
        rn="mac-pool-MAC_POOL_PS"
        status="deleted,modified"
        
        sacl="addchild,del,mod">
        </macpoolPool>
    </orgOrg>
</pair>
    </inConfigs>
</configConfMos>
-----------------------------------------------------]

```

```powershell
# Convert the XML log file contents into UCS PowerTool commands
ConverTo-UcsCmdlet -xml -LiteralPath MAC_POOL_OPS_PS_xmlReq.log > MAC_POOL_OPS.ps1
```



:floppy_disk: UCS Director REST API

- API endpoint to request API key

```raw
https://{{ucsd}}/app/api/rest?opName=getRESTKey&user={{username}}&password={{password}}
```

- UCSD authentication header

```raw
X-Cloupia-Request-Key
```

- There are three possible URL query parameters:
  - `opName` - name of the current operation
  - `opData`- payload body
  - `formatType` - json (default) or xml
- API operation query parameter values `opName=*value*`

```raw
# Get user profile
userAPIGetMyLoginProfile

# Modify user profile password
userAPIModifyLoginProfilePassword

```

* Modify a user password

```raw
# Construct a payload, spaces are optional
{param0: {"oldPassword": "ciscopsdt", "newPassword": "new-password"}}

# Set the endpoint
https://{{ucsd}}/app/api/rest?formatType=json&opName=userAPIModifyLoginProfile?opData={param0: {"oldPassword": "ciscopsdt", "newPassword": "ciscopsdt1"}}
```



---



#### :notebook: 5/6/21

##### UCS Director, continued

- Automatically update the Postman environment variable for the **api_key** using automated test code (in the **Tests** tab of a request)

```javascript
// The environment variable to update is "api_key"
if (request.url.includes(getRESTKey)) {
  postman.setEnvironmentVariable("api_key", responseBody.replace(/"g, ""))
}
```



* UCSD Custom Workflow Task Script

```javascript
var input1 = input.firstInput;
var input2 = input.secondInput;

var outputMsg = "OUTPUT :" +input1 + " " +input2;
output.firstOutput=outputMsg;
```

* Invoke a UCSD Workflow via REST API

```json
// API Endpoint
// userAPISubmitWorkflowServiceRequest
// opData JSON payload (unformatted)
{param0: "InvokeCustTask", param1: {"list": [{"name": "First Input", "value": "Babs"}, {"name": "Second Input", "value": "Skip"}]}, param2: -1}

// formatted
{
  param0: "InvokeCustTask",
  param1: {
    "list": [
      {
        "name": "firstInput",
        "value": "Babs"
      },
      {
        "name": "secondInput",
        "value": "Skip"
      }
    ]
  },
  param2: -1
}
```



##### :snake: Python SDK

```python
# Connect to UCS
from ucsmsdk.ucshandle import UcsHandle

UCS_CONN = {
  'ip': '192.168.72.4',
	'username': 'admin',
	'password': 'admin',
  'secure': False
}

handle = UcsHandle(**UCS_CONN)
handle.login()
```

```python
# Review handle object attributes
vars(handle)

handle.ip
handle.ucs
handle.cookie
```

```python
# Query and display all compute blade objects
blades = handle.query_classid('computeBlade')

for blade in blades:
  print(blade)
```

```python
# Display specific blade attributes
for blade in blades:
  print(blade.dn, blade.num_of_cpus, blade.available_memory)
```



- SDK Query Methods

```python
# Get objects from a single class
query_classid # returns a list of objects
handle.query_classid('computeBlade')

# Get objects from multiple classes
query_classids # returns a dictionary where classid is the key and objects are value
handle.query_classids('computeBlade', 'computeRackUnit')

# Get a single object by DN
query_dn # Returns an object
handle.query_dn('sys/chassis-3/blade-1')

# Get multiple objects by DN
query_dns # Returns a dictionary where the DN is the key and the object is the value
handle.query_dn('sys/chassis-3/blade-1', 'sys/chassis-3/blade-3')

# Get child objects for a specific object
query_children # Returns a list
handle.query_children(handle.query_dn('sys/chassis-3/blade-1'))
```



* Get Server DN and LED State

```python
# Get all server objects, using classes
servers = handle.query_children('computeBlade', 'computeRackUnit')

# Loop over all servers
for server_class in servers.values():
    # Loop over each server class object
    for server in server_class:
      # Assign the equipmentLocatorLed class data to a variable
      led = handle.query_children(server, class_id='equipmentLocatorLed')
      print(server.dn, led[0].oper_state)
```

- Chanege the state of all LEDs

```python
# Get a list of all server objects, by class
# Each class becomes its own dictionary key
server_classes = handle.query_classids('computeBlade', 'computeRackUnit')

# Loop over each server class object list (computeBlade and computeRackUnit)
for server_list in server_classes.values():
      # Loop over each server object within the list
      for server in server_list:
        # Get server LED status
        led = handle.query_children(server, class_id='equipmentLocatorLed')
        # Set previous LED status
        prev_led_status = led[0].oper_state

        # Set the new LED status
        if led[0].oper_state == 'off':
            led[0].admin_state = 'on'
        else:
          led[0].admin_state = 'off'

        # Set the handle MO value and commit the change
        handle.set_mo(led[0])
        handle.commit()
        
        # Display output
        print(f'DN {server.dn}:\n'
              f'\tPrevious - {prev_led_status}\n'
              f'\tNew - {led[0].admin_state}')
```



---



#### :notebook: 5/7/21

##### :snake: Python SDK, continued

*  Query the locator LED status for all servers, reverse the setting, and display results

```python
# Get lists of all servers (returns a dict)
servers = handle.query_classids('computeBlade', 'computeRackUnit')

# Loop over each of the dict values (separate lists of server classes)
for server_classes in servers.values():
  # Loop over each individual server class

  for server in server_classes:
  	# Get the LED subclass status for each server
	  led = handle.query_children(server, class_id='EquipmentLocatorLed')

    # Get the current LED properties
    led_dn = led[0].dn
    led_oper_state = led[0].oper_state

    # Reverse the LED state
    if led_oper_state == 'off':
    	led[0].admin_state = 'on'
    else:
      led[0].admin_state = 'off'
     
		# Set the new LED state
    handle.set_mo(led[0])
    handle.commit()

    # Get the updated status
    led_new_props = handle.query_dn(led_dn)

    # Display the results
    print(f'Locator LED State for {server.dn}:\n'
          f'\tPrevious state - {led_oper_state}\n'
          f'\tNew state - {led_new_props.admin_state}')
```



* Create a new VLAN

```python
# Import the UcsHandle and FabricVlan modules
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

# Connect to the UCSM
UCSM_CONN = {
  'ip': '192.168.72.4',
  'username': 'admin',
  'password': 'admin',
  'secure': False
}

handle = UcsHandle(**UCSM_CONN)
handle.login()

# Get the FabricLanCloud class
lan_cloud = handle.query_classid('FabricLanCloud')

# Display the lan_cloud DN
# lan_cloud[0].dn

# Create a MO for the VLAN
vlan_mo = FabricVlan(lan_cloud[0].dn, name='vlan100', id='100')

# Add the VLAN MO to the UCS
handle.add_mo(vlan_mo)
# handle.add_mo(mo=vlan_mo, modify_present=True)
handle.commit()
```



* Create multiple VLANs in a transaction

```python
# Import the UcsHandle and FabricVlan modules
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

# Connect to the UCSM
UCSM_CONN = {
  'ip': '192.168.72.4',
  'username': 'admin',
  'password': 'admin',
  'secure': False
}

handle = UcsHandle(**UCSM_CONN)
handle.login()

# Create a FabricLanCloud MO
lan_cloud = handle.query_classid('FabricLanCloud')

# Loop over a range of VLAN numbers
for vlan in range (300, 303):
  # Create a MO for each VLAN
  vlan_mo = FabricVlan(
    parent_mo_or_dn=lan_cloud[0].dn,
    name=f'vlan{vlan}',
    id=str(vlan)
  )

  # Add each MO to the handle object
  handle.add_mo(vlan_mo)

# Commit the changes to UCSM
handle.commit()
```



* Delete multiple VLANs in a transaction

```python
# Import modules
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

# Log in
CONN = {
  'ip': '192.168.72.4',
  'username': 'admin',
  'password': 'admin',
  'secure': False
}

handle = UcsHandle(**CONN)
handle.login()

# Create a MO for all VLANs
vlans_mo = handle.query_classid('FabricVlan')

# Loop over the list of VLANs (in the vlans_mo), and remove them, except for VLAN 1
for vlan_mo in vlans_mo:
  if vlan_mo.id != '1':
	  handle.add_mo(vlan_mo)

handle.commit()
```



##### :computer: UCS PowerTool Intermediate

- Time zones, NTP, & DNS

```powershell
# Get UCSM properties
Get-UcsTimeZone
Get-UcsNtpServer
Get-UcsDns # Specifies system domain name

```

```powershell
# Set UCSM time zone
# First, get the time zone object to update and pipe it to the Set-UcsTimeZone Cmdlet
Get-UcsTimezone | Set-UcsTimezone -Timezone America/Los_Angeles -Force
```

```powershell
# Add an NTP server
# Pipe the current time zone object to the Add-UcsNtpServer command in order to send
# a 'Cisco.Ucsm.CommDateTime' object to the Cmdlet (a System.String for the time zone)
# will not work.

Get-UcsTimezone | Add-UcsNtpServer -name 172.16.20.5

# Remove an NTP server
Get-UcsNtpServer -Name 172.16.20.5 | Remove-UcsNtpServer -Force
```

```powershell
# Add a DNS server by piping it to the UcsDns object
Get-UcsDns | Add-UcsDnsServer -Name 8.8.8.8

# Remove a DNS server
Get-UcsDnsServer -Name 8.8.8.8 | Remove-UcsDnsServer
```



- Export and Import UCSM configurations
  - Four types of backups
    - Full-state - not available with PowerTool
    - All configuration - all system and logical configuration settings
    - System configuration - usernames, roles, locales, etc.
    - Logical configuration - service profiles, VLANs, VSANs, pools, policies, etc.

```powershell
# Backup all configuration
Backup-Ucs -Type config-all -PathPattern ./config-all.xml

# Backup with a PathPattern which includes variables
Backup-Ucs -Type config-logical -PathPattern ./${ucs}-${yyyy}${MM}${dd}-${HH}${mm}-config-logical.xml

ucs - Name of the UCS System
yyyy - Four-digit year
MM - Two-digit month
dd - Two-digit day
HH - Two-digit hour (24-hour clock)
mm - Two-digit minute
```

```powershell
# Import UCS configuration
Import-UcsBackup -Merge -LiteralPath ./config-all.xml
```



:snake: UCS Python SDK Intermediate

* UCSM time zone and NTP settings

```python
# Import UcsHandle
from ucsmsdk.ucshandle import UcsHandle

# Login
UCSM = {
  'ip': '192.168.72.4',
  'username': 'admin',
  'password': 'admin',
  'secure': 'false'
}

handle = UcsHandle(**UCSM)
handle.login()
```

- Get time zones

```python
# Import the CommDateTime class
from ucsmsdk.mometa.comm.CommDateTime import CommDateTime

# Query the CommDateTime DN that is a reference to the 'Timezone-managed' object
timezone_mo = handle.query_dn('sys/svc-ext/datetime-svc')
# timezone_mo = handle.query_classid('CommDatTime') # Also works the same way
```

* Get NTP

```python
# Import the CommNtpProvider class
from ucsmsdk.mometa.comm.CommNtpProvider import CommNtpProvider

# Create a MO for the NTP objects
ntp_mos = handle.query_classid('CommNtpProvider')

# Display NTP object details
for n in ntp_mos:
  print(n)
```

* Get DNS

```python
# Import classes and create MOs
from ucsmsdk.mometa.comm.CommDns import CommDns
dns_mo = handle.query_classid('CommDns')
print(dns_mo[0])

from ucsmsdk.mometa.comm.CommDnsProvider import CommDnsProvider
dns_mos = handle.query_classid('CommDnsProvider')
print(dns_mos[0])
```

- Set time zones

```python
# Create a time zone variable
tz = 'America/Chicago'

# Update the time zone MO with the new value
timezone_mo[0].timezone = tz

# Update the MO
handle.set_mo(timezone_mo[0])
```



- Add and remove NTP servers

```python
# Create NTP server veriable
ntp_server = '172.16.20.5'

# Create an NTP parent MO
datetime_mo = handle.query_dn('sys/svc-ext/datetime-svc')

# Create an NTP MO
ntp_mo = CommNtpProvider(
	datetime_mo,
  name='172.16.20.5'
)

# Add and commit the MO
handle.add_mo(
	mo=ntp_mo,
  modify_present=True
)
handle.commit()

# Get a new MO for the new NTP provider
ntp_class = handle.query_classid('CommNtpProvider')
ntp_mo = ntp_class[0]

# Remove the NTP provider
handle.remove_mo(ntp_mo)
handle.commit()
```



- Add and remove DNS servers

```python
# Get parent DNS service object
dns_svc_mo = handle.query_dn('sys/svc-ext/dns-svc')

# Create a DNS provider MO
dns_provider_mo = CommDnsProvider(dns_svc_mo, name='8.8.8.8')

# Add and commit the MO to UCSM
handle.add_mo(dns_provider_mo, True)
handle.commit()

# Remove the DNS Provider
dns_providers_mo = handle.query_classid('CommDnsProvider')

### Option #1, loop ###
# Loop over the DNS providers and remove the entry for 8.8.8.8
for dns_server in dns_providers_mo:
  if dns_server.name == '8.8.8.8':
    dns_server_mo = dns_server
    handle.remove_mo(dns_server_mo)
    handle.commit()
    
### Option #2, user a filter string in the query_classid method ###
dns_provider_mos = handle.query_classid(
  class_id='CommDnsProvider',
  filter_str='(dn, "sys/svc-ext/dns-svc/*", type="re")'
)
```

* Handle query filter

```raw
handle.query_classid(
    class_id=None,
    filter_str=None,
    hierarchy=False,
    need_response=False,
    timeout=None,
)
Docstring:
Finds an object using it's class id.

Args:
    class_id (str): class id of the object to be queried for.
    filter_str(str): query objects with specific property with specific value or pattern specifying value.

              (property_name, "property_value, type="filter_type")

              property_name: Name of the Property
              ## example, dn (without quotes) ##

              property_value: Value of the property (str or regular expression)
              ## example, "sys/svc-ext/dns-svc/*" (with quotes) ##

              filter_type: eq - equal to

                           ne - not equal to

                           ge - greater than or equal to

                           gt - greater than

                           le - less than or equal to

                           lt - less than

                           re - regular expression

							## example, "re" (with quotes) ##

              logical filter type: not, and, or
```



* Backup UCS configuration

```python
# Import the backup_ucs class
from ucsmsdk.utils.ucsbackup import backup_ucs

# Perform the backup
backup_ucs(
  handle,
  'config-all',
  './',
  'py-sdk-config-all.xml'
)
```

```raw
# backup_ucs doc string
backup_ucs(
    handle,
    backup_type,
    file_dir,
    file_name,
    timeout_in_sec=600,
    preserve_pooled_values=False,
)
Docstring:
backup_ucs helps create and download Ucs backups.

Args:
    handle (UcsHandle): Ucs Connection handle
    backup_type (str): type of backup
                    i.e. fullstate/config-logical/config-system/config-all
    file_dir (str): directory to download ucs backup file to
    file_name (str): name for the backup file
                     (supported file extension are '.tar.gz' and '.xml')
    timeout_in_sec (number) : time in seconds for which method waits
                          for the backUp file to generate before it exits.
    preserve_pooled_values (boolean): True/False,
                                        False - by default

Example:
    file_dir = "/home/user/backup"

    file_name = "config_backup.xml"

    backup_ucs(handle, backup_type="config-logical",
                file_dir=file_dir, file_name=file_name)
```



- Import UCS configuration

```python
# Import UCS configuration
from ucsmsdk.utils.ucsbackup import import_ucs_backup

# Import configuration
import_ucs_backup(
	handle,
  './',
  'py-sdk-config-all.xml',
  merge=True
)
```

