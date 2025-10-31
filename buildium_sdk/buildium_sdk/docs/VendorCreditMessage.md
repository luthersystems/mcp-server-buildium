# VendorCreditMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Vendor credit unique identifier. | [optional] 
**entry_date** | **date** | Date the vendor credit was made. | [optional] 
**reference_number** | **str** | The invoice or reference number that the vendor assigned to the credit. | [optional] 
**memo** | **str** | Memo associated with the vendor credit, if applicable. | [optional] 
**lines** | [**List[VendorCreditLineItemMessage]**](VendorCreditLineItemMessage.md) | A collection of line items associated with the vendor credit. | [optional] 

## Example

```python
from buildium_sdk.models.vendor_credit_message import VendorCreditMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorCreditMessage from a JSON string
vendor_credit_message_instance = VendorCreditMessage.from_json(json)
# print the JSON string representation of the object
print(VendorCreditMessage.to_json())

# convert the object into a dict
vendor_credit_message_dict = vendor_credit_message_instance.to_dict()
# create an instance of VendorCreditMessage from a dict
vendor_credit_message_from_dict = VendorCreditMessage.from_dict(vendor_credit_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


