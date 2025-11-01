# BillPostMessage

This object represents a bill.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date that the bill was received. This date typically corresponds with a Bill Received Date, Invoice Date, or Invoice Received Date from an invoice. The date must be formatted as YYYY-MM-DD. | 
**due_date** | **date** | The date that payment is due to the vendor. The due date must be after the value in the &#x60;Date&#x60; field. The date must be formatted as YYYY-MM-DD. | 
**memo** | **str** | A description of what the invoice was for. The value cannot exceed 245 characters. | [optional] 
**vendor_id** | **int** | The unique identifier of the vendor or supplier who sent you an invoice. | 
**work_order_id** | **int** | Unique identifier of the work order associated with this bill. | [optional] 
**reference_number** | **str** | The reference or invoice number that the vendor assigned to the invoice. The value cannot exceed 40 characters. | [optional] 
**lines** | [**List[BillLinePostMessage]**](BillLinePostMessage.md) | A collection of line items associated with the bill. | 

## Example

```python
from buildium_sdk.models.bill_post_message import BillPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillPostMessage from a JSON string
bill_post_message_instance = BillPostMessage.from_json(json)
# print the JSON string representation of the object
print(BillPostMessage.to_json())

# convert the object into a dict
bill_post_message_dict = bill_post_message_instance.to_dict()
# create an instance of BillPostMessage from a dict
bill_post_message_from_dict = BillPostMessage.from_dict(bill_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


