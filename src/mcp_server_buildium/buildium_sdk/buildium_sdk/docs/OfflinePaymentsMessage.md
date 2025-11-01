# OfflinePaymentsMessage

Offline payment settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_info_in_resident_center** | **bool** | Indicates whether the offline payment information is displayed in the Buildium Resident Center. | [optional] 
**display_company_address** | **bool** | Indicates whether to display the company address along with the offline payment information. If &#x60;DisplayInfoInResidentCenter&#x60; is false the company address will not be displayed. | [optional] 
**payment_instructions** | **str** | Directions for how to make offline payments. If &#x60;DisplayInfoInResidentCenter&#x60; is false the payment instructions will not be displayed. | [optional] 

## Example

```python
from buildium_sdk.models.offline_payments_message import OfflinePaymentsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OfflinePaymentsMessage from a JSON string
offline_payments_message_instance = OfflinePaymentsMessage.from_json(json)
# print the JSON string representation of the object
print(OfflinePaymentsMessage.to_json())

# convert the object into a dict
offline_payments_message_dict = offline_payments_message_instance.to_dict()
# create an instance of OfflinePaymentsMessage from a dict
offline_payments_message_from_dict = OfflinePaymentsMessage.from_dict(offline_payments_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


