# RentalPropertyPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Rental property name. The value cannot exceed 127 characters. | 
**structure_description** | **str** | Description of the rental property building. The description cannot exceed 65,535 characters. | [optional] 
**address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Rental property address. | 
**rental_sub_type** | **str** | Subtype of the rental property. | 
**rental_owner_ids** | **List[int]** | List of existing rental owner ID&#39;s that are owners of this property. | [optional] 
**operating_bank_account_id** | **int** | The primary bank account that a rental property uses for its income and expenses. | 
**property_manager_id** | **int** | Indicates the staff member identifier that acts as the property manager for this rental property. Note, the staff member must have permissions to this rental to be assigned as the property manager.  Set this field to null if you don&#39;t want to assign a staff member to the rental property. | [optional] 
**reserve** | **float** | A property reserve is cash that a property manager keeps on hand in case of unexpected expenses. It is available cash that isn&#39;t disbursed in an owner draw. | [optional] 
**year_built** | **int** | Indicates the year the rental property was built. If provided this value must be a four digit integer between 1000 and the current year. | [optional] 
**units** | [**List[RentalPropertyUnitPostMessage]**](RentalPropertyUnitPostMessage.md) | Units of the rental property. If no values are provided, a default unit will be created for the property. The number of units cannot exceed 100. If you need to create more than 100 units for the property, use the &lt;a href&#x3D;\&quot;#operation/RentalUnitsExternalApi_CreateRentalUnit\&quot;&gt;Create a unit&lt;/a&gt; endpoint to create the additional units once the property has been created. | [optional] 

## Example

```python
from buildium_sdk.models.rental_property_post_message import RentalPropertyPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalPropertyPostMessage from a JSON string
rental_property_post_message_instance = RentalPropertyPostMessage.from_json(json)
# print the JSON string representation of the object
print(RentalPropertyPostMessage.to_json())

# convert the object into a dict
rental_property_post_message_dict = rental_property_post_message_instance.to_dict()
# create an instance of RentalPropertyPostMessage from a dict
rental_property_post_message_from_dict = RentalPropertyPostMessage.from_dict(rental_property_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


