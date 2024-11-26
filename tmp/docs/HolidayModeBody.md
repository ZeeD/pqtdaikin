# HolidayModeBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether or not the holiday mode is enabled | 
**start_date** | **date** | The startDate of the holiday mode | [optional] 
**end_date** | **date** | The endDate of the holiday mode | [optional] 

## Example

```python
from openapi_client.models.holiday_mode_body import HolidayModeBody

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayModeBody from a JSON string
holiday_mode_body_instance = HolidayModeBody.from_json(json)
# print the JSON string representation of the object
print(HolidayModeBody.to_json())

# convert the object into a dict
holiday_mode_body_dict = holiday_mode_body_instance.to_dict()
# create an instance of HolidayModeBody from a dict
holiday_mode_body_from_dict = HolidayModeBody.from_dict(holiday_mode_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


