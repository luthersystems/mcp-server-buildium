# ClientLeadMessage

This is an object that represents a client lead

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Client lead unique identifier. | [optional] 
**date_received** | **datetime** | The date the lead was received. | [optional] 
**name** | **str** | The name of the lead. | [optional] 
**email** | **str** | The email of the lead. | [optional] 
**phone_number** | **str** | The phone number of the lead. | [optional] 
**price_paid** | **float** | The price paid for the lead. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | The address of the lead&#39;s property. | [optional] 
**property_type** | **str** | The property type of the lead&#39;s property. | [optional] 
**comments** | **str** | Additional comments submitted for the lead. | [optional] 
**lead_status** | **str** | The current status of the client lead. | [optional] 
**credit_request** | [**ClientLeadCreditRequestMessage**](ClientLeadCreditRequestMessage.md) | The credit request of the lead. This will be null if no credit has been requested. | [optional] 

## Example

```python
from buildium_sdk.models.client_lead_message import ClientLeadMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ClientLeadMessage from a JSON string
client_lead_message_instance = ClientLeadMessage.from_json(json)
# print the JSON string representation of the object
print(ClientLeadMessage.to_json())

# convert the object into a dict
client_lead_message_dict = client_lead_message_instance.to_dict()
# create an instance of ClientLeadMessage from a dict
client_lead_message_from_dict = ClientLeadMessage.from_dict(client_lead_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


