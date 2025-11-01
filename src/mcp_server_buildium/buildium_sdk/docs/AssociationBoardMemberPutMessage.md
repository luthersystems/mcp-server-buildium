# AssociationBoardMemberPutMessage

This object represents the Board Member for an Association.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**board_position_type** | **str** | Indicates the board position held by the association owner. | 
**start_date** | **date** | Start date of the association owners term as a board member. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
**end_date** | **date** | End date of the association owners term as a board member. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 

## Example

```python
from buildium_sdk.models.association_board_member_put_message import AssociationBoardMemberPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationBoardMemberPutMessage from a JSON string
association_board_member_put_message_instance = AssociationBoardMemberPutMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationBoardMemberPutMessage.to_json())

# convert the object into a dict
association_board_member_put_message_dict = association_board_member_put_message_instance.to_dict()
# create an instance of AssociationBoardMemberPutMessage from a dict
association_board_member_put_message_from_dict = AssociationBoardMemberPutMessage.from_dict(association_board_member_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


