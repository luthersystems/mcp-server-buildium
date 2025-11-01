# buildium_sdk.RentalOwnersApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_rental_owner_notes_create_rental_owner_note**](RentalOwnersApi.md#external_api_rental_owner_notes_create_rental_owner_note) | **POST** /v1/rentals/owners/{rentalOwnerId}/notes | Create a note
[**external_api_rental_owner_notes_get_rental_owner_note_by_id**](RentalOwnersApi.md#external_api_rental_owner_notes_get_rental_owner_note_by_id) | **GET** /v1/rentals/owners/{rentalOwnerId}/notes/{noteId} | Retrieve a note
[**external_api_rental_owner_notes_get_rental_owner_notes**](RentalOwnersApi.md#external_api_rental_owner_notes_get_rental_owner_notes) | **GET** /v1/rentals/owners/{rentalOwnerId}/notes | Retrieves all notes
[**external_api_rental_owner_notes_update_rental_owner_note**](RentalOwnersApi.md#external_api_rental_owner_notes_update_rental_owner_note) | **PUT** /v1/rentals/owners/{rentalOwnerId}/notes/{noteId} | Update a note
[**external_api_rental_owners_create_rental_owner**](RentalOwnersApi.md#external_api_rental_owners_create_rental_owner) | **POST** /v1/rentals/owners | Create an owner
[**external_api_rental_owners_get_rental_owner_by_id**](RentalOwnersApi.md#external_api_rental_owners_get_rental_owner_by_id) | **GET** /v1/rentals/owners/{rentalOwnerId} | Retrieve an owner
[**external_api_rental_owners_get_rental_owners**](RentalOwnersApi.md#external_api_rental_owners_get_rental_owners) | **GET** /v1/rentals/owners | Retrieve all owners
[**external_api_rental_owners_update_rental_owner**](RentalOwnersApi.md#external_api_rental_owners_update_rental_owner) | **PUT** /v1/rentals/owners/{rentalOwnerId} | Update an owner


# **external_api_rental_owner_notes_create_rental_owner_note**
> NoteMessage external_api_rental_owner_notes_create_rental_owner_note(rental_owner_id, note_post_message)

Create a note

Creates a new Rental Owner note.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Property Rental Owners</span> - `View` `Edit`

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
    api_instance = buildium_sdk.RentalOwnersApi(api_client)
    rental_owner_id = 56 # int | 
    note_post_message = buildium_sdk.NotePostMessage() # NotePostMessage | 

    try:
        # Create a note
        api_response = await api_instance.external_api_rental_owner_notes_create_rental_owner_note(rental_owner_id, note_post_message)
        print("The response of RentalOwnersApi->external_api_rental_owner_notes_create_rental_owner_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnersApi->external_api_rental_owner_notes_create_rental_owner_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_owner_id** | **int**|  | 
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

# **external_api_rental_owner_notes_get_rental_owner_note_by_id**
> NoteMessage external_api_rental_owner_notes_get_rental_owner_note_by_id(rental_owner_id, note_id)

Retrieve a note

Retrieves a rental owner note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Property Rental Owners</span> - `View`

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
    api_instance = buildium_sdk.RentalOwnersApi(api_client)
    rental_owner_id = 56 # int | 
    note_id = 56 # int | 

    try:
        # Retrieve a note
        api_response = await api_instance.external_api_rental_owner_notes_get_rental_owner_note_by_id(rental_owner_id, note_id)
        print("The response of RentalOwnersApi->external_api_rental_owner_notes_get_rental_owner_note_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnersApi->external_api_rental_owner_notes_get_rental_owner_note_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_owner_id** | **int**|  | 
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

# **external_api_rental_owner_notes_get_rental_owner_notes**
> List[NoteMessage] external_api_rental_owner_notes_get_rental_owner_notes(rental_owner_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)

Retrieves all notes

Retrieves all rental owner notes.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Property Rental Owners</span> - `View`

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
    api_instance = buildium_sdk.RentalOwnersApi(api_client)
    rental_owner_id = 56 # int | 
    updateddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    updateddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    lastupdatedbyuserid = 56 # int | Filters results to only notes that were last updated by the specified user identifier. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieves all notes
        api_response = await api_instance.external_api_rental_owner_notes_get_rental_owner_notes(rental_owner_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)
        print("The response of RentalOwnersApi->external_api_rental_owner_notes_get_rental_owner_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnersApi->external_api_rental_owner_notes_get_rental_owner_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_owner_id** | **int**|  | 
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

# **external_api_rental_owner_notes_update_rental_owner_note**
> NoteMessage external_api_rental_owner_notes_update_rental_owner_note(rental_owner_id, note_id, note_put_message)

Update a note

Updates a Rental Owner note.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Property Rental Owners</span> - `View` `Edit`

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
    api_instance = buildium_sdk.RentalOwnersApi(api_client)
    rental_owner_id = 56 # int | 
    note_id = 56 # int | 
    note_put_message = buildium_sdk.NotePutMessage() # NotePutMessage | 

    try:
        # Update a note
        api_response = await api_instance.external_api_rental_owner_notes_update_rental_owner_note(rental_owner_id, note_id, note_put_message)
        print("The response of RentalOwnersApi->external_api_rental_owner_notes_update_rental_owner_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnersApi->external_api_rental_owner_notes_update_rental_owner_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_owner_id** | **int**|  | 
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

# **external_api_rental_owners_create_rental_owner**
> RentalOwnerMessage external_api_rental_owners_create_rental_owner(rental_owner_post_message)

Create an owner

Creates a rental owner.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Property Rental Owners</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_owner_message import RentalOwnerMessage
from buildium_sdk.models.rental_owner_post_message import RentalOwnerPostMessage
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
    api_instance = buildium_sdk.RentalOwnersApi(api_client)
    rental_owner_post_message = buildium_sdk.RentalOwnerPostMessage() # RentalOwnerPostMessage | 

    try:
        # Create an owner
        api_response = await api_instance.external_api_rental_owners_create_rental_owner(rental_owner_post_message)
        print("The response of RentalOwnersApi->external_api_rental_owners_create_rental_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnersApi->external_api_rental_owners_create_rental_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_owner_post_message** | [**RentalOwnerPostMessage**](RentalOwnerPostMessage.md)|  | 

### Return type

[**RentalOwnerMessage**](RentalOwnerMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - The location to retrieve the created resource. <br>  |
**400** | The request data had some invalid information in it. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_rental_owners_get_rental_owner_by_id**
> RentalOwnerMessage external_api_rental_owners_get_rental_owner_by_id(rental_owner_id)

Retrieve an owner

Retrieves a specific rental owner.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Property Rental Owners</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_owner_message import RentalOwnerMessage
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
    api_instance = buildium_sdk.RentalOwnersApi(api_client)
    rental_owner_id = 56 # int | The rental owner identifier.

    try:
        # Retrieve an owner
        api_response = await api_instance.external_api_rental_owners_get_rental_owner_by_id(rental_owner_id)
        print("The response of RentalOwnersApi->external_api_rental_owners_get_rental_owner_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnersApi->external_api_rental_owners_get_rental_owner_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_owner_id** | **int**| The rental owner identifier. | 

### Return type

[**RentalOwnerMessage**](RentalOwnerMessage.md)

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

# **external_api_rental_owners_get_rental_owners**
> List[RentalOwnerMessage] external_api_rental_owners_get_rental_owners(propertyids=propertyids, status=status, agreementdaysremaining=agreementdaysremaining, ownername=ownername, phone=phone, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)

Retrieve all owners

Retrieves a list of rental owners.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Property Rental Owners</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_owner_message import RentalOwnerMessage
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
    api_instance = buildium_sdk.RentalOwnersApi(api_client)
    propertyids = [56] # List[int] | Filters results to any lease whose unit belongs to the specified set of property ids. (optional)
    status = 'status_example' # str | Filters results by the status of the user. If no status is specified both `active` and `inactive` users will be returned. (optional)
    agreementdaysremaining = 56 # int | Filters results by the days remaining on their lease agreement. (optional)
    ownername = 'ownername_example' # str | Filters results to any owner whose name *contains* the specified value. (optional)
    phone = 'phone_example' # str | Filters results to any owner who has a phone number that *contains* the specified value. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any rental owners that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any rental owners that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all owners
        api_response = await api_instance.external_api_rental_owners_get_rental_owners(propertyids=propertyids, status=status, agreementdaysremaining=agreementdaysremaining, ownername=ownername, phone=phone, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)
        print("The response of RentalOwnersApi->external_api_rental_owners_get_rental_owners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnersApi->external_api_rental_owners_get_rental_owners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **propertyids** | [**List[int]**](int.md)| Filters results to any lease whose unit belongs to the specified set of property ids. | [optional] 
 **status** | **str**| Filters results by the status of the user. If no status is specified both &#x60;active&#x60; and &#x60;inactive&#x60; users will be returned. | [optional] 
 **agreementdaysremaining** | **int**| Filters results by the days remaining on their lease agreement. | [optional] 
 **ownername** | **str**| Filters results to any owner whose name *contains* the specified value. | [optional] 
 **phone** | **str**| Filters results to any owner who has a phone number that *contains* the specified value. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to any rental owners that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to any rental owners that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[RentalOwnerMessage]**](RentalOwnerMessage.md)

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

# **external_api_rental_owners_update_rental_owner**
> RentalOwnerMessage external_api_rental_owners_update_rental_owner(rental_owner_id, rental_owner_put_message)

Update an owner

Updates a rental owner.


<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Property Rental Owners</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_owner_message import RentalOwnerMessage
from buildium_sdk.models.rental_owner_put_message import RentalOwnerPutMessage
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
    api_instance = buildium_sdk.RentalOwnersApi(api_client)
    rental_owner_id = 56 # int | The identifier of the rental owner to update.
    rental_owner_put_message = buildium_sdk.RentalOwnerPutMessage() # RentalOwnerPutMessage | 

    try:
        # Update an owner
        api_response = await api_instance.external_api_rental_owners_update_rental_owner(rental_owner_id, rental_owner_put_message)
        print("The response of RentalOwnersApi->external_api_rental_owners_update_rental_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnersApi->external_api_rental_owners_update_rental_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_owner_id** | **int**| The identifier of the rental owner to update. | 
 **rental_owner_put_message** | [**RentalOwnerPutMessage**](RentalOwnerPutMessage.md)|  | 

### Return type

[**RentalOwnerMessage**](RentalOwnerMessage.md)

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

