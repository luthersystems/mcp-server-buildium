# AssociationPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Association name. The value cannot exceed 127 characters. | 
**description** | **str** | Description of the association. The value cannot exceed 65,535 characters. | [optional] 
**year_built** | **int** | Indicates the year the association was established. If provided this value must be a four digit integer between 1000 and the current year. | [optional] 
**operating_bank_account_id** | **int** | The primary bank account that an association uses for its income and expenses. | 
**reserve** | **float** | A property reserve is cash that a property manager keeps on hand in case of unexpected expenses. It is available cash that isn&#39;t disbursed in an owner draw. | [optional] 
**address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Association address. | 
**property_manager_id** | **int** | Indicates the staff member identifier that acts as the property manager for this association. Note, the staff member must have permissions to this association to be assigned as the property manager.  Set this field to null if you don&#39;t want to assign a staff member to the association. | [optional] 
**fiscal_year_end_day** | **int** | The day the fiscal year ends for the association. | 
**fiscal_year_end_month** | **int** | The month the fiscal year ends for the association. | 

## Example

```python
from buildium_sdk.models.association_put_message import AssociationPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationPutMessage from a JSON string
association_put_message_instance = AssociationPutMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationPutMessage.to_json())

# convert the object into a dict
association_put_message_dict = association_put_message_instance.to_dict()
# create an instance of AssociationPutMessage from a dict
association_put_message_from_dict = AssociationPutMessage.from_dict(association_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


