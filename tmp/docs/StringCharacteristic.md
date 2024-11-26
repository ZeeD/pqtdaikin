# StringCharacteristic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The string value of this characteristic | [optional] 
**error** | **str** |  | [optional] 
**settable** | **bool** | Whether or not the characteristic can be changed by the user | [optional] 
**deprecated** | **str** | Whether or not the characteristic is deprecated | [optional] 
**max_length** | **float** | The max length of the characteristic | [optional] 

## Example

```python
from openapi_client.models.string_characteristic import StringCharacteristic

# TODO update the JSON string below
json = "{}"
# create an instance of StringCharacteristic from a JSON string
string_characteristic_instance = StringCharacteristic.from_json(json)
# print the JSON string representation of the object
print(StringCharacteristic.to_json())

# convert the object into a dict
string_characteristic_dict = string_characteristic_instance.to_dict()
# create an instance of StringCharacteristic from a dict
string_characteristic_from_dict = StringCharacteristic.from_dict(string_characteristic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


