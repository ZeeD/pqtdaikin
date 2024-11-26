# ObjectCharacteristicMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**settable** | **bool** | Whether or not the characteristic can be changed by the user | [optional] 
**deprecated** | **str** | Whether or not the characteristic is deprecated | [optional] 
**value** | **object** | The detail of this object can be found in the JSON schemas | [optional] 

## Example

```python
from openapi_client.models.object_characteristic_meta_data import ObjectCharacteristicMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectCharacteristicMetaData from a JSON string
object_characteristic_meta_data_instance = ObjectCharacteristicMetaData.from_json(json)
# print the JSON string representation of the object
print(ObjectCharacteristicMetaData.to_json())

# convert the object into a dict
object_characteristic_meta_data_dict = object_characteristic_meta_data_instance.to_dict()
# create an instance of ObjectCharacteristicMetaData from a dict
object_characteristic_meta_data_from_dict = ObjectCharacteristicMetaData.from_dict(object_characteristic_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


