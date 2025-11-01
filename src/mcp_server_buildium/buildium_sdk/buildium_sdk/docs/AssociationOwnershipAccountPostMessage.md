# AssociationOwnershipAccountPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_id** | **int** | Association unit unique identifier that the ownership account is related to. | 
**date_of_purchase** | **date** | Date the unit was purchased by the owner. Must be formatted as YYYY-MM-DD.   If an existing association ownership account is being replaced then this date must be after the existing ownership accounts date of sale. | 
**association_fee** | **float** | Recurring association fee charge. If provided, a recurring transaction will be created that adds a charge in the amount specified to the ownership account ledger with the frequency indicated in RecurringFrequency. | [optional] 
**recurring_frequency** | **str** | Indicates the frequency of the recurring association fee. This field is required if &#x60;AssociationFee&#x60; has a value. | [optional] 
**association_owner_ids** | **List[int]** | Current or former association owners to assign to this ownership account. Values must be an active association owner identifiers. The request must include at least one owner in this property OR the &#x60;AssociationOwners&#x60; property. | [optional] 
**association_owners** | [**List[AssociationOwnerPostMessage]**](AssociationOwnerPostMessage.md) | Create new association owner(s) and assigns them to this new ownership account. The request must include at least one owner in this property OR the &#x60;AssociationOwnerIds&#x60; property. | [optional] 
**send_welcome_email** | **bool** | Indicates whether to send an owner portal welcome email to all of the association owners assigned to this ownership account. Once the owners sign into the portal, they can make online payments, view important documents, submit requests, and more. | 
**replace_existing_ownership_account** | **bool** | Indicates whether to replace an ownership account if one already exists for this unit.   If this value is false and an ownership account exists the request will fail.This protects against inadvertently overwriting of an existing ownership account.   If the value is true and an ownership account exists then the existing ownership account will be marked as with a status of Past and the newly created ownership account will be Active for the unit. | 

## Example

```python
from buildium_sdk.models.association_ownership_account_post_message import AssociationOwnershipAccountPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationOwnershipAccountPostMessage from a JSON string
association_ownership_account_post_message_instance = AssociationOwnershipAccountPostMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationOwnershipAccountPostMessage.to_json())

# convert the object into a dict
association_ownership_account_post_message_dict = association_ownership_account_post_message_instance.to_dict()
# create an instance of AssociationOwnershipAccountPostMessage from a dict
association_ownership_account_post_message_from_dict = AssociationOwnershipAccountPostMessage.from_dict(association_ownership_account_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


