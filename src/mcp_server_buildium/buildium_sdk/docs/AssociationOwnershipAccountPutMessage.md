# AssociationOwnershipAccountPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_of_purchase** | **date** | Date the unit was purchased by the owner. Must be formatted as YYYY-MM-DD. | 

## Example

```python
from buildium_sdk.models.association_ownership_account_put_message import AssociationOwnershipAccountPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationOwnershipAccountPutMessage from a JSON string
association_ownership_account_put_message_instance = AssociationOwnershipAccountPutMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationOwnershipAccountPutMessage.to_json())

# convert the object into a dict
association_ownership_account_put_message_dict = association_ownership_account_put_message_instance.to_dict()
# create an instance of AssociationOwnershipAccountPutMessage from a dict
association_ownership_account_put_message_from_dict = AssociationOwnershipAccountPutMessage.from_dict(association_ownership_account_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


