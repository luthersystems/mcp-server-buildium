# AppliedVendorCreditMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The vendor credit id applied to the bill payment. | [optional] 
**href** | **str** | A link to the resource endpoint associated with the vendor credit. | [optional] 

## Example

```python
from buildium_sdk.models.applied_vendor_credit_message import AppliedVendorCreditMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedVendorCreditMessage from a JSON string
applied_vendor_credit_message_instance = AppliedVendorCreditMessage.from_json(json)
# print the JSON string representation of the object
print(AppliedVendorCreditMessage.to_json())

# convert the object into a dict
applied_vendor_credit_message_dict = applied_vendor_credit_message_instance.to_dict()
# create an instance of AppliedVendorCreditMessage from a dict
applied_vendor_credit_message_from_dict = AppliedVendorCreditMessage.from_dict(applied_vendor_credit_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


