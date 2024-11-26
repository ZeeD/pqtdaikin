# GatewayDevice


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
from openapi_client.models.gateway_device import GatewayDevice

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayDevice from a JSON string
gateway_device_instance = GatewayDevice.from_json(json)
# print the JSON string representation of the object
print(GatewayDevice.to_json())

# convert the object into a dict
gateway_device_dict = gateway_device_instance.to_dict()
# create an instance of GatewayDevice from a dict
gateway_device_from_dict = GatewayDevice.from_dict(gateway_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


