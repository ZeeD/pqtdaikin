# CharacteristicPatchValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path of the value that has to be changed (https://tools.ietf.org/html/rfc6901) | [optional] 
**value** | **str** | The value of the characteristic | 

## Example

```python
from openapi_client.models.characteristic_patch_value import CharacteristicPatchValue

# TODO update the JSON string below
json = "{}"
# create an instance of CharacteristicPatchValue from a JSON string
characteristic_patch_value_instance = CharacteristicPatchValue.from_json(json)
# print the JSON string representation of the object
print(CharacteristicPatchValue.to_json())

# convert the object into a dict
characteristic_patch_value_dict = characteristic_patch_value_instance.to_dict()
# create an instance of CharacteristicPatchValue from a dict
characteristic_patch_value_from_dict = CharacteristicPatchValue.from_dict(characteristic_patch_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


