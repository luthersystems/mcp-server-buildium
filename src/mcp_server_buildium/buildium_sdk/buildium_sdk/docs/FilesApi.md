# buildium_sdk.FilesApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_file_categories_create_file_category**](FilesApi.md#external_api_file_categories_create_file_category) | **POST** /v1/files/categories | Create a category
[**external_api_file_categories_get_file_categories**](FilesApi.md#external_api_file_categories_get_file_categories) | **GET** /v1/files/categories | Retrieve all categories
[**external_api_file_categories_get_file_category_by_id**](FilesApi.md#external_api_file_categories_get_file_category_by_id) | **GET** /v1/files/categories/{fileCategoryId} | Retrieve a category
[**external_api_file_categories_update_file_category**](FilesApi.md#external_api_file_categories_update_file_category) | **PUT** /v1/files/categories/{fileCategoryId} | Update a category
[**external_api_file_download_get_file_download_url_async**](FilesApi.md#external_api_file_download_get_file_download_url_async) | **POST** /v1/files/{fileId}/downloadrequest | Download a file
[**external_api_file_sharing_get_file_share_settings_by_id**](FilesApi.md#external_api_file_sharing_get_file_share_settings_by_id) | **GET** /v1/files/{fileId}/sharing | Retrieve file share settings
[**external_api_file_sharing_update_file_sharing_setting**](FilesApi.md#external_api_file_sharing_update_file_sharing_setting) | **PUT** /v1/files/{fileId}/sharing | Update file share settings
[**external_api_files_get_file_by_id**](FilesApi.md#external_api_files_get_file_by_id) | **GET** /v1/files/{fileId} | Retrieve a file
[**external_api_files_get_files**](FilesApi.md#external_api_files_get_files) | **GET** /v1/files | Retrieve all files
[**external_api_files_update_file**](FilesApi.md#external_api_files_update_file) | **PUT** /v1/files/{fileId} | Update a file
[**external_api_files_uploads_create_upload_file_request_async**](FilesApi.md#external_api_files_uploads_create_upload_file_request_async) | **POST** /v1/files/uploadrequests | Upload a file


# **external_api_file_categories_create_file_category**
> FileCategoryMessage external_api_file_categories_create_file_category(file_category_post_message)

Create a category

Creates a file category.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Documents > Files</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_category_message import FileCategoryMessage
from buildium_sdk.models.file_category_post_message import FileCategoryPostMessage
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
    api_instance = buildium_sdk.FilesApi(api_client)
    file_category_post_message = buildium_sdk.FileCategoryPostMessage() # FileCategoryPostMessage | 

    try:
        # Create a category
        api_response = await api_instance.external_api_file_categories_create_file_category(file_category_post_message)
        print("The response of FilesApi->external_api_file_categories_create_file_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->external_api_file_categories_create_file_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_category_post_message** | [**FileCategoryPostMessage**](FileCategoryPostMessage.md)|  | 

### Return type

[**FileCategoryMessage**](FileCategoryMessage.md)

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

# **external_api_file_categories_get_file_categories**
> List[FileCategoryMessage] external_api_file_categories_get_file_categories(orderby=orderby, offset=offset, limit=limit)

Retrieve all categories

Retrieves a list of file categories.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Documents > Files</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_category_message import FileCategoryMessage
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
    api_instance = buildium_sdk.FilesApi(api_client)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all categories
        api_response = await api_instance.external_api_file_categories_get_file_categories(orderby=orderby, offset=offset, limit=limit)
        print("The response of FilesApi->external_api_file_categories_get_file_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->external_api_file_categories_get_file_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[FileCategoryMessage]**](FileCategoryMessage.md)

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

# **external_api_file_categories_get_file_category_by_id**
> FileCategoryMessage external_api_file_categories_get_file_category_by_id(file_category_id)

Retrieve a category

Retrieves a specific file category.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Documents > Files</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_category_message import FileCategoryMessage
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
    api_instance = buildium_sdk.FilesApi(api_client)
    file_category_id = 56 # int | 

    try:
        # Retrieve a category
        api_response = await api_instance.external_api_file_categories_get_file_category_by_id(file_category_id)
        print("The response of FilesApi->external_api_file_categories_get_file_category_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->external_api_file_categories_get_file_category_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_category_id** | **int**|  | 

### Return type

[**FileCategoryMessage**](FileCategoryMessage.md)

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

# **external_api_file_categories_update_file_category**
> FileCategoryMessage external_api_file_categories_update_file_category(file_category_id, file_category_put_message)

Update a category

Updates a file category. Note that file categories where `IsEditable` is `false` can not be updated.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Documents > Files</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_category_message import FileCategoryMessage
from buildium_sdk.models.file_category_put_message import FileCategoryPutMessage
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
    api_instance = buildium_sdk.FilesApi(api_client)
    file_category_id = 56 # int | 
    file_category_put_message = buildium_sdk.FileCategoryPutMessage() # FileCategoryPutMessage | 

    try:
        # Update a category
        api_response = await api_instance.external_api_file_categories_update_file_category(file_category_id, file_category_put_message)
        print("The response of FilesApi->external_api_file_categories_update_file_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->external_api_file_categories_update_file_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_category_id** | **int**|  | 
 **file_category_put_message** | [**FileCategoryPutMessage**](FileCategoryPutMessage.md)|  | 

### Return type

[**FileCategoryMessage**](FileCategoryMessage.md)

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

# **external_api_file_download_get_file_download_url_async**
> FileDownloadMessage external_api_file_download_get_file_download_url_async(file_id)

Download a file

Downloading a file requires making two API requests. The first request to `/v1/files/{fileId}/downloadrequest` will return a secure URL that can be used to download the file contents. Note the download URL is transient and will expire after 5 minutes. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Documents > Files</span> - `View`

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
    api_instance = buildium_sdk.FilesApi(api_client)
    file_id = 56 # int | 

    try:
        # Download a file
        api_response = await api_instance.external_api_file_download_get_file_download_url_async(file_id)
        print("The response of FilesApi->external_api_file_download_get_file_download_url_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->external_api_file_download_get_file_download_url_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **external_api_file_sharing_get_file_share_settings_by_id**
> FileSharingMessage external_api_file_sharing_get_file_share_settings_by_id(file_id)

Retrieve file share settings

Retrieves a file's share settings. Note, that the response JSON schema includes share setting fields for all file entity types, however only fields that pertain to the queried file entity type will be populated. For example, if a file of entity type Rental is retrieved only the fields in the Rental section of the response will have values.
            
<h4>Required permission(s):</h4><span class="permissionBlock">Documents > Files</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_sharing_message import FileSharingMessage
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
    api_instance = buildium_sdk.FilesApi(api_client)
    file_id = 56 # int | 

    try:
        # Retrieve file share settings
        api_response = await api_instance.external_api_file_sharing_get_file_share_settings_by_id(file_id)
        print("The response of FilesApi->external_api_file_sharing_get_file_share_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->external_api_file_sharing_get_file_share_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**|  | 

### Return type

[**FileSharingMessage**](FileSharingMessage.md)

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

# **external_api_file_sharing_update_file_sharing_setting**
> FileSharingMessage external_api_file_sharing_update_file_sharing_setting(file_id, file_sharing_put_message)

Update file share settings

Updates a file's share settings. Note, can only update a file's share settings based on the file's entity type (ie: If the file belongs to a rental property, you can only update the rental file sharing settings). The response payload contains file share setting values for all file entity types, but the relevant setting values correlate to the file's entity type.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Documents > Files</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_sharing_message import FileSharingMessage
from buildium_sdk.models.file_sharing_put_message import FileSharingPutMessage
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
    api_instance = buildium_sdk.FilesApi(api_client)
    file_id = 56 # int | 
    file_sharing_put_message = buildium_sdk.FileSharingPutMessage() # FileSharingPutMessage | 

    try:
        # Update file share settings
        api_response = await api_instance.external_api_file_sharing_update_file_sharing_setting(file_id, file_sharing_put_message)
        print("The response of FilesApi->external_api_file_sharing_update_file_sharing_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->external_api_file_sharing_update_file_sharing_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**|  | 
 **file_sharing_put_message** | [**FileSharingPutMessage**](FileSharingPutMessage.md)|  | 

### Return type

[**FileSharingMessage**](FileSharingMessage.md)

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

# **external_api_files_get_file_by_id**
> FileMessage external_api_files_get_file_by_id(file_id)

Retrieve a file

Retrieves the file metadata for a specific file. Note this endpoint will only return file metadata. To download files make requests to the <a href="#operation/FileDownloadExternalApi_GetFileDownloadUrlAsync">Download File endpoint.</a>

<h4>Required permission(s):</h4><span class="permissionBlock">Documents > Files</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_message import FileMessage
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
    api_instance = buildium_sdk.FilesApi(api_client)
    file_id = 56 # int | 

    try:
        # Retrieve a file
        api_response = await api_instance.external_api_files_get_file_by_id(file_id)
        print("The response of FilesApi->external_api_files_get_file_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->external_api_files_get_file_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**|  | 

### Return type

[**FileMessage**](FileMessage.md)

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

# **external_api_files_get_files**
> List[FileMessage] external_api_files_get_files(entityid=entityid, entitytype=entitytype, categoryid=categoryid, titleordescription=titleordescription, uploadedfrom=uploadedfrom, uploadedto=uploadedto, physicalfilenames=physicalfilenames, orderby=orderby, offset=offset, limit=limit)

Retrieve all files

Retrieves a list of files that exist within the customer account. Note this endpoint will only return file metadata. To download files make requests to the <a href="#operation/FileDownloadExternalApi_GetFileDownloadUrlAsync">Download File</a> endpoint. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Documents > Files</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_message import FileMessage
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
    api_instance = buildium_sdk.FilesApi(api_client)
    entityid = 56 # int | Filters results to any file associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references. (optional)
    entitytype = 'entitytype_example' # str | Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified. (optional)
    categoryid = 56 # int | Filters results to any file associated with the specified category identifier. (optional)
    titleordescription = 'titleordescription_example' # str | Filters results to files whose title or description *contains* the specified value. (optional)
    uploadedfrom = '2013-10-20' # date | Filters results to any files that were updated on or after the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    uploadedto = '2013-10-20' # date | Filters results to any files that were updated on or before the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    physicalfilenames = ['physicalfilenames_example'] # List[str] | Filters results to any files with a `PhysicalFileName`exactly matching one of the provided values. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all files
        api_response = await api_instance.external_api_files_get_files(entityid=entityid, entitytype=entitytype, categoryid=categoryid, titleordescription=titleordescription, uploadedfrom=uploadedfrom, uploadedto=uploadedto, physicalfilenames=physicalfilenames, orderby=orderby, offset=offset, limit=limit)
        print("The response of FilesApi->external_api_files_get_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->external_api_files_get_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entityid** | **int**| Filters results to any file associated with the specified entity identifier. This filter is used in conjunction with the &#x60;EntityType&#x60; field which must be set to the type of entity this identifier references. | [optional] 
 **entitytype** | **str**| Specifies the type of entity that &#x60;EntityId&#x60; refers to. This field is required if &#x60;EntityId&#x60; is specified. | [optional] 
 **categoryid** | **int**| Filters results to any file associated with the specified category identifier. | [optional] 
 **titleordescription** | **str**| Filters results to files whose title or description *contains* the specified value. | [optional] 
 **uploadedfrom** | **date**| Filters results to any files that were updated on or after the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **uploadedto** | **date**| Filters results to any files that were updated on or before the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **physicalfilenames** | [**List[str]**](str.md)| Filters results to any files with a &#x60;PhysicalFileName&#x60;exactly matching one of the provided values. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[FileMessage]**](FileMessage.md)

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

# **external_api_files_update_file**
> FileMessage external_api_files_update_file(file_id, file_put_message)

Update a file

Updates a metadata of the file. 
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Documents > Files</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_message import FileMessage
from buildium_sdk.models.file_put_message import FilePutMessage
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
    api_instance = buildium_sdk.FilesApi(api_client)
    file_id = 56 # int | 
    file_put_message = buildium_sdk.FilePutMessage() # FilePutMessage | 

    try:
        # Update a file
        api_response = await api_instance.external_api_files_update_file(file_id, file_put_message)
        print("The response of FilesApi->external_api_files_update_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->external_api_files_update_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**|  | 
 **file_put_message** | [**FilePutMessage**](FilePutMessage.md)|  | 

### Return type

[**FileMessage**](FileMessage.md)

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

# **external_api_files_uploads_create_upload_file_request_async**
> FileUploadTicketMessage external_api_files_uploads_create_upload_file_request_async(file_upload_post_message)

Upload a file

Uploading a file requires making two API requests. Each step is outlined below.


<strong>Step 1 - Save file metadata</strong>

The first step in the file upload process is to submit the file metadata to `/v1/files/uploadrequests`. The response of this call will contain a URL and a collection of form data that will be used in step 2 to generate the request for the file binary upload.


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


<h4>Required permission(s):</h4><span class="permissionBlock">Documents > Files</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_upload_post_message import FileUploadPostMessage
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
    api_instance = buildium_sdk.FilesApi(api_client)
    file_upload_post_message = buildium_sdk.FileUploadPostMessage() # FileUploadPostMessage | 

    try:
        # Upload a file
        api_response = await api_instance.external_api_files_uploads_create_upload_file_request_async(file_upload_post_message)
        print("The response of FilesApi->external_api_files_uploads_create_upload_file_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->external_api_files_uploads_create_upload_file_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_upload_post_message** | [**FileUploadPostMessage**](FileUploadPostMessage.md)|  | 

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

