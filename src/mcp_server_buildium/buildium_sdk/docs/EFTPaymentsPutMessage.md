# EFTPaymentsPutMessage

Electronic payment settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payments_enabled** | **bool** | Indicates whether EFT payments are enabled in the Buildium Resident Center for all residents of this property. Note, to enable EFT payments the operating bank account for the property must have EFT payments provisioned. | 

## Example

```python
from buildium_sdk.models.eft_payments_put_message import EFTPaymentsPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of EFTPaymentsPutMessage from a JSON string
eft_payments_put_message_instance = EFTPaymentsPutMessage.from_json(json)
# print the JSON string representation of the object
print(EFTPaymentsPutMessage.to_json())

# convert the object into a dict
eft_payments_put_message_dict = eft_payments_put_message_instance.to_dict()
# create an instance of EFTPaymentsPutMessage from a dict
eft_payments_put_message_from_dict = EFTPaymentsPutMessage.from_dict(eft_payments_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


