# PropertyManagerMessage

This is an object that represents a property manager.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Property manager unique identifier. | [optional] 
**first_name** | **str** | First name of the property manager. | [optional] 
**last_name** | **str** | Last name of the property manager. | [optional] 
**company_name** | **str** | Company name of the rental owner. Empty if &#x60;IsCompany&#x60; is &#x60;false&#x60;. | [optional] 
**is_company** | **bool** | Denotes if the property manager is a company. | [optional] 
**profile_photo_url** | **str** | Profile photo URL for the property manager. | [optional] 
**email** | **str** | Email of the property manager. | [optional] 
**phone_numbers** | [**List[PhoneNumberMessage]**](PhoneNumberMessage.md) | List of phone numbers associated with the property manager. | [optional] 

## Example

```python
from buildium_sdk.models.property_manager_message import PropertyManagerMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyManagerMessage from a JSON string
property_manager_message_instance = PropertyManagerMessage.from_json(json)
# print the JSON string representation of the object
print(PropertyManagerMessage.to_json())

# convert the object into a dict
property_manager_message_dict = property_manager_message_instance.to_dict()
# create an instance of PropertyManagerMessage from a dict
property_manager_message_from_dict = PropertyManagerMessage.from_dict(property_manager_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


