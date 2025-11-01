# buildium_sdk.BankAccountsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_bank_account_check_file_download_requests_download_check_file**](BankAccountsApi.md#external_api_bank_account_check_file_download_requests_download_check_file) | **POST** /v1/bankaccounts/{bankAccountId}/checks/{checkId}/files/{fileId}/downloadrequests | Download a file for a check
[**external_api_bank_account_check_file_uploads_create_check_upload_file_request**](BankAccountsApi.md#external_api_bank_account_check_file_uploads_create_check_upload_file_request) | **POST** /v1/bankaccounts/{bankAccountId}/checks/{checkId}/files/uploadrequests | Upload a file for a check
[**external_api_bank_account_check_files_delete_bank_account_check_file**](BankAccountsApi.md#external_api_bank_account_check_files_delete_bank_account_check_file) | **DELETE** /v1/bankaccounts/{bankAccountId}/checks/{checkId}/files/{fileId} | Delete a file for a check
[**external_api_bank_account_check_files_get_bank_account_check_file_by_id**](BankAccountsApi.md#external_api_bank_account_check_files_get_bank_account_check_file_by_id) | **GET** /v1/bankaccounts/{bankAccountId}/checks/{checkId}/files/{fileId} | Retrieve a file for a check
[**external_api_bank_account_check_files_get_files_for_bank_account_check**](BankAccountsApi.md#external_api_bank_account_check_files_get_files_for_bank_account_check) | **GET** /v1/bankaccounts/{bankAccountId}/checks/{checkId}/files | Retrieve all files for a check
[**external_api_bank_account_checks_create_bank_account_check**](BankAccountsApi.md#external_api_bank_account_checks_create_bank_account_check) | **POST** /v1/bankaccounts/{bankAccountId}/checks | Create a check
[**external_api_bank_account_checks_get_bank_account_checks**](BankAccountsApi.md#external_api_bank_account_checks_get_bank_account_checks) | **GET** /v1/bankaccounts/{bankAccountId}/checks | Retrieve all checks
[**external_api_bank_account_checks_get_check_for_bank_account**](BankAccountsApi.md#external_api_bank_account_checks_get_check_for_bank_account) | **GET** /v1/bankaccounts/{bankAccountId}/checks/{checkId} | Retrieve a check
[**external_api_bank_account_checks_update_check_for_bank_account**](BankAccountsApi.md#external_api_bank_account_checks_update_check_for_bank_account) | **PUT** /v1/bankaccounts/{bankAccountId}/checks/{checkId} | Update a check
[**external_api_bank_account_deposits_create_bank_account_deposit**](BankAccountsApi.md#external_api_bank_account_deposits_create_bank_account_deposit) | **POST** /v1/bankaccounts/{bankAccountId}/deposits | Create a deposit
[**external_api_bank_account_deposits_get_bank_account_deposit_by_id**](BankAccountsApi.md#external_api_bank_account_deposits_get_bank_account_deposit_by_id) | **GET** /v1/bankaccounts/{bankAccountId}/deposits/{depositId} | Retrieve a deposit
[**external_api_bank_account_deposits_get_bank_account_deposits**](BankAccountsApi.md#external_api_bank_account_deposits_get_bank_account_deposits) | **GET** /v1/bankaccounts/{bankAccountId}/deposits | Retrieve all deposits
[**external_api_bank_account_deposits_update_bank_account_deposit**](BankAccountsApi.md#external_api_bank_account_deposits_update_bank_account_deposit) | **PUT** /v1/bankaccounts/{bankAccountId}/deposits/{depositId} | Update a deposit
[**external_api_bank_account_pending_reconciliations_create_pending_reconciliations**](BankAccountsApi.md#external_api_bank_account_pending_reconciliations_create_pending_reconciliations) | **POST** /v1/bankaccounts/{bankAccountId}/reconciliations | Create a reconciliation
[**external_api_bank_account_quick_deposits_create_quick_deposit**](BankAccountsApi.md#external_api_bank_account_quick_deposits_create_quick_deposit) | **POST** /v1/bankaccounts/{bankAccountId}/quickdeposits | Create a quick deposit
[**external_api_bank_account_quick_deposits_get_all_quick_deposits**](BankAccountsApi.md#external_api_bank_account_quick_deposits_get_all_quick_deposits) | **GET** /v1/bankaccounts/{bankAccountId}/quickdeposits | Retrieve all quick deposits
[**external_api_bank_account_quick_deposits_get_quick_deposit_by_id**](BankAccountsApi.md#external_api_bank_account_quick_deposits_get_quick_deposit_by_id) | **GET** /v1/bankaccounts/{bankAccountId}/quickdeposits/{quickDepositId} | Retrieve a quick deposit
[**external_api_bank_account_quick_deposits_update_quick_deposit**](BankAccountsApi.md#external_api_bank_account_quick_deposits_update_quick_deposit) | **PUT** /v1/bankaccounts/{bankAccountId}/quickdeposits/{quickDepositId} | Update a quick deposit
[**external_api_bank_account_reconciliation_finalize_finalize_reconciliation**](BankAccountsApi.md#external_api_bank_account_reconciliation_finalize_finalize_reconciliation) | **POST** /v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}/finalizerequest | Finalize a manual reconciliation
[**external_api_bank_account_reconciliations_read_get_bank_account_reconciliation_transactions**](BankAccountsApi.md#external_api_bank_account_reconciliations_read_get_bank_account_reconciliation_transactions) | **GET** /v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}/transactions | Retrieve all transactions for a reconciliation
[**external_api_bank_account_reconciliations_read_get_reconciliation_balance_by_id**](BankAccountsApi.md#external_api_bank_account_reconciliations_read_get_reconciliation_balance_by_id) | **GET** /v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}/balances | Retrieve a reconciliation&#39;s balance
[**external_api_bank_account_reconciliations_read_get_reconciliation_by_id**](BankAccountsApi.md#external_api_bank_account_reconciliations_read_get_reconciliation_by_id) | **GET** /v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId} | Retrieve a reconciliation
[**external_api_bank_account_reconciliations_read_get_reconciliations**](BankAccountsApi.md#external_api_bank_account_reconciliations_read_get_reconciliations) | **GET** /v1/bankaccounts/{bankAccountId}/reconciliations | Retrieve all reconciliations
[**external_api_bank_account_reconciliations_write_clear_transactions**](BankAccountsApi.md#external_api_bank_account_reconciliations_write_clear_transactions) | **POST** /v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}/cleartransactionsrequest | Clear transactions for a reconciliation
[**external_api_bank_account_reconciliations_write_unclear_transactions**](BankAccountsApi.md#external_api_bank_account_reconciliations_write_unclear_transactions) | **POST** /v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}/uncleartransactionsrequest | Un-clear transactions for a reconciliation
[**external_api_bank_account_reconciliations_write_update_reconciliation**](BankAccountsApi.md#external_api_bank_account_reconciliations_write_update_reconciliation) | **PUT** /v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId} | Update a reconciliation
[**external_api_bank_account_reconciliations_write_update_reconciliation_balances**](BankAccountsApi.md#external_api_bank_account_reconciliations_write_update_reconciliation_balances) | **PUT** /v1/bankaccounts/{bankAccountId}/reconciliations/{reconciliationId}/balances | Update a reconciliation&#39;s balance
[**external_api_bank_account_transactions_get_bank_account_transaction_by_id**](BankAccountsApi.md#external_api_bank_account_transactions_get_bank_account_transaction_by_id) | **GET** /v1/bankaccounts/{bankAccountId}/transactions/{transactionId} | Retrieve a transaction
[**external_api_bank_account_transactions_get_bank_account_transactions**](BankAccountsApi.md#external_api_bank_account_transactions_get_bank_account_transactions) | **GET** /v1/bankaccounts/{bankAccountId}/transactions | Retrieve all transactions
[**external_api_bank_account_transfers_create_bank_account_transfer**](BankAccountsApi.md#external_api_bank_account_transfers_create_bank_account_transfer) | **POST** /v1/bankaccounts/{bankAccountId}/transfers | Create a transfer
[**external_api_bank_account_transfers_get_bank_account_transfer_by_id**](BankAccountsApi.md#external_api_bank_account_transfers_get_bank_account_transfer_by_id) | **GET** /v1/bankaccounts/{bankAccountId}/transfers/{transferId} | Retrieve a transfer
[**external_api_bank_account_transfers_get_bank_account_transfers**](BankAccountsApi.md#external_api_bank_account_transfers_get_bank_account_transfers) | **GET** /v1/bankaccounts/{bankAccountId}/transfers | Retrieve all transfers
[**external_api_bank_account_transfers_update_bank_account_transfer**](BankAccountsApi.md#external_api_bank_account_transfers_update_bank_account_transfer) | **PUT** /v1/bankaccounts/{bankAccountId}/transfers/{transferId} | Update a transfer
[**external_api_bank_account_undeposited_funds_get_undeposited_funds**](BankAccountsApi.md#external_api_bank_account_undeposited_funds_get_undeposited_funds) | **GET** /v1/bankaccounts/{bankAccountId}/undepositedfunds | Retrieve all undeposited funds
[**external_api_bank_account_withdrawals_create_withdrawal_for_bank_account**](BankAccountsApi.md#external_api_bank_account_withdrawals_create_withdrawal_for_bank_account) | **POST** /v1/bankaccounts/{bankAccountId}/withdrawals | Create a withdrawal
[**external_api_bank_account_withdrawals_get_bank_account_withdrawal_by_id**](BankAccountsApi.md#external_api_bank_account_withdrawals_get_bank_account_withdrawal_by_id) | **GET** /v1/bankaccounts/{bankAccountId}/withdrawals/{withdrawalId} | Retrieve a withdrawal
[**external_api_bank_account_withdrawals_get_bank_account_withdrawals**](BankAccountsApi.md#external_api_bank_account_withdrawals_get_bank_account_withdrawals) | **GET** /v1/bankaccounts/{bankAccountId}/withdrawals | Retrieve all withdrawals
[**external_api_bank_account_withdrawals_update_bank_account_withdrawal**](BankAccountsApi.md#external_api_bank_account_withdrawals_update_bank_account_withdrawal) | **PUT** /v1/bankaccounts/{bankAccountId}/withdrawals/{withdrawalId} | Update a withdrawal
[**external_api_bank_accounts_create_bank_account**](BankAccountsApi.md#external_api_bank_accounts_create_bank_account) | **POST** /v1/bankaccounts | Create a bank account
[**external_api_bank_accounts_get_all_bank_accounts**](BankAccountsApi.md#external_api_bank_accounts_get_all_bank_accounts) | **GET** /v1/bankaccounts | Retrieve all bank accounts
[**external_api_bank_accounts_get_bank_account**](BankAccountsApi.md#external_api_bank_accounts_get_bank_account) | **GET** /v1/bankaccounts/{bankAccountId} | Retrieve a bank account
[**external_api_bank_accounts_update_bank_account**](BankAccountsApi.md#external_api_bank_accounts_update_bank_account) | **PUT** /v1/bankaccounts/{bankAccountId} | Update a bank account


# **external_api_bank_account_check_file_download_requests_download_check_file**
> FileDownloadMessage external_api_bank_account_check_file_download_requests_download_check_file(bank_account_id, check_id, file_id)

Download a file for a check

Downloads a specific file associated to the check.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View`
            
<span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View` <span class="permissionBlock">(Required for checks associated with a Company) </span>

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_download_message import FileDownloadMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    check_id = 56 # int | 
    file_id = 56 # int | 

    try:
        # Download a file for a check
        api_response = await api_instance.external_api_bank_account_check_file_download_requests_download_check_file(bank_account_id, check_id, file_id)
        print("The response of BankAccountsApi->external_api_bank_account_check_file_download_requests_download_check_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_check_file_download_requests_download_check_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **check_id** | **int**|  | 
 **file_id** | **int**|  | 

### Return type

[**FileDownloadMessage**](FileDownloadMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - The location to retrieve the created resource. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_check_file_uploads_create_check_upload_file_request**
> FileUploadTicketMessage external_api_bank_account_check_file_uploads_create_check_upload_file_request(bank_account_id, check_id, file_name_post_message)

Upload a file for a check

Uploads a file and associates it to the specified check record.


Uploading a file requires making two API requests. Each step is outlined below.


<strong>Step 1 - Save file metadata</strong>

The first step in the file upload process is to submit the file metadata to `/v1/bankaccounts/{bankAccountId:int}/checks/{checkId:int}/files/uploadrequests`. The response of this call will contain a URL and a collection of form data that will be used in step 2 to generate the request for the file binary upload.


<strong>NOTE:</strong> The response data will expire after 5 minutes. The file metadata will not be saved in the Buildium system if step 2 of this process is not completed successfully.


<strong>Step 2 - Upload the file binary</strong>

Uploading the file binary will require using the response from step 1 to form a POST request to the Buildium file provider. Follow these steps to create the request:


1. Form a POST request using the value of the `BucketUrl` property as the URL. 



2. Set the `Content-Type` header to `multipart/form-data`.



3. Copy the fields from the `FormData`  property to this request as form-data key/value pairs.

<strong>NOTE:</strong> These values must added to the request form-data in the order they were received in the response.



4. Lastly create a form-data key named `file` and set the value to the file binary.

<strong>NOTE:</strong> This must be the last field in the form-data list.


This image shows what the POST request should look like if you're using Postman:
<img src="file-upload-example.png" />


5. Send the POST request! A successful request will return with a `204 - NO CONTENT` HTTP response code. For any failure responses, please refer to <a target="_blank" href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#RESTErrorResponses">AWS documentation</a> on REST error responses.


<strong>NOTE:</strong> The file identifier is not generated in this response. To retrieve the file identifier, call `/v1/files` and pass the `PhysicalFileName` value received from the response of this endpoint into the `physicalfilenames` query parameter.


<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Checks</span> - `View` `Edit`
<span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View` <span class="permissionBlock">(Required for checks associated with a Company) </span>

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_name_post_message import FileNamePostMessage
from buildium_sdk.models.file_upload_ticket_message import FileUploadTicketMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    check_id = 56 # int | 
    file_name_post_message = buildium_sdk.FileNamePostMessage() # FileNamePostMessage | 

    try:
        # Upload a file for a check
        api_response = await api_instance.external_api_bank_account_check_file_uploads_create_check_upload_file_request(bank_account_id, check_id, file_name_post_message)
        print("The response of BankAccountsApi->external_api_bank_account_check_file_uploads_create_check_upload_file_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_check_file_uploads_create_check_upload_file_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **check_id** | **int**|  | 
 **file_name_post_message** | [**FileNamePostMessage**](FileNamePostMessage.md)|  | 

### Return type

[**FileUploadTicketMessage**](FileUploadTicketMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - The location to retrieve the created resource. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**409** | There is a request conflict with the current state of the target resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_check_files_delete_bank_account_check_file**
> external_api_bank_account_check_files_delete_bank_account_check_file(bank_account_id, check_id, file_id)

Delete a file for a check

Deletes a file for a check
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccounts</span> - `View` `Edit` `Delete`
            
<span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View` <span class="permissionBlock">(Required for checks associated with a Company) </span>

### Example


```python
import buildium_sdk
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    check_id = 56 # int | 
    file_id = 56 # int | 

    try:
        # Delete a file for a check
        await api_instance.external_api_bank_account_check_files_delete_bank_account_check_file(bank_account_id, check_id, file_id)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_check_files_delete_bank_account_check_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **check_id** | **int**|  | 
 **file_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK - No Content. |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_check_files_get_bank_account_check_file_by_id**
> BankAccountCheckFileMessage external_api_bank_account_check_files_get_bank_account_check_file_by_id(bank_account_id, check_id, file_id)

Retrieve a file for a check

Retrieves the metadata for a specific file associated with the specified check.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View`
            
<span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View` <span class="permissionBlock">(Required for checks associated with a Company) </span>

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_check_file_message import BankAccountCheckFileMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    check_id = 56 # int | 
    file_id = 56 # int | 

    try:
        # Retrieve a file for a check
        api_response = await api_instance.external_api_bank_account_check_files_get_bank_account_check_file_by_id(bank_account_id, check_id, file_id)
        print("The response of BankAccountsApi->external_api_bank_account_check_files_get_bank_account_check_file_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_check_files_get_bank_account_check_file_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **check_id** | **int**|  | 
 **file_id** | **int**|  | 

### Return type

[**BankAccountCheckFileMessage**](BankAccountCheckFileMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_check_files_get_files_for_bank_account_check**
> List[BankAccountCheckFileMessage] external_api_bank_account_check_files_get_files_for_bank_account_check(bank_account_id, check_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all files for a check

Retrieves the metadata for all files associated to the specified check.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View`
            
<span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View` <span class="permissionBlock">(Required for checks associated with a Company) </span>

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_check_file_message import BankAccountCheckFileMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    check_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all files for a check
        api_response = await api_instance.external_api_bank_account_check_files_get_files_for_bank_account_check(bank_account_id, check_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of BankAccountsApi->external_api_bank_account_check_files_get_files_for_bank_account_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_check_files_get_files_for_bank_account_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **check_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BankAccountCheckFileMessage]**](BankAccountCheckFileMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Total-Count - The total number of records available in the overall result set of the request. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_checks_create_bank_account_check**
> BankAccountCheckMessage external_api_bank_account_checks_create_bank_account_check(bank_account_id, bank_account_check_post_message)

Create a check

Creates a check.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_check_message import BankAccountCheckMessage
from buildium_sdk.models.bank_account_check_post_message import BankAccountCheckPostMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    bank_account_check_post_message = buildium_sdk.BankAccountCheckPostMessage() # BankAccountCheckPostMessage | 

    try:
        # Create a check
        api_response = await api_instance.external_api_bank_account_checks_create_bank_account_check(bank_account_id, bank_account_check_post_message)
        print("The response of BankAccountsApi->external_api_bank_account_checks_create_bank_account_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_checks_create_bank_account_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **bank_account_check_post_message** | [**BankAccountCheckPostMessage**](BankAccountCheckPostMessage.md)|  | 

### Return type

[**BankAccountCheckMessage**](BankAccountCheckMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - The location to retrieve the created resource. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_checks_get_bank_account_checks**
> List[BankAccountCheckMessage] external_api_bank_account_checks_get_bank_account_checks(bank_account_id, startdate, enddate, orderby=orderby, offset=offset, limit=limit)

Retrieve all checks

Retrieves all bank account checks.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View`
            
<span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View` <span class="permissionBlock">(Required for checks associated with a Company) </span>

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_check_message import BankAccountCheckMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    startdate = '2013-10-20' # date | Filters results to any transactions that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD.
    enddate = '2013-10-20' # date | Filters results to any transactions that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD.
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all checks
        api_response = await api_instance.external_api_bank_account_checks_get_bank_account_checks(bank_account_id, startdate, enddate, orderby=orderby, offset=offset, limit=limit)
        print("The response of BankAccountsApi->external_api_bank_account_checks_get_bank_account_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_checks_get_bank_account_checks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **startdate** | **date**| Filters results to any transactions that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD. | 
 **enddate** | **date**| Filters results to any transactions that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD. | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BankAccountCheckMessage]**](BankAccountCheckMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Total-Count - The total number of records available in the overall result set of the request. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_checks_get_check_for_bank_account**
> BankAccountCheckMessage external_api_bank_account_checks_get_check_for_bank_account(bank_account_id, check_id)

Retrieve a check

Retrieves a bank account check.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View`
            
<span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View` <span class="permissionBlock">(Required for checks associated with a Company) </span>

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_check_message import BankAccountCheckMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    check_id = 56 # int | 

    try:
        # Retrieve a check
        api_response = await api_instance.external_api_bank_account_checks_get_check_for_bank_account(bank_account_id, check_id)
        print("The response of BankAccountsApi->external_api_bank_account_checks_get_check_for_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_checks_get_check_for_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **check_id** | **int**|  | 

### Return type

[**BankAccountCheckMessage**](BankAccountCheckMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_checks_update_check_for_bank_account**
> BankAccountCheckMessage external_api_bank_account_checks_update_check_for_bank_account(bank_account_id, check_id, bank_account_check_put_message)

Update a check

Updates a check.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_check_message import BankAccountCheckMessage
from buildium_sdk.models.bank_account_check_put_message import BankAccountCheckPutMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    check_id = 56 # int | 
    bank_account_check_put_message = buildium_sdk.BankAccountCheckPutMessage() # BankAccountCheckPutMessage | 

    try:
        # Update a check
        api_response = await api_instance.external_api_bank_account_checks_update_check_for_bank_account(bank_account_id, check_id, bank_account_check_put_message)
        print("The response of BankAccountsApi->external_api_bank_account_checks_update_check_for_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_checks_update_check_for_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **check_id** | **int**|  | 
 **bank_account_check_put_message** | [**BankAccountCheckPutMessage**](BankAccountCheckPutMessage.md)|  | 

### Return type

[**BankAccountCheckMessage**](BankAccountCheckMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_deposits_create_bank_account_deposit**
> BankAccountDepositMessage external_api_bank_account_deposits_create_bank_account_deposit(bank_account_id, bank_account_deposit_post_message)

Create a deposit

Creates a deposit.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_deposit_message import BankAccountDepositMessage
from buildium_sdk.models.bank_account_deposit_post_message import BankAccountDepositPostMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    bank_account_deposit_post_message = buildium_sdk.BankAccountDepositPostMessage() # BankAccountDepositPostMessage | 

    try:
        # Create a deposit
        api_response = await api_instance.external_api_bank_account_deposits_create_bank_account_deposit(bank_account_id, bank_account_deposit_post_message)
        print("The response of BankAccountsApi->external_api_bank_account_deposits_create_bank_account_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_deposits_create_bank_account_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **bank_account_deposit_post_message** | [**BankAccountDepositPostMessage**](BankAccountDepositPostMessage.md)|  | 

### Return type

[**BankAccountDepositMessage**](BankAccountDepositMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - The location to retrieve the created resource. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_deposits_get_bank_account_deposit_by_id**
> BankAccountDepositMessage external_api_bank_account_deposits_get_bank_account_deposit_by_id(bank_account_id, deposit_id)

Retrieve a deposit

Retrieves a bank account deposit.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View`
            
<span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View` <span class="permissionBlock">(Required for deposits associated with a Company) </span>

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_deposit_message import BankAccountDepositMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    deposit_id = 56 # int | 

    try:
        # Retrieve a deposit
        api_response = await api_instance.external_api_bank_account_deposits_get_bank_account_deposit_by_id(bank_account_id, deposit_id)
        print("The response of BankAccountsApi->external_api_bank_account_deposits_get_bank_account_deposit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_deposits_get_bank_account_deposit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **deposit_id** | **int**|  | 

### Return type

[**BankAccountDepositMessage**](BankAccountDepositMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_deposits_get_bank_account_deposits**
> List[BankAccountDepositMessage] external_api_bank_account_deposits_get_bank_account_deposits(bank_account_id, startdate, enddate, orderby=orderby, offset=offset, limit=limit)

Retrieve all deposits

Retrieves all bank account deposits.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View`
            
<span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View` <span class="permissionBlock">(Required for deposits associated with a Company) </span>

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_deposit_message import BankAccountDepositMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    startdate = '2013-10-20' # date | Filters results to any deposits that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD.
    enddate = '2013-10-20' # date | Filters results to any deposits that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD.
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all deposits
        api_response = await api_instance.external_api_bank_account_deposits_get_bank_account_deposits(bank_account_id, startdate, enddate, orderby=orderby, offset=offset, limit=limit)
        print("The response of BankAccountsApi->external_api_bank_account_deposits_get_bank_account_deposits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_deposits_get_bank_account_deposits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **startdate** | **date**| Filters results to any deposits that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD. | 
 **enddate** | **date**| Filters results to any deposits that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD. | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BankAccountDepositMessage]**](BankAccountDepositMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Total-Count - The total number of records available in the overall result set of the request. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_deposits_update_bank_account_deposit**
> BankAccountDepositMessage external_api_bank_account_deposits_update_bank_account_deposit(bank_account_id, deposit_id, bank_account_deposit_put_message)

Update a deposit

Updates a deposit.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_deposit_message import BankAccountDepositMessage
from buildium_sdk.models.bank_account_deposit_put_message import BankAccountDepositPutMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    deposit_id = 56 # int | 
    bank_account_deposit_put_message = buildium_sdk.BankAccountDepositPutMessage() # BankAccountDepositPutMessage | 

    try:
        # Update a deposit
        api_response = await api_instance.external_api_bank_account_deposits_update_bank_account_deposit(bank_account_id, deposit_id, bank_account_deposit_put_message)
        print("The response of BankAccountsApi->external_api_bank_account_deposits_update_bank_account_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_deposits_update_bank_account_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **deposit_id** | **int**|  | 
 **bank_account_deposit_put_message** | [**BankAccountDepositPutMessage**](BankAccountDepositPutMessage.md)|  | 

### Return type

[**BankAccountDepositMessage**](BankAccountDepositMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_pending_reconciliations_create_pending_reconciliations**
> BankAccountReconciliationMessage external_api_bank_account_pending_reconciliations_create_pending_reconciliations(bank_account_id, bank_pending_reconciliation_post_message)

Create a reconciliation

Creates a reconciliation. Reconciliations can only be created for bank accounts that are not linked externally.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_reconciliation_message import BankAccountReconciliationMessage
from buildium_sdk.models.bank_pending_reconciliation_post_message import BankPendingReconciliationPostMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    bank_pending_reconciliation_post_message = buildium_sdk.BankPendingReconciliationPostMessage() # BankPendingReconciliationPostMessage | 

    try:
        # Create a reconciliation
        api_response = await api_instance.external_api_bank_account_pending_reconciliations_create_pending_reconciliations(bank_account_id, bank_pending_reconciliation_post_message)
        print("The response of BankAccountsApi->external_api_bank_account_pending_reconciliations_create_pending_reconciliations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_pending_reconciliations_create_pending_reconciliations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **bank_pending_reconciliation_post_message** | [**BankPendingReconciliationPostMessage**](BankPendingReconciliationPostMessage.md)|  | 

### Return type

[**BankAccountReconciliationMessage**](BankAccountReconciliationMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - The location to retrieve the created resource. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**409** | There is a request conflict with the current state of the target resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_quick_deposits_create_quick_deposit**
> BankAccountQuickDepositMessage external_api_bank_account_quick_deposits_create_quick_deposit(bank_account_id, bank_account_quick_deposit_save_message)

Create a quick deposit

Creates a quick deposit.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_quick_deposit_message import BankAccountQuickDepositMessage
from buildium_sdk.models.bank_account_quick_deposit_save_message import BankAccountQuickDepositSaveMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    bank_account_quick_deposit_save_message = buildium_sdk.BankAccountQuickDepositSaveMessage() # BankAccountQuickDepositSaveMessage | 

    try:
        # Create a quick deposit
        api_response = await api_instance.external_api_bank_account_quick_deposits_create_quick_deposit(bank_account_id, bank_account_quick_deposit_save_message)
        print("The response of BankAccountsApi->external_api_bank_account_quick_deposits_create_quick_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_quick_deposits_create_quick_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **bank_account_quick_deposit_save_message** | [**BankAccountQuickDepositSaveMessage**](BankAccountQuickDepositSaveMessage.md)|  | 

### Return type

[**BankAccountQuickDepositMessage**](BankAccountQuickDepositMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - The location to retrieve the created resource. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_quick_deposits_get_all_quick_deposits**
> List[BankAccountQuickDepositMessage] external_api_bank_account_quick_deposits_get_all_quick_deposits(bank_account_id, startdate, enddate, orderby=orderby, offset=offset, limit=limit)

Retrieve all quick deposits

Retrieves all quick deposits.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_quick_deposit_message import BankAccountQuickDepositMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    startdate = '2013-10-20' # date | Filters results to any transactions that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD.
    enddate = '2013-10-20' # date | Filters results to any transactions that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD.
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all quick deposits
        api_response = await api_instance.external_api_bank_account_quick_deposits_get_all_quick_deposits(bank_account_id, startdate, enddate, orderby=orderby, offset=offset, limit=limit)
        print("The response of BankAccountsApi->external_api_bank_account_quick_deposits_get_all_quick_deposits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_quick_deposits_get_all_quick_deposits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **startdate** | **date**| Filters results to any transactions that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD. | 
 **enddate** | **date**| Filters results to any transactions that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD. | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BankAccountQuickDepositMessage]**](BankAccountQuickDepositMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Total-Count - The total number of records available in the overall result set of the request. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_quick_deposits_get_quick_deposit_by_id**
> BankAccountQuickDepositMessage external_api_bank_account_quick_deposits_get_quick_deposit_by_id(bank_account_id, quick_deposit_id)

Retrieve a quick deposit

Retrieves a quick deposit.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_quick_deposit_message import BankAccountQuickDepositMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    quick_deposit_id = 56 # int | 

    try:
        # Retrieve a quick deposit
        api_response = await api_instance.external_api_bank_account_quick_deposits_get_quick_deposit_by_id(bank_account_id, quick_deposit_id)
        print("The response of BankAccountsApi->external_api_bank_account_quick_deposits_get_quick_deposit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_quick_deposits_get_quick_deposit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **quick_deposit_id** | **int**|  | 

### Return type

[**BankAccountQuickDepositMessage**](BankAccountQuickDepositMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_quick_deposits_update_quick_deposit**
> BankAccountQuickDepositMessage external_api_bank_account_quick_deposits_update_quick_deposit(bank_account_id, quick_deposit_id, bank_account_quick_deposit_save_message)

Update a quick deposit

Updates a quick deposit.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_quick_deposit_message import BankAccountQuickDepositMessage
from buildium_sdk.models.bank_account_quick_deposit_save_message import BankAccountQuickDepositSaveMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    quick_deposit_id = 56 # int | 
    bank_account_quick_deposit_save_message = buildium_sdk.BankAccountQuickDepositSaveMessage() # BankAccountQuickDepositSaveMessage | 

    try:
        # Update a quick deposit
        api_response = await api_instance.external_api_bank_account_quick_deposits_update_quick_deposit(bank_account_id, quick_deposit_id, bank_account_quick_deposit_save_message)
        print("The response of BankAccountsApi->external_api_bank_account_quick_deposits_update_quick_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_quick_deposits_update_quick_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **quick_deposit_id** | **int**|  | 
 **bank_account_quick_deposit_save_message** | [**BankAccountQuickDepositSaveMessage**](BankAccountQuickDepositSaveMessage.md)|  | 

### Return type

[**BankAccountQuickDepositMessage**](BankAccountQuickDepositMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_reconciliation_finalize_finalize_reconciliation**
> external_api_bank_account_reconciliation_finalize_finalize_reconciliation(bank_account_id, reconciliation_id)

Finalize a manual reconciliation

Finalizes a manual reconciliation. Reconciliations can only be finalized for bank accounts that are not linked externally.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    reconciliation_id = 56 # int | 

    try:
        # Finalize a manual reconciliation
        await api_instance.external_api_bank_account_reconciliation_finalize_finalize_reconciliation(bank_account_id, reconciliation_id)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_reconciliation_finalize_finalize_reconciliation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **reconciliation_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NoContent |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | The specified bank account or reconciliation could not be found. |  -  |
**409** | There is a request conflict with the current state of the target resource. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_reconciliations_read_get_bank_account_reconciliation_transactions**
> List[BankAccountReconciliationTransactionMessage] external_api_bank_account_reconciliations_read_get_bank_account_reconciliation_transactions(bank_account_id, reconciliation_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all transactions for a reconciliation

Retrieves all transactions, both cleared and uncleared, up to the Statement Ending Date of the related reconciliation. This is true for pending and completed reconciliations. Transactions can only be retrieved for bank accounts that are not linked externally.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_reconciliation_transaction_message import BankAccountReconciliationTransactionMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    reconciliation_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all transactions for a reconciliation
        api_response = await api_instance.external_api_bank_account_reconciliations_read_get_bank_account_reconciliation_transactions(bank_account_id, reconciliation_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of BankAccountsApi->external_api_bank_account_reconciliations_read_get_bank_account_reconciliation_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_reconciliations_read_get_bank_account_reconciliation_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **reconciliation_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BankAccountReconciliationTransactionMessage]**](BankAccountReconciliationTransactionMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Total-Count - The total number of records available in the overall result set of the request. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**409** | There is a request conflict with the current state of the target resource. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_reconciliations_read_get_reconciliation_balance_by_id**
> BankAccountReconciliationBalanceMessage external_api_bank_account_reconciliations_read_get_reconciliation_balance_by_id(bank_account_id, reconciliation_id)

Retrieve a reconciliation's balance

Retrieves a bank account reconciliation's balance. Reconciliation balances can only be retrieved for bank accounts that are not linked externally.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_reconciliation_balance_message import BankAccountReconciliationBalanceMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    reconciliation_id = 56 # int | 

    try:
        # Retrieve a reconciliation's balance
        api_response = await api_instance.external_api_bank_account_reconciliations_read_get_reconciliation_balance_by_id(bank_account_id, reconciliation_id)
        print("The response of BankAccountsApi->external_api_bank_account_reconciliations_read_get_reconciliation_balance_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_reconciliations_read_get_reconciliation_balance_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **reconciliation_id** | **int**|  | 

### Return type

[**BankAccountReconciliationBalanceMessage**](BankAccountReconciliationBalanceMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**409** | There is a request conflict with the current state of the target resource. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_reconciliations_read_get_reconciliation_by_id**
> BankAccountReconciliationMessage external_api_bank_account_reconciliations_read_get_reconciliation_by_id(bank_account_id, reconciliation_id)

Retrieve a reconciliation

Retrieves a bank account reconciliation. Reconciliations can only be retrieved for bank accounts that are not linked externally.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_reconciliation_message import BankAccountReconciliationMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    reconciliation_id = 56 # int | 

    try:
        # Retrieve a reconciliation
        api_response = await api_instance.external_api_bank_account_reconciliations_read_get_reconciliation_by_id(bank_account_id, reconciliation_id)
        print("The response of BankAccountsApi->external_api_bank_account_reconciliations_read_get_reconciliation_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_reconciliations_read_get_reconciliation_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **reconciliation_id** | **int**|  | 

### Return type

[**BankAccountReconciliationMessage**](BankAccountReconciliationMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**409** | There is a request conflict with the current state of the target resource. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_reconciliations_read_get_reconciliations**
> List[BankAccountReconciliationMessage] external_api_bank_account_reconciliations_read_get_reconciliations(bank_account_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all reconciliations

Retrieves all bank account reconciliations. Reconciliations can only be retrieved for bank accounts that are not linked externally.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_reconciliation_message import BankAccountReconciliationMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all reconciliations
        api_response = await api_instance.external_api_bank_account_reconciliations_read_get_reconciliations(bank_account_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of BankAccountsApi->external_api_bank_account_reconciliations_read_get_reconciliations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_reconciliations_read_get_reconciliations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BankAccountReconciliationMessage]**](BankAccountReconciliationMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Total-Count - The total number of records available in the overall result set of the request. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**409** | There is a request conflict with the current state of the target resource. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_reconciliations_write_clear_transactions**
> external_api_bank_account_reconciliations_write_clear_transactions(bank_account_id, reconciliation_id, bank_reconciliation_clear_transactions_post_message)

Clear transactions for a reconciliation

Clears transactions for a reconciliation. Reconciliation transactions can only be cleared for bank accounts that are not linked externally.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_reconciliation_clear_transactions_post_message import BankReconciliationClearTransactionsPostMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    reconciliation_id = 56 # int | 
    bank_reconciliation_clear_transactions_post_message = buildium_sdk.BankReconciliationClearTransactionsPostMessage() # BankReconciliationClearTransactionsPostMessage | 

    try:
        # Clear transactions for a reconciliation
        await api_instance.external_api_bank_account_reconciliations_write_clear_transactions(bank_account_id, reconciliation_id, bank_reconciliation_clear_transactions_post_message)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_reconciliations_write_clear_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **reconciliation_id** | **int**|  | 
 **bank_reconciliation_clear_transactions_post_message** | [**BankReconciliationClearTransactionsPostMessage**](BankReconciliationClearTransactionsPostMessage.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NoContent |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**409** | There is a request conflict with the current state of the target resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_reconciliations_write_unclear_transactions**
> external_api_bank_account_reconciliations_write_unclear_transactions(bank_account_id, reconciliation_id, bank_reconciliation_unclear_transactions_post_message)

Un-clear transactions for a reconciliation

Un-clears transactions for a reconciliation. Reconciliation transactions can only be un-cleared for bank accounts that are not linked externally.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_reconciliation_unclear_transactions_post_message import BankReconciliationUnclearTransactionsPostMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    reconciliation_id = 56 # int | 
    bank_reconciliation_unclear_transactions_post_message = buildium_sdk.BankReconciliationUnclearTransactionsPostMessage() # BankReconciliationUnclearTransactionsPostMessage | 

    try:
        # Un-clear transactions for a reconciliation
        await api_instance.external_api_bank_account_reconciliations_write_unclear_transactions(bank_account_id, reconciliation_id, bank_reconciliation_unclear_transactions_post_message)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_reconciliations_write_unclear_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **reconciliation_id** | **int**|  | 
 **bank_reconciliation_unclear_transactions_post_message** | [**BankReconciliationUnclearTransactionsPostMessage**](BankReconciliationUnclearTransactionsPostMessage.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NoContent |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**409** | There is a request conflict with the current state of the target resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_reconciliations_write_update_reconciliation**
> BankAccountReconciliationMessage external_api_bank_account_reconciliations_write_update_reconciliation(bank_account_id, reconciliation_id, bank_reconciliation_put_message)

Update a reconciliation

Updates a reconciliation. Reconciliations can only be updated for bank accounts that are not linked externally.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_reconciliation_message import BankAccountReconciliationMessage
from buildium_sdk.models.bank_reconciliation_put_message import BankReconciliationPutMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    reconciliation_id = 56 # int | 
    bank_reconciliation_put_message = buildium_sdk.BankReconciliationPutMessage() # BankReconciliationPutMessage | 

    try:
        # Update a reconciliation
        api_response = await api_instance.external_api_bank_account_reconciliations_write_update_reconciliation(bank_account_id, reconciliation_id, bank_reconciliation_put_message)
        print("The response of BankAccountsApi->external_api_bank_account_reconciliations_write_update_reconciliation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_reconciliations_write_update_reconciliation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **reconciliation_id** | **int**|  | 
 **bank_reconciliation_put_message** | [**BankReconciliationPutMessage**](BankReconciliationPutMessage.md)|  | 

### Return type

[**BankAccountReconciliationMessage**](BankAccountReconciliationMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**409** | There is a request conflict with the current state of the target resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_reconciliations_write_update_reconciliation_balances**
> BankAccountReconciliationBalanceMessage external_api_bank_account_reconciliations_write_update_reconciliation_balances(bank_account_id, reconciliation_id, bank_account_reconciliation_balance_put_message)

Update a reconciliation's balance

Updates a bank account reconciliation's balance. Reconciliation balances can only be updated for bank accounts that are not linked externally.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_reconciliation_balance_message import BankAccountReconciliationBalanceMessage
from buildium_sdk.models.bank_account_reconciliation_balance_put_message import BankAccountReconciliationBalancePutMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    reconciliation_id = 56 # int | 
    bank_account_reconciliation_balance_put_message = buildium_sdk.BankAccountReconciliationBalancePutMessage() # BankAccountReconciliationBalancePutMessage | 

    try:
        # Update a reconciliation's balance
        api_response = await api_instance.external_api_bank_account_reconciliations_write_update_reconciliation_balances(bank_account_id, reconciliation_id, bank_account_reconciliation_balance_put_message)
        print("The response of BankAccountsApi->external_api_bank_account_reconciliations_write_update_reconciliation_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_reconciliations_write_update_reconciliation_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **reconciliation_id** | **int**|  | 
 **bank_account_reconciliation_balance_put_message** | [**BankAccountReconciliationBalancePutMessage**](BankAccountReconciliationBalancePutMessage.md)|  | 

### Return type

[**BankAccountReconciliationBalanceMessage**](BankAccountReconciliationBalanceMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**409** | There is a request conflict with the current state of the target resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_transactions_get_bank_account_transaction_by_id**
> BankAccountTransactionMessage external_api_bank_account_transactions_get_bank_account_transaction_by_id(bank_account_id, transaction_id)

Retrieve a transaction

Retrieves a specific bank account transaction.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Account</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_transaction_message import BankAccountTransactionMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    transaction_id = 56 # int | 

    try:
        # Retrieve a transaction
        api_response = await api_instance.external_api_bank_account_transactions_get_bank_account_transaction_by_id(bank_account_id, transaction_id)
        print("The response of BankAccountsApi->external_api_bank_account_transactions_get_bank_account_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_transactions_get_bank_account_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **transaction_id** | **int**|  | 

### Return type

[**BankAccountTransactionMessage**](BankAccountTransactionMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_transactions_get_bank_account_transactions**
> List[BankAccountTransactionMessage] external_api_bank_account_transactions_get_bank_account_transactions(bank_account_id, startdate, enddate, selectionentityid=selectionentityid, selectionentitytype=selectionentitytype, orderby=orderby, offset=offset, limit=limit)

Retrieve all transactions

Retrieves all bank account transactions.
            


            Note: When using the `orderby` query string parameter, the only supported parameter is `EntryDate`.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_transaction_message import BankAccountTransactionMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    startdate = '2013-10-20' # date | Filters results to any transactions that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD.
    enddate = '2013-10-20' # date | Filters results to any transactions that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD.
    selectionentityid = 56 # int | Filters results to any transaction containing journal lines for an entity associated with the specified entity id value. The id must be of the type specified in SelectionEntityType. (optional)
    selectionentitytype = 'selectionentitytype_example' # str | Specifies the type of entity that SelectionEntityId refers to. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all transactions
        api_response = await api_instance.external_api_bank_account_transactions_get_bank_account_transactions(bank_account_id, startdate, enddate, selectionentityid=selectionentityid, selectionentitytype=selectionentitytype, orderby=orderby, offset=offset, limit=limit)
        print("The response of BankAccountsApi->external_api_bank_account_transactions_get_bank_account_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_transactions_get_bank_account_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **startdate** | **date**| Filters results to any transactions that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD. | 
 **enddate** | **date**| Filters results to any transactions that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD. | 
 **selectionentityid** | **int**| Filters results to any transaction containing journal lines for an entity associated with the specified entity id value. The id must be of the type specified in SelectionEntityType. | [optional] 
 **selectionentitytype** | **str**| Specifies the type of entity that SelectionEntityId refers to. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BankAccountTransactionMessage]**](BankAccountTransactionMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Total-Count - The total number of records available in the overall result set of the request. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_transfers_create_bank_account_transfer**
> BankAccountTransferMessage external_api_bank_account_transfers_create_bank_account_transfer(bank_account_id, bank_account_transfer_save_message)

Create a transfer

Creates a bank account transfer.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_transfer_message import BankAccountTransferMessage
from buildium_sdk.models.bank_account_transfer_save_message import BankAccountTransferSaveMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    bank_account_transfer_save_message = buildium_sdk.BankAccountTransferSaveMessage() # BankAccountTransferSaveMessage | 

    try:
        # Create a transfer
        api_response = await api_instance.external_api_bank_account_transfers_create_bank_account_transfer(bank_account_id, bank_account_transfer_save_message)
        print("The response of BankAccountsApi->external_api_bank_account_transfers_create_bank_account_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_transfers_create_bank_account_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **bank_account_transfer_save_message** | [**BankAccountTransferSaveMessage**](BankAccountTransferSaveMessage.md)|  | 

### Return type

[**BankAccountTransferMessage**](BankAccountTransferMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - The location to retrieve the created resource. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_transfers_get_bank_account_transfer_by_id**
> BankAccountMessage external_api_bank_account_transfers_get_bank_account_transfer_by_id(bank_account_id, transfer_id)

Retrieve a transfer

Retrieves a bank account transfer.


<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_message import BankAccountMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | The bank account identifier.
    transfer_id = 56 # int | The transfer identifier.

    try:
        # Retrieve a transfer
        api_response = await api_instance.external_api_bank_account_transfers_get_bank_account_transfer_by_id(bank_account_id, transfer_id)
        print("The response of BankAccountsApi->external_api_bank_account_transfers_get_bank_account_transfer_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_transfers_get_bank_account_transfer_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**| The bank account identifier. | 
 **transfer_id** | **int**| The transfer identifier. | 

### Return type

[**BankAccountMessage**](BankAccountMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_transfers_get_bank_account_transfers**
> List[BankAccountTransferMessage] external_api_bank_account_transfers_get_bank_account_transfers(bank_account_id, startdate, enddate, orderby=orderby, offset=offset, limit=limit)

Retrieve all transfers

Retrieves all bank account transfers.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccount</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_transfer_message import BankAccountTransferMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    startdate = '2013-10-20' # date | Filters results to any transfers that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD.
    enddate = '2013-10-20' # date | Filters results to any transfers that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD.
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all transfers
        api_response = await api_instance.external_api_bank_account_transfers_get_bank_account_transfers(bank_account_id, startdate, enddate, orderby=orderby, offset=offset, limit=limit)
        print("The response of BankAccountsApi->external_api_bank_account_transfers_get_bank_account_transfers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_transfers_get_bank_account_transfers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **startdate** | **date**| Filters results to any transfers that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD. | 
 **enddate** | **date**| Filters results to any transfers that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD. | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BankAccountTransferMessage]**](BankAccountTransferMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Total-Count - The total number of records available in the overall result set of the request. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_transfers_update_bank_account_transfer**
> BankAccountTransferMessage external_api_bank_account_transfers_update_bank_account_transfer(bank_account_id, transfer_id, bank_account_transfer_save_message)

Update a transfer

Updates a bank account transfer.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_transfer_message import BankAccountTransferMessage
from buildium_sdk.models.bank_account_transfer_save_message import BankAccountTransferSaveMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    transfer_id = 56 # int | 
    bank_account_transfer_save_message = buildium_sdk.BankAccountTransferSaveMessage() # BankAccountTransferSaveMessage | 

    try:
        # Update a transfer
        api_response = await api_instance.external_api_bank_account_transfers_update_bank_account_transfer(bank_account_id, transfer_id, bank_account_transfer_save_message)
        print("The response of BankAccountsApi->external_api_bank_account_transfers_update_bank_account_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_transfers_update_bank_account_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **transfer_id** | **int**|  | 
 **bank_account_transfer_save_message** | [**BankAccountTransferSaveMessage**](BankAccountTransferSaveMessage.md)|  | 

### Return type

[**BankAccountTransferMessage**](BankAccountTransferMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_undeposited_funds_get_undeposited_funds**
> List[UndepositedFundsMessage] external_api_bank_account_undeposited_funds_get_undeposited_funds(bank_account_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all undeposited funds

Retrieve all bank account undeposited funds.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.undeposited_funds_message import UndepositedFundsMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all undeposited funds
        api_response = await api_instance.external_api_bank_account_undeposited_funds_get_undeposited_funds(bank_account_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of BankAccountsApi->external_api_bank_account_undeposited_funds_get_undeposited_funds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_undeposited_funds_get_undeposited_funds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[UndepositedFundsMessage]**](UndepositedFundsMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Total-Count - The total number of records available in the overall result set of the request. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_withdrawals_create_withdrawal_for_bank_account**
> BankAccountWithdrawalMessage external_api_bank_account_withdrawals_create_withdrawal_for_bank_account(bank_account_id, bank_account_withdrawal_save_message)

Create a withdrawal

Creates a bank account withdrawal.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_withdrawal_message import BankAccountWithdrawalMessage
from buildium_sdk.models.bank_account_withdrawal_save_message import BankAccountWithdrawalSaveMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    bank_account_withdrawal_save_message = buildium_sdk.BankAccountWithdrawalSaveMessage() # BankAccountWithdrawalSaveMessage | 

    try:
        # Create a withdrawal
        api_response = await api_instance.external_api_bank_account_withdrawals_create_withdrawal_for_bank_account(bank_account_id, bank_account_withdrawal_save_message)
        print("The response of BankAccountsApi->external_api_bank_account_withdrawals_create_withdrawal_for_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_withdrawals_create_withdrawal_for_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **bank_account_withdrawal_save_message** | [**BankAccountWithdrawalSaveMessage**](BankAccountWithdrawalSaveMessage.md)|  | 

### Return type

[**BankAccountWithdrawalMessage**](BankAccountWithdrawalMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - The location to retrieve the created resource. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_withdrawals_get_bank_account_withdrawal_by_id**
> BankAccountWithdrawalMessage external_api_bank_account_withdrawals_get_bank_account_withdrawal_by_id(bank_account_id, withdrawal_id)

Retrieve a withdrawal

Retrieves a bank account withdrawal.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_withdrawal_message import BankAccountWithdrawalMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    withdrawal_id = 56 # int | 

    try:
        # Retrieve a withdrawal
        api_response = await api_instance.external_api_bank_account_withdrawals_get_bank_account_withdrawal_by_id(bank_account_id, withdrawal_id)
        print("The response of BankAccountsApi->external_api_bank_account_withdrawals_get_bank_account_withdrawal_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_withdrawals_get_bank_account_withdrawal_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **withdrawal_id** | **int**|  | 

### Return type

[**BankAccountWithdrawalMessage**](BankAccountWithdrawalMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_withdrawals_get_bank_account_withdrawals**
> List[BankAccountWithdrawalMessage] external_api_bank_account_withdrawals_get_bank_account_withdrawals(bank_account_id, startdate, enddate, orderby=orderby, offset=offset, limit=limit)

Retrieve all withdrawals

Retrieves all bank account withdrawals.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > BankAccounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_withdrawal_message import BankAccountWithdrawalMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    startdate = '2013-10-20' # date | Filters results to any transactions that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD.
    enddate = '2013-10-20' # date | Filters results to any transactions that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD.
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all withdrawals
        api_response = await api_instance.external_api_bank_account_withdrawals_get_bank_account_withdrawals(bank_account_id, startdate, enddate, orderby=orderby, offset=offset, limit=limit)
        print("The response of BankAccountsApi->external_api_bank_account_withdrawals_get_bank_account_withdrawals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_withdrawals_get_bank_account_withdrawals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **startdate** | **date**| Filters results to any transactions that were recorded on or after the specified date. The value must be formatted as YYYY-MM-DD. | 
 **enddate** | **date**| Filters results to any transactions that were recorded on or before the specified date. The value must be formatted as YYYY-MM-DD. | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BankAccountWithdrawalMessage]**](BankAccountWithdrawalMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Total-Count - The total number of records available in the overall result set of the request. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_account_withdrawals_update_bank_account_withdrawal**
> BankAccountWithdrawalMessage external_api_bank_account_withdrawals_update_bank_account_withdrawal(bank_account_id, withdrawal_id, bank_account_withdrawal_save_message)

Update a withdrawal

Updates a bank account withdrawal.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_withdrawal_message import BankAccountWithdrawalMessage
from buildium_sdk.models.bank_account_withdrawal_save_message import BankAccountWithdrawalSaveMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    withdrawal_id = 56 # int | 
    bank_account_withdrawal_save_message = buildium_sdk.BankAccountWithdrawalSaveMessage() # BankAccountWithdrawalSaveMessage | 

    try:
        # Update a withdrawal
        api_response = await api_instance.external_api_bank_account_withdrawals_update_bank_account_withdrawal(bank_account_id, withdrawal_id, bank_account_withdrawal_save_message)
        print("The response of BankAccountsApi->external_api_bank_account_withdrawals_update_bank_account_withdrawal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_account_withdrawals_update_bank_account_withdrawal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **withdrawal_id** | **int**|  | 
 **bank_account_withdrawal_save_message** | [**BankAccountWithdrawalSaveMessage**](BankAccountWithdrawalSaveMessage.md)|  | 

### Return type

[**BankAccountWithdrawalMessage**](BankAccountWithdrawalMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_accounts_create_bank_account**
> BankAccountMessage external_api_bank_accounts_create_bank_account(bank_account_post_message)

Create a bank account

Creates a bank account.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Banking</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_message import BankAccountMessage
from buildium_sdk.models.bank_account_post_message import BankAccountPostMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_post_message = buildium_sdk.BankAccountPostMessage() # BankAccountPostMessage | 

    try:
        # Create a bank account
        api_response = await api_instance.external_api_bank_accounts_create_bank_account(bank_account_post_message)
        print("The response of BankAccountsApi->external_api_bank_accounts_create_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_accounts_create_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_post_message** | [**BankAccountPostMessage**](BankAccountPostMessage.md)|  | 

### Return type

[**BankAccountMessage**](BankAccountMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - The location to retrieve the created resource. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_accounts_get_all_bank_accounts**
> List[BankAccountMessage] external_api_bank_accounts_get_all_bank_accounts(bankaccountstatus=bankaccountstatus, bankname=bankname, routingnumbers=routingnumbers, orderby=orderby, offset=offset, limit=limit)

Retrieve all bank accounts

Retrieves a list of bank accounts.


<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_message import BankAccountMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bankaccountstatus = 'bankaccountstatus_example' # str | Filters results by the status of the bank account. If no status is specified, bank accounts with any status will be returned. (optional)
    bankname = 'bankname_example' # str | Filters results to any bank account whose name *contains* the specified value. (optional)
    routingnumbers = ['routingnumbers_example'] # List[str] | Filters results to any bank accounts whose routing number *contains* the specified value. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all bank accounts
        api_response = await api_instance.external_api_bank_accounts_get_all_bank_accounts(bankaccountstatus=bankaccountstatus, bankname=bankname, routingnumbers=routingnumbers, orderby=orderby, offset=offset, limit=limit)
        print("The response of BankAccountsApi->external_api_bank_accounts_get_all_bank_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_accounts_get_all_bank_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankaccountstatus** | **str**| Filters results by the status of the bank account. If no status is specified, bank accounts with any status will be returned. | [optional] 
 **bankname** | **str**| Filters results to any bank account whose name *contains* the specified value. | [optional] 
 **routingnumbers** | [**List[str]**](str.md)| Filters results to any bank accounts whose routing number *contains* the specified value. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BankAccountMessage]**](BankAccountMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Total-Count - The total number of records available in the overall result set of the request. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_accounts_get_bank_account**
> BankAccountMessage external_api_bank_accounts_get_bank_account(bank_account_id)

Retrieve a bank account

Retrieves a specific bank account.


<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_message import BankAccountMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | The bank account identifier.

    try:
        # Retrieve a bank account
        api_response = await api_instance.external_api_bank_accounts_get_bank_account(bank_account_id)
        print("The response of BankAccountsApi->external_api_bank_accounts_get_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_accounts_get_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**| The bank account identifier. | 

### Return type

[**BankAccountMessage**](BankAccountMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bank_accounts_update_bank_account**
> BankAccountMessage external_api_bank_accounts_update_bank_account(bank_account_id, bank_account_put_message)

Update a bank account

Updates a bank account.;
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Banking</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_account_message import BankAccountMessage
from buildium_sdk.models.bank_account_put_message import BankAccountPutMessage
from buildium_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.buildium.com
# See configuration.py for a list of all supported configuration parameters.
configuration = buildium_sdk.Configuration(
    host = "https://api.buildium.com"
)


# Enter a context with an instance of the API client
async with buildium_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buildium_sdk.BankAccountsApi(api_client)
    bank_account_id = 56 # int | 
    bank_account_put_message = buildium_sdk.BankAccountPutMessage() # BankAccountPutMessage | 

    try:
        # Update a bank account
        api_response = await api_instance.external_api_bank_accounts_update_bank_account(bank_account_id, bank_account_put_message)
        print("The response of BankAccountsApi->external_api_bank_accounts_update_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->external_api_bank_accounts_update_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**|  | 
 **bank_account_put_message** | [**BankAccountPutMessage**](BankAccountPutMessage.md)|  | 

### Return type

[**BankAccountMessage**](BankAccountMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

