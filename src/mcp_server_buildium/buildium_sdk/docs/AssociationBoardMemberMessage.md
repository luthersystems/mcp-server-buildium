# AssociationBoardMemberMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Association board member unique identifier. | [optional] 
**association_owner_id** | **int** | Association owner unique identifier. | [optional] 
**first_name** | **str** | Association owner first name. | [optional] 
**last_name** | **str** | Association owner last name. | [optional] 
**email** | **str** | Association owner email. | [optional] 
**phone_numbers** | [**List[PhoneNumberMessage]**](PhoneNumberMessage.md) | List of phone numbers of the association owner. | [optional] 
**board_position_type** | **str** | Indicates the board position held by the association owner. | [optional] 
**start_date** | **date** | Start date of the association owner&#39;s term as board member | [optional] 
**end_date** | **date** | End date of the association owner&#39;s term as board member | [optional] 
**created_date_time** | **datetime** | Date and time when the board member was created. | [optional] 

## Example

```python
from buildium_sdk.models.association_board_member_message import AssociationBoardMemberMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationBoardMemberMessage from a JSON string
association_board_member_message_instance = AssociationBoardMemberMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationBoardMemberMessage.to_json())

# convert the object into a dict
association_board_member_message_dict = association_board_member_message_instance.to_dict()
# create an instance of AssociationBoardMemberMessage from a dict
association_board_member_message_from_dict = AssociationBoardMemberMessage.from_dict(association_board_member_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


