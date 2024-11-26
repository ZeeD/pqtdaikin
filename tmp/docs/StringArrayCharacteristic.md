# StringArrayCharacteristic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The selected value of the StringArray characteristic. Should be part of the values as well. | [optional] 
**error** | **str** |  | [optional] 
**settable** | **bool** | Whether or not the characteristic can be changed by the user | [optional] 
**deprecated** | **str** | Whether or not the characteristic is deprecated | [optional] 
**values** | **List[str]** | The values allowed in this characteristic | [optional] 

## Example

```python
from openapi_client.models.string_array_characteristic import StringArrayCharacteristic

# TODO update the JSON string below
json = "{}"
# create an instance of StringArrayCharacteristic from a JSON string
string_array_characteristic_instance = StringArrayCharacteristic.from_json(json)
# print the JSON string representation of the object
print(StringArrayCharacteristic.to_json())

# convert the object into a dict
string_array_characteristic_dict = string_array_characteristic_instance.to_dict()
# create an instance of StringArrayCharacteristic from a dict
string_array_characteristic_from_dict = StringArrayCharacteristic.from_dict(string_array_characteristic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


