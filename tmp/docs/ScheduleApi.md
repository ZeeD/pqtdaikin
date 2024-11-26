# openapi_client.ScheduleApi

All URIs are relative to *https://api.onecta.daikineurope.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gateway_devices_gateway_device_id_management_points_embedded_id_schedule_mode_current_put**](ScheduleApi.md#gateway_devices_gateway_device_id_management_points_embedded_id_schedule_mode_current_put) | **PUT** /gateway-devices/{gatewayDeviceId}/management-points/{embeddedId}/schedule/{mode}/current | Update the current schedule


# **gateway_devices_gateway_device_id_management_points_embedded_id_schedule_mode_current_put**
> gateway_devices_gateway_device_id_management_points_embedded_id_schedule_mode_current_put(gateway_device_id, embedded_id, mode, current_schedule)

Update the current schedule

Update which schedule is currently active and enabled.

### Example

* Bearer (JWT) Authentication (AccessTokenAuth):

```python
import openapi_client
from openapi_client.models.current_schedule import CurrentSchedule
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
    api_instance = openapi_client.ScheduleApi(api_client)
    gateway_device_id = '507f1f77bcf86cd799439011' # str | The id of the gatewayDevice to which the managementPoint belongs
    embedded_id = '1234' # str | The id of the managementPoint to which the characteristic belongs
    mode = 'mode_example' # str | The schedule mode to update
    current_schedule = openapi_client.CurrentSchedule() # CurrentSchedule | 

    try:
        # Update the current schedule
        api_instance.gateway_devices_gateway_device_id_management_points_embedded_id_schedule_mode_current_put(gateway_device_id, embedded_id, mode, current_schedule)
    except Exception as e:
        print("Exception when calling ScheduleApi->gateway_devices_gateway_device_id_management_points_embedded_id_schedule_mode_current_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_device_id** | **str**| The id of the gatewayDevice to which the managementPoint belongs | 
 **embedded_id** | **str**| The id of the managementPoint to which the characteristic belongs | 
 **mode** | **str**| The schedule mode to update | 
 **current_schedule** | [**CurrentSchedule**](CurrentSchedule.md)|  | 

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

