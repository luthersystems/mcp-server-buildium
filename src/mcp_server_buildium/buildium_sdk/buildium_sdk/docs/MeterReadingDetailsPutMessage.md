# MeterReadingDetailsPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reading_date** | **date** | Date the meter reading occurred on. Date must be formatted as YYYY-MM-DD. | 
**meter_type** | **str** | Type of meter being read. | 
**details** | [**List[MeterReadingDetailPutMessage]**](MeterReadingDetailPutMessage.md) | Collection of detailed meter readings. At least one item is required. | 

## Example

```python
from buildium_sdk.models.meter_reading_details_put_message import MeterReadingDetailsPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MeterReadingDetailsPutMessage from a JSON string
meter_reading_details_put_message_instance = MeterReadingDetailsPutMessage.from_json(json)
# print the JSON string representation of the object
print(MeterReadingDetailsPutMessage.to_json())

# convert the object into a dict
meter_reading_details_put_message_dict = meter_reading_details_put_message_instance.to_dict()
# create an instance of MeterReadingDetailsPutMessage from a dict
meter_reading_details_put_message_from_dict = MeterReadingDetailsPutMessage.from_dict(meter_reading_details_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


