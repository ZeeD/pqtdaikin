# SitesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_devices** | **List[str]** |  | [optional] 
**id** | **str** | Object Id | [optional] 
**name** | **str** | The name of the site | [optional] 
**role** | **str** | The role of the user who did the request | [optional] 
**location** | [**SiteBodyLocation**](SiteBodyLocation.md) |  | [optional] 
**users** | [**List[SiteBodyUsersInner]**](SiteBodyUsersInner.md) | The users that are linked to a site | [optional] 

## Example

```python
from openapi_client.models.sites_inner import SitesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SitesInner from a JSON string
sites_inner_instance = SitesInner.from_json(json)
# print the JSON string representation of the object
print(SitesInner.to_json())

# convert the object into a dict
sites_inner_dict = sites_inner_instance.to_dict()
# create an instance of SitesInner from a dict
sites_inner_from_dict = SitesInner.from_dict(sites_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


