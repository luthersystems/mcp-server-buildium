# RentalMessage

This is an object that represents a rental property.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rental property unique identifier. | [optional] 
**name** | **str** | Name of the rental property. | [optional] 
**structure_description** | **str** | Description of the rental property structure. | [optional] 
**number_units** | **int** | Number of units in the rental property. | [optional] 
**is_active** | **bool** | Indicates whether the rental property is active within the Buildium platform. | [optional] 
**operating_bank_account_id** | **int** | The primary bank account that a rental property uses for its income and expenses. | [optional] 
**reserve** | **float** | A property reserve is cash that a property manager keeps on hand in case of unexpected expenses. It is available cash that isn&#39;t disbursed in an owner draw. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Address of the rental property. | [optional] 
**year_built** | **int** | Year the rental property was built. | [optional] 
**rental_type** | **str** | Indicates the type of rental property. | [optional] 
**rental_sub_type** | **str** | Indicates the sub type of the rental property. | [optional] 
**rental_manager** | [**PropertyManagerMessage**](PropertyManagerMessage.md) | Property manager associated with rental property. | [optional] 

## Example

```python
from buildium_sdk.models.rental_message import RentalMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalMessage from a JSON string
rental_message_instance = RentalMessage.from_json(json)
# print the JSON string representation of the object
print(RentalMessage.to_json())

# convert the object into a dict
rental_message_dict = rental_message_instance.to_dict()
# create an instance of RentalMessage from a dict
rental_message_from_dict = RentalMessage.from_dict(rental_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


