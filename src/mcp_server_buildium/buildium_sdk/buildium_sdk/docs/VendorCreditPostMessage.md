# VendorCreditPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_date** | **date** | Date the vendor credit was made. The date must be formatted as YYYY-MM-DD. | 
**reference_number** | **str** | The invoice or reference number that the vendor assigned to the credit. The value cannot exceed 40 characters. | [optional] 
**memo** | **str** | Memo associated with the vendor credit, if applicable. The value cannot exceed 40 characters. | [optional] 
**lines** | [**List[VendorCreditLineItemPostMessage]**](VendorCreditLineItemPostMessage.md) | A collection of line items associated with the vendor credit. At least one line item is required and cannot exceed 100 line items. | 

## Example

```python
from buildium_sdk.models.vendor_credit_post_message import VendorCreditPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorCreditPostMessage from a JSON string
vendor_credit_post_message_instance = VendorCreditPostMessage.from_json(json)
# print the JSON string representation of the object
print(VendorCreditPostMessage.to_json())

# convert the object into a dict
vendor_credit_post_message_dict = vendor_credit_post_message_instance.to_dict()
# create an instance of VendorCreditPostMessage from a dict
vendor_credit_post_message_from_dict = VendorCreditPostMessage.from_dict(vendor_credit_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


