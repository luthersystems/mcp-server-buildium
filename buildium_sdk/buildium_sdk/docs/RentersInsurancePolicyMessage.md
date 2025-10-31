# RentersInsurancePolicyMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Renters insurance policy unique identifier. | [optional] 
**insurance_company** | **str** | The name of the insurance company that issued the policy. | [optional] 
**carrier_type** | **str** | The carrier type for the policy. | [optional] 
**policy_identifier** | **str** | The policy identifier. | [optional] 
**effective_date** | **date** | The date that the policy becomes effective. | [optional] 
**expiration_date** | **date** | The date that the policy expires. | [optional] 
**cancellation_date** | **date** | The cancellation date of the policy. This only applies to policies with a &#x60;CarrierType&#x60; of &#x60;MSI&#x60;, and is independent of &#x60;ExpirationDate&#x60;. | [optional] 
**insured_tenants** | [**List[InsuredTenantMessage]**](InsuredTenantMessage.md) | A collection of tenants associated with this policy. | [optional] 

## Example

```python
from buildium_sdk.models.renters_insurance_policy_message import RentersInsurancePolicyMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentersInsurancePolicyMessage from a JSON string
renters_insurance_policy_message_instance = RentersInsurancePolicyMessage.from_json(json)
# print the JSON string representation of the object
print(RentersInsurancePolicyMessage.to_json())

# convert the object into a dict
renters_insurance_policy_message_dict = renters_insurance_policy_message_instance.to_dict()
# create an instance of RentersInsurancePolicyMessage from a dict
renters_insurance_policy_message_from_dict = RentersInsurancePolicyMessage.from_dict(renters_insurance_policy_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


