# GatewayDevicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_cloud_connection_up** | [**BooleanCharacteristic**](BooleanCharacteristic.md) |  | [optional] 
**timestamp** | **str** | dateTime when gateway device was last updated | [optional] 
**mananagement_points** | [**List[ManagementPoint]**](ManagementPoint.md) |  | [optional] 
**id** | **str** | Object Id | [optional] 
**embedded_id** | **str** | The internal device id | [optional] 
**device_model** | **str** | The model of the gateway device | [optional] 

## Example

```python
from openapi_client.models.gateway_devices_inner import GatewayDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayDevicesInner from a JSON string
gateway_devices_inner_instance = GatewayDevicesInner.from_json(json)
# print the JSON string representation of the object
print(GatewayDevicesInner.to_json())

# convert the object into a dict
gateway_devices_inner_dict = gateway_devices_inner_instance.to_dict()
# create an instance of GatewayDevicesInner from a dict
gateway_devices_inner_from_dict = GatewayDevicesInner.from_dict(gateway_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


