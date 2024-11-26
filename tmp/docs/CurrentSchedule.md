# CurrentSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** | The id of the current schedule | 
**enabled** | **bool** | Whether the current schedule should be enabled or disabled | 

## Example

```python
from openapi_client.models.current_schedule import CurrentSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentSchedule from a JSON string
current_schedule_instance = CurrentSchedule.from_json(json)
# print the JSON string representation of the object
print(CurrentSchedule.to_json())

# convert the object into a dict
current_schedule_dict = current_schedule_instance.to_dict()
# create an instance of CurrentSchedule from a dict
current_schedule_from_dict = CurrentSchedule.from_dict(current_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


