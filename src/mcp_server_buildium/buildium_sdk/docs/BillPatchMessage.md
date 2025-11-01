# BillPatchMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date that an invoice was received. This date typically corresponds with a Bill Received Date, Invoice Date, or Invoice Received Date from an invoice. The date must be formatted as YYYY-MM-DD. | [optional] 
**due_date** | **date** | The date that payment for a bill is due to the vendor. The date must be formatted as YYYY-MM-DD. | [optional] 
**memo** | **str** | A description of what the invoice was for. The value cannot exceed 245 characters. | [optional] 
**vendor_id** | **int** | The unique identifier of the vendor or supplier who sent you an invoice. | [optional] 
**reference_number** | **str** | The reference or invoice number that the vendor assigned to the invoice. The value cannot exceed 40 characters. | [optional] 
**lines** | [**List[BillLineItemPatchMessage]**](BillLineItemPatchMessage.md) | A collection of line items associated with the bill. | [optional] 

## Example

```python
from buildium_sdk.models.bill_patch_message import BillPatchMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillPatchMessage from a JSON string
bill_patch_message_instance = BillPatchMessage.from_json(json)
# print the JSON string representation of the object
print(BillPatchMessage.to_json())

# convert the object into a dict
bill_patch_message_dict = bill_patch_message_instance.to_dict()
# create an instance of BillPatchMessage from a dict
bill_patch_message_from_dict = BillPatchMessage.from_dict(bill_patch_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


