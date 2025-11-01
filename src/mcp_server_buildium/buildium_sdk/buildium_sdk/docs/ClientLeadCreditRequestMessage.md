# ClientLeadCreditRequestMessage

Lead credit request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_status** | **str** | Indicates the current status of the credit. | [optional] 
**credit_reason** | **str** | Indicates the reason a credit was requested. | [optional] 
**comments** | **str** | Additional comments about the credit request. | [optional] 
**request_date** | **date** | The date the credit was requested. | [optional] 

## Example

```python
from buildium_sdk.models.client_lead_credit_request_message import ClientLeadCreditRequestMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ClientLeadCreditRequestMessage from a JSON string
client_lead_credit_request_message_instance = ClientLeadCreditRequestMessage.from_json(json)
# print the JSON string representation of the object
print(ClientLeadCreditRequestMessage.to_json())

# convert the object into a dict
client_lead_credit_request_message_dict = client_lead_credit_request_message_instance.to_dict()
# create an instance of ClientLeadCreditRequestMessage from a dict
client_lead_credit_request_message_from_dict = ClientLeadCreditRequestMessage.from_dict(client_lead_credit_request_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


