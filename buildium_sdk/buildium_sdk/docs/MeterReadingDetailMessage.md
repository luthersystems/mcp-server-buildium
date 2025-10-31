# MeterReadingDetailMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the reading detail. | [optional] 
**unit_id** | **int** | Unique identifier of the unit. | [optional] 
**unit_number** | **str** | Number of the unit. | [optional] 
**prior_value** | **int** | Previous meter reading value. | [optional] 
**value** | **int** | Most recent meter reading value. | [optional] 
**reading_date** | **date** | Date the meter was read. | [optional] 

## Example

```python
from buildium_sdk.models.meter_reading_detail_message import MeterReadingDetailMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MeterReadingDetailMessage from a JSON string
meter_reading_detail_message_instance = MeterReadingDetailMessage.from_json(json)
# print the JSON string representation of the object
print(MeterReadingDetailMessage.to_json())

# convert the object into a dict
meter_reading_detail_message_dict = meter_reading_detail_message_instance.to_dict()
# create an instance of MeterReadingDetailMessage from a dict
meter_reading_detail_message_from_dict = MeterReadingDetailMessage.from_dict(meter_reading_detail_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


