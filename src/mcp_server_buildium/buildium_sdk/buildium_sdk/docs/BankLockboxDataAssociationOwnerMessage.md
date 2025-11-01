# BankLockboxDataAssociationOwnerMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Association owner unique identifier. | [optional] 
**first_name** | **str** | Association owner first name. | [optional] 
**last_name** | **str** | Association owner last name. | [optional] 
**email** | **str** | Association owner email. | [optional] 
**alternate_email** | **str** | Association owner alternate email. | [optional] 
**phone_numbers** | [**List[PhoneNumberMessage]**](PhoneNumberMessage.md) | List of phone numbers associated with the association owner. | [optional] 
**delinquency_status** | **str** | Indicates the delinquency status of the association owner. | [optional] 
**primary_address** | [**AddressMessage**](AddressMessage.md) | Primary address. | [optional] 
**alternate_address** | [**AddressMessage**](AddressMessage.md) | Alternate address. | [optional] 
**mailing_preference** | **str** | Indicates the association owner&#39;s mailing preference. | [optional] 

## Example

```python
from buildium_sdk.models.bank_lockbox_data_association_owner_message import BankLockboxDataAssociationOwnerMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankLockboxDataAssociationOwnerMessage from a JSON string
bank_lockbox_data_association_owner_message_instance = BankLockboxDataAssociationOwnerMessage.from_json(json)
# print the JSON string representation of the object
print(BankLockboxDataAssociationOwnerMessage.to_json())

# convert the object into a dict
bank_lockbox_data_association_owner_message_dict = bank_lockbox_data_association_owner_message_instance.to_dict()
# create an instance of BankLockboxDataAssociationOwnerMessage from a dict
bank_lockbox_data_association_owner_message_from_dict = BankLockboxDataAssociationOwnerMessage.from_dict(bank_lockbox_data_association_owner_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


