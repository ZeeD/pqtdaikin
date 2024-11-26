# openapi_client.GatewayDeviceApi

All URIs are relative to *https://api.onecta.daikineurope.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gateway_devices_gateway_device_id_get**](GatewayDeviceApi.md#gateway_devices_gateway_device_id_get) | **GET** /gateway-devices/{gatewayDeviceId} | Get the gatewayDevice and all its management points
[**gateway_devices_get**](GatewayDeviceApi.md#gateway_devices_get) | **GET** /gateway-devices | Get an array of gatewayDevices related to the user


# **gateway_devices_gateway_device_id_get**
> GatewayDevice gateway_devices_gateway_device_id_get(gateway_device_id)

Get the gatewayDevice and all its management points

With all their related characteristics

### Example

* Bearer (JWT) Authentication (AccessTokenAuth):

```python
import openapi_client
from openapi_client.models.gateway_device import GatewayDevice
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
    api_instance = openapi_client.GatewayDeviceApi(api_client)
    gateway_device_id = '657f1f77bcf86cd799439023' # str | The id of the gatewayDevice to which the managementPoint belongs

    try:
        # Get the gatewayDevice and all its management points
        api_response = api_instance.gateway_devices_gateway_device_id_get(gateway_device_id)
        print("The response of GatewayDeviceApi->gateway_devices_gateway_device_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GatewayDeviceApi->gateway_devices_gateway_device_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_device_id** | **str**| The id of the gatewayDevice to which the managementPoint belongs | 

### Return type

[**GatewayDevice**](GatewayDevice.md)

### Authorization

[AccessTokenAuth](../README.md#AccessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Not found _________ error codes:   * GATEWAY_DEVICE_MISSING   * SITE_MISSING |  -  |
**422** | Unprocessable Entity _________ error codes:   * INVALID_REQUEST |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gateway_devices_get**
> List[GatewayDevicesInner] gateway_devices_get()

Get an array of gatewayDevices related to the user

With all related management points and characteristics

### Example

* Bearer (JWT) Authentication (AccessTokenAuth):

```python
import openapi_client
from openapi_client.models.gateway_devices_inner import GatewayDevicesInner
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
    api_instance = openapi_client.GatewayDeviceApi(api_client)

    try:
        # Get an array of gatewayDevices related to the user
        api_response = api_instance.gateway_devices_get()
        print("The response of GatewayDeviceApi->gateway_devices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GatewayDeviceApi->gateway_devices_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GatewayDevicesInner]**](GatewayDevicesInner.md)

### Authorization

[AccessTokenAuth](../README.md#AccessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Not found _________ error codes:   * GATEWAY_DEVICE_MISSING |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

