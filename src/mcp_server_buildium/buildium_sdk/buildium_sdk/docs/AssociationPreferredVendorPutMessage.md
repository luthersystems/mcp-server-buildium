# AssociationPreferredVendorPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_ids** | **List[int]** | A list of vendor identifiers that will be assigned as preferred vendors to the specified association. The submitted list of identifiers will overwrite any existing preferred vendors. Leaving the array empty will remove all vendors from the association. | 

## Example

```python
from buildium_sdk.models.association_preferred_vendor_put_message import AssociationPreferredVendorPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationPreferredVendorPutMessage from a JSON string
association_preferred_vendor_put_message_instance = AssociationPreferredVendorPutMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationPreferredVendorPutMessage.to_json())

# convert the object into a dict
association_preferred_vendor_put_message_dict = association_preferred_vendor_put_message_instance.to_dict()
# create an instance of AssociationPreferredVendorPutMessage from a dict
association_preferred_vendor_put_message_from_dict = AssociationPreferredVendorPutMessage.from_dict(association_preferred_vendor_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


