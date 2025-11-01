# ApplicationRefundMessage

This is an object that represents a refund tied to an application.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Refund unique identifier. | [optional] 
**var_date** | **date** | Date of the refund. | [optional] 
**payees** | [**List[ApplicantPayeeMessage]**](ApplicantPayeeMessage.md) | List of payees being refunded. | [optional] 
**memo** | **str** | Memo associated with the refund, if applicable. | [optional] 
**check_number** | **str** | Check number associated with the refund, if applicable. | [optional] 
**bank_account_id** | **int** | Unique identifier of the bank account that the refund was made from. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Address to be displayed on the refund check. | [optional] 
**total_amount** | **float** | Total amount of the refund. | [optional] 
**lines** | [**List[ApplicationRefundLineMessage]**](ApplicationRefundLineMessage.md) | A collection of line items included in the refund. | [optional] 

## Example

```python
from buildium_sdk.models.application_refund_message import ApplicationRefundMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRefundMessage from a JSON string
application_refund_message_instance = ApplicationRefundMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationRefundMessage.to_json())

# convert the object into a dict
application_refund_message_dict = application_refund_message_instance.to_dict()
# create an instance of ApplicationRefundMessage from a dict
application_refund_message_from_dict = ApplicationRefundMessage.from_dict(application_refund_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


