# RentalPreferredVendorPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_ids** | **List[int]** | A list of vendor identifiers that will be assigned as preferred vendors to the specified rental property. The submitted list of identifiers will overwrite any existing preferred vendors. Leaving the array empty will remove all vendors from the rental property. | 

## Example

```python
from buildium_sdk.models.rental_preferred_vendor_put_message import RentalPreferredVendorPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalPreferredVendorPutMessage from a JSON string
rental_preferred_vendor_put_message_instance = RentalPreferredVendorPutMessage.from_json(json)
# print the JSON string representation of the object
print(RentalPreferredVendorPutMessage.to_json())

# convert the object into a dict
rental_preferred_vendor_put_message_dict = rental_preferred_vendor_put_message_instance.to_dict()
# create an instance of RentalPreferredVendorPutMessage from a dict
rental_preferred_vendor_put_message_from_dict = RentalPreferredVendorPutMessage.from_dict(rental_preferred_vendor_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


