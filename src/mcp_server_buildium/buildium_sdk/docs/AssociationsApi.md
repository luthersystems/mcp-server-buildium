# buildium_sdk.AssociationsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_association_active_status_inactivate_association**](AssociationsApi.md#external_api_association_active_status_inactivate_association) | **POST** /v1/associations/{associationId}/inactivationrequest | Inactivate an association
[**external_api_association_active_status_reactivate_association**](AssociationsApi.md#external_api_association_active_status_reactivate_association) | **POST** /v1/associations/{associationId}/reactivationrequest | Reactivate an association
[**external_api_association_bank_lock_box_data_get_bank_lock_box_data**](AssociationsApi.md#external_api_association_bank_lock_box_data_get_bank_lock_box_data) | **GET** /v1/associations/banklockboxdata | Retrieve all association bank lockbox data
[**external_api_association_notes_create_association_note**](AssociationsApi.md#external_api_association_notes_create_association_note) | **POST** /v1/associations/{associationId}/notes | Create a note
[**external_api_association_notes_get_association_note_by_note_id**](AssociationsApi.md#external_api_association_notes_get_association_note_by_note_id) | **GET** /v1/associations/{associationId}/notes/{noteId} | Retrieve a note
[**external_api_association_notes_get_association_notes**](AssociationsApi.md#external_api_association_notes_get_association_notes) | **GET** /v1/associations/{associationId}/notes | Retrieve all notes
[**external_api_association_notes_update_association_note**](AssociationsApi.md#external_api_association_notes_update_association_note) | **PUT** /v1/associations/{associationId}/notes/{noteId} | Update a note
[**external_api_association_preferred_vendors_get_association_preferred_vendors**](AssociationsApi.md#external_api_association_preferred_vendors_get_association_preferred_vendors) | **GET** /v1/associations/{associationId}/vendors | Retrieve all preferred vendors
[**external_api_association_preferred_vendors_update_association_preferred_vendors**](AssociationsApi.md#external_api_association_preferred_vendors_update_association_preferred_vendors) | **PUT** /v1/associations/{associationId}/vendors | Update preferred vendors
[**external_api_associations_create_association**](AssociationsApi.md#external_api_associations_create_association) | **POST** /v1/associations | Create an association
[**external_api_associations_e_pay_settings_get_e_pay_settings_for_association_by_id**](AssociationsApi.md#external_api_associations_e_pay_settings_get_e_pay_settings_for_association_by_id) | **GET** /v1/associations/{associationId}/epaysettings | Retrieve ePay settings
[**external_api_associations_e_pay_settings_update_e_pay_settings_for_association**](AssociationsApi.md#external_api_associations_e_pay_settings_update_e_pay_settings_for_association) | **PUT** /v1/associations/{associationId}/epaysettings | Update ePay settings
[**external_api_associations_get_association_by_id**](AssociationsApi.md#external_api_associations_get_association_by_id) | **GET** /v1/associations/{associationId} | Retrieve an association
[**external_api_associations_get_associations**](AssociationsApi.md#external_api_associations_get_associations) | **GET** /v1/associations | Retrieve all associations
[**external_api_associations_update_association**](AssociationsApi.md#external_api_associations_update_association) | **PUT** /v1/associations/{associationId} | Update an association


# **external_api_association_active_status_inactivate_association**
> external_api_association_active_status_inactivate_association(association_id)

Inactivate an association

Inactivates an association along with associated units and ownership accounts. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    association_id = 56 # int | 

    try:
        # Inactivate an association
        await api_instance.external_api_association_active_status_inactivate_association(association_id)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_association_active_status_inactivate_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 

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
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_association_active_status_reactivate_association**
> external_api_association_active_status_reactivate_association(association_id)

Reactivate an association

Reactivates an association along with associated units and ownership accounts. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    association_id = 56 # int | 

    try:
        # Reactivate an association
        await api_instance.external_api_association_active_status_reactivate_association(association_id)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_association_active_status_reactivate_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 

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
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_association_bank_lock_box_data_get_bank_lock_box_data**
> List[BankLockboxDataMessage] external_api_association_bank_lock_box_data_get_bank_lock_box_data(associationids=associationids, orderby=orderby, offset=offset, limit=limit)

Retrieve all association bank lockbox data

Retrieves all association bank lockbox data.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bank_lockbox_data_message import BankLockboxDataMessage
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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    associationids = [56] # List[int] | Filters results to only include Associations with matching IDs (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all association bank lockbox data
        api_response = await api_instance.external_api_association_bank_lock_box_data_get_bank_lock_box_data(associationids=associationids, orderby=orderby, offset=offset, limit=limit)
        print("The response of AssociationsApi->external_api_association_bank_lock_box_data_get_bank_lock_box_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_association_bank_lock_box_data_get_bank_lock_box_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **associationids** | [**List[int]**](int.md)| Filters results to only include Associations with matching IDs | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BankLockboxDataMessage]**](BankLockboxDataMessage.md)

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

# **external_api_association_notes_create_association_note**
> NoteMessage external_api_association_notes_create_association_note(association_id, note_post_message)

Create a note

Creates a note.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    association_id = 56 # int | 
    note_post_message = buildium_sdk.NotePostMessage() # NotePostMessage | 

    try:
        # Create a note
        api_response = await api_instance.external_api_association_notes_create_association_note(association_id, note_post_message)
        print("The response of AssociationsApi->external_api_association_notes_create_association_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_association_notes_create_association_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
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

# **external_api_association_notes_get_association_note_by_note_id**
> NoteMessage external_api_association_notes_get_association_note_by_note_id(association_id, note_id)

Retrieve a note

Retrieves a note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`

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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    association_id = 56 # int | 
    note_id = 56 # int | 

    try:
        # Retrieve a note
        api_response = await api_instance.external_api_association_notes_get_association_note_by_note_id(association_id, note_id)
        print("The response of AssociationsApi->external_api_association_notes_get_association_note_by_note_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_association_notes_get_association_note_by_note_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
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

# **external_api_association_notes_get_association_notes**
> List[NoteMessage] external_api_association_notes_get_association_notes(association_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)

Retrieve all notes

Retrieves all notes.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`

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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    association_id = 56 # int | 
    updateddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    updateddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    lastupdatedbyuserid = 56 # int | Filters results to only notes that were last updated by the specified user identifier. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all notes
        api_response = await api_instance.external_api_association_notes_get_association_notes(association_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)
        print("The response of AssociationsApi->external_api_association_notes_get_association_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_association_notes_get_association_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
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

# **external_api_association_notes_update_association_note**
> NoteMessage external_api_association_notes_update_association_note(association_id, note_id, note_put_message)

Update a note

Updates a note.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    association_id = 56 # int | 
    note_id = 56 # int | 
    note_put_message = buildium_sdk.NotePutMessage() # NotePutMessage | 

    try:
        # Update a note
        api_response = await api_instance.external_api_association_notes_update_association_note(association_id, note_id, note_put_message)
        print("The response of AssociationsApi->external_api_association_notes_update_association_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_association_notes_update_association_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
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

# **external_api_association_preferred_vendors_get_association_preferred_vendors**
> List[AssociationPreferredVendorMessage] external_api_association_preferred_vendors_get_association_preferred_vendors(association_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all preferred vendors

Retrieves all preferred vendors.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`
            
<span class="permissionBlock">Maintenance > Vendors</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_preferred_vendor_message import AssociationPreferredVendorMessage
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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    association_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all preferred vendors
        api_response = await api_instance.external_api_association_preferred_vendors_get_association_preferred_vendors(association_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of AssociationsApi->external_api_association_preferred_vendors_get_association_preferred_vendors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_association_preferred_vendors_get_association_preferred_vendors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[AssociationPreferredVendorMessage]**](AssociationPreferredVendorMessage.md)

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

# **external_api_association_preferred_vendors_update_association_preferred_vendors**
> List[AssociationPreferredVendorMessage] external_api_association_preferred_vendors_update_association_preferred_vendors(association_id, association_preferred_vendor_put_message)

Update preferred vendors

Updates preferred vendors.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 

The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`
            
<span class="permissionBlock">Maintenance > Vendors</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_preferred_vendor_message import AssociationPreferredVendorMessage
from buildium_sdk.models.association_preferred_vendor_put_message import AssociationPreferredVendorPutMessage
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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    association_id = 56 # int | 
    association_preferred_vendor_put_message = buildium_sdk.AssociationPreferredVendorPutMessage() # AssociationPreferredVendorPutMessage | 

    try:
        # Update preferred vendors
        api_response = await api_instance.external_api_association_preferred_vendors_update_association_preferred_vendors(association_id, association_preferred_vendor_put_message)
        print("The response of AssociationsApi->external_api_association_preferred_vendors_update_association_preferred_vendors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_association_preferred_vendors_update_association_preferred_vendors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
 **association_preferred_vendor_put_message** | [**AssociationPreferredVendorPutMessage**](AssociationPreferredVendorPutMessage.md)|  | 

### Return type

[**List[AssociationPreferredVendorMessage]**](AssociationPreferredVendorMessage.md)

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

# **external_api_associations_create_association**
> AssociationMessage external_api_associations_create_association(association_post_message)

Create an association

Creates an association.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_message import AssociationMessage
from buildium_sdk.models.association_post_message import AssociationPostMessage
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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    association_post_message = buildium_sdk.AssociationPostMessage() # AssociationPostMessage | 

    try:
        # Create an association
        api_response = await api_instance.external_api_associations_create_association(association_post_message)
        print("The response of AssociationsApi->external_api_associations_create_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_associations_create_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_post_message** | [**AssociationPostMessage**](AssociationPostMessage.md)|  | 

### Return type

[**AssociationMessage**](AssociationMessage.md)

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

# **external_api_associations_e_pay_settings_get_e_pay_settings_for_association_by_id**
> EPaySettingsMessage external_api_associations_e_pay_settings_get_e_pay_settings_for_association_by_id(association_id)

Retrieve ePay settings

Retrieves ePay settings for an association.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.e_pay_settings_message import EPaySettingsMessage
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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    association_id = 56 # int | 

    try:
        # Retrieve ePay settings
        api_response = await api_instance.external_api_associations_e_pay_settings_get_e_pay_settings_for_association_by_id(association_id)
        print("The response of AssociationsApi->external_api_associations_e_pay_settings_get_e_pay_settings_for_association_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_associations_e_pay_settings_get_e_pay_settings_for_association_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 

### Return type

[**EPaySettingsMessage**](EPaySettingsMessage.md)

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

# **external_api_associations_e_pay_settings_update_e_pay_settings_for_association**
> EPaySettingsMessage external_api_associations_e_pay_settings_update_e_pay_settings_for_association(association_id, e_pay_settings_put_message)

Update ePay settings

Updates ePay settings for an association.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.e_pay_settings_message import EPaySettingsMessage
from buildium_sdk.models.e_pay_settings_put_message import EPaySettingsPutMessage
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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    association_id = 56 # int | 
    e_pay_settings_put_message = buildium_sdk.EPaySettingsPutMessage() # EPaySettingsPutMessage | 

    try:
        # Update ePay settings
        api_response = await api_instance.external_api_associations_e_pay_settings_update_e_pay_settings_for_association(association_id, e_pay_settings_put_message)
        print("The response of AssociationsApi->external_api_associations_e_pay_settings_update_e_pay_settings_for_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_associations_e_pay_settings_update_e_pay_settings_for_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
 **e_pay_settings_put_message** | [**EPaySettingsPutMessage**](EPaySettingsPutMessage.md)|  | 

### Return type

[**EPaySettingsMessage**](EPaySettingsMessage.md)

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

# **external_api_associations_get_association_by_id**
> AssociationMessage external_api_associations_get_association_by_id(association_id)

Retrieve an association

Retrieve a specific association.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_message import AssociationMessage
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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    association_id = 56 # int | The association identifier.

    try:
        # Retrieve an association
        api_response = await api_instance.external_api_associations_get_association_by_id(association_id)
        print("The response of AssociationsApi->external_api_associations_get_association_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_associations_get_association_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**| The association identifier. | 

### Return type

[**AssociationMessage**](AssociationMessage.md)

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

# **external_api_associations_get_associations**
> List[AssociationMessage] external_api_associations_get_associations(ids=ids, location=location, status=status, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, operatingbankaccountids=operatingbankaccountids, orderby=orderby, offset=offset, limit=limit)

Retrieve all associations

Retrieves a list of associations.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_message import AssociationMessage
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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    ids = [56] # List[int] | Filters results to the specified set of ids. (optional)
    location = 'location_example' # str | Filters results to any association whose city or state *contains* the specified value. (optional)
    status = 'status_example' # str | Filters results by the status of the association. If no status is specified both `active` and `inactive` associations will be returned. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any associations that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any associations that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    operatingbankaccountids = [56] # List[int] | Filters results to any associations associated to any of the specified set of operating bank account ids. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all associations
        api_response = await api_instance.external_api_associations_get_associations(ids=ids, location=location, status=status, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, operatingbankaccountids=operatingbankaccountids, orderby=orderby, offset=offset, limit=limit)
        print("The response of AssociationsApi->external_api_associations_get_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_associations_get_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| Filters results to the specified set of ids. | [optional] 
 **location** | **str**| Filters results to any association whose city or state *contains* the specified value. | [optional] 
 **status** | **str**| Filters results by the status of the association. If no status is specified both &#x60;active&#x60; and &#x60;inactive&#x60; associations will be returned. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to any associations that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to any associations that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **operatingbankaccountids** | [**List[int]**](int.md)| Filters results to any associations associated to any of the specified set of operating bank account ids. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[AssociationMessage]**](AssociationMessage.md)

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

# **external_api_associations_update_association**
> AssociationMessage external_api_associations_update_association(association_id, association_put_message)

Update an association

Updates an association.


<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 

The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_message import AssociationMessage
from buildium_sdk.models.association_put_message import AssociationPutMessage
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
    api_instance = buildium_sdk.AssociationsApi(api_client)
    association_id = 56 # int | 
    association_put_message = buildium_sdk.AssociationPutMessage() # AssociationPutMessage | 

    try:
        # Update an association
        api_response = await api_instance.external_api_associations_update_association(association_id, association_put_message)
        print("The response of AssociationsApi->external_api_associations_update_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationsApi->external_api_associations_update_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
 **association_put_message** | [**AssociationPutMessage**](AssociationPutMessage.md)|  | 

### Return type

[**AssociationMessage**](AssociationMessage.md)

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

