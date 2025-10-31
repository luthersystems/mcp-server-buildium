# BillMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Bill unique identifier. | [optional] 
**var_date** | **date** | Date of the bill. | [optional] 
**due_date** | **date** | The date that payment is due to the vendor. | [optional] 
**paid_date** | **date** | The date that payment was made to the vendor. | [optional] 
**memo** | **str** | A description of what the invoice was for. | [optional] 
**vendor_id** | **int** | Unique identifier of the vendor who submitted the bill. | [optional] 
**work_order_id** | **int** | Unique identifier of the work order associated with this bill. | [optional] 
**reference_number** | **str** | The invoice or reference number that the vendor assigned to the invoice. | [optional] 
**approval_status** | **str** | The current approval status for the bill. | [optional] 
**lines** | [**List[BillLineMessage]**](BillLineMessage.md) | A collection of line items associated with the bill. | [optional] 

## Example

```python
from buildium_sdk.models.bill_message import BillMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillMessage from a JSON string
bill_message_instance = BillMessage.from_json(json)
# print the JSON string representation of the object
print(BillMessage.to_json())

# convert the object into a dict
bill_message_dict = bill_message_instance.to_dict()
# create an instance of BillMessage from a dict
bill_message_from_dict = BillMessage.from_dict(bill_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


