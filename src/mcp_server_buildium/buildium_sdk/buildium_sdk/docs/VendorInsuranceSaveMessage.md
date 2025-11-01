# VendorInsuranceSaveMessage

Vendor insurance information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Insurance provider. This value can not exceed 65 characters. | [optional] 
**policy_number** | **str** | Insurance policy number. This value can not exceed 65 characters. | [optional] 
**expiration_date** | **date** | Expiration date of the insurance policy. The date must be formatted as YYYY-MM-DD. | [optional] 

## Example

```python
from buildium_sdk.models.vendor_insurance_save_message import VendorInsuranceSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorInsuranceSaveMessage from a JSON string
vendor_insurance_save_message_instance = VendorInsuranceSaveMessage.from_json(json)
# print the JSON string representation of the object
print(VendorInsuranceSaveMessage.to_json())

# convert the object into a dict
vendor_insurance_save_message_dict = vendor_insurance_save_message_instance.to_dict()
# create an instance of VendorInsuranceSaveMessage from a dict
vendor_insurance_save_message_from_dict = VendorInsuranceSaveMessage.from_dict(vendor_insurance_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


