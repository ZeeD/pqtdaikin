# ManagementPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded_id** | **str** | The id of the embedded device, this id can contain a number or a string. | [optional] 
**management_point_type** | **str** | The type of a management point | [optional] 
**management_point_sub_type** | **str** | The sub type of a management point | [optional] 
**management_point_category** | **str** | The category of a management point | [optional] 
**name** | [**StringCharacteristic**](StringCharacteristic.md) |  | [optional] 
**on_off_mode** | [**StringArrayCharacteristic**](StringArrayCharacteristic.md) |  | [optional] 
**consumption_data** | [**ObjectCharacteristic**](ObjectCharacteristic.md) |  | [optional] 
**ip_address** | [**StringCharacteristic**](StringCharacteristic.md) |  | [optional] 
**mac_address** | [**StringCharacteristic**](StringCharacteristic.md) |  | [optional] 
**firmware_version** | [**StringCharacteristic**](StringCharacteristic.md) |  | [optional] 
**serial_number** | [**StringCharacteristic**](StringCharacteristic.md) |  | [optional] 
**model_info** | [**StringCharacteristic**](StringCharacteristic.md) |  | [optional] 
**software_version** | [**StringCharacteristic**](StringCharacteristic.md) |  | [optional] 
**sensory_data** | [**ObjectCharacteristic**](ObjectCharacteristic.md) |  | [optional] 
**control_mode** | [**StringArrayCharacteristic**](StringArrayCharacteristic.md) |  | [optional] 
**powerful_mode** | [**StringArrayCharacteristic**](StringArrayCharacteristic.md) |  | [optional] 
**operation_mode** | [**StringArrayCharacteristic**](StringArrayCharacteristic.md) |  | [optional] 
**temperature_control** | [**ObjectCharacteristic**](ObjectCharacteristic.md) |  | [optional] 
**is_in_error_state** | [**BooleanCharacteristic**](BooleanCharacteristic.md) |  | [optional] 
**is_in_warning_state** | [**BooleanCharacteristic**](BooleanCharacteristic.md) |  | [optional] 
**is_in_caution_state** | [**BooleanCharacteristic**](BooleanCharacteristic.md) |  | [optional] 
**is_in_installer_state** | [**BooleanCharacteristic**](BooleanCharacteristic.md) |  | [optional] 
**is_in_emergency_state** | [**BooleanCharacteristic**](BooleanCharacteristic.md) |  | [optional] 
**is_holiday_mode_active** | [**BooleanCharacteristic**](BooleanCharacteristic.md) |  | [optional] 
**is_powerful_mode_active** | [**BooleanCharacteristic**](BooleanCharacteristic.md) |  | [optional] 
**error_code** | [**StringCharacteristic**](StringCharacteristic.md) |  | [optional] 
**schedule** | [**ObjectCharacteristic**](ObjectCharacteristic.md) |  | [optional] 
**holiday_mode** | [**ObjectCharacteristic**](ObjectCharacteristic.md) |  | [optional] 
**heatup_mode** | [**StringArrayCharacteristic**](StringArrayCharacteristic.md) |  | [optional] 
**setpoint_mode** | [**StringArrayCharacteristic**](StringArrayCharacteristic.md) |  | [optional] 
**fan_control** | [**ObjectCharacteristic**](ObjectCharacteristic.md) |  | [optional] 
**humidity_control** | [**ObjectCharacteristic**](ObjectCharacteristic.md) |  | [optional] 
**firmware_update** | [**ObjectCharacteristic**](ObjectCharacteristic.md) |  | [optional] 
**firmware_update_status** | [**StringArrayCharacteristic**](StringArrayCharacteristic.md) |  | [optional] 

## Example

```python
from openapi_client.models.management_point import ManagementPoint

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementPoint from a JSON string
management_point_instance = ManagementPoint.from_json(json)
# print the JSON string representation of the object
print(ManagementPoint.to_json())

# convert the object into a dict
management_point_dict = management_point_instance.to_dict()
# create an instance of ManagementPoint from a dict
management_point_from_dict = ManagementPoint.from_dict(management_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


