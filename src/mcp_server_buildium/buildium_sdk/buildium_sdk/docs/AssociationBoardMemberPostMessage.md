# AssociationBoardMemberPostMessage

This object represents the Board Member for an Association.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_owner_id** | **int** | The association owner&#39;s unique identifier. | 
**board_position_type** | **str** | Indicates the board position held by the association owner. | 
**start_date** | **date** | Start date of the association owners term as a board member. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
**end_date** | **date** | End date of the association owners term as a board member. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 

## Example

```python
from buildium_sdk.models.association_board_member_post_message import AssociationBoardMemberPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationBoardMemberPostMessage from a JSON string
association_board_member_post_message_instance = AssociationBoardMemberPostMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationBoardMemberPostMessage.to_json())

# convert the object into a dict
association_board_member_post_message_dict = association_board_member_post_message_instance.to_dict()
# create an instance of AssociationBoardMemberPostMessage from a dict
association_board_member_post_message_from_dict = AssociationBoardMemberPostMessage.from_dict(association_board_member_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


