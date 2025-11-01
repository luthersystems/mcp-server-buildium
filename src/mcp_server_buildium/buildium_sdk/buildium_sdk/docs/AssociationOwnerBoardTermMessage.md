# AssociationOwnerBoardTermMessage

Board member term.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Board term unique identifier. | [optional] 
**association_id** | **int** | Association unique identifier. | [optional] 
**board_position_type** | **str** | Indicates the board position held by the association owner. | [optional] 
**start_date** | **date** | Start date of the board member term. | [optional] 
**end_date** | **date** | End date of the board member term. | [optional] 
**created_date_time** | **datetime** | Date and time the board member position was created. | [optional] 

## Example

```python
from buildium_sdk.models.association_owner_board_term_message import AssociationOwnerBoardTermMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationOwnerBoardTermMessage from a JSON string
association_owner_board_term_message_instance = AssociationOwnerBoardTermMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationOwnerBoardTermMessage.to_json())

# convert the object into a dict
association_owner_board_term_message_dict = association_owner_board_term_message_instance.to_dict()
# create an instance of AssociationOwnerBoardTermMessage from a dict
association_owner_board_term_message_from_dict = AssociationOwnerBoardTermMessage.from_dict(association_owner_board_term_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


