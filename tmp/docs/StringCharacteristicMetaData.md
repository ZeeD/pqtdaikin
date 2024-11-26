# StringCharacteristicMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**settable** | **bool** | Whether or not the characteristic can be changed by the user | [optional] 
**deprecated** | **str** | Whether or not the characteristic is deprecated | [optional] 
**value** | **str** | The string value of this characteristic | [optional] 
**max_length** | **float** | The max length of the characteristic | [optional] 

## Example

```python
from openapi_client.models.string_characteristic_meta_data import StringCharacteristicMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of StringCharacteristicMetaData from a JSON string
string_characteristic_meta_data_instance = StringCharacteristicMetaData.from_json(json)
# print the JSON string representation of the object
print(StringCharacteristicMetaData.to_json())

# convert the object into a dict
string_characteristic_meta_data_dict = string_characteristic_meta_data_instance.to_dict()
# create an instance of StringCharacteristicMetaData from a dict
string_characteristic_meta_data_from_dict = StringCharacteristicMetaData.from_dict(string_characteristic_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


