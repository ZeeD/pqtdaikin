# CharacteristicMetadataBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**settable** | **bool** | Whether or not the characteristic can be changed by the user | [optional] 
**deprecated** | **str** | Whether or not the characteristic is deprecated | [optional] 

## Example

```python
from openapi_client.models.characteristic_metadata_body import CharacteristicMetadataBody

# TODO update the JSON string below
json = "{}"
# create an instance of CharacteristicMetadataBody from a JSON string
characteristic_metadata_body_instance = CharacteristicMetadataBody.from_json(json)
# print the JSON string representation of the object
print(CharacteristicMetadataBody.to_json())

# convert the object into a dict
characteristic_metadata_body_dict = characteristic_metadata_body_instance.to_dict()
# create an instance of CharacteristicMetadataBody from a dict
characteristic_metadata_body_from_dict = CharacteristicMetadataBody.from_dict(characteristic_metadata_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


