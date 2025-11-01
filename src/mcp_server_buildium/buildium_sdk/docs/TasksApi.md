# buildium_sdk.TasksApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_task_categories_create_task_category**](TasksApi.md#external_api_task_categories_create_task_category) | **POST** /v1/tasks/categories | Create a task category
[**external_api_task_categories_get_all_task_categories**](TasksApi.md#external_api_task_categories_get_all_task_categories) | **GET** /v1/tasks/categories | Retrieve all task categories
[**external_api_task_categories_get_task_category_by_id**](TasksApi.md#external_api_task_categories_get_task_category_by_id) | **GET** /v1/tasks/categories/{taskCategoryId} | Retrieve a task category
[**external_api_task_categories_update_task_category**](TasksApi.md#external_api_task_categories_update_task_category) | **PUT** /v1/tasks/categories/{taskCategoryId} | Update a task category
[**external_api_task_history_file_downloads_get_file_download_request**](TasksApi.md#external_api_task_history_file_downloads_get_file_download_request) | **POST** /v1/tasks/{taskId}/history/{taskHistoryId}/files/{fileId}/downloadrequest | Download a task history file
[**external_api_task_history_file_uploads_create_upload_file_request_async**](TasksApi.md#external_api_task_history_file_uploads_create_upload_file_request_async) | **POST** /v1/tasks/{taskId}/history/{taskHistoryId}/files/uploadrequests | Upload a task history file
[**external_api_task_history_files_delete_task_history_file**](TasksApi.md#external_api_task_history_files_delete_task_history_file) | **DELETE** /v1/tasks/{taskId}/history/{taskHistoryId}/files/{fileId} | Delete task history file
[**external_api_task_history_files_get_all_task_history_files**](TasksApi.md#external_api_task_history_files_get_all_task_history_files) | **GET** /v1/tasks/{taskId}/history/{taskHistoryId}/files | Retrieve all task history files
[**external_api_task_history_files_get_task_history_file_by_id**](TasksApi.md#external_api_task_history_files_get_task_history_file_by_id) | **GET** /v1/tasks/{taskId}/history/{taskHistoryId}/files/{fileId} | Retrieve a task history file
[**external_api_task_history_get_task_histories**](TasksApi.md#external_api_task_history_get_task_histories) | **GET** /v1/tasks/{taskId}/history | Retrieve all task history
[**external_api_task_history_get_task_history_by_id**](TasksApi.md#external_api_task_history_get_task_history_by_id) | **GET** /v1/tasks/{taskId}/history/{taskHistoryId} | Retrieve a task history
[**external_api_task_history_update_task_history**](TasksApi.md#external_api_task_history_update_task_history) | **PUT** /v1/tasks/{taskId}/history/{taskHistoryId} | Update a task history
[**external_api_tasks_get_all_tasks**](TasksApi.md#external_api_tasks_get_all_tasks) | **GET** /v1/tasks | Retrieve all tasks
[**external_api_tasks_get_task_by_id**](TasksApi.md#external_api_tasks_get_task_by_id) | **GET** /v1/tasks/{taskId} | Retrieve a task


# **external_api_task_categories_create_task_category**
> TaskCategoryMessage external_api_task_categories_create_task_category(task_category_save_message)

Create a task category

Create a task category.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.task_category_message import TaskCategoryMessage
from buildium_sdk.models.task_category_save_message import TaskCategorySaveMessage
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
    api_instance = buildium_sdk.TasksApi(api_client)
    task_category_save_message = buildium_sdk.TaskCategorySaveMessage() # TaskCategorySaveMessage | 

    try:
        # Create a task category
        api_response = await api_instance.external_api_task_categories_create_task_category(task_category_save_message)
        print("The response of TasksApi->external_api_task_categories_create_task_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_task_categories_create_task_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_category_save_message** | [**TaskCategorySaveMessage**](TaskCategorySaveMessage.md)|  | 

### Return type

[**TaskCategoryMessage**](TaskCategoryMessage.md)

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

# **external_api_task_categories_get_all_task_categories**
> List[TaskCategoryMessage] external_api_task_categories_get_all_task_categories(orderby=orderby, offset=offset, limit=limit)

Retrieve all task categories

Retrieves a list of task categories.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.task_category_message import TaskCategoryMessage
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
    api_instance = buildium_sdk.TasksApi(api_client)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all task categories
        api_response = await api_instance.external_api_task_categories_get_all_task_categories(orderby=orderby, offset=offset, limit=limit)
        print("The response of TasksApi->external_api_task_categories_get_all_task_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_task_categories_get_all_task_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[TaskCategoryMessage]**](TaskCategoryMessage.md)

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

# **external_api_task_categories_get_task_category_by_id**
> TaskCategoryMessage external_api_task_categories_get_task_category_by_id(task_category_id)

Retrieve a task category

Retrieves a specific task category.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.task_category_message import TaskCategoryMessage
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
    api_instance = buildium_sdk.TasksApi(api_client)
    task_category_id = 56 # int | The task category identifier.

    try:
        # Retrieve a task category
        api_response = await api_instance.external_api_task_categories_get_task_category_by_id(task_category_id)
        print("The response of TasksApi->external_api_task_categories_get_task_category_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_task_categories_get_task_category_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_category_id** | **int**| The task category identifier. | 

### Return type

[**TaskCategoryMessage**](TaskCategoryMessage.md)

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

# **external_api_task_categories_update_task_category**
> TaskCategoryMessage external_api_task_categories_update_task_category(task_category_id, task_category_put_message)

Update a task category

Updates a task category.


<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.task_category_message import TaskCategoryMessage
from buildium_sdk.models.task_category_put_message import TaskCategoryPutMessage
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
    api_instance = buildium_sdk.TasksApi(api_client)
    task_category_id = 56 # int | The task category identifier.
    task_category_put_message = buildium_sdk.TaskCategoryPutMessage() # TaskCategoryPutMessage | 

    try:
        # Update a task category
        api_response = await api_instance.external_api_task_categories_update_task_category(task_category_id, task_category_put_message)
        print("The response of TasksApi->external_api_task_categories_update_task_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_task_categories_update_task_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_category_id** | **int**| The task category identifier. | 
 **task_category_put_message** | [**TaskCategoryPutMessage**](TaskCategoryPutMessage.md)|  | 

### Return type

[**TaskCategoryMessage**](TaskCategoryMessage.md)

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

# **external_api_task_history_file_downloads_get_file_download_request**
> FileDownloadMessage external_api_task_history_file_downloads_get_file_download_request(task_id, task_history_id, file_id)

Download a task history file

Downloads a specific file associated to the task history record.
            

This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

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
    api_instance = buildium_sdk.TasksApi(api_client)
    task_id = 56 # int | 
    task_history_id = 56 # int | 
    file_id = 56 # int | 

    try:
        # Download a task history file
        api_response = await api_instance.external_api_task_history_file_downloads_get_file_download_request(task_id, task_history_id, file_id)
        print("The response of TasksApi->external_api_task_history_file_downloads_get_file_download_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_task_history_file_downloads_get_file_download_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **task_history_id** | **int**|  | 
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
**503** | The file download service is currently unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_task_history_file_uploads_create_upload_file_request_async**
> FileUploadTicketMessage external_api_task_history_file_uploads_create_upload_file_request_async(task_id, task_history_id, task_history_file_upload_post_message)

Upload a task history file

Uploads a file and associates it to the specified task history record.


This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's.


Uploading a file requires making two API requests. Each step is outlined below.


<strong>Step 1 - Save file metadata</strong>

The first step in the file upload process is to submit the file metadata to `/v1/tasks/{taskId}/history/{taskHistoryId}/files/uploadrequests`. The response of this call will contain a URL and a collection of form data that will be used in step 2 to generate the request for the file binary upload.


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


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_upload_ticket_message import FileUploadTicketMessage
from buildium_sdk.models.task_history_file_upload_post_message import TaskHistoryFileUploadPostMessage
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
    api_instance = buildium_sdk.TasksApi(api_client)
    task_id = 56 # int | 
    task_history_id = 56 # int | 
    task_history_file_upload_post_message = buildium_sdk.TaskHistoryFileUploadPostMessage() # TaskHistoryFileUploadPostMessage | 

    try:
        # Upload a task history file
        api_response = await api_instance.external_api_task_history_file_uploads_create_upload_file_request_async(task_id, task_history_id, task_history_file_upload_post_message)
        print("The response of TasksApi->external_api_task_history_file_uploads_create_upload_file_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_task_history_file_uploads_create_upload_file_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **task_history_id** | **int**|  | 
 **task_history_file_upload_post_message** | [**TaskHistoryFileUploadPostMessage**](TaskHistoryFileUploadPostMessage.md)|  | 

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

# **external_api_task_history_files_delete_task_history_file**
> external_api_task_history_files_delete_task_history_file(task_id, task_history_id, file_id)

Delete task history file

Deletes a specific file from a task history record. The file will be permanently deleted from the Buildium platform an can not be recovered.
            

This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View` `Edit` `Delete`

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
    api_instance = buildium_sdk.TasksApi(api_client)
    task_id = 56 # int | 
    task_history_id = 56 # int | 
    file_id = 56 # int | 

    try:
        # Delete task history file
        await api_instance.external_api_task_history_files_delete_task_history_file(task_id, task_history_id, file_id)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_task_history_files_delete_task_history_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **task_history_id** | **int**|  | 
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

# **external_api_task_history_files_get_all_task_history_files**
> List[TaskHistoryFileMessage] external_api_task_history_files_get_all_task_history_files(task_id, task_history_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all task history files

Retrieves the metadata for all files associated with a task history record.
            

This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.task_history_file_message import TaskHistoryFileMessage
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
    api_instance = buildium_sdk.TasksApi(api_client)
    task_id = 56 # int | 
    task_history_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all task history files
        api_response = await api_instance.external_api_task_history_files_get_all_task_history_files(task_id, task_history_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of TasksApi->external_api_task_history_files_get_all_task_history_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_task_history_files_get_all_task_history_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **task_history_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[TaskHistoryFileMessage]**](TaskHistoryFileMessage.md)

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

# **external_api_task_history_files_get_task_history_file_by_id**
> TaskHistoryFileMessage external_api_task_history_files_get_task_history_file_by_id(task_id, task_history_id, file_id)

Retrieve a task history file

Retrieves the metadata for a specific file associated with a task history record.
            

This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.task_history_file_message import TaskHistoryFileMessage
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
    api_instance = buildium_sdk.TasksApi(api_client)
    task_id = 56 # int | 
    task_history_id = 56 # int | 
    file_id = 56 # int | 

    try:
        # Retrieve a task history file
        api_response = await api_instance.external_api_task_history_files_get_task_history_file_by_id(task_id, task_history_id, file_id)
        print("The response of TasksApi->external_api_task_history_files_get_task_history_file_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_task_history_files_get_task_history_file_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **task_history_id** | **int**|  | 
 **file_id** | **int**|  | 

### Return type

[**TaskHistoryFileMessage**](TaskHistoryFileMessage.md)

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

# **external_api_task_history_get_task_histories**
> List[TaskHistoryMessage] external_api_task_history_get_task_histories(task_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all task history

Retrieves all task history records for a specific task.
            

This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.task_history_message import TaskHistoryMessage
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
    api_instance = buildium_sdk.TasksApi(api_client)
    task_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all task history
        api_response = await api_instance.external_api_task_history_get_task_histories(task_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of TasksApi->external_api_task_history_get_task_histories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_task_history_get_task_histories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[TaskHistoryMessage]**](TaskHistoryMessage.md)

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

# **external_api_task_history_get_task_history_by_id**
> TaskHistoryMessage external_api_task_history_get_task_history_by_id(task_id, task_history_id)

Retrieve a task history

Retrieves a specific task history record for a task.
            

This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.task_history_message import TaskHistoryMessage
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
    api_instance = buildium_sdk.TasksApi(api_client)
    task_id = 56 # int | 
    task_history_id = 56 # int | 

    try:
        # Retrieve a task history
        api_response = await api_instance.external_api_task_history_get_task_history_by_id(task_id, task_history_id)
        print("The response of TasksApi->external_api_task_history_get_task_history_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_task_history_get_task_history_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **task_history_id** | **int**|  | 

### Return type

[**TaskHistoryMessage**](TaskHistoryMessage.md)

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

# **external_api_task_history_update_task_history**
> TaskHistoryMessage external_api_task_history_update_task_history(task_id, task_history_id, task_history_put_message)

Update a task history

Updates a specific task history record for a task.
            

This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.task_history_message import TaskHistoryMessage
from buildium_sdk.models.task_history_put_message import TaskHistoryPutMessage
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
    api_instance = buildium_sdk.TasksApi(api_client)
    task_id = 56 # int | 
    task_history_id = 56 # int | 
    task_history_put_message = buildium_sdk.TaskHistoryPutMessage() # TaskHistoryPutMessage | 

    try:
        # Update a task history
        api_response = await api_instance.external_api_task_history_update_task_history(task_id, task_history_id, task_history_put_message)
        print("The response of TasksApi->external_api_task_history_update_task_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_task_history_update_task_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **task_history_id** | **int**|  | 
 **task_history_put_message** | [**TaskHistoryPutMessage**](TaskHistoryPutMessage.md)|  | 

### Return type

[**TaskHistoryMessage**](TaskHistoryMessage.md)

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

# **external_api_tasks_get_all_tasks**
> List[AllTasksMessage] external_api_tasks_get_all_tasks(entitytype=entitytype, entityid=entityid, statuses=statuses, type=type, unitid=unitid, unitagreementid=unitagreementid, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, duedatefrom=duedatefrom, duedateto=duedateto, taskcategoryid=taskcategoryid, priorities=priorities, assignedtoid=assignedtoid, tasktitle=tasktitle, orderby=orderby, offset=offset, limit=limit)

Retrieve all tasks

Retrieves a list of all task/request types (Contact, Owner, Resident and To Do). Note, the response payload only contains fields common across all of the request types. To retrieve the full details of the task query the retrieve endpoint specific to the task type.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.all_tasks_message import AllTasksMessage
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
    api_instance = buildium_sdk.TasksApi(api_client)
    entitytype = 'entitytype_example' # str | Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated. (optional)
    entityid = 56 # int | Filters results to any task associated with the specified entity id value. The value must be of the type specified in the `EntityType` field. (optional)
    statuses = ['statuses_example'] # List[str] | Filters results by the status of the task. If no status is specified, tasks with any status will be returned. (optional)
    type = 'type_example' # str | Filters results to any task associated with the task type specified. (optional)
    unitid = 56 # int | Filters results to any task associated with the unit identifier. (optional)
    unitagreementid = 56 # int | Filters results to any task associated with the unit agreement identifier specified. (optional)
    lastupdatedfrom = '2013-10-20' # date | Filters results to any tasks were updated on or after the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    lastupdatedto = '2013-10-20' # date | Filters results to any tasks were updated on or before the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    duedatefrom = '2013-10-20' # date | Filters results to any tasks with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    duedateto = '2013-10-20' # date | Filters results to any tasks with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    taskcategoryid = 56 # int | Filters results to any tasks with the specified category identifier. (optional)
    priorities = ['priorities_example'] # List[str] | Filters results to any tasks whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned. (optional)
    assignedtoid = 56 # int | Filters results to any tasks that have been assigned to the specified staff user identifier. (optional)
    tasktitle = 'tasktitle_example' # str | Filters results to any task whose title *contains* the specified value. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all tasks
        api_response = await api_instance.external_api_tasks_get_all_tasks(entitytype=entitytype, entityid=entityid, statuses=statuses, type=type, unitid=unitid, unitagreementid=unitagreementid, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, duedatefrom=duedatefrom, duedateto=duedateto, taskcategoryid=taskcategoryid, priorities=priorities, assignedtoid=assignedtoid, tasktitle=tasktitle, orderby=orderby, offset=offset, limit=limit)
        print("The response of TasksApi->external_api_tasks_get_all_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_tasks_get_all_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitytype** | **str**| Specifies the type of entity that the &#x60;EntityId&#x60; field refers to. This field is required if the &#x60;EntityId&#x60; field is populated. | [optional] 
 **entityid** | **int**| Filters results to any task associated with the specified entity id value. The value must be of the type specified in the &#x60;EntityType&#x60; field. | [optional] 
 **statuses** | [**List[str]**](str.md)| Filters results by the status of the task. If no status is specified, tasks with any status will be returned. | [optional] 
 **type** | **str**| Filters results to any task associated with the task type specified. | [optional] 
 **unitid** | **int**| Filters results to any task associated with the unit identifier. | [optional] 
 **unitagreementid** | **int**| Filters results to any task associated with the unit agreement identifier specified. | [optional] 
 **lastupdatedfrom** | **date**| Filters results to any tasks were updated on or after the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **lastupdatedto** | **date**| Filters results to any tasks were updated on or before the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **duedatefrom** | **date**| Filters results to any tasks with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **duedateto** | **date**| Filters results to any tasks with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **taskcategoryid** | **int**| Filters results to any tasks with the specified category identifier. | [optional] 
 **priorities** | [**List[str]**](str.md)| Filters results to any tasks whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned. | [optional] 
 **assignedtoid** | **int**| Filters results to any tasks that have been assigned to the specified staff user identifier. | [optional] 
 **tasktitle** | **str**| Filters results to any task whose title *contains* the specified value. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[AllTasksMessage]**](AllTasksMessage.md)

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

# **external_api_tasks_get_task_by_id**
> AllTasksMessage external_api_tasks_get_task_by_id(task_id)

Retrieve a task

Retrieves a specific task. This endpoint can be used for any task type - contact requests, rental owner requests, resident requests or to do's. Note, the response payload only contains fields common across all of the request types. To retrieve the full details of the task query the retrieve endpoint specific to the task type.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.all_tasks_message import AllTasksMessage
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
    api_instance = buildium_sdk.TasksApi(api_client)
    task_id = 56 # int | The task identifier

    try:
        # Retrieve a task
        api_response = await api_instance.external_api_tasks_get_task_by_id(task_id)
        print("The response of TasksApi->external_api_tasks_get_task_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->external_api_tasks_get_task_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| The task identifier | 

### Return type

[**AllTasksMessage**](AllTasksMessage.md)

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

