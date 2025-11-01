# OfflinePaymentsPutMessage

Offline payment settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_info_in_resident_center** | **bool** | Indicates whether the offline payment information is displayed in the Buildium Resident Center. | 
**display_company_address** | **bool** | Indicates whether to display the company address along with the offline payment information. If &#x60;DisplayInfoInResidentCenter&#x60; is false the company address will not be displayed. | 
**payment_instructions** | **str** | Directions for how to make offline payments. The value cannot exceed 65,535 characters. If &#x60;DisplayInfoInResidentCenter&#x60; is false the payment instructions will not be displayed. | [optional] 

## Example

```python
from buildium_sdk.models.offline_payments_put_message import OfflinePaymentsPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OfflinePaymentsPutMessage from a JSON string
offline_payments_put_message_instance = OfflinePaymentsPutMessage.from_json(json)
# print the JSON string representation of the object
print(OfflinePaymentsPutMessage.to_json())

# convert the object into a dict
offline_payments_put_message_dict = offline_payments_put_message_instance.to_dict()
# create an instance of OfflinePaymentsPutMessage from a dict
offline_payments_put_message_from_dict = OfflinePaymentsPutMessage.from_dict(offline_payments_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


