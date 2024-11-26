# GatewayDeviceBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded_id** | **str** | The internal device id | [optional] 
**device_model** | **str** | The model of the gateway device | [optional] 

## Example

```python
from openapi_client.models.gateway_device_body import GatewayDeviceBody

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayDeviceBody from a JSON string
gateway_device_body_instance = GatewayDeviceBody.from_json(json)
# print the JSON string representation of the object
print(GatewayDeviceBody.to_json())

# convert the object into a dict
gateway_device_body_dict = gateway_device_body_instance.to_dict()
# create an instance of GatewayDeviceBody from a dict
gateway_device_body_from_dict = GatewayDeviceBody.from_dict(gateway_device_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


