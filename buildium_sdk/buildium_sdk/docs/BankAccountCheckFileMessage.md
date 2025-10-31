# BankAccountCheckFileMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File unique identifier. | [optional] 
**title** | **str** | The title of the file. | [optional] 
**physical_file_name** | **str** | Physical name of the file on the server. | [optional] 
**size** | **int** | Size of the file, in kilobytes. | [optional] 
**content_type** | **str** | MIME type of the file. | [optional] 
**uploaded_date_time** | **datetime** | Date and time the file was uploaded. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_check_file_message import BankAccountCheckFileMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountCheckFileMessage from a JSON string
bank_account_check_file_message_instance = BankAccountCheckFileMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountCheckFileMessage.to_json())

# convert the object into a dict
bank_account_check_file_message_dict = bank_account_check_file_message_instance.to_dict()
# create an instance of BankAccountCheckFileMessage from a dict
bank_account_check_file_message_from_dict = BankAccountCheckFileMessage.from_dict(bank_account_check_file_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


