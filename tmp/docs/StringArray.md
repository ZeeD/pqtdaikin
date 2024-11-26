# StringArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The selected value of the StringArray characteristic. Should be part of the values as well. | [optional] 
**values** | **List[str]** | The values allowed in this characteristic | [optional] 

## Example

```python
from openapi_client.models.string_array import StringArray

# TODO update the JSON string below
json = "{}"
# create an instance of StringArray from a JSON string
string_array_instance = StringArray.from_json(json)
# print the JSON string representation of the object
print(StringArray.to_json())

# convert the object into a dict
string_array_dict = string_array_instance.to_dict()
# create an instance of StringArray from a dict
string_array_from_dict = StringArray.from_dict(string_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


