# EFTPaymentsMessage

Electronic payment settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payments_enabled** | **bool** | Indicates whether EFT payments are enabled in the Buildium Resident Center for all residents of this property. | [optional] 

## Example

```python
from buildium_sdk.models.eft_payments_message import EFTPaymentsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of EFTPaymentsMessage from a JSON string
eft_payments_message_instance = EFTPaymentsMessage.from_json(json)
# print the JSON string representation of the object
print(EFTPaymentsMessage.to_json())

# convert the object into a dict
eft_payments_message_dict = eft_payments_message_instance.to_dict()
# create an instance of EFTPaymentsMessage from a dict
eft_payments_message_from_dict = EFTPaymentsMessage.from_dict(eft_payments_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


