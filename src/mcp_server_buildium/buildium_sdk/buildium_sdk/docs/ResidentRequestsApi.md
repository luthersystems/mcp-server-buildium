# buildium_sdk.ResidentRequestsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_resident_request_tasks_create_resource**](ResidentRequestsApi.md#external_api_resident_request_tasks_create_resource) | **POST** /v1/tasks/residentrequests | Create a resident request
[**external_api_resident_request_tasks_get_resident_request_task**](ResidentRequestsApi.md#external_api_resident_request_tasks_get_resident_request_task) | **GET** /v1/tasks/residentrequests/{residentRequestTaskId} | Retrieve a resident request
[**external_api_resident_request_tasks_get_resident_request_tasks**](ResidentRequestsApi.md#external_api_resident_request_tasks_get_resident_request_tasks) | **GET** /v1/tasks/residentrequests | Retrieve all resident requests
[**external_api_resident_request_tasks_update_resource**](ResidentRequestsApi.md#external_api_resident_request_tasks_update_resource) | **PUT** /v1/tasks/residentrequests/{residentRequestTaskId} | Update a resident request


# **external_api_resident_request_tasks_create_resource**
> ResidentRequestTaskMessage external_api_resident_request_tasks_create_resource(resident_request_task_post_message)

Create a resident request

Creates a resident request.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.resident_request_task_message import ResidentRequestTaskMessage
from buildium_sdk.models.resident_request_task_post_message import ResidentRequestTaskPostMessage
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
    api_instance = buildium_sdk.ResidentRequestsApi(api_client)
    resident_request_task_post_message = buildium_sdk.ResidentRequestTaskPostMessage() # ResidentRequestTaskPostMessage | 

    try:
        # Create a resident request
        api_response = await api_instance.external_api_resident_request_tasks_create_resource(resident_request_task_post_message)
        print("The response of ResidentRequestsApi->external_api_resident_request_tasks_create_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResidentRequestsApi->external_api_resident_request_tasks_create_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resident_request_task_post_message** | [**ResidentRequestTaskPostMessage**](ResidentRequestTaskPostMessage.md)|  | 

### Return type

[**ResidentRequestTaskMessage**](ResidentRequestTaskMessage.md)

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

# **external_api_resident_request_tasks_get_resident_request_task**
> ResidentRequestTaskMessage external_api_resident_request_tasks_get_resident_request_task(resident_request_task_id)

Retrieve a resident request

Retrieves a specific resident request.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.resident_request_task_message import ResidentRequestTaskMessage
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
    api_instance = buildium_sdk.ResidentRequestsApi(api_client)
    resident_request_task_id = 56 # int | The resident request identifier.

    try:
        # Retrieve a resident request
        api_response = await api_instance.external_api_resident_request_tasks_get_resident_request_task(resident_request_task_id)
        print("The response of ResidentRequestsApi->external_api_resident_request_tasks_get_resident_request_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResidentRequestsApi->external_api_resident_request_tasks_get_resident_request_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resident_request_task_id** | **int**| The resident request identifier. | 

### Return type

[**ResidentRequestTaskMessage**](ResidentRequestTaskMessage.md)

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

# **external_api_resident_request_tasks_get_resident_request_tasks**
> List[ResidentRequestTaskMessage] external_api_resident_request_tasks_get_resident_request_tasks(entitytype=entitytype, entityid=entityid, statuses=statuses, unitid=unitid, unitagreementid=unitagreementid, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, duedatefrom=duedatefrom, duedateto=duedateto, taskcategoryid=taskcategoryid, priorities=priorities, assignedtoid=assignedtoid, tasktitle=tasktitle, orderby=orderby, offset=offset, limit=limit)

Retrieve all resident requests

Retrieves a list of resident requests.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.resident_request_task_message import ResidentRequestTaskMessage
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
    api_instance = buildium_sdk.ResidentRequestsApi(api_client)
    entitytype = 'entitytype_example' # str | Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated. (optional)
    entityid = 56 # int | Filters results to any task associated with the specified entity id value. The value must be of the type specified in the `EntityType` field. (optional)
    statuses = ['statuses_example'] # List[str] | Filters results by the status of the task. If no status is specified, tasks with any status will be returned. (optional)
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
        # Retrieve all resident requests
        api_response = await api_instance.external_api_resident_request_tasks_get_resident_request_tasks(entitytype=entitytype, entityid=entityid, statuses=statuses, unitid=unitid, unitagreementid=unitagreementid, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, duedatefrom=duedatefrom, duedateto=duedateto, taskcategoryid=taskcategoryid, priorities=priorities, assignedtoid=assignedtoid, tasktitle=tasktitle, orderby=orderby, offset=offset, limit=limit)
        print("The response of ResidentRequestsApi->external_api_resident_request_tasks_get_resident_request_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResidentRequestsApi->external_api_resident_request_tasks_get_resident_request_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitytype** | **str**| Specifies the type of entity that the &#x60;EntityId&#x60; field refers to. This field is required if the &#x60;EntityId&#x60; field is populated. | [optional] 
 **entityid** | **int**| Filters results to any task associated with the specified entity id value. The value must be of the type specified in the &#x60;EntityType&#x60; field. | [optional] 
 **statuses** | [**List[str]**](str.md)| Filters results by the status of the task. If no status is specified, tasks with any status will be returned. | [optional] 
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

[**List[ResidentRequestTaskMessage]**](ResidentRequestTaskMessage.md)

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

# **external_api_resident_request_tasks_update_resource**
> ResidentRequestTaskMessage external_api_resident_request_tasks_update_resource(resident_request_task_id, resident_request_task_put_message)

Update a resident request

Update a resident request.


<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.resident_request_task_message import ResidentRequestTaskMessage
from buildium_sdk.models.resident_request_task_put_message import ResidentRequestTaskPutMessage
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
    api_instance = buildium_sdk.ResidentRequestsApi(api_client)
    resident_request_task_id = 56 # int | The resident request identifier.
    resident_request_task_put_message = buildium_sdk.ResidentRequestTaskPutMessage() # ResidentRequestTaskPutMessage | 

    try:
        # Update a resident request
        api_response = await api_instance.external_api_resident_request_tasks_update_resource(resident_request_task_id, resident_request_task_put_message)
        print("The response of ResidentRequestsApi->external_api_resident_request_tasks_update_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResidentRequestsApi->external_api_resident_request_tasks_update_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resident_request_task_id** | **int**| The resident request identifier. | 
 **resident_request_task_put_message** | [**ResidentRequestTaskPutMessage**](ResidentRequestTaskPutMessage.md)|  | 

### Return type

[**ResidentRequestTaskMessage**](ResidentRequestTaskMessage.md)

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

