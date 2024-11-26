# openapi_client.HolidayModeApi

All URIs are relative to *https://api.onecta.daikineurope.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gateway_devices_gateway_device_id_management_points_embedded_id_holiday_mode_post**](HolidayModeApi.md#gateway_devices_gateway_device_id_management_points_embedded_id_holiday_mode_post) | **POST** /gateway-devices/{gatewayDeviceId}/management-points/{embeddedId}/holiday-mode | Add a holiday period


# **gateway_devices_gateway_device_id_management_points_embedded_id_holiday_mode_post**
> gateway_devices_gateway_device_id_management_points_embedded_id_holiday_mode_post(gateway_device_id, embedded_id, holiday_mode_body)

Add a holiday period

Insert a holiday period

### Example

* Bearer (JWT) Authentication (AccessTokenAuth):

```python
import openapi_client
from openapi_client.models.holiday_mode_body import HolidayModeBody
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
    api_instance = openapi_client.HolidayModeApi(api_client)
    gateway_device_id = '507f1f77bcf86cd799439011' # str | The id of the gatewayDevice to which the managementPoint belongs
    embedded_id = '1234' # str | The id of the managementPoint to which the characteristic belongs
    holiday_mode_body = openapi_client.HolidayModeBody() # HolidayModeBody | 

    try:
        # Add a holiday period
        api_instance.gateway_devices_gateway_device_id_management_points_embedded_id_holiday_mode_post(gateway_device_id, embedded_id, holiday_mode_body)
    except Exception as e:
        print("Exception when calling HolidayModeApi->gateway_devices_gateway_device_id_management_points_embedded_id_holiday_mode_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_device_id** | **str**| The id of the gatewayDevice to which the managementPoint belongs | 
 **embedded_id** | **str**| The id of the managementPoint to which the characteristic belongs | 
 **holiday_mode_body** | [**HolidayModeBody**](HolidayModeBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessTokenAuth](../README.md#AccessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource updated successfully |  -  |
**400** | Bad request |  -  |
**404** | Resource not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

