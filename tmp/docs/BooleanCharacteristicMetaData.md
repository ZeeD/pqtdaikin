# BooleanCharacteristicMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**settable** | **bool** | Whether or not the characteristic can be changed by the user | [optional] 
**deprecated** | **str** | Whether or not the characteristic is deprecated | [optional] 
**value** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.boolean_characteristic_meta_data import BooleanCharacteristicMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanCharacteristicMetaData from a JSON string
boolean_characteristic_meta_data_instance = BooleanCharacteristicMetaData.from_json(json)
# print the JSON string representation of the object
print(BooleanCharacteristicMetaData.to_json())

# convert the object into a dict
boolean_characteristic_meta_data_dict = boolean_characteristic_meta_data_instance.to_dict()
# create an instance of BooleanCharacteristicMetaData from a dict
boolean_characteristic_meta_data_from_dict = BooleanCharacteristicMetaData.from_dict(boolean_characteristic_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


