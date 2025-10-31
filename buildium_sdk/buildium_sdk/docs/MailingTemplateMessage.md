# MailingTemplateMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the mailing template. | [optional] 
**name** | **str** | Name of the mailing template. | [optional] 
**description** | **str** | Description of the mailing template. | [optional] 
**recipient_type** | **str** | Intended recipient type for mailings using the template. | [optional] 

## Example

```python
from buildium_sdk.models.mailing_template_message import MailingTemplateMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MailingTemplateMessage from a JSON string
mailing_template_message_instance = MailingTemplateMessage.from_json(json)
# print the JSON string representation of the object
print(MailingTemplateMessage.to_json())

# convert the object into a dict
mailing_template_message_dict = mailing_template_message_instance.to_dict()
# create an instance of MailingTemplateMessage from a dict
mailing_template_message_from_dict = MailingTemplateMessage.from_dict(mailing_template_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


