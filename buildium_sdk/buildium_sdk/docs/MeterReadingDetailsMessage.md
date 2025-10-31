# MeterReadingDetailsMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reading_date** | **date** | Requested date for meter reading details. Details will be the most recent readings on or before this date. | [optional] 
**meter_type** | **str** | Type of meter the reading is for. | [optional] 
**details** | [**List[MeterReadingDetailMessage]**](MeterReadingDetailMessage.md) | List of reading details for all units. | [optional] 

## Example

```python
from buildium_sdk.models.meter_reading_details_message import MeterReadingDetailsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MeterReadingDetailsMessage from a JSON string
meter_reading_details_message_instance = MeterReadingDetailsMessage.from_json(json)
# print the JSON string representation of the object
print(MeterReadingDetailsMessage.to_json())

# convert the object into a dict
meter_reading_details_message_dict = meter_reading_details_message_instance.to_dict()
# create an instance of MeterReadingDetailsMessage from a dict
meter_reading_details_message_from_dict = MeterReadingDetailsMessage.from_dict(meter_reading_details_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


