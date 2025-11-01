# ApplicationRefundLineSaveMessage

This is an object that represents a line item on an application ledger refund.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the line item. | 
**gl_account_id** | **int** | Unique identifier of the general ledger account associated with the refund. | 

## Example

```python
from buildium_sdk.models.application_refund_line_save_message import ApplicationRefundLineSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRefundLineSaveMessage from a JSON string
application_refund_line_save_message_instance = ApplicationRefundLineSaveMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationRefundLineSaveMessage.to_json())

# convert the object into a dict
application_refund_line_save_message_dict = application_refund_line_save_message_instance.to_dict()
# create an instance of ApplicationRefundLineSaveMessage from a dict
application_refund_line_save_message_from_dict = ApplicationRefundLineSaveMessage.from_dict(application_refund_line_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


