# ObjectCharacteristic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** | The detail of this object can be found in the JSON schemas | [optional] 
**error** | **str** |  | [optional] 
**settable** | **bool** | Whether or not the characteristic can be changed by the user | [optional] 
**deprecated** | **str** | Whether or not the characteristic is deprecated | [optional] 

## Example

```python
from openapi_client.models.object_characteristic import ObjectCharacteristic

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectCharacteristic from a JSON string
object_characteristic_instance = ObjectCharacteristic.from_json(json)
# print the JSON string representation of the object
print(ObjectCharacteristic.to_json())

# convert the object into a dict
object_characteristic_dict = object_characteristic_instance.to_dict()
# create an instance of ObjectCharacteristic from a dict
object_characteristic_from_dict = ObjectCharacteristic.from_dict(object_characteristic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


