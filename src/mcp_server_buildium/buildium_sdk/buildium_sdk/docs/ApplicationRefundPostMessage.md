# ApplicationRefundPostMessage

This is an object that represents a refund made in a particular application ledger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the refund. The date must be formatted as YYYY-MM-DD. | 
**memo** | **str** | A brief note describing the reason for the refund. The value cannot exceed 65 characters. | [optional] 
**check_number** | **str** | Check number associated with the refund, if applicable. The value cannot exceed 30 characters. | [optional] 
**bank_account_id** | **int** | Unique identifier of the bank account the refund is issued from. | 
**address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Address to be displayed on the refund check. | 
**lines** | [**List[ApplicationRefundLineSaveMessage]**](ApplicationRefundLineSaveMessage.md) | A collection of line items included in the refund. At least one line item is required. | 

## Example

```python
from buildium_sdk.models.application_refund_post_message import ApplicationRefundPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRefundPostMessage from a JSON string
application_refund_post_message_instance = ApplicationRefundPostMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationRefundPostMessage.to_json())

# convert the object into a dict
application_refund_post_message_dict = application_refund_post_message_instance.to_dict()
# create an instance of ApplicationRefundPostMessage from a dict
application_refund_post_message_from_dict = ApplicationRefundPostMessage.from_dict(application_refund_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


