# SiteBodyLocation

The location details of the site

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | ISO 3166-1 alpha-2 country code | [optional] 
**place_id** | **str** | An Azure maps place ID for the (sub)municipality | [optional] 
**latitude** | **float** | The latitude of the (sub)municipality | [optional] 
**longitude** | **float** | The longitude of the (sub)municipality | [optional] 
**level** | **str** | The level of preciseness of a location | [optional] 

## Example

```python
from openapi_client.models.site_body_location import SiteBodyLocation

# TODO update the JSON string below
json = "{}"
# create an instance of SiteBodyLocation from a JSON string
site_body_location_instance = SiteBodyLocation.from_json(json)
# print the JSON string representation of the object
print(SiteBodyLocation.to_json())

# convert the object into a dict
site_body_location_dict = site_body_location_instance.to_dict()
# create an instance of SiteBodyLocation from a dict
site_body_location_from_dict = SiteBodyLocation.from_dict(site_body_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


