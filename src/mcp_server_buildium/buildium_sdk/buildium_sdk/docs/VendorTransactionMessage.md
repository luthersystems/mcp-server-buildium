# VendorTransactionMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction unique identifier. | [optional] 
**var_date** | **date** | Date of the transaction. | [optional] 
**total_amount** | **float** | Total amount of the transaction. | [optional] 
**transaction_type** | **str** | Type of transaction. | [optional] 
**reference_number** | **str** | Reference number for the transaction. | [optional] 
**memo** | **str** | Memo for the transaction. | [optional] 

## Example

```python
from buildium_sdk.models.vendor_transaction_message import VendorTransactionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorTransactionMessage from a JSON string
vendor_transaction_message_instance = VendorTransactionMessage.from_json(json)
# print the JSON string representation of the object
print(VendorTransactionMessage.to_json())

# convert the object into a dict
vendor_transaction_message_dict = vendor_transaction_message_instance.to_dict()
# create an instance of VendorTransactionMessage from a dict
vendor_transaction_message_from_dict = VendorTransactionMessage.from_dict(vendor_transaction_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


