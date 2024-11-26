# InfoVersions

The versions of the service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | **str** | API version | [optional] 
**build** | **str** | Build version | [optional] 

## Example

```python
from openapi_client.models.info_versions import InfoVersions

# TODO update the JSON string below
json = "{}"
# create an instance of InfoVersions from a JSON string
info_versions_instance = InfoVersions.from_json(json)
# print the JSON string representation of the object
print(InfoVersions.to_json())

# convert the object into a dict
info_versions_dict = info_versions_instance.to_dict()
# create an instance of InfoVersions from a dict
info_versions_from_dict = InfoVersions.from_dict(info_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


