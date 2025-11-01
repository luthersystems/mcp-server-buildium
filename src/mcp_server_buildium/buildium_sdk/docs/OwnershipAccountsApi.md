# buildium_sdk.OwnershipAccountsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_ownership_account_notes_create_association_ownership_account_note**](OwnershipAccountsApi.md#external_api_ownership_account_notes_create_association_ownership_account_note) | **POST** /v1/associations/ownershipaccounts/{ownershipAccountId}/notes | Create a note
[**external_api_ownership_account_notes_get_association_ownership_account_note_by_note_id**](OwnershipAccountsApi.md#external_api_ownership_account_notes_get_association_ownership_account_note_by_note_id) | **GET** /v1/associations/ownershipaccounts/{ownershipAccountId}/notes/{noteId} | Retrieve a note
[**external_api_ownership_account_notes_get_association_ownership_account_notes**](OwnershipAccountsApi.md#external_api_ownership_account_notes_get_association_ownership_account_notes) | **GET** /v1/associations/ownershipaccounts/{ownershipAccountId}/notes | Retrieve all notes
[**external_api_ownership_account_notes_update_association_ownership_account_note**](OwnershipAccountsApi.md#external_api_ownership_account_notes_update_association_ownership_account_note) | **PUT** /v1/associations/ownershipaccounts/{ownershipAccountId}/notes/{noteId} | Update a note
[**external_api_ownership_account_update_partial_payment_settings_patch_ownership_account_partial_payment**](OwnershipAccountsApi.md#external_api_ownership_account_update_partial_payment_settings_patch_ownership_account_partial_payment) | **PATCH** /v1/associations/ownershipaccounts/{ownershipAccountId}/partialpaymentsettings | Update partial payment settings for an ownership account
[**external_api_ownership_accounts_create_association_ownership_account**](OwnershipAccountsApi.md#external_api_ownership_accounts_create_association_ownership_account) | **POST** /v1/associations/ownershipaccounts | Create an ownership account
[**external_api_ownership_accounts_get_all_ownership_accounts**](OwnershipAccountsApi.md#external_api_ownership_accounts_get_all_ownership_accounts) | **GET** /v1/associations/ownershipaccounts | Retrieve all ownership accounts
[**external_api_ownership_accounts_get_ownership_account_by_id**](OwnershipAccountsApi.md#external_api_ownership_accounts_get_ownership_account_by_id) | **GET** /v1/associations/ownershipaccounts/{ownershipAccountId} | Retrieve an ownership account
[**external_api_ownership_accounts_partial_payment_settings_get_ownership_account_partial_payment_settings**](OwnershipAccountsApi.md#external_api_ownership_accounts_partial_payment_settings_get_ownership_account_partial_payment_settings) | **GET** /v1/associations/ownershipaccounts/{ownershipAccountId}/partialpaymentsettings | Retrieve all partial payment settings for an ownership account
[**external_api_ownership_accounts_update_association_ownership_account**](OwnershipAccountsApi.md#external_api_ownership_accounts_update_association_ownership_account) | **PUT** /v1/associations/ownershipaccounts/{ownershipAccountId} | Update an ownership account


# **external_api_ownership_account_notes_create_association_ownership_account_note**
> NoteMessage external_api_ownership_account_notes_create_association_ownership_account_note(ownership_account_id, note_post_message)

Create a note

Creates a new ownership account note.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.note_message import NoteMessage
from buildium_sdk.models.note_post_message import NotePostMessage
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
    api_instance = buildium_sdk.OwnershipAccountsApi(api_client)
    ownership_account_id = 56 # int | 
    note_post_message = buildium_sdk.NotePostMessage() # NotePostMessage | 

    try:
        # Create a note
        api_response = await api_instance.external_api_ownership_account_notes_create_association_ownership_account_note(ownership_account_id, note_post_message)
        print("The response of OwnershipAccountsApi->external_api_ownership_account_notes_create_association_ownership_account_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountsApi->external_api_ownership_account_notes_create_association_ownership_account_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **note_post_message** | [**NotePostMessage**](NotePostMessage.md)|  | 

### Return type

[**NoteMessage**](NoteMessage.md)

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

# **external_api_ownership_account_notes_get_association_ownership_account_note_by_note_id**
> NoteMessage external_api_ownership_account_notes_get_association_ownership_account_note_by_note_id(ownership_account_id, note_id)

Retrieve a note

Retrieves an ownership account note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > OwnershipAccounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.note_message import NoteMessage
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
    api_instance = buildium_sdk.OwnershipAccountsApi(api_client)
    ownership_account_id = 56 # int | 
    note_id = 56 # int | 

    try:
        # Retrieve a note
        api_response = await api_instance.external_api_ownership_account_notes_get_association_ownership_account_note_by_note_id(ownership_account_id, note_id)
        print("The response of OwnershipAccountsApi->external_api_ownership_account_notes_get_association_ownership_account_note_by_note_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountsApi->external_api_ownership_account_notes_get_association_ownership_account_note_by_note_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **note_id** | **int**|  | 

### Return type

[**NoteMessage**](NoteMessage.md)

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

# **external_api_ownership_account_notes_get_association_ownership_account_notes**
> List[NoteMessage] external_api_ownership_account_notes_get_association_ownership_account_notes(ownership_account_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)

Retrieve all notes

Retrieves notes for an ownership account.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > OwnershipAccounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.note_message import NoteMessage
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
    api_instance = buildium_sdk.OwnershipAccountsApi(api_client)
    ownership_account_id = 56 # int | 
    updateddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    updateddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    lastupdatedbyuserid = 56 # int | Filters results to only notes that were last updated by the specified user identifier. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all notes
        api_response = await api_instance.external_api_ownership_account_notes_get_association_ownership_account_notes(ownership_account_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)
        print("The response of OwnershipAccountsApi->external_api_ownership_account_notes_get_association_ownership_account_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountsApi->external_api_ownership_account_notes_get_association_ownership_account_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **updateddatetimefrom** | **datetime**| Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. | [optional] 
 **updateddatetimeto** | **datetime**| Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. | [optional] 
 **lastupdatedbyuserid** | **int**| Filters results to only notes that were last updated by the specified user identifier. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[NoteMessage]**](NoteMessage.md)

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

# **external_api_ownership_account_notes_update_association_ownership_account_note**
> NoteMessage external_api_ownership_account_notes_update_association_ownership_account_note(ownership_account_id, note_id, note_put_message)

Update a note

Updates an association ownership account note.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.note_message import NoteMessage
from buildium_sdk.models.note_put_message import NotePutMessage
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
    api_instance = buildium_sdk.OwnershipAccountsApi(api_client)
    ownership_account_id = 56 # int | 
    note_id = 56 # int | 
    note_put_message = buildium_sdk.NotePutMessage() # NotePutMessage | 

    try:
        # Update a note
        api_response = await api_instance.external_api_ownership_account_notes_update_association_ownership_account_note(ownership_account_id, note_id, note_put_message)
        print("The response of OwnershipAccountsApi->external_api_ownership_account_notes_update_association_ownership_account_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountsApi->external_api_ownership_account_notes_update_association_ownership_account_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **note_id** | **int**|  | 
 **note_put_message** | [**NotePutMessage**](NotePutMessage.md)|  | 

### Return type

[**NoteMessage**](NoteMessage.md)

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

# **external_api_ownership_account_update_partial_payment_settings_patch_ownership_account_partial_payment**
> PartialPaymentSettingsMessage external_api_ownership_account_update_partial_payment_settings_patch_ownership_account_partial_payment(ownership_account_id, partial_payment_settings_patch_message)

Update partial payment settings for an ownership account

Updates partial payment settings for an ownership account.
            

<h4>Required Permission(s):</h4><span class="permissionBlock">Associations > Ownership Accounts</span> - `View` `Edit`
            <span class="permissionBlock">Administration > Application Settings</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.partial_payment_settings_message import PartialPaymentSettingsMessage
from buildium_sdk.models.partial_payment_settings_patch_message import PartialPaymentSettingsPatchMessage
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
    api_instance = buildium_sdk.OwnershipAccountsApi(api_client)
    ownership_account_id = 56 # int | 
    partial_payment_settings_patch_message = buildium_sdk.PartialPaymentSettingsPatchMessage() # PartialPaymentSettingsPatchMessage | <span>Represents the structure of the data that can be provided to a <a target=\"_blank\" href=\"https://datatracker.ietf.org/doc/html/rfc6902\">JSON patch document</a> as path values via <a target=\"_blank\" href=\"https://datatracker.ietf.org/doc/html/rfc6901/\">JSON pointer</a> syntax.</span>

    try:
        # Update partial payment settings for an ownership account
        api_response = await api_instance.external_api_ownership_account_update_partial_payment_settings_patch_ownership_account_partial_payment(ownership_account_id, partial_payment_settings_patch_message)
        print("The response of OwnershipAccountsApi->external_api_ownership_account_update_partial_payment_settings_patch_ownership_account_partial_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountsApi->external_api_ownership_account_update_partial_payment_settings_patch_ownership_account_partial_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **partial_payment_settings_patch_message** | [**PartialPaymentSettingsPatchMessage**](PartialPaymentSettingsPatchMessage.md)| &lt;span&gt;Represents the structure of the data that can be provided to a &lt;a target&#x3D;\&quot;_blank\&quot; href&#x3D;\&quot;https://datatracker.ietf.org/doc/html/rfc6902\&quot;&gt;JSON patch document&lt;/a&gt; as path values via &lt;a target&#x3D;\&quot;_blank\&quot; href&#x3D;\&quot;https://datatracker.ietf.org/doc/html/rfc6901/\&quot;&gt;JSON pointer&lt;/a&gt; syntax.&lt;/span&gt; | 

### Return type

[**PartialPaymentSettingsMessage**](PartialPaymentSettingsMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
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

# **external_api_ownership_accounts_create_association_ownership_account**
> AssociationOwnershipAccountMessage external_api_ownership_accounts_create_association_ownership_account(association_ownership_account_post_message)

Create an ownership account

Creates an ownership account.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership accounts</span> - `View` `Edit`

<span class="permissionBlock">Associations > Owners</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_ownership_account_message import AssociationOwnershipAccountMessage
from buildium_sdk.models.association_ownership_account_post_message import AssociationOwnershipAccountPostMessage
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
    api_instance = buildium_sdk.OwnershipAccountsApi(api_client)
    association_ownership_account_post_message = buildium_sdk.AssociationOwnershipAccountPostMessage() # AssociationOwnershipAccountPostMessage | 

    try:
        # Create an ownership account
        api_response = await api_instance.external_api_ownership_accounts_create_association_ownership_account(association_ownership_account_post_message)
        print("The response of OwnershipAccountsApi->external_api_ownership_accounts_create_association_ownership_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountsApi->external_api_ownership_accounts_create_association_ownership_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_ownership_account_post_message** | [**AssociationOwnershipAccountPostMessage**](AssociationOwnershipAccountPostMessage.md)|  | 

### Return type

[**AssociationOwnershipAccountMessage**](AssociationOwnershipAccountMessage.md)

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
**409** | An association ownership account already exists for this unit. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_ownership_accounts_get_all_ownership_accounts**
> List[AssociationOwnershipAccountMessage] external_api_ownership_accounts_get_all_ownership_accounts(ids=ids, associationids=associationids, unitorowner=unitorowner, datefrom=datefrom, dateto=dateto, status=status, delinquencystatuses=delinquencystatuses, orderby=orderby, offset=offset, limit=limit)

Retrieve all ownership accounts

Retrieves a list of ownership accounts.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_ownership_account_message import AssociationOwnershipAccountMessage
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
    api_instance = buildium_sdk.OwnershipAccountsApi(api_client)
    ids = [56] # List[int] | Filters results to the specified set of ids. (optional)
    associationids = [56] # List[int] | Filters results to any ownership accounts who belong to the specified set of association ids. (optional)
    unitorowner = 'unitorowner_example' # str | Filters results to any association whose unit or owner *contains* the specified value. (optional)
    datefrom = '2013-10-20' # date | Filters results to any ownership account whose start date is greater than or equal to the specified value. (optional)
    dateto = '2013-10-20' # date | Filters results to any ownership account whose start date is less than or equal to the specified value. (optional)
    status = ['status_example'] # List[str] | Filters results by the status of the association. If no status is specified, `active`, `past` and `future` associations will be returned. (optional)
    delinquencystatuses = ['delinquencystatuses_example'] # List[str] | Filters results by the delinquency status of the ownership account. If no status is specified, ownership accounts of any delinquency status will be returned. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all ownership accounts
        api_response = await api_instance.external_api_ownership_accounts_get_all_ownership_accounts(ids=ids, associationids=associationids, unitorowner=unitorowner, datefrom=datefrom, dateto=dateto, status=status, delinquencystatuses=delinquencystatuses, orderby=orderby, offset=offset, limit=limit)
        print("The response of OwnershipAccountsApi->external_api_ownership_accounts_get_all_ownership_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountsApi->external_api_ownership_accounts_get_all_ownership_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| Filters results to the specified set of ids. | [optional] 
 **associationids** | [**List[int]**](int.md)| Filters results to any ownership accounts who belong to the specified set of association ids. | [optional] 
 **unitorowner** | **str**| Filters results to any association whose unit or owner *contains* the specified value. | [optional] 
 **datefrom** | **date**| Filters results to any ownership account whose start date is greater than or equal to the specified value. | [optional] 
 **dateto** | **date**| Filters results to any ownership account whose start date is less than or equal to the specified value. | [optional] 
 **status** | [**List[str]**](str.md)| Filters results by the status of the association. If no status is specified, &#x60;active&#x60;, &#x60;past&#x60; and &#x60;future&#x60; associations will be returned. | [optional] 
 **delinquencystatuses** | [**List[str]**](str.md)| Filters results by the delinquency status of the ownership account. If no status is specified, ownership accounts of any delinquency status will be returned. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[AssociationOwnershipAccountMessage]**](AssociationOwnershipAccountMessage.md)

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

# **external_api_ownership_accounts_get_ownership_account_by_id**
> AssociationOwnershipAccountMessage external_api_ownership_accounts_get_ownership_account_by_id(ownership_account_id)

Retrieve an ownership account

Retrieves a specific ownership account.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_ownership_account_message import AssociationOwnershipAccountMessage
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
    api_instance = buildium_sdk.OwnershipAccountsApi(api_client)
    ownership_account_id = 56 # int | The ownership account identifier.

    try:
        # Retrieve an ownership account
        api_response = await api_instance.external_api_ownership_accounts_get_ownership_account_by_id(ownership_account_id)
        print("The response of OwnershipAccountsApi->external_api_ownership_accounts_get_ownership_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountsApi->external_api_ownership_accounts_get_ownership_account_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**| The ownership account identifier. | 

### Return type

[**AssociationOwnershipAccountMessage**](AssociationOwnershipAccountMessage.md)

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

# **external_api_ownership_accounts_partial_payment_settings_get_ownership_account_partial_payment_settings**
> PartialPaymentSettingsMessage external_api_ownership_accounts_partial_payment_settings_get_ownership_account_partial_payment_settings(ownership_account_id)

Retrieve all partial payment settings for an ownership account

Retrieves partial payment settings for an ownership account.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > OwnershipAccounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.partial_payment_settings_message import PartialPaymentSettingsMessage
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
    api_instance = buildium_sdk.OwnershipAccountsApi(api_client)
    ownership_account_id = 56 # int | 

    try:
        # Retrieve all partial payment settings for an ownership account
        api_response = await api_instance.external_api_ownership_accounts_partial_payment_settings_get_ownership_account_partial_payment_settings(ownership_account_id)
        print("The response of OwnershipAccountsApi->external_api_ownership_accounts_partial_payment_settings_get_ownership_account_partial_payment_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountsApi->external_api_ownership_accounts_partial_payment_settings_get_ownership_account_partial_payment_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 

### Return type

[**PartialPaymentSettingsMessage**](PartialPaymentSettingsMessage.md)

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
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_ownership_accounts_update_association_ownership_account**
> AssociationOwnershipAccountMessage external_api_ownership_accounts_update_association_ownership_account(ownership_account_id, association_ownership_account_put_message)

Update an ownership account

Updates an ownership account.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_ownership_account_message import AssociationOwnershipAccountMessage
from buildium_sdk.models.association_ownership_account_put_message import AssociationOwnershipAccountPutMessage
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
    api_instance = buildium_sdk.OwnershipAccountsApi(api_client)
    ownership_account_id = 56 # int | 
    association_ownership_account_put_message = buildium_sdk.AssociationOwnershipAccountPutMessage() # AssociationOwnershipAccountPutMessage | 

    try:
        # Update an ownership account
        api_response = await api_instance.external_api_ownership_accounts_update_association_ownership_account(ownership_account_id, association_ownership_account_put_message)
        print("The response of OwnershipAccountsApi->external_api_ownership_accounts_update_association_ownership_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountsApi->external_api_ownership_accounts_update_association_ownership_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **association_ownership_account_put_message** | [**AssociationOwnershipAccountPutMessage**](AssociationOwnershipAccountPutMessage.md)|  | 

### Return type

[**AssociationOwnershipAccountMessage**](AssociationOwnershipAccountMessage.md)

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

