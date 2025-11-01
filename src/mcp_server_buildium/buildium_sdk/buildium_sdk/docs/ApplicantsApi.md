# buildium_sdk.ApplicantsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_applicant_applications_get_application_for_applicant_by_id**](ApplicantsApi.md#external_api_applicant_applications_get_application_for_applicant_by_id) | **GET** /v1/applicants/{applicantId}/applications/{applicationId} | Retrieve an application
[**external_api_applicant_applications_get_applications_for_applicant**](ApplicantsApi.md#external_api_applicant_applications_get_applications_for_applicant) | **GET** /v1/applicants/{applicantId}/applications | Retrieve all applications
[**external_api_applicant_applications_update_application**](ApplicantsApi.md#external_api_applicant_applications_update_application) | **PUT** /v1/applicants/{applicantId}/applications/{applicationId} | Update an application
[**external_api_applicant_group_notes_create_application_group_note**](ApplicantsApi.md#external_api_applicant_group_notes_create_application_group_note) | **POST** /v1/applicants/groups/{applicantGroupId}/notes | Create an applicant group note
[**external_api_applicant_group_notes_get_applicant_group_note_by_note_id**](ApplicantsApi.md#external_api_applicant_group_notes_get_applicant_group_note_by_note_id) | **GET** /v1/applicants/groups/{applicantGroupId}/notes/{noteId} | Retrieve an applicant group note
[**external_api_applicant_group_notes_get_applicant_group_notes**](ApplicantsApi.md#external_api_applicant_group_notes_get_applicant_group_notes) | **GET** /v1/applicants/groups/{applicantGroupId}/notes | Retrieve all applicant group notes
[**external_api_applicant_group_notes_update_application_group_note**](ApplicantsApi.md#external_api_applicant_group_notes_update_application_group_note) | **PUT** /v1/applicants/groups/{applicantGroupId}/notes/{noteId} | Update an applicant group note
[**external_api_applicant_groups_create_applicant_group**](ApplicantsApi.md#external_api_applicant_groups_create_applicant_group) | **POST** /v1/applicants/groups | Create an applicant group
[**external_api_applicant_groups_get_applicant_group_by_id**](ApplicantsApi.md#external_api_applicant_groups_get_applicant_group_by_id) | **GET** /v1/applicants/groups/{applicantGroupId} | Retrieve an applicant group
[**external_api_applicant_groups_get_applicant_groups**](ApplicantsApi.md#external_api_applicant_groups_get_applicant_groups) | **GET** /v1/applicants/groups | Retrieve all applicant groups
[**external_api_applicant_groups_update_applicant_group**](ApplicantsApi.md#external_api_applicant_groups_update_applicant_group) | **PUT** /v1/applicants/groups/{applicantGroupId} | Update an applicant group
[**external_api_applicant_notes_create_applicant_note**](ApplicantsApi.md#external_api_applicant_notes_create_applicant_note) | **POST** /v1/applicants/{applicantId}/notes | Create an applicant note
[**external_api_applicant_notes_get_all_applicant_notes**](ApplicantsApi.md#external_api_applicant_notes_get_all_applicant_notes) | **GET** /v1/applicants/{applicantId}/notes | Retrieve all applicant notes
[**external_api_applicant_notes_get_applicant_note_by_id**](ApplicantsApi.md#external_api_applicant_notes_get_applicant_note_by_id) | **GET** /v1/applicants/{applicantId}/notes/{noteId} | Retrieve an applicant note
[**external_api_applicants_create_applicant**](ApplicantsApi.md#external_api_applicants_create_applicant) | **POST** /v1/applicants | Create an applicant
[**external_api_applicants_get_applicant_by_id**](ApplicantsApi.md#external_api_applicants_get_applicant_by_id) | **GET** /v1/applicants/{applicantId} | Retrieve an applicant
[**external_api_applicants_get_applicants**](ApplicantsApi.md#external_api_applicants_get_applicants) | **GET** /v1/applicants | Retrieve all applicants
[**external_api_applicants_update_applicant**](ApplicantsApi.md#external_api_applicants_update_applicant) | **PUT** /v1/applicants/{applicantId} | Update an applicant


# **external_api_applicant_applications_get_application_for_applicant_by_id**
> ApplicationMessage external_api_applicant_applications_get_application_for_applicant_by_id(applicant_id, application_id)

Retrieve an application

Retrieves an application.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_message import ApplicationMessage
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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_id = 56 # int | 
    application_id = 56 # int | 

    try:
        # Retrieve an application
        api_response = await api_instance.external_api_applicant_applications_get_application_for_applicant_by_id(applicant_id, application_id)
        print("The response of ApplicantsApi->external_api_applicant_applications_get_application_for_applicant_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_applications_get_application_for_applicant_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **int**|  | 
 **application_id** | **int**|  | 

### Return type

[**ApplicationMessage**](ApplicationMessage.md)

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

# **external_api_applicant_applications_get_applications_for_applicant**
> List[ApplicationMessage] external_api_applicant_applications_get_applications_for_applicant(applicant_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all applications

Retrieves all the applications for a given applicant.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_message import ApplicationMessage
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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all applications
        api_response = await api_instance.external_api_applicant_applications_get_applications_for_applicant(applicant_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of ApplicantsApi->external_api_applicant_applications_get_applications_for_applicant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_applications_get_applications_for_applicant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[ApplicationMessage]**](ApplicationMessage.md)

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

# **external_api_applicant_applications_update_application**
> ApplicationMessage external_api_applicant_applications_update_application(applicant_id, application_id, application_put_message)

Update an application

Updates a rental application.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_message import ApplicationMessage
from buildium_sdk.models.application_put_message import ApplicationPutMessage
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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_id = 56 # int | 
    application_id = 56 # int | 
    application_put_message = buildium_sdk.ApplicationPutMessage() # ApplicationPutMessage | 

    try:
        # Update an application
        api_response = await api_instance.external_api_applicant_applications_update_application(applicant_id, application_id, application_put_message)
        print("The response of ApplicantsApi->external_api_applicant_applications_update_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_applications_update_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **int**|  | 
 **application_id** | **int**|  | 
 **application_put_message** | [**ApplicationPutMessage**](ApplicationPutMessage.md)|  | 

### Return type

[**ApplicationMessage**](ApplicationMessage.md)

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

# **external_api_applicant_group_notes_create_application_group_note**
> NoteMessage external_api_applicant_group_notes_create_application_group_note(applicant_group_id, note_post_message)

Create an applicant group note

Creates an applicant group note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View` `Edit`

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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_group_id = 56 # int | 
    note_post_message = buildium_sdk.NotePostMessage() # NotePostMessage | 

    try:
        # Create an applicant group note
        api_response = await api_instance.external_api_applicant_group_notes_create_application_group_note(applicant_group_id, note_post_message)
        print("The response of ApplicantsApi->external_api_applicant_group_notes_create_application_group_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_group_notes_create_application_group_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_group_id** | **int**|  | 
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

# **external_api_applicant_group_notes_get_applicant_group_note_by_note_id**
> NoteMessage external_api_applicant_group_notes_get_applicant_group_note_by_note_id(applicant_group_id, note_id)

Retrieve an applicant group note

Retrieves an applicant group note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View`

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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_group_id = 56 # int | 
    note_id = 56 # int | 

    try:
        # Retrieve an applicant group note
        api_response = await api_instance.external_api_applicant_group_notes_get_applicant_group_note_by_note_id(applicant_group_id, note_id)
        print("The response of ApplicantsApi->external_api_applicant_group_notes_get_applicant_group_note_by_note_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_group_notes_get_applicant_group_note_by_note_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_group_id** | **int**|  | 
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

# **external_api_applicant_group_notes_get_applicant_group_notes**
> List[NoteMessage] external_api_applicant_group_notes_get_applicant_group_notes(applicant_group_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)

Retrieve all applicant group notes

Retrieves all applicant group notes.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View`

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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_group_id = 56 # int | 
    updateddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    updateddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    lastupdatedbyuserid = 56 # int | Filters results to only notes that were last updated by the specified user identifier. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all applicant group notes
        api_response = await api_instance.external_api_applicant_group_notes_get_applicant_group_notes(applicant_group_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)
        print("The response of ApplicantsApi->external_api_applicant_group_notes_get_applicant_group_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_group_notes_get_applicant_group_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_group_id** | **int**|  | 
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

# **external_api_applicant_group_notes_update_application_group_note**
> NoteMessage external_api_applicant_group_notes_update_application_group_note(applicant_group_id, note_id, note_put_message)

Update an applicant group note

Updates an applicant group note.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View` `Edit`

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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_group_id = 56 # int | 
    note_id = 56 # int | 
    note_put_message = buildium_sdk.NotePutMessage() # NotePutMessage | 

    try:
        # Update an applicant group note
        api_response = await api_instance.external_api_applicant_group_notes_update_application_group_note(applicant_group_id, note_id, note_put_message)
        print("The response of ApplicantsApi->external_api_applicant_group_notes_update_application_group_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_group_notes_update_application_group_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_group_id** | **int**|  | 
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

# **external_api_applicant_groups_create_applicant_group**
> ApplicantGroupMessage external_api_applicant_groups_create_applicant_group(applicant_group_post_message)

Create an applicant group

Creates an applicant group.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.applicant_group_message import ApplicantGroupMessage
from buildium_sdk.models.applicant_group_post_message import ApplicantGroupPostMessage
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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_group_post_message = buildium_sdk.ApplicantGroupPostMessage() # ApplicantGroupPostMessage | 

    try:
        # Create an applicant group
        api_response = await api_instance.external_api_applicant_groups_create_applicant_group(applicant_group_post_message)
        print("The response of ApplicantsApi->external_api_applicant_groups_create_applicant_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_groups_create_applicant_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_group_post_message** | [**ApplicantGroupPostMessage**](ApplicantGroupPostMessage.md)|  | 

### Return type

[**ApplicantGroupMessage**](ApplicantGroupMessage.md)

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

# **external_api_applicant_groups_get_applicant_group_by_id**
> ApplicantGroupMessage external_api_applicant_groups_get_applicant_group_by_id(applicant_group_id)

Retrieve an applicant group

Retrieves an applicant group.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.applicant_group_message import ApplicantGroupMessage
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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_group_id = 56 # int | 

    try:
        # Retrieve an applicant group
        api_response = await api_instance.external_api_applicant_groups_get_applicant_group_by_id(applicant_group_id)
        print("The response of ApplicantsApi->external_api_applicant_groups_get_applicant_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_groups_get_applicant_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_group_id** | **int**|  | 

### Return type

[**ApplicantGroupMessage**](ApplicantGroupMessage.md)

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

# **external_api_applicant_groups_get_applicant_groups**
> List[ApplicantGroupMessage] external_api_applicant_groups_get_applicant_groups(entitytype=entitytype, entityid=entityid, applicationgroupstatuses=applicationgroupstatuses, unitids=unitids, name=name, orderby=orderby, offset=offset, limit=limit)

Retrieve all applicant groups

Retrieves all applicant groups.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.applicant_group_message import ApplicantGroupMessage
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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    entitytype = 'entitytype_example' # str | Filters results to any applicant groups associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references. (optional)
    entityid = 56 # int | Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified. (optional)
    applicationgroupstatuses = ['applicationgroupstatuses_example'] # List[str] | Filters results by the applicant group status. If no status is specified, applicant groups in any status will be returned. (optional)
    unitids = [56] # List[int] | Filters results to applicant groups associated to any of the specified rental property unit identifiers. (optional)
    name = 'name_example' # str | Filters results to applicant groups that includes applicants whose name *contains* the specified value. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all applicant groups
        api_response = await api_instance.external_api_applicant_groups_get_applicant_groups(entitytype=entitytype, entityid=entityid, applicationgroupstatuses=applicationgroupstatuses, unitids=unitids, name=name, orderby=orderby, offset=offset, limit=limit)
        print("The response of ApplicantsApi->external_api_applicant_groups_get_applicant_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_groups_get_applicant_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitytype** | **str**| Filters results to any applicant groups associated with the specified entity identifier. This filter is used in conjunction with the &#x60;EntityType&#x60; field which must be set to the type of entity this identifier references. | [optional] 
 **entityid** | **int**| Specifies the type of entity that &#x60;EntityId&#x60; refers to. This field is required if &#x60;EntityId&#x60; is specified. | [optional] 
 **applicationgroupstatuses** | [**List[str]**](str.md)| Filters results by the applicant group status. If no status is specified, applicant groups in any status will be returned. | [optional] 
 **unitids** | [**List[int]**](int.md)| Filters results to applicant groups associated to any of the specified rental property unit identifiers. | [optional] 
 **name** | **str**| Filters results to applicant groups that includes applicants whose name *contains* the specified value. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[ApplicantGroupMessage]**](ApplicantGroupMessage.md)

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

# **external_api_applicant_groups_update_applicant_group**
> ApplicantGroupMessage external_api_applicant_groups_update_applicant_group(applicant_group_id, applicant_group_put_message)

Update an applicant group

Updates an applicant group.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.applicant_group_message import ApplicantGroupMessage
from buildium_sdk.models.applicant_group_put_message import ApplicantGroupPutMessage
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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_group_id = 56 # int | 
    applicant_group_put_message = buildium_sdk.ApplicantGroupPutMessage() # ApplicantGroupPutMessage | 

    try:
        # Update an applicant group
        api_response = await api_instance.external_api_applicant_groups_update_applicant_group(applicant_group_id, applicant_group_put_message)
        print("The response of ApplicantsApi->external_api_applicant_groups_update_applicant_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_groups_update_applicant_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_group_id** | **int**|  | 
 **applicant_group_put_message** | [**ApplicantGroupPutMessage**](ApplicantGroupPutMessage.md)|  | 

### Return type

[**ApplicantGroupMessage**](ApplicantGroupMessage.md)

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

# **external_api_applicant_notes_create_applicant_note**
> NoteMessage external_api_applicant_notes_create_applicant_note(applicant_id, note_post_message)

Create an applicant note

Creates an applicant note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> -  `View` `Edit`

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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_id = 56 # int | 
    note_post_message = buildium_sdk.NotePostMessage() # NotePostMessage | 

    try:
        # Create an applicant note
        api_response = await api_instance.external_api_applicant_notes_create_applicant_note(applicant_id, note_post_message)
        print("The response of ApplicantsApi->external_api_applicant_notes_create_applicant_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_notes_create_applicant_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **int**|  | 
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

# **external_api_applicant_notes_get_all_applicant_notes**
> List[NoteMessage] external_api_applicant_notes_get_all_applicant_notes(applicant_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)

Retrieve all applicant notes

Retrieves all applicant notes.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View`

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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_id = 56 # int | 
    updateddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    updateddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    lastupdatedbyuserid = 56 # int | Filters results to only notes that were last updated by the specified user identifier. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all applicant notes
        api_response = await api_instance.external_api_applicant_notes_get_all_applicant_notes(applicant_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)
        print("The response of ApplicantsApi->external_api_applicant_notes_get_all_applicant_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_notes_get_all_applicant_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **int**|  | 
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

# **external_api_applicant_notes_get_applicant_note_by_id**
> NoteMessage external_api_applicant_notes_get_applicant_note_by_id(applicant_id, note_id)

Retrieve an applicant note

Retrieves an applicant note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View`

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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_id = 56 # int | 
    note_id = 56 # int | 

    try:
        # Retrieve an applicant note
        api_response = await api_instance.external_api_applicant_notes_get_applicant_note_by_id(applicant_id, note_id)
        print("The response of ApplicantsApi->external_api_applicant_notes_get_applicant_note_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicant_notes_get_applicant_note_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **int**|  | 
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

# **external_api_applicants_create_applicant**
> ApplicantDetailsMessage external_api_applicants_create_applicant(applicant_post_message)

Create an applicant

Creates an applicant.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.applicant_details_message import ApplicantDetailsMessage
from buildium_sdk.models.applicant_post_message import ApplicantPostMessage
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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_post_message = buildium_sdk.ApplicantPostMessage() # ApplicantPostMessage | 

    try:
        # Create an applicant
        api_response = await api_instance.external_api_applicants_create_applicant(applicant_post_message)
        print("The response of ApplicantsApi->external_api_applicants_create_applicant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicants_create_applicant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_post_message** | [**ApplicantPostMessage**](ApplicantPostMessage.md)|  | 

### Return type

[**ApplicantDetailsMessage**](ApplicantDetailsMessage.md)

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

# **external_api_applicants_get_applicant_by_id**
> ApplicantDetailsMessage external_api_applicants_get_applicant_by_id(applicant_id)

Retrieve an applicant

Retrieves an applicant.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.applicant_details_message import ApplicantDetailsMessage
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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_id = 56 # int | 

    try:
        # Retrieve an applicant
        api_response = await api_instance.external_api_applicants_get_applicant_by_id(applicant_id)
        print("The response of ApplicantsApi->external_api_applicants_get_applicant_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicants_get_applicant_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **int**|  | 

### Return type

[**ApplicantDetailsMessage**](ApplicantDetailsMessage.md)

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

# **external_api_applicants_get_applicants**
> List[ApplicantDetailsMessage] external_api_applicants_get_applicants(entityid=entityid, entitytype=entitytype, applicationstatuses=applicationstatuses, unitids=unitids, name=name, email=email, applicationsubmittedstartdate=applicationsubmittedstartdate, applicationsubmittedenddate=applicationsubmittedenddate, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)

Retrieve all applicants

Retrieves all applicants.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.applicant_details_message import ApplicantDetailsMessage
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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    entityid = 56 # int | Filters results to any applicant associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references. (optional)
    entitytype = 'entitytype_example' # str | Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified. (optional)
    applicationstatuses = ['applicationstatuses_example'] # List[str] | Filters results by the applicant application status. If no status is specified, applicants with an application in any status will be returned. (optional)
    unitids = [56] # List[int] | Filters results to applicants associated to any of the specified rental property unit identifiers. (optional)
    name = 'name_example' # str | Filters results to applicants whose name *contains* the specified value. (optional)
    email = 'email_example' # str | Filters results to applicants whose email *contains* the specified value (optional)
    applicationsubmittedstartdate = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any applicant who submitted an application on or after the date specified. (optional)
    applicationsubmittedenddate = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any applicant who submitted an application on or prior to the date specified. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any applicants that were updated on or after the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any applicants that were updated on or before the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all applicants
        api_response = await api_instance.external_api_applicants_get_applicants(entityid=entityid, entitytype=entitytype, applicationstatuses=applicationstatuses, unitids=unitids, name=name, email=email, applicationsubmittedstartdate=applicationsubmittedstartdate, applicationsubmittedenddate=applicationsubmittedenddate, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)
        print("The response of ApplicantsApi->external_api_applicants_get_applicants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicants_get_applicants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entityid** | **int**| Filters results to any applicant associated with the specified entity identifier. This filter is used in conjunction with the &#x60;EntityType&#x60; field which must be set to the type of entity this identifier references. | [optional] 
 **entitytype** | **str**| Specifies the type of entity that &#x60;EntityId&#x60; refers to. This field is required if &#x60;EntityId&#x60; is specified. | [optional] 
 **applicationstatuses** | [**List[str]**](str.md)| Filters results by the applicant application status. If no status is specified, applicants with an application in any status will be returned. | [optional] 
 **unitids** | [**List[int]**](int.md)| Filters results to applicants associated to any of the specified rental property unit identifiers. | [optional] 
 **name** | **str**| Filters results to applicants whose name *contains* the specified value. | [optional] 
 **email** | **str**| Filters results to applicants whose email *contains* the specified value | [optional] 
 **applicationsubmittedstartdate** | **datetime**| Filters results to any applicant who submitted an application on or after the date specified. | [optional] 
 **applicationsubmittedenddate** | **datetime**| Filters results to any applicant who submitted an application on or prior to the date specified. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to any applicants that were updated on or after the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to any applicants that were updated on or before the specified date and time. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[ApplicantDetailsMessage]**](ApplicantDetailsMessage.md)

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

# **external_api_applicants_update_applicant**
> ApplicantDetailsMessage external_api_applicants_update_applicant(applicant_id, applicant_put_message)

Update an applicant

Updates an applicant.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Applicants</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.applicant_details_message import ApplicantDetailsMessage
from buildium_sdk.models.applicant_put_message import ApplicantPutMessage
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
    api_instance = buildium_sdk.ApplicantsApi(api_client)
    applicant_id = 56 # int | 
    applicant_put_message = buildium_sdk.ApplicantPutMessage() # ApplicantPutMessage | 

    try:
        # Update an applicant
        api_response = await api_instance.external_api_applicants_update_applicant(applicant_id, applicant_put_message)
        print("The response of ApplicantsApi->external_api_applicants_update_applicant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicantsApi->external_api_applicants_update_applicant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **int**|  | 
 **applicant_put_message** | [**ApplicantPutMessage**](ApplicantPutMessage.md)|  | 

### Return type

[**ApplicantDetailsMessage**](ApplicantDetailsMessage.md)

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

