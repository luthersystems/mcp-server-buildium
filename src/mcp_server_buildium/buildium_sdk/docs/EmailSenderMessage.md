# EmailSenderMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User unique identifier. | [optional] 
**first_name** | **str** | First name of the user. | [optional] 
**last_name** | **str** | Last name of the user. | [optional] 
**href** | **str** | A link to the user resource. | [optional] 

## Example

```python
from buildium_sdk.models.email_sender_message import EmailSenderMessage

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSenderMessage from a JSON string
email_sender_message_instance = EmailSenderMessage.from_json(json)
# print the JSON string representation of the object
print(EmailSenderMessage.to_json())

# convert the object into a dict
email_sender_message_dict = email_sender_message_instance.to_dict()
# create an instance of EmailSenderMessage from a dict
email_sender_message_from_dict = EmailSenderMessage.from_dict(email_sender_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


