# AssociationOwnerBoardTermPostMessage

Board member term.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**board_position_type** | **str** | Indicates the board position held by the association owner. | 
**start_date** | **date** | Start date of the board member term. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
**end_date** | **date** | End date of the board member term. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 

## Example

```python
from buildium_sdk.models.association_owner_board_term_post_message import AssociationOwnerBoardTermPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationOwnerBoardTermPostMessage from a JSON string
association_owner_board_term_post_message_instance = AssociationOwnerBoardTermPostMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationOwnerBoardTermPostMessage.to_json())

# convert the object into a dict
association_owner_board_term_post_message_dict = association_owner_board_term_post_message_instance.to_dict()
# create an instance of AssociationOwnerBoardTermPostMessage from a dict
association_owner_board_term_post_message_from_dict = AssociationOwnerBoardTermPostMessage.from_dict(association_owner_board_term_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


