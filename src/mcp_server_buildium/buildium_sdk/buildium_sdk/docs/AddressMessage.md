# AddressMessage

Address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | Address line 1 (e.g., street, PO Box, or company name). | [optional] 
**address_line2** | **str** | Address line 2 (e.g., apartment, suite, unit, or building). | [optional] 
**address_line3** | **str** | Address line 3 | [optional] 
**city** | **str** | City, district, suburb, town, or village. | [optional] 
**state** | **str** | State, county, province, or region. | [optional] 
**postal_code** | **str** | ZIP or postal code. | [optional] 
**country** | **str** | Country. | [optional] 

## Example

```python
from buildium_sdk.models.address_message import AddressMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AddressMessage from a JSON string
address_message_instance = AddressMessage.from_json(json)
# print the JSON string representation of the object
print(AddressMessage.to_json())

# convert the object into a dict
address_message_dict = address_message_instance.to_dict()
# create an instance of AddressMessage from a dict
address_message_from_dict = AddressMessage.from_dict(address_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


