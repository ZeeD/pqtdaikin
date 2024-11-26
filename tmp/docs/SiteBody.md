# SiteBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the site | [optional] 
**role** | **str** | The role of the user who did the request | [optional] 
**location** | [**SiteBodyLocation**](SiteBodyLocation.md) |  | [optional] 
**users** | [**List[SiteBodyUsersInner]**](SiteBodyUsersInner.md) | The users that are linked to a site | [optional] 

## Example

```python
from openapi_client.models.site_body import SiteBody

# TODO update the JSON string below
json = "{}"
# create an instance of SiteBody from a JSON string
site_body_instance = SiteBody.from_json(json)
# print the JSON string representation of the object
print(SiteBody.to_json())

# convert the object into a dict
site_body_dict = site_body_instance.to_dict()
# create an instance of SiteBody from a dict
site_body_from_dict = SiteBody.from_dict(site_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


