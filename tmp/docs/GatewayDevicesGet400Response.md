# GatewayDevicesGet400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** | message describing why error occured | 

## Example

```python
from openapi_client.models.gateway_devices_get400_response import GatewayDevicesGet400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayDevicesGet400Response from a JSON string
gateway_devices_get400_response_instance = GatewayDevicesGet400Response.from_json(json)
# print the JSON string representation of the object
print(GatewayDevicesGet400Response.to_json())

# convert the object into a dict
gateway_devices_get400_response_dict = gateway_devices_get400_response_instance.to_dict()
# create an instance of GatewayDevicesGet400Response from a dict
gateway_devices_get400_response_from_dict = GatewayDevicesGet400Response.from_dict(gateway_devices_get400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


