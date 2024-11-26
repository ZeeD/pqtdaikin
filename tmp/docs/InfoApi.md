# openapi_client.InfoApi

All URIs are relative to *https://api.onecta.daikineurope.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_get**](InfoApi.md#info_get) | **GET** /info | Get service information


# **info_get**
> Info info_get()

Get service information

Service information

### Example

* Bearer (JWT) Authentication (AccessTokenAuth):

```python
import openapi_client
from openapi_client.models.info import Info
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
    api_instance = openapi_client.InfoApi(api_client)

    try:
        # Get service information
        api_response = api_instance.info_get()
        print("The response of InfoApi->info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->info_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Info**](Info.md)

### Authorization

[AccessTokenAuth](../README.md#AccessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

