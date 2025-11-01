# CheckPrintingInfoPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_remote_check_printing** | **bool** | Indicates whether remote check printing is enabled. | [optional] 
**enable_local_check_printing** | **bool** | Indicates whether local check printing is enabled. | [optional] 
**check_layout_type** | **str** | The check layout type. Defaults to &#x60;Voucher2StubsPrePrintedLayout&#x60; if not specified. | [optional] 
**signature_heading** | **str** | The signature heading. Defaults to \&quot;VOID AFTER 90 DAYS\&quot; if not specified. | [optional] 
**fractional_number** | **str** | The fractional form of the routing number. Typically is used to identify the bank of the check in cases where the MICR is unreadable. | [optional] 
**bank_information_line1** | **str** | Bank information line 1. | [optional] 
**bank_information_line2** | **str** | Bank information line 2. | [optional] 
**bank_information_line3** | **str** | Bank information line 3. | [optional] 
**bank_information_line4** | **str** | Bank information line 4. | [optional] 
**bank_information_line5** | **str** | Bank information line 5. | [optional] 
**company_information_line1** | **str** | Company information 1. Defaults to the company name from the account if not specified. | [optional] 
**company_information_line2** | **str** | Company information 2. Defaults to the company address if not specified. | [optional] 
**company_information_line3** | **str** | Company information 3. Defaults to the company address if not specified. | [optional] 
**company_information_line4** | **str** | Company information 4. Defaults to the company address if not specified. | [optional] 
**company_information_line5** | **str** | Company information 5. Defaults to the company address if not specified. | [optional] 

## Example

```python
from buildium_sdk.models.check_printing_info_post_message import CheckPrintingInfoPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CheckPrintingInfoPostMessage from a JSON string
check_printing_info_post_message_instance = CheckPrintingInfoPostMessage.from_json(json)
# print the JSON string representation of the object
print(CheckPrintingInfoPostMessage.to_json())

# convert the object into a dict
check_printing_info_post_message_dict = check_printing_info_post_message_instance.to_dict()
# create an instance of CheckPrintingInfoPostMessage from a dict
check_printing_info_post_message_from_dict = CheckPrintingInfoPostMessage.from_dict(check_printing_info_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


