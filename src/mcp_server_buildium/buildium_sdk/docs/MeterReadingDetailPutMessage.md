# MeterReadingDetailPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the detail being updated. | [optional] 
**unit_id** | **int** | Unique identifier of the unit associated with the meter reading. | 
**prior_value** | **int** | Previous meter reading value. | 
**value** | **int** | Current meter reading value. | 

## Example

```python
from buildium_sdk.models.meter_reading_detail_put_message import MeterReadingDetailPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MeterReadingDetailPutMessage from a JSON string
meter_reading_detail_put_message_instance = MeterReadingDetailPutMessage.from_json(json)
# print the JSON string representation of the object
print(MeterReadingDetailPutMessage.to_json())

# convert the object into a dict
meter_reading_detail_put_message_dict = meter_reading_detail_put_message_instance.to_dict()
# create an instance of MeterReadingDetailPutMessage from a dict
meter_reading_detail_put_message_from_dict = MeterReadingDetailPutMessage.from_dict(meter_reading_detail_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


