# PayeeMessage

The payer of the transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The payer user unique identifier. | [optional] 
**name** | **str** | The name of the payer. | [optional] 
**type** | **str** | The payer user entity type. | [optional] 
**href** | **str** | A link to the resource endpoint associated with the payer. | [optional] 

## Example

```python
from buildium_sdk.models.payee_message import PayeeMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeMessage from a JSON string
payee_message_instance = PayeeMessage.from_json(json)
# print the JSON string representation of the object
print(PayeeMessage.to_json())

# convert the object into a dict
payee_message_dict = payee_message_instance.to_dict()
# create an instance of PayeeMessage from a dict
payee_message_from_dict = PayeeMessage.from_dict(payee_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


