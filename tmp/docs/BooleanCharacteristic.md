# BooleanCharacteristic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **bool** |  | [optional] 
**error** | **str** |  | [optional] 
**settable** | **bool** | Whether or not the characteristic can be changed by the user | [optional] 
**deprecated** | **str** | Whether or not the characteristic is deprecated | [optional] 

## Example

```python
from openapi_client.models.boolean_characteristic import BooleanCharacteristic

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanCharacteristic from a JSON string
boolean_characteristic_instance = BooleanCharacteristic.from_json(json)
# print the JSON string representation of the object
print(BooleanCharacteristic.to_json())

# convert the object into a dict
boolean_characteristic_dict = boolean_characteristic_instance.to_dict()
# create an instance of BooleanCharacteristic from a dict
boolean_characteristic_from_dict = BooleanCharacteristic.from_dict(boolean_characteristic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


