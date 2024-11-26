# SiteBodyUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the user | [optional] 
**role** | **str** | The role of the user | [optional] 

## Example

```python
from openapi_client.models.site_body_users_inner import SiteBodyUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of SiteBodyUsersInner from a JSON string
site_body_users_inner_instance = SiteBodyUsersInner.from_json(json)
# print the JSON string representation of the object
print(SiteBodyUsersInner.to_json())

# convert the object into a dict
site_body_users_inner_dict = site_body_users_inner_instance.to_dict()
# create an instance of SiteBodyUsersInner from a dict
site_body_users_inner_from_dict = SiteBodyUsersInner.from_dict(site_body_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


