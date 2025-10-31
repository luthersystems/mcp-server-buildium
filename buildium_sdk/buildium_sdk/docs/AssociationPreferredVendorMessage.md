# AssociationPreferredVendorMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Preferred vendor unique identifier. | [optional] 
**first_name** | **str** | First name of the preferred vendor. | [optional] 
**last_name** | **str** | Last name of the preferred vendor. | [optional] 
**company_name** | **str** | Company name of the preferred vendor. | [optional] 
**primary_email** | **str** | Primary email for the preferred vendor. | [optional] 
**alternate_email** | **str** | Alternate email for the preferred vendor. | [optional] 
**phone_numbers** | [**List[PhoneNumberMessage]**](PhoneNumberMessage.md) | List of phone numbers of the preferred vendor. | [optional] 
**website** | **str** | Website of the preferred vendor. | [optional] 
**is_company** | **bool** | Indicates whether the preferred vendor is a company. | [optional] 

## Example

```python
from buildium_sdk.models.association_preferred_vendor_message import AssociationPreferredVendorMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationPreferredVendorMessage from a JSON string
association_preferred_vendor_message_instance = AssociationPreferredVendorMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationPreferredVendorMessage.to_json())

# convert the object into a dict
association_preferred_vendor_message_dict = association_preferred_vendor_message_instance.to_dict()
# create an instance of AssociationPreferredVendorMessage from a dict
association_preferred_vendor_message_from_dict = AssociationPreferredVendorMessage.from_dict(association_preferred_vendor_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


