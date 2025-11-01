# FileSharingRentalUnitPutMesage

The file share settings for the rental unit file entity type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rental_owners** | **bool** | Indicates whether file is shared with rental owners of the property. | [optional] 
**tenants** | **bool** | Indicates whether file is shared with tenants of the property. | [optional] 

## Example

```python
from buildium_sdk.models.file_sharing_rental_unit_put_mesage import FileSharingRentalUnitPutMesage

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingRentalUnitPutMesage from a JSON string
file_sharing_rental_unit_put_mesage_instance = FileSharingRentalUnitPutMesage.from_json(json)
# print the JSON string representation of the object
print(FileSharingRentalUnitPutMesage.to_json())

# convert the object into a dict
file_sharing_rental_unit_put_mesage_dict = file_sharing_rental_unit_put_mesage_instance.to_dict()
# create an instance of FileSharingRentalUnitPutMesage from a dict
file_sharing_rental_unit_put_mesage_from_dict = FileSharingRentalUnitPutMesage.from_dict(file_sharing_rental_unit_put_mesage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


