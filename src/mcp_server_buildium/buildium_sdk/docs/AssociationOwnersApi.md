# buildium_sdk.AssociationOwnersApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_association_owner_notes_create_association_owner_note**](AssociationOwnersApi.md#external_api_association_owner_notes_create_association_owner_note) | **POST** /v1/associations/owners/{ownerId}/notes | Create a note
[**external_api_association_owner_notes_get_association_owner_note_by_note_id**](AssociationOwnersApi.md#external_api_association_owner_notes_get_association_owner_note_by_note_id) | **GET** /v1/associations/owners/{ownerId}/notes/{noteId} | Retrieve a note
[**external_api_association_owner_notes_get_association_owner_notes**](AssociationOwnersApi.md#external_api_association_owner_notes_get_association_owner_notes) | **GET** /v1/associations/owners/{ownerId}/notes | Retrieve all notes
[**external_api_association_owner_notes_update_association_owner_note**](AssociationOwnersApi.md#external_api_association_owner_notes_update_association_owner_note) | **PUT** /v1/associations/owners/{ownerId}/notes/{noteId} | Update a note
[**external_api_association_owner_units_get_unit_occupancy_statuses_by_id_for_association_owner**](AssociationOwnersApi.md#external_api_association_owner_units_get_unit_occupancy_statuses_by_id_for_association_owner) | **GET** /v1/associations/owners/{ownerId}/units/{unitId} | Retrieve an occupancy status
[**external_api_association_owner_units_get_unit_occupancy_statuses_for_association_owner**](AssociationOwnersApi.md#external_api_association_owner_units_get_unit_occupancy_statuses_for_association_owner) | **GET** /v1/associations/owners/{ownerId}/units | Retrieve all occupancy statuses
[**external_api_association_owner_units_update_association_owner_occupancy_status**](AssociationOwnersApi.md#external_api_association_owner_units_update_association_owner_occupancy_status) | **PUT** /v1/associations/owners/{ownerId}/units/{unitId} | Update occupancy status
[**external_api_association_owners_create_association_owner**](AssociationOwnersApi.md#external_api_association_owners_create_association_owner) | **POST** /v1/associations/owners | Create an owner
[**external_api_association_owners_get_all_association_owners**](AssociationOwnersApi.md#external_api_association_owners_get_all_association_owners) | **GET** /v1/associations/owners | Retrieve all owners
[**external_api_association_owners_get_association_owner_by_id**](AssociationOwnersApi.md#external_api_association_owners_get_association_owner_by_id) | **GET** /v1/associations/owners/{ownerId} | Retrieve an owner
[**external_api_association_owners_update_association_owner**](AssociationOwnersApi.md#external_api_association_owners_update_association_owner) | **PUT** /v1/associations/owners/{ownerId} | Update an owner


# **external_api_association_owner_notes_create_association_owner_note**
> NoteMessage external_api_association_owner_notes_create_association_owner_note(owner_id, note_post_message)

Create a note

Creates an association owner note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View` `Edit`

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
    api_instance = buildium_sdk.AssociationOwnersApi(api_client)
    owner_id = 56 # int | 
    note_post_message = buildium_sdk.NotePostMessage() # NotePostMessage | 

    try:
        # Create a note
        api_response = await api_instance.external_api_association_owner_notes_create_association_owner_note(owner_id, note_post_message)
        print("The response of AssociationOwnersApi->external_api_association_owner_notes_create_association_owner_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationOwnersApi->external_api_association_owner_notes_create_association_owner_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**|  | 
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

# **external_api_association_owner_notes_get_association_owner_note_by_note_id**
> NoteMessage external_api_association_owner_notes_get_association_owner_note_by_note_id(owner_id, note_id)

Retrieve a note

Retrieves an association owner note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View`

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
    api_instance = buildium_sdk.AssociationOwnersApi(api_client)
    owner_id = 56 # int | 
    note_id = 56 # int | 

    try:
        # Retrieve a note
        api_response = await api_instance.external_api_association_owner_notes_get_association_owner_note_by_note_id(owner_id, note_id)
        print("The response of AssociationOwnersApi->external_api_association_owner_notes_get_association_owner_note_by_note_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationOwnersApi->external_api_association_owner_notes_get_association_owner_note_by_note_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**|  | 
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

# **external_api_association_owner_notes_get_association_owner_notes**
> List[NoteMessage] external_api_association_owner_notes_get_association_owner_notes(owner_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)

Retrieve all notes

Retrieves all association owner notes.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View`

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
    api_instance = buildium_sdk.AssociationOwnersApi(api_client)
    owner_id = 56 # int | 
    updateddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    updateddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    lastupdatedbyuserid = 56 # int | Filters results to only notes that were last updated by the specified user identifier. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all notes
        api_response = await api_instance.external_api_association_owner_notes_get_association_owner_notes(owner_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)
        print("The response of AssociationOwnersApi->external_api_association_owner_notes_get_association_owner_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationOwnersApi->external_api_association_owner_notes_get_association_owner_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**|  | 
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

# **external_api_association_owner_notes_update_association_owner_note**
> NoteMessage external_api_association_owner_notes_update_association_owner_note(owner_id, note_id, note_put_message)

Update a note

Updates an association owner note.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View` `Edit`

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
    api_instance = buildium_sdk.AssociationOwnersApi(api_client)
    owner_id = 56 # int | 
    note_id = 56 # int | 
    note_put_message = buildium_sdk.NotePutMessage() # NotePutMessage | 

    try:
        # Update a note
        api_response = await api_instance.external_api_association_owner_notes_update_association_owner_note(owner_id, note_id, note_put_message)
        print("The response of AssociationOwnersApi->external_api_association_owner_notes_update_association_owner_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationOwnersApi->external_api_association_owner_notes_update_association_owner_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**|  | 
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

# **external_api_association_owner_units_get_unit_occupancy_statuses_by_id_for_association_owner**
> AssociationOwnerUnitOccupancyStatusMessage external_api_association_owner_units_get_unit_occupancy_statuses_by_id_for_association_owner(owner_id, unit_id)

Retrieve an occupancy status

Retrieves the owner occupancy status for an association unit.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View` 
<span class="permissionBlock">Associations > Ownership Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_owner_unit_occupancy_status_message import AssociationOwnerUnitOccupancyStatusMessage
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
    api_instance = buildium_sdk.AssociationOwnersApi(api_client)
    owner_id = 56 # int | 
    unit_id = 56 # int | 

    try:
        # Retrieve an occupancy status
        api_response = await api_instance.external_api_association_owner_units_get_unit_occupancy_statuses_by_id_for_association_owner(owner_id, unit_id)
        print("The response of AssociationOwnersApi->external_api_association_owner_units_get_unit_occupancy_statuses_by_id_for_association_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationOwnersApi->external_api_association_owner_units_get_unit_occupancy_statuses_by_id_for_association_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**|  | 
 **unit_id** | **int**|  | 

### Return type

[**AssociationOwnerUnitOccupancyStatusMessage**](AssociationOwnerUnitOccupancyStatusMessage.md)

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
**503** | This service is currently unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_association_owner_units_get_unit_occupancy_statuses_for_association_owner**
> List[AssociationOwnerUnitOccupancyStatusMessage] external_api_association_owner_units_get_unit_occupancy_statuses_for_association_owner(owner_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all occupancy statuses

Retrieves the occupancy status for all of the units owned by the association owner. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View` 
<span class="permissionBlock">Associations > Ownership Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_owner_unit_occupancy_status_message import AssociationOwnerUnitOccupancyStatusMessage
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
    api_instance = buildium_sdk.AssociationOwnersApi(api_client)
    owner_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all occupancy statuses
        api_response = await api_instance.external_api_association_owner_units_get_unit_occupancy_statuses_for_association_owner(owner_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of AssociationOwnersApi->external_api_association_owner_units_get_unit_occupancy_statuses_for_association_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationOwnersApi->external_api_association_owner_units_get_unit_occupancy_statuses_for_association_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[AssociationOwnerUnitOccupancyStatusMessage]**](AssociationOwnerUnitOccupancyStatusMessage.md)

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
**503** | This service is currently unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_association_owner_units_update_association_owner_occupancy_status**
> AssociationOwnerUnitOccupancyStatusMessage external_api_association_owner_units_update_association_owner_occupancy_status(owner_id, unit_id, association_owner_unit_occupancy_put_message)

Update occupancy status

Updates whether a unit is occupied by the association owner.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View` `Edit` 
<span class="permissionBlock">Associations > Ownership Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_owner_unit_occupancy_put_message import AssociationOwnerUnitOccupancyPutMessage
from buildium_sdk.models.association_owner_unit_occupancy_status_message import AssociationOwnerUnitOccupancyStatusMessage
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
    api_instance = buildium_sdk.AssociationOwnersApi(api_client)
    owner_id = 56 # int | 
    unit_id = 56 # int | 
    association_owner_unit_occupancy_put_message = buildium_sdk.AssociationOwnerUnitOccupancyPutMessage() # AssociationOwnerUnitOccupancyPutMessage | 

    try:
        # Update occupancy status
        api_response = await api_instance.external_api_association_owner_units_update_association_owner_occupancy_status(owner_id, unit_id, association_owner_unit_occupancy_put_message)
        print("The response of AssociationOwnersApi->external_api_association_owner_units_update_association_owner_occupancy_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationOwnersApi->external_api_association_owner_units_update_association_owner_occupancy_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**|  | 
 **unit_id** | **int**|  | 
 **association_owner_unit_occupancy_put_message** | [**AssociationOwnerUnitOccupancyPutMessage**](AssociationOwnerUnitOccupancyPutMessage.md)|  | 

### Return type

[**AssociationOwnerUnitOccupancyStatusMessage**](AssociationOwnerUnitOccupancyStatusMessage.md)

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
**503** | This service is currently unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_association_owners_create_association_owner**
> AssociationOwnerMessage external_api_association_owners_create_association_owner(association_owner_to_existing_ownership_account_post_message)

Create an owner

Creates an association owner.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View` `Edit`

<span class="permissionBlock">Associations > Ownership accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_owner_message import AssociationOwnerMessage
from buildium_sdk.models.association_owner_to_existing_ownership_account_post_message import AssociationOwnerToExistingOwnershipAccountPostMessage
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
    api_instance = buildium_sdk.AssociationOwnersApi(api_client)
    association_owner_to_existing_ownership_account_post_message = buildium_sdk.AssociationOwnerToExistingOwnershipAccountPostMessage() # AssociationOwnerToExistingOwnershipAccountPostMessage | 

    try:
        # Create an owner
        api_response = await api_instance.external_api_association_owners_create_association_owner(association_owner_to_existing_ownership_account_post_message)
        print("The response of AssociationOwnersApi->external_api_association_owners_create_association_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationOwnersApi->external_api_association_owners_create_association_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_owner_to_existing_ownership_account_post_message** | [**AssociationOwnerToExistingOwnershipAccountPostMessage**](AssociationOwnerToExistingOwnershipAccountPostMessage.md)|  | 

### Return type

[**AssociationOwnerMessage**](AssociationOwnerMessage.md)

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

# **external_api_association_owners_get_all_association_owners**
> List[AssociationOwnerMessage] external_api_association_owners_get_all_association_owners(name=name, phone=phone, email=email, associationids=associationids, statuses=statuses, createddatetimeto=createddatetimeto, createddatetimefrom=createddatetimefrom, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)

Retrieve all owners

Retrieves a list of association owners.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_owner_message import AssociationOwnerMessage
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
    api_instance = buildium_sdk.AssociationOwnersApi(api_client)
    name = 'name_example' # str | Filters results to only records whose name *contains* the specified value. (optional)
    phone = 'phone_example' # str | Filters results to only records whose phone number *contains* the specified value. (optional)
    email = 'email_example' # str | Filters results to only records whose email *contains* the specified value. (optional)
    associationids = [56] # List[int] | Filters results to only records that belong to the specified set of association identifiers. (optional)
    statuses = ['statuses_example'] # List[str] | Filters results to only records whose status is equal to the specified value. (optional)
    createddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only records that were created before this date. Must be formatted as `YYYY-MM-DD`. (optional)
    createddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only records that were created after this date. Must be formatted as `YYYY-MM-DD`. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any association owners that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any association owners that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all owners
        api_response = await api_instance.external_api_association_owners_get_all_association_owners(name=name, phone=phone, email=email, associationids=associationids, statuses=statuses, createddatetimeto=createddatetimeto, createddatetimefrom=createddatetimefrom, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)
        print("The response of AssociationOwnersApi->external_api_association_owners_get_all_association_owners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationOwnersApi->external_api_association_owners_get_all_association_owners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filters results to only records whose name *contains* the specified value. | [optional] 
 **phone** | **str**| Filters results to only records whose phone number *contains* the specified value. | [optional] 
 **email** | **str**| Filters results to only records whose email *contains* the specified value. | [optional] 
 **associationids** | [**List[int]**](int.md)| Filters results to only records that belong to the specified set of association identifiers. | [optional] 
 **statuses** | [**List[str]**](str.md)| Filters results to only records whose status is equal to the specified value. | [optional] 
 **createddatetimeto** | **datetime**| Filters results to only records that were created before this date. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
 **createddatetimefrom** | **datetime**| Filters results to only records that were created after this date. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to any association owners that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to any association owners that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[AssociationOwnerMessage]**](AssociationOwnerMessage.md)

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

# **external_api_association_owners_get_association_owner_by_id**
> AssociationOwnerMessage external_api_association_owners_get_association_owner_by_id(owner_id)

Retrieve an owner

Retrieve a specific association owner.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_owner_message import AssociationOwnerMessage
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
    api_instance = buildium_sdk.AssociationOwnersApi(api_client)
    owner_id = 56 # int | The association owner identifier.

    try:
        # Retrieve an owner
        api_response = await api_instance.external_api_association_owners_get_association_owner_by_id(owner_id)
        print("The response of AssociationOwnersApi->external_api_association_owners_get_association_owner_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationOwnersApi->external_api_association_owners_get_association_owner_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**| The association owner identifier. | 

### Return type

[**AssociationOwnerMessage**](AssociationOwnerMessage.md)

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

# **external_api_association_owners_update_association_owner**
> AssociationOwnerMessage external_api_association_owners_update_association_owner(owner_id, association_owner_put_message)

Update an owner

Updates an existing association owner.


<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_owner_message import AssociationOwnerMessage
from buildium_sdk.models.association_owner_put_message import AssociationOwnerPutMessage
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
    api_instance = buildium_sdk.AssociationOwnersApi(api_client)
    owner_id = 56 # int | The identifier of the association owner to update.
    association_owner_put_message = buildium_sdk.AssociationOwnerPutMessage() # AssociationOwnerPutMessage | 

    try:
        # Update an owner
        api_response = await api_instance.external_api_association_owners_update_association_owner(owner_id, association_owner_put_message)
        print("The response of AssociationOwnersApi->external_api_association_owners_update_association_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationOwnersApi->external_api_association_owners_update_association_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **int**| The identifier of the association owner to update. | 
 **association_owner_put_message** | [**AssociationOwnerPutMessage**](AssociationOwnerPutMessage.md)|  | 

### Return type

[**AssociationOwnerMessage**](AssociationOwnerMessage.md)

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

