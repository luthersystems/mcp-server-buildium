# buildium_sdk.GeneralLedgerApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_general_ledger_accounts_create_general_ledger_account**](GeneralLedgerApi.md#external_api_general_ledger_accounts_create_general_ledger_account) | **POST** /v1/glaccounts | Create a general ledger account
[**external_api_general_ledger_accounts_get_all_gl_accounts**](GeneralLedgerApi.md#external_api_general_ledger_accounts_get_all_gl_accounts) | **GET** /v1/glaccounts | Retrieve all general ledger accounts
[**external_api_general_ledger_accounts_get_gl_account_by_id**](GeneralLedgerApi.md#external_api_general_ledger_accounts_get_gl_account_by_id) | **GET** /v1/glaccounts/{glAccountId} | Retrieve a general ledger account
[**external_api_general_ledger_accounts_update_gl_account**](GeneralLedgerApi.md#external_api_general_ledger_accounts_update_gl_account) | **PUT** /v1/glaccounts/{glAccountId} | Update a general ledger account
[**external_api_general_ledger_get_general_ledger_entries**](GeneralLedgerApi.md#external_api_general_ledger_get_general_ledger_entries) | **GET** /v1/generalledger | Retrieve all general ledger entries
[**external_api_general_ledger_journal_entries_create_general_journal_entry**](GeneralLedgerApi.md#external_api_general_ledger_journal_entries_create_general_journal_entry) | **POST** /v1/generalledger/journalentries | Create a general journal entry
[**external_api_general_ledger_journal_entries_update_general_journal_entry**](GeneralLedgerApi.md#external_api_general_ledger_journal_entries_update_general_journal_entry) | **PUT** /v1/generalledger/journalentries/{journalEntryId} | Update a general journal entry
[**external_api_general_ledger_transactions_get_all_transactions**](GeneralLedgerApi.md#external_api_general_ledger_transactions_get_all_transactions) | **GET** /v1/generalledger/transactions | Retrieve all general ledger transactions
[**external_api_general_ledger_transactions_get_transaction_by_id**](GeneralLedgerApi.md#external_api_general_ledger_transactions_get_transaction_by_id) | **GET** /v1/generalledger/transactions/{transactionId} | Retrieve a general ledger transaction
[**external_api_gl_account_balances_get_gl_account_balances**](GeneralLedgerApi.md#external_api_gl_account_balances_get_gl_account_balances) | **GET** /v1/glaccounts/balances | Retrieve all general ledger account balances


# **external_api_general_ledger_accounts_create_general_ledger_account**
> GLAccountMessage external_api_general_ledger_accounts_create_general_ledger_account(gl_account_post_message)

Create a general ledger account

Creates a general ledger account.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > General Ledger Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.gl_account_message import GLAccountMessage
from buildium_sdk.models.gl_account_post_message import GLAccountPostMessage
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
    api_instance = buildium_sdk.GeneralLedgerApi(api_client)
    gl_account_post_message = buildium_sdk.GLAccountPostMessage() # GLAccountPostMessage | 

    try:
        # Create a general ledger account
        api_response = await api_instance.external_api_general_ledger_accounts_create_general_ledger_account(gl_account_post_message)
        print("The response of GeneralLedgerApi->external_api_general_ledger_accounts_create_general_ledger_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralLedgerApi->external_api_general_ledger_accounts_create_general_ledger_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gl_account_post_message** | [**GLAccountPostMessage**](GLAccountPostMessage.md)|  | 

### Return type

[**GLAccountMessage**](GLAccountMessage.md)

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
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_general_ledger_accounts_get_all_gl_accounts**
> List[GLAccountMessage] external_api_general_ledger_accounts_get_all_gl_accounts(accounttypes=accounttypes, orderby=orderby, offset=offset, limit=limit)

Retrieve all general ledger accounts

Retrieves a list of general ledger accounts.

General ledger accounts are used to categorize transactions for accounting purposes.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > General Ledger Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.gl_account_message import GLAccountMessage
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
    api_instance = buildium_sdk.GeneralLedgerApi(api_client)
    accounttypes = ['accounttypes_example'] # List[str] | Filters results by the specified general ledger account types. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all general ledger accounts
        api_response = await api_instance.external_api_general_ledger_accounts_get_all_gl_accounts(accounttypes=accounttypes, orderby=orderby, offset=offset, limit=limit)
        print("The response of GeneralLedgerApi->external_api_general_ledger_accounts_get_all_gl_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralLedgerApi->external_api_general_ledger_accounts_get_all_gl_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounttypes** | [**List[str]**](str.md)| Filters results by the specified general ledger account types. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[GLAccountMessage]**](GLAccountMessage.md)

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

# **external_api_general_ledger_accounts_get_gl_account_by_id**
> GLAccountMessage external_api_general_ledger_accounts_get_gl_account_by_id(gl_account_id)

Retrieve a general ledger account

Retrieves a specific general ledger account.


<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > General Ledger Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.gl_account_message import GLAccountMessage
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
    api_instance = buildium_sdk.GeneralLedgerApi(api_client)
    gl_account_id = 56 # int | The general ledger account identifier.

    try:
        # Retrieve a general ledger account
        api_response = await api_instance.external_api_general_ledger_accounts_get_gl_account_by_id(gl_account_id)
        print("The response of GeneralLedgerApi->external_api_general_ledger_accounts_get_gl_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralLedgerApi->external_api_general_ledger_accounts_get_gl_account_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gl_account_id** | **int**| The general ledger account identifier. | 

### Return type

[**GLAccountMessage**](GLAccountMessage.md)

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

# **external_api_general_ledger_accounts_update_gl_account**
> GLAccountMessage external_api_general_ledger_accounts_update_gl_account(gl_account_id, gl_account_put_message)

Update a general ledger account

Updates a general ledger account.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > General Ledger Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.gl_account_message import GLAccountMessage
from buildium_sdk.models.gl_account_put_message import GLAccountPutMessage
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
    api_instance = buildium_sdk.GeneralLedgerApi(api_client)
    gl_account_id = 56 # int | 
    gl_account_put_message = buildium_sdk.GLAccountPutMessage() # GLAccountPutMessage | 

    try:
        # Update a general ledger account
        api_response = await api_instance.external_api_general_ledger_accounts_update_gl_account(gl_account_id, gl_account_put_message)
        print("The response of GeneralLedgerApi->external_api_general_ledger_accounts_update_gl_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralLedgerApi->external_api_general_ledger_accounts_update_gl_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gl_account_id** | **int**|  | 
 **gl_account_put_message** | [**GLAccountPutMessage**](GLAccountPutMessage.md)|  | 

### Return type

[**GLAccountMessage**](GLAccountMessage.md)

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

# **external_api_general_ledger_get_general_ledger_entries**
> List[GeneralLedgerMessage] external_api_general_ledger_get_general_ledger_entries(accountingbasis, glaccountids, startdate, enddate, entitytype=entitytype, entityid=entityid, orderby=orderby, offset=offset, limit=limit)

Retrieve all general ledger entries

Retrieves all general ledger entries
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.general_ledger_message import GeneralLedgerMessage
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
    api_instance = buildium_sdk.GeneralLedgerApi(api_client)
    accountingbasis = 'accountingbasis_example' # str | The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened.
    glaccountids = [56] # List[int] | Filters results to entries whose general ledger account belongs to the specified set of general ledger account ids.
    startdate = '2013-10-20' # date | Filters results to any entries whose start date is greater than or equal to the specified value.
    enddate = '2013-10-20' # date | Filters results to any entries whose end date is less than or equal to the specified value.
    entitytype = 'entitytype_example' # str | Specifies the type of entity that `EntityId` field refers to. (optional)
    entityid = 56 # int | Filters results to any general ledger entry containing line items associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all general ledger entries
        api_response = await api_instance.external_api_general_ledger_get_general_ledger_entries(accountingbasis, glaccountids, startdate, enddate, entitytype=entitytype, entityid=entityid, orderby=orderby, offset=offset, limit=limit)
        print("The response of GeneralLedgerApi->external_api_general_ledger_get_general_ledger_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralLedgerApi->external_api_general_ledger_get_general_ledger_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountingbasis** | **str**| The methodology in which revenues and expenses are recognized when calculating the balances. Specifying &#x60;Cash&#x60; calculates balances based on when money changes hands. Specifying &#x60;Accrual&#x60; calculates balances based on the period in which the transaction originally happened. | 
 **glaccountids** | [**List[int]**](int.md)| Filters results to entries whose general ledger account belongs to the specified set of general ledger account ids. | 
 **startdate** | **date**| Filters results to any entries whose start date is greater than or equal to the specified value. | 
 **enddate** | **date**| Filters results to any entries whose end date is less than or equal to the specified value. | 
 **entitytype** | **str**| Specifies the type of entity that &#x60;EntityId&#x60; field refers to. | [optional] 
 **entityid** | **int**| Filters results to any general ledger entry containing line items associated with the specified entity identifier. This filter is used in conjunction with the &#x60;EntityType&#x60; field which must be set to the type of entity this identifier references. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[GeneralLedgerMessage]**](GeneralLedgerMessage.md)

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
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_general_ledger_journal_entries_create_general_journal_entry**
> GeneralLedgerTransactionMessage external_api_general_ledger_journal_entries_create_general_journal_entry(general_journal_entry_post_message)

Create a general journal entry

Creates a general journal entry.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.general_journal_entry_post_message import GeneralJournalEntryPostMessage
from buildium_sdk.models.general_ledger_transaction_message import GeneralLedgerTransactionMessage
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
    api_instance = buildium_sdk.GeneralLedgerApi(api_client)
    general_journal_entry_post_message = buildium_sdk.GeneralJournalEntryPostMessage() # GeneralJournalEntryPostMessage | 

    try:
        # Create a general journal entry
        api_response = await api_instance.external_api_general_ledger_journal_entries_create_general_journal_entry(general_journal_entry_post_message)
        print("The response of GeneralLedgerApi->external_api_general_ledger_journal_entries_create_general_journal_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralLedgerApi->external_api_general_ledger_journal_entries_create_general_journal_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **general_journal_entry_post_message** | [**GeneralJournalEntryPostMessage**](GeneralJournalEntryPostMessage.md)|  | 

### Return type

[**GeneralLedgerTransactionMessage**](GeneralLedgerTransactionMessage.md)

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
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_general_ledger_journal_entries_update_general_journal_entry**
> GeneralLedgerTransactionMessage external_api_general_ledger_journal_entries_update_general_journal_entry(journal_entry_id, general_journal_entry_put_message)

Update a general journal entry

Updates a general journal entry.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.general_journal_entry_put_message import GeneralJournalEntryPutMessage
from buildium_sdk.models.general_ledger_transaction_message import GeneralLedgerTransactionMessage
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
    api_instance = buildium_sdk.GeneralLedgerApi(api_client)
    journal_entry_id = 56 # int | 
    general_journal_entry_put_message = buildium_sdk.GeneralJournalEntryPutMessage() # GeneralJournalEntryPutMessage | 

    try:
        # Update a general journal entry
        api_response = await api_instance.external_api_general_ledger_journal_entries_update_general_journal_entry(journal_entry_id, general_journal_entry_put_message)
        print("The response of GeneralLedgerApi->external_api_general_ledger_journal_entries_update_general_journal_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralLedgerApi->external_api_general_ledger_journal_entries_update_general_journal_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_entry_id** | **int**|  | 
 **general_journal_entry_put_message** | [**GeneralJournalEntryPutMessage**](GeneralJournalEntryPutMessage.md)|  | 

### Return type

[**GeneralLedgerTransactionMessage**](GeneralLedgerTransactionMessage.md)

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

# **external_api_general_ledger_transactions_get_all_transactions**
> List[GeneralLedgerTransactionMessage] external_api_general_ledger_transactions_get_all_transactions(startdate, enddate, glaccountids, selectionentityid=selectionentityid, selectionentitytype=selectionentitytype, selectionentityunitid=selectionentityunitid, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)

Retrieve all general ledger transactions

Retrieves a list of general ledger transactions.


<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.general_ledger_transaction_message import GeneralLedgerTransactionMessage
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
    api_instance = buildium_sdk.GeneralLedgerApi(api_client)
    startdate = '2013-10-20' # date | Filters results to any transaction whose date is greater than or equal to the specified value.
    enddate = '2013-10-20' # date | Filters results to any transaction whose date is less than or equal to the specified value.
    glaccountids = [56] # List[int] | Filters results to transactions whose general ledger account belongs to the specified set of general ledger account ids.
    selectionentityid = 56 # int | Filters results to any transaction containing journal lines for an entity associated with the specified entity id value. The id must be of the type specified in SelectionEntityType. (optional)
    selectionentitytype = 'selectionentitytype_example' # str | Specifies the type of entity that SelectionEntityId refers to. (optional)
    selectionentityunitid = 56 # int | Filters results to any transaction containing journal lines for the unitId specified. Only applicable when the SelectionEntityType is Rentals or Associations. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any transactions that were updated on or after the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any transactions that were updated on or before the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all general ledger transactions
        api_response = await api_instance.external_api_general_ledger_transactions_get_all_transactions(startdate, enddate, glaccountids, selectionentityid=selectionentityid, selectionentitytype=selectionentitytype, selectionentityunitid=selectionentityunitid, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)
        print("The response of GeneralLedgerApi->external_api_general_ledger_transactions_get_all_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralLedgerApi->external_api_general_ledger_transactions_get_all_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startdate** | **date**| Filters results to any transaction whose date is greater than or equal to the specified value. | 
 **enddate** | **date**| Filters results to any transaction whose date is less than or equal to the specified value. | 
 **glaccountids** | [**List[int]**](int.md)| Filters results to transactions whose general ledger account belongs to the specified set of general ledger account ids. | 
 **selectionentityid** | **int**| Filters results to any transaction containing journal lines for an entity associated with the specified entity id value. The id must be of the type specified in SelectionEntityType. | [optional] 
 **selectionentitytype** | **str**| Specifies the type of entity that SelectionEntityId refers to. | [optional] 
 **selectionentityunitid** | **int**| Filters results to any transaction containing journal lines for the unitId specified. Only applicable when the SelectionEntityType is Rentals or Associations. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to any transactions that were updated on or after the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to any transactions that were updated on or before the specified date. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[GeneralLedgerTransactionMessage]**](GeneralLedgerTransactionMessage.md)

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
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_general_ledger_transactions_get_transaction_by_id**
> GeneralLedgerTransactionMessage external_api_general_ledger_transactions_get_transaction_by_id(transaction_id)

Retrieve a general ledger transaction

Retrieves a specific general ledger transaction.


<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.general_ledger_transaction_message import GeneralLedgerTransactionMessage
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
    api_instance = buildium_sdk.GeneralLedgerApi(api_client)
    transaction_id = 56 # int | The general ledger transaction identifier.

    try:
        # Retrieve a general ledger transaction
        api_response = await api_instance.external_api_general_ledger_transactions_get_transaction_by_id(transaction_id)
        print("The response of GeneralLedgerApi->external_api_general_ledger_transactions_get_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralLedgerApi->external_api_general_ledger_transactions_get_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **int**| The general ledger transaction identifier. | 

### Return type

[**GeneralLedgerTransactionMessage**](GeneralLedgerTransactionMessage.md)

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

# **external_api_gl_account_balances_get_gl_account_balances**
> List[GLAccountBalanceMessage] external_api_gl_account_balances_get_gl_account_balances(accountingbasis, asofdate, entitytype=entitytype, entityid=entityid, glaccountids=glaccountids, aggregatebalancesbyunitid=aggregatebalancesbyunitid, orderby=orderby, offset=offset, limit=limit)

Retrieve all general ledger account balances

Retrieves all general ledger account balances as of a given date. The response includes the total balance of each account along with the subtotals for any accounting entities (company, associations or rental properties) that have transactions assigned to the account.


<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > General Ledger Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.gl_account_balance_message import GLAccountBalanceMessage
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
    api_instance = buildium_sdk.GeneralLedgerApi(api_client)
    accountingbasis = 'accountingbasis_example' # str | The methodology in which revenues and expenses are recognized when calculating the balances. Specifying `Cash` calculates balances based on when money changes hands. Specifying `Accrual` calculates balances based on the period in which the transaction originally happened.
    asofdate = '2013-10-20' # date | Indicates the end date through which the balances will be calculated. This will include all transactions in your account until this specified date.
    entitytype = 'entitytype_example' # str | Specifies the type of entity that `EntityId` field refers to. (optional)
    entityid = 56 # int | Filters transactions used in calculating the general ledger account balances to only those containing journal lines for with the specified entity id value. The entity id specified must be of the type specified in `EntityType`. (optional)
    glaccountids = [56] # List[int] | Filters results to the specified set of general ledger account identifiers. (optional)
    aggregatebalancesbyunitid = True # bool | Indicates whether to aggregate the AccountingEntityBalances by unit identifier in the response. If the value is set to true the AccountingEntityBalances will be aggregated by AccountingEntity.Unit.Id otherwise the response will have the balances aggregated by AccountingEntity.Id. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all general ledger account balances
        api_response = await api_instance.external_api_gl_account_balances_get_gl_account_balances(accountingbasis, asofdate, entitytype=entitytype, entityid=entityid, glaccountids=glaccountids, aggregatebalancesbyunitid=aggregatebalancesbyunitid, orderby=orderby, offset=offset, limit=limit)
        print("The response of GeneralLedgerApi->external_api_gl_account_balances_get_gl_account_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralLedgerApi->external_api_gl_account_balances_get_gl_account_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountingbasis** | **str**| The methodology in which revenues and expenses are recognized when calculating the balances. Specifying &#x60;Cash&#x60; calculates balances based on when money changes hands. Specifying &#x60;Accrual&#x60; calculates balances based on the period in which the transaction originally happened. | 
 **asofdate** | **date**| Indicates the end date through which the balances will be calculated. This will include all transactions in your account until this specified date. | 
 **entitytype** | **str**| Specifies the type of entity that &#x60;EntityId&#x60; field refers to. | [optional] 
 **entityid** | **int**| Filters transactions used in calculating the general ledger account balances to only those containing journal lines for with the specified entity id value. The entity id specified must be of the type specified in &#x60;EntityType&#x60;. | [optional] 
 **glaccountids** | [**List[int]**](int.md)| Filters results to the specified set of general ledger account identifiers. | [optional] 
 **aggregatebalancesbyunitid** | **bool**| Indicates whether to aggregate the AccountingEntityBalances by unit identifier in the response. If the value is set to true the AccountingEntityBalances will be aggregated by AccountingEntity.Unit.Id otherwise the response will have the balances aggregated by AccountingEntity.Id. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[GLAccountBalanceMessage]**](GLAccountBalanceMessage.md)

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
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

