# OwnershipAccountRefundLinesPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Line item amount. | 
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount will be recorded. The account must be a liability or income type. | 

## Example

```python
from buildium_sdk.models.ownership_account_refund_lines_post_message import OwnershipAccountRefundLinesPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountRefundLinesPostMessage from a JSON string
ownership_account_refund_lines_post_message_instance = OwnershipAccountRefundLinesPostMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountRefundLinesPostMessage.to_json())

# convert the object into a dict
ownership_account_refund_lines_post_message_dict = ownership_account_refund_lines_post_message_instance.to_dict()
# create an instance of OwnershipAccountRefundLinesPostMessage from a dict
ownership_account_refund_lines_post_message_from_dict = OwnershipAccountRefundLinesPostMessage.from_dict(ownership_account_refund_lines_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


