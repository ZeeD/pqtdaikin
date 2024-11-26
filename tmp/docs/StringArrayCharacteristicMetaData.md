# StringArrayCharacteristicMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**settable** | **bool** | Whether or not the characteristic can be changed by the user | [optional] 
**deprecated** | **str** | Whether or not the characteristic is deprecated | [optional] 
**value** | **str** | The selected value of the StringArray characteristic. Should be part of the values as well. | [optional] 
**values** | **List[str]** | The values allowed in this characteristic | [optional] 

## Example

```python
from openapi_client.models.string_array_characteristic_meta_data import StringArrayCharacteristicMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of StringArrayCharacteristicMetaData from a JSON string
string_array_characteristic_meta_data_instance = StringArrayCharacteristicMetaData.from_json(json)
# print the JSON string representation of the object
print(StringArrayCharacteristicMetaData.to_json())

# convert the object into a dict
string_array_characteristic_meta_data_dict = string_array_characteristic_meta_data_instance.to_dict()
# create an instance of StringArrayCharacteristicMetaData from a dict
string_array_characteristic_meta_data_from_dict = StringArrayCharacteristicMetaData.from_dict(string_array_characteristic_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


