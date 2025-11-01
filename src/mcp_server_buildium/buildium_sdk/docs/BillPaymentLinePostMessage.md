# BillPaymentLinePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill_line_id** | **int** | The unique identifier of the bill line item toward which the payment is being made. | 
**amount** | **float** | The amount that is being paid toward the bill line item. | 

## Example

```python
from buildium_sdk.models.bill_payment_line_post_message import BillPaymentLinePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillPaymentLinePostMessage from a JSON string
bill_payment_line_post_message_instance = BillPaymentLinePostMessage.from_json(json)
# print the JSON string representation of the object
print(BillPaymentLinePostMessage.to_json())

# convert the object into a dict
bill_payment_line_post_message_dict = bill_payment_line_post_message_instance.to_dict()
# create an instance of BillPaymentLinePostMessage from a dict
bill_payment_line_post_message_from_dict = BillPaymentLinePostMessage.from_dict(bill_payment_line_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


