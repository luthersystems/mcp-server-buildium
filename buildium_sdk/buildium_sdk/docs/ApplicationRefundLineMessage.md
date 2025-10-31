# ApplicationRefundLineMessage

This is an object that represents a line on an application refund.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the line item. | [optional] 
**gl_account_id** | **int** | Unique identifier of the general ledger account associated with the refund. | [optional] 

## Example

```python
from buildium_sdk.models.application_refund_line_message import ApplicationRefundLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRefundLineMessage from a JSON string
application_refund_line_message_instance = ApplicationRefundLineMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationRefundLineMessage.to_json())

# convert the object into a dict
application_refund_line_message_dict = application_refund_line_message_instance.to_dict()
# create an instance of ApplicationRefundLineMessage from a dict
application_refund_line_message_from_dict = ApplicationRefundLineMessage.from_dict(application_refund_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


