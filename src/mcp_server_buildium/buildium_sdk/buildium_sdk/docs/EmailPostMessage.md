# EmailPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** | Unique identifier of the email template to use for the body of the email. Any tokens present in the template will be replaced based on the recipient(s) of the email.  The following email templates cannot be used:  &lt;ul&gt;&lt;li&gt;1 (Tenant Statement)&lt;/li&gt;&lt;li&gt;2 (Homeowner Statement)&lt;/li&gt;&lt;li&gt;3 (Rental Owner Statement)&lt;/li&gt;&lt;li&gt;123 (Association Tenant Invoice)&lt;/li&gt;&lt;li&gt;124 (Rental Tenant Invoice)&lt;/li&gt;&lt;/ul&gt; | 
**subject** | **str** | Email subject. | 
**include_alternate_emails** | **bool** | Indicates whether to send the email to the recipient&#39;s primary and alternate email addresses. | 
**exclude_delinquent_recipients** | **bool** | Indicates whether to exclude sending emails to association owners that are flagged as delinquent. This only applies to association recipients. | 
**include_association_tenants** | **bool** | Indicates whether to include association tenants. Only applies to association properties. | 
**property_ids** | **List[int]** | A list of association and/or rental property unique identifiers to send the email to. Cannot be populated if &#39;RecipientIds&#39; is present. | [optional] 
**recipient_ids** | **List[int]** | A list of individual unique identifiers to send the email to. Cannot be populated if &#39;PropertyIds&#39; is present. | [optional] 

## Example

```python
from buildium_sdk.models.email_post_message import EmailPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of EmailPostMessage from a JSON string
email_post_message_instance = EmailPostMessage.from_json(json)
# print the JSON string representation of the object
print(EmailPostMessage.to_json())

# convert the object into a dict
email_post_message_dict = email_post_message_instance.to_dict()
# create an instance of EmailPostMessage from a dict
email_post_message_from_dict = EmailPostMessage.from_dict(email_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


