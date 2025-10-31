# buildium_sdk.ArchitecturalRequestsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_association_architectural_requests_create_architectural_request_async**](ArchitecturalRequestsApi.md#external_api_association_architectural_requests_create_architectural_request_async) | **POST** /v1/associations/ownershipaccounts/architecturalrequests | Create an architectural request
[**external_api_association_architectural_requests_create_upload_file_request**](ArchitecturalRequestsApi.md#external_api_association_architectural_requests_create_upload_file_request) | **POST** /v1/associations/ownershipaccounts/architecturalrequests/{architecturalRequestId}/files/uploadrequests | Upload an architectural request file
[**external_api_association_architectural_requests_download_architectural_request_file_async**](ArchitecturalRequestsApi.md#external_api_association_architectural_requests_download_architectural_request_file_async) | **POST** /v1/associations/ownershipaccounts/architecturalrequests/{architecturalRequestId}/files/{fileId}/downloadrequests | Download an architectural request file
[**external_api_association_architectural_requests_get_architectural_request_by_id**](ArchitecturalRequestsApi.md#external_api_association_architectural_requests_get_architectural_request_by_id) | **GET** /v1/associations/ownershipaccounts/architecturalrequests/{architecturalRequestId} | Retrieve an architectural request
[**external_api_association_architectural_requests_get_architectural_request_file_async**](ArchitecturalRequestsApi.md#external_api_association_architectural_requests_get_architectural_request_file_async) | **GET** /v1/associations/ownershipaccounts/architecturalrequests/{architecturalRequestId}/files/{fileId} | Retrieve an architectural request file
[**external_api_association_architectural_requests_get_architectural_request_files_history_paged_async**](ArchitecturalRequestsApi.md#external_api_association_architectural_requests_get_architectural_request_files_history_paged_async) | **GET** /v1/associations/ownershipaccounts/architecturalrequests/{architecturalRequestId}/files | Retrieve all files for an architectural request
[**external_api_association_architectural_requests_get_architectural_requests**](ArchitecturalRequestsApi.md#external_api_association_architectural_requests_get_architectural_requests) | **GET** /v1/associations/ownershipaccounts/architecturalrequests | Retrieve all architectural requests


# **external_api_association_architectural_requests_create_architectural_request_async**
> AssociationArchitecturalRequestMessage external_api_association_architectural_requests_create_architectural_request_async(architectural_requests_post_message)

Create an architectural request

Creates an architectural request


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

<span class="permissionBlock">Associations > Ownership accounts</span> - `View` `Edit`

<span class="permissionBlock">Associations > Architectural requests</span> - `View` `Edit`

<span class="permissionBlock">Associations > Association owners and tenants</span> - `View` `Edit`



### Example


```python
import buildium_sdk
from buildium_sdk.models.architectural_requests_post_message import ArchitecturalRequestsPostMessage
from buildium_sdk.models.association_architectural_request_message import AssociationArchitecturalRequestMessage
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
    api_instance = buildium_sdk.ArchitecturalRequestsApi(api_client)
    architectural_requests_post_message = buildium_sdk.ArchitecturalRequestsPostMessage() # ArchitecturalRequestsPostMessage | 

    try:
        # Create an architectural request
        api_response = await api_instance.external_api_association_architectural_requests_create_architectural_request_async(architectural_requests_post_message)
        print("The response of ArchitecturalRequestsApi->external_api_association_architectural_requests_create_architectural_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchitecturalRequestsApi->external_api_association_architectural_requests_create_architectural_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **architectural_requests_post_message** | [**ArchitecturalRequestsPostMessage**](ArchitecturalRequestsPostMessage.md)|  | 

### Return type

[**AssociationArchitecturalRequestMessage**](AssociationArchitecturalRequestMessage.md)

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

# **external_api_association_architectural_requests_create_upload_file_request**
> FileUploadTicketMessage external_api_association_architectural_requests_create_upload_file_request(architectural_request_id, file_name_post_message)

Upload an architectural request file

Uploads a file and associates it to the specified architectural request record.


Uploading a file requires making two API requests. Each step is outlined below.


<strong>Step 1 - Save file metadata</strong>

The first step in the file upload process is to submit the file metadata to `/v1/associations/ownershipaccounts/architecturalrequests/{architecturalRequestId:int}/files/uploadrequests`. The response of this call will contain a URL and a collection of form data that will be used in step 2 to generate the request for the file binary upload.


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


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

<span class="permissionBlock">Associations > Ownership accounts</span> - `View` `Edit`

<span class="permissionBlock">Associations > Architectural requests</span> - `View` `Edit`

<span class="permissionBlock">Associations > Association owners and tenants</span> - `View` `Edit`

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
    api_instance = buildium_sdk.ArchitecturalRequestsApi(api_client)
    architectural_request_id = 56 # int | 
    file_name_post_message = buildium_sdk.FileNamePostMessage() # FileNamePostMessage | 

    try:
        # Upload an architectural request file
        api_response = await api_instance.external_api_association_architectural_requests_create_upload_file_request(architectural_request_id, file_name_post_message)
        print("The response of ArchitecturalRequestsApi->external_api_association_architectural_requests_create_upload_file_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchitecturalRequestsApi->external_api_association_architectural_requests_create_upload_file_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **architectural_request_id** | **int**|  | 
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
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_association_architectural_requests_download_architectural_request_file_async**
> FileDownloadMessage external_api_association_architectural_requests_download_architectural_request_file_async(architectural_request_id, file_id)

Download an architectural request file

Downloads a specific file associated to the architectural request.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`
            
<span class="permissionBlock">Associations > Ownership accounts</span> - `View`
            
<span class="permissionBlock">Associations > Association owners and tenants</span> - `View`
            
<span class="permissionBlock">Associations > Architectural requests</span> - `View`

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
    api_instance = buildium_sdk.ArchitecturalRequestsApi(api_client)
    architectural_request_id = 56 # int | 
    file_id = 56 # int | 

    try:
        # Download an architectural request file
        api_response = await api_instance.external_api_association_architectural_requests_download_architectural_request_file_async(architectural_request_id, file_id)
        print("The response of ArchitecturalRequestsApi->external_api_association_architectural_requests_download_architectural_request_file_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchitecturalRequestsApi->external_api_association_architectural_requests_download_architectural_request_file_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **architectural_request_id** | **int**|  | 
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
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_association_architectural_requests_get_architectural_request_by_id**
> AssociationArchitecturalRequestMessage external_api_association_architectural_requests_get_architectural_request_by_id(architectural_request_id)

Retrieve an architectural request

Retrieves a specific architectural request.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`
            
<span class="permissionBlock">Associations > Ownership accounts</span> - `View`
            
<span class="permissionBlock">Associations > Association owners and tenants</span> - `View`
            
<span class="permissionBlock">Associations > Architectural requests</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_architectural_request_message import AssociationArchitecturalRequestMessage
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
    api_instance = buildium_sdk.ArchitecturalRequestsApi(api_client)
    architectural_request_id = 56 # int | 

    try:
        # Retrieve an architectural request
        api_response = await api_instance.external_api_association_architectural_requests_get_architectural_request_by_id(architectural_request_id)
        print("The response of ArchitecturalRequestsApi->external_api_association_architectural_requests_get_architectural_request_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchitecturalRequestsApi->external_api_association_architectural_requests_get_architectural_request_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **architectural_request_id** | **int**|  | 

### Return type

[**AssociationArchitecturalRequestMessage**](AssociationArchitecturalRequestMessage.md)

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

# **external_api_association_architectural_requests_get_architectural_request_file_async**
> AssociationArchitecturalRequestFileMessage external_api_association_architectural_requests_get_architectural_request_file_async(architectural_request_id, file_id)

Retrieve an architectural request file

Retrieves an architectural request file.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`
            
<span class="permissionBlock">Associations > Ownership accounts</span> - `View`
            
<span class="permissionBlock">Associations > Association owners and tenants</span> - `View`
            
<span class="permissionBlock">Associations > Architectural requests</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_architectural_request_file_message import AssociationArchitecturalRequestFileMessage
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
    api_instance = buildium_sdk.ArchitecturalRequestsApi(api_client)
    architectural_request_id = 56 # int | 
    file_id = 56 # int | 

    try:
        # Retrieve an architectural request file
        api_response = await api_instance.external_api_association_architectural_requests_get_architectural_request_file_async(architectural_request_id, file_id)
        print("The response of ArchitecturalRequestsApi->external_api_association_architectural_requests_get_architectural_request_file_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchitecturalRequestsApi->external_api_association_architectural_requests_get_architectural_request_file_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **architectural_request_id** | **int**|  | 
 **file_id** | **int**|  | 

### Return type

[**AssociationArchitecturalRequestFileMessage**](AssociationArchitecturalRequestFileMessage.md)

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

# **external_api_association_architectural_requests_get_architectural_request_files_history_paged_async**
> AssociationArchitecturalRequestFileMessage external_api_association_architectural_requests_get_architectural_request_files_history_paged_async(architectural_request_id, ids=ids, orderby=orderby, offset=offset, limit=limit)

Retrieve all files for an architectural request

Retrieves all files for an architectural request.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`
            
<span class="permissionBlock">Associations > Ownership accounts</span> - `View`
            
<span class="permissionBlock">Associations > Association owners and tenants</span> - `View`
            
<span class="permissionBlock">Associations > Architectural requests</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_architectural_request_file_message import AssociationArchitecturalRequestFileMessage
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
    api_instance = buildium_sdk.ArchitecturalRequestsApi(api_client)
    architectural_request_id = 56 # int | 
    ids = [56] # List[int] | The IDs of the architectural request files to filter by. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all files for an architectural request
        api_response = await api_instance.external_api_association_architectural_requests_get_architectural_request_files_history_paged_async(architectural_request_id, ids=ids, orderby=orderby, offset=offset, limit=limit)
        print("The response of ArchitecturalRequestsApi->external_api_association_architectural_requests_get_architectural_request_files_history_paged_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchitecturalRequestsApi->external_api_association_architectural_requests_get_architectural_request_files_history_paged_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **architectural_request_id** | **int**|  | 
 **ids** | [**List[int]**](int.md)| The IDs of the architectural request files to filter by. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**AssociationArchitecturalRequestFileMessage**](AssociationArchitecturalRequestFileMessage.md)

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
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_association_architectural_requests_get_architectural_requests**
> List[AssociationArchitecturalRequestMessage] external_api_association_architectural_requests_get_architectural_requests(associationids=associationids, ownershipaccountids=ownershipaccountids, ids=ids, statuses=statuses, decisions=decisions, createddatetimefrom=createddatetimefrom, createddatetimeto=createddatetimeto, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, submitteddatetimefrom=submitteddatetimefrom, submitteddatetimeto=submitteddatetimeto, orderby=orderby, offset=offset, limit=limit)

Retrieve all architectural requests

Retrieves all architectural requests.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`
            
<span class="permissionBlock">Associations > Ownership accounts</span> - `View`
            
<span class="permissionBlock">Associations > Association owners and tenants</span> - `View`
            
<span class="permissionBlock">Associations > Architectural requests</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_architectural_request_message import AssociationArchitecturalRequestMessage
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
    api_instance = buildium_sdk.ArchitecturalRequestsApi(api_client)
    associationids = [56] # List[int] | Filters results to only records that belong to the specified set of association identifiers. (optional)
    ownershipaccountids = [56] # List[int] | Filters results to only records that belong to the specified set of ownership account identifiers. (optional)
    ids = [56] # List[int] | Filters results to only records that belong to the specified set of architectural request identifiers. (optional)
    statuses = ['statuses_example'] # List[str] | Filters results to only records whose status is equal to the specified value. (optional)
    decisions = ['decisions_example'] # List[str] | Filters results to only records whose decision is equal to the specified value. (optional)
    createddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only records that were created after this date. Must be formatted as `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    createddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only records that were created before this date. Must be formatted as `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only records that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only records that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    submitteddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only records that were submitted on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    submitteddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only records that were submitted on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all architectural requests
        api_response = await api_instance.external_api_association_architectural_requests_get_architectural_requests(associationids=associationids, ownershipaccountids=ownershipaccountids, ids=ids, statuses=statuses, decisions=decisions, createddatetimefrom=createddatetimefrom, createddatetimeto=createddatetimeto, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, submitteddatetimefrom=submitteddatetimefrom, submitteddatetimeto=submitteddatetimeto, orderby=orderby, offset=offset, limit=limit)
        print("The response of ArchitecturalRequestsApi->external_api_association_architectural_requests_get_architectural_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchitecturalRequestsApi->external_api_association_architectural_requests_get_architectural_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **associationids** | [**List[int]**](int.md)| Filters results to only records that belong to the specified set of association identifiers. | [optional] 
 **ownershipaccountids** | [**List[int]**](int.md)| Filters results to only records that belong to the specified set of ownership account identifiers. | [optional] 
 **ids** | [**List[int]**](int.md)| Filters results to only records that belong to the specified set of architectural request identifiers. | [optional] 
 **statuses** | [**List[str]**](str.md)| Filters results to only records whose status is equal to the specified value. | [optional] 
 **decisions** | [**List[str]**](str.md)| Filters results to only records whose decision is equal to the specified value. | [optional] 
 **createddatetimefrom** | **datetime**| Filters results to only records that were created after this date. Must be formatted as &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **createddatetimeto** | **datetime**| Filters results to only records that were created before this date. Must be formatted as &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to only records that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to only records that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **submitteddatetimefrom** | **datetime**| Filters results to only records that were submitted on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **submitteddatetimeto** | **datetime**| Filters results to only records that were submitted on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[AssociationArchitecturalRequestMessage]**](AssociationArchitecturalRequestMessage.md)

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

