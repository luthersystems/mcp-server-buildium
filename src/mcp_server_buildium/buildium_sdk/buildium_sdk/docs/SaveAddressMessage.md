# SaveAddressMessage

Address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | Address line 1 (e.g., street, PO Box, or company name). This value cannot exceed 100 characters. | 
**address_line2** | **str** | Address line 2 (e.g., apartment, suite, unit, or building). This value cannot exceed 100 characters. | [optional] 
**address_line3** | **str** | Address line 3.  This value cannot exceed 100 characters. | [optional] 
**city** | **str** | City, district, suburb, town, or village. This value cannot exceed 100 characters. | [optional] 
**state** | **str** | State, county, province, or region. When &#x60;Country&#x60; is set to &#x60;UnitedStates&#x60; this value must be a valid state name or abbreviation. If the value is &#x60;Canada&#x60; this value must be a valid Canadian province. For all other countries this field is optional and not validated. | [optional] 
**postal_code** | **str** | ZIP or postal code. | 
**country** | **str** | Country. Must be a valid &#x60;Country&#x60; enumeration value. | 

## Example

```python
from buildium_sdk.models.save_address_message import SaveAddressMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SaveAddressMessage from a JSON string
save_address_message_instance = SaveAddressMessage.from_json(json)
# print the JSON string representation of the object
print(SaveAddressMessage.to_json())

# convert the object into a dict
save_address_message_dict = save_address_message_instance.to_dict()
# create an instance of SaveAddressMessage from a dict
save_address_message_from_dict = SaveAddressMessage.from_dict(save_address_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


