# ChargeLineMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the line item. | [optional] 
**gl_account_id** | **int** | Unique identifier of the general ledger account associated with the charge. | [optional] 

## Example

```python
from buildium_sdk.models.charge_line_message import ChargeLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeLineMessage from a JSON string
charge_line_message_instance = ChargeLineMessage.from_json(json)
# print the JSON string representation of the object
print(ChargeLineMessage.to_json())

# convert the object into a dict
charge_line_message_dict = charge_line_message_instance.to_dict()
# create an instance of ChargeLineMessage from a dict
charge_line_message_from_dict = ChargeLineMessage.from_dict(charge_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


