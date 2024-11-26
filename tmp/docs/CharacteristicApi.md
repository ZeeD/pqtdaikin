# openapi_client.CharacteristicApi

All URIs are relative to *https://api.onecta.daikineurope.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gateway_devices_gateway_device_id_management_points_embedded_id_characteristics_name_patch**](CharacteristicApi.md#gateway_devices_gateway_device_id_management_points_embedded_id_characteristics_name_patch) | **PATCH** /gateway-devices/{gatewayDeviceId}/management-points/{embeddedId}/characteristics/{name} | Update characteristic information.


# **gateway_devices_gateway_device_id_management_points_embedded_id_characteristics_name_patch**
> gateway_devices_gateway_device_id_management_points_embedded_id_characteristics_name_patch(gateway_device_id, embedded_id, name, characteristic_patch_value)

Update characteristic information.

Update characteristic information.

### Example

* Bearer (JWT) Authentication (AccessTokenAuth):

```python
import openapi_client
from openapi_client.models.characteristic_patch_value import CharacteristicPatchValue
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.onecta.daikineurope.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.onecta.daikineurope.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): AccessTokenAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CharacteristicApi(api_client)
    gateway_device_id = 'f28f4e28-b993-4ba0-a3d3-386503c5a1d0' # str | The id of the gatewayDevice to which the managementPoint belongs
    embedded_id = 'climateControl' # str | The id of the managementPoint to which the characteristic belongs
    name = 'onOffMode' # str | The name of the characteristic to update
    characteristic_patch_value = {"value":"on"} # CharacteristicPatchValue | 

    try:
        # Update characteristic information.
        api_instance.gateway_devices_gateway_device_id_management_points_embedded_id_characteristics_name_patch(gateway_device_id, embedded_id, name, characteristic_patch_value)
    except Exception as e:
        print("Exception when calling CharacteristicApi->gateway_devices_gateway_device_id_management_points_embedded_id_characteristics_name_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_device_id** | **str**| The id of the gatewayDevice to which the managementPoint belongs | 
 **embedded_id** | **str**| The id of the managementPoint to which the characteristic belongs | 
 **name** | **str**| The name of the characteristic to update | 
 **characteristic_patch_value** | [**CharacteristicPatchValue**](CharacteristicPatchValue.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessTokenAuth](../README.md#AccessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource updated successfully |  -  |
**400** | Bad request _________ error codes:   * READ_ONLY_CHARACTERISTIC   * INVALID_CHARACTERISTIC_VALUE |  -  |
**404** | Not found _________ error codes:   * GATEWAY_DEVICE_MISSING   * MANAGEMENT_POINT_MISSING   * CHARACTERISTIC_MISSING |  -  |
**409** | Conflict _________ error codes:   * MANAGEMENT_POINT_BLOCKED |  -  |
**422** | Unprocessable Entity _________ error codes:   * INVALID_REQUEST |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

