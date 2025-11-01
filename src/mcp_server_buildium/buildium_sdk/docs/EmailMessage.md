# EmailMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Email unique identifier. | [optional] 
**sent_date_time** | **datetime** | The date and time the email was sent. | [optional] 
**subject** | **str** | Email subject. | [optional] 
**sender** | [**EmailSenderMessage**](EmailSenderMessage.md) | User who sent the email. | [optional] 

## Example

```python
from buildium_sdk.models.email_message import EmailMessage

# TODO update the JSON string below
json = "{}"
# create an instance of EmailMessage from a JSON string
email_message_instance = EmailMessage.from_json(json)
# print the JSON string representation of the object
print(EmailMessage.to_json())

# convert the object into a dict
email_message_dict = email_message_instance.to_dict()
# create an instance of EmailMessage from a dict
email_message_from_dict = EmailMessage.from_dict(email_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


