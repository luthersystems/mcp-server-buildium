# AssociationOwnershipAccountMessage

This object represents a home owner association ownership account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Association ownership account unique identifier. | [optional] 
**association_id** | **int** | Association unique identifier that the ownership account belongs to. | [optional] 
**unit_id** | **int** | Association unit unique identifier that the ownership account is related to. | [optional] 
**status** | **str** | Indicates the status of the ownership account. | [optional] 
**date_of_purchase** | **date** | Date the unit(s) where purchased by the owner. | [optional] 
**date_of_sale** | **date** | Date the unit(s) where sold by the owner. | [optional] 
**comments** | **str** | Comments about the ownership account. | [optional] 
**association_owner_ids** | **List[int]** | Association owners associated with the ownership account | [optional] 
**delinquency_status** | **str** | Indicates the delinquency status of the ownership account | [optional] 

## Example

```python
from buildium_sdk.models.association_ownership_account_message import AssociationOwnershipAccountMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationOwnershipAccountMessage from a JSON string
association_ownership_account_message_instance = AssociationOwnershipAccountMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationOwnershipAccountMessage.to_json())

# convert the object into a dict
association_ownership_account_message_dict = association_ownership_account_message_instance.to_dict()
# create an instance of AssociationOwnershipAccountMessage from a dict
association_ownership_account_message_from_dict = AssociationOwnershipAccountMessage.from_dict(association_ownership_account_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


