# EmailRecipientMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Recipient unique identifier. | [optional] 
**name** | **str** | Name of the recipient. | [optional] 
**email** | **str** | Email address of the recipient. | [optional] 
**recipient_type** | **str** | The type of recipient. | [optional] 
**href** | **str** | A link to the resource associated with the recipient. | [optional] 

## Example

```python
from buildium_sdk.models.email_recipient_message import EmailRecipientMessage

# TODO update the JSON string below
json = "{}"
# create an instance of EmailRecipientMessage from a JSON string
email_recipient_message_instance = EmailRecipientMessage.from_json(json)
# print the JSON string representation of the object
print(EmailRecipientMessage.to_json())

# convert the object into a dict
email_recipient_message_dict = email_recipient_message_instance.to_dict()
# create an instance of EmailRecipientMessage from a dict
email_recipient_message_from_dict = EmailRecipientMessage.from_dict(email_recipient_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


