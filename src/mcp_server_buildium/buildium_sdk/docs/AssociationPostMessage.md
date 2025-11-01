# AssociationPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Association name. The value cannot exceed 127 characters. | 
**operating_bank_account_id** | **int** | The primary bank account that an association uses for its income and expenses. | 
**address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Association address. | 
**is_active** | **bool** | Indicates whether the association is active within the Buildium platform. If no value is passed in the default is &#x60;true&#x60;. | [optional] 
**reserve** | **float** | A property reserve is cash that a property manager keeps on hand in case of unexpected expenses. It is available cash that isn&#39;t disbursed in an owner draw. | [optional] 
**description** | **str** | Description of the association. The description cannot exceed 65,535 characters. | [optional] 
**year_built** | **int** | Indicates the year the association was established. If provided this value must be a four digit integer between 1000 and the current year. | [optional] 
**property_manager_id** | **int** | Indicates the staff member identifier that acts as the property manager for this association. Note, the staff member must have permissions to this association to be assigned as the property manager.  Leave this field null if you don&#39;t want to assign a staff member to the association. | [optional] 
**tax_information** | [**TaxInformationPostMessage**](TaxInformationPostMessage.md) | The tax information of the association. | [optional] 

## Example

```python
from buildium_sdk.models.association_post_message import AssociationPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationPostMessage from a JSON string
association_post_message_instance = AssociationPostMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationPostMessage.to_json())

# convert the object into a dict
association_post_message_dict = association_post_message_instance.to_dict()
# create an instance of AssociationPostMessage from a dict
association_post_message_from_dict = AssociationPostMessage.from_dict(association_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


