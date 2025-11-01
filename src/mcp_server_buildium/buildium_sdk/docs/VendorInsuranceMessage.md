# VendorInsuranceMessage

Vendor insurance information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Insurance provider. | [optional] 
**policy_number** | **str** | Insurance policy number. | [optional] 
**expiration_date** | **datetime** | Expiration date of the insurance policy. Null if no expiration exists. | [optional] 

## Example

```python
from buildium_sdk.models.vendor_insurance_message import VendorInsuranceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorInsuranceMessage from a JSON string
vendor_insurance_message_instance = VendorInsuranceMessage.from_json(json)
# print the JSON string representation of the object
print(VendorInsuranceMessage.to_json())

# convert the object into a dict
vendor_insurance_message_dict = vendor_insurance_message_instance.to_dict()
# create an instance of VendorInsuranceMessage from a dict
vendor_insurance_message_from_dict = VendorInsuranceMessage.from_dict(vendor_insurance_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


