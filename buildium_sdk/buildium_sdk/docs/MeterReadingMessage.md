# MeterReadingMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reading_date** | **date** | Date the meter reading was recorded. | [optional] 
**response_meter_type** | **str** | Meter type for the meter reading. | [optional] 
**value** | **int** | Total value across all units for the meter reading. | [optional] 
**usage** | **int** | The amount used between the prior reading and this reading, calculated by subtracting prior value from value. Usage will be the basis used when charging tenants for a reading. | [optional] 
**charges_created** | **bool** | Indicates if charges were created for the meter reading. | [optional] 

## Example

```python
from buildium_sdk.models.meter_reading_message import MeterReadingMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MeterReadingMessage from a JSON string
meter_reading_message_instance = MeterReadingMessage.from_json(json)
# print the JSON string representation of the object
print(MeterReadingMessage.to_json())

# convert the object into a dict
meter_reading_message_dict = meter_reading_message_instance.to_dict()
# create an instance of MeterReadingMessage from a dict
meter_reading_message_from_dict = MeterReadingMessage.from_dict(meter_reading_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


