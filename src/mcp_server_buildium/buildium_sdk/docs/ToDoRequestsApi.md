# buildium_sdk.ToDoRequestsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_to_do_tasks_create_to_do_task**](ToDoRequestsApi.md#external_api_to_do_tasks_create_to_do_task) | **POST** /v1/tasks/todorequests | Create a to do request
[**external_api_to_do_tasks_get_to_do_task_by_id**](ToDoRequestsApi.md#external_api_to_do_tasks_get_to_do_task_by_id) | **GET** /v1/tasks/todorequests/{toDoTaskId} | Retrieve a to do request
[**external_api_to_do_tasks_get_to_do_tasks**](ToDoRequestsApi.md#external_api_to_do_tasks_get_to_do_tasks) | **GET** /v1/tasks/todorequests | Retrieve all to do requests
[**external_api_to_do_tasks_update_to_do_task**](ToDoRequestsApi.md#external_api_to_do_tasks_update_to_do_task) | **PUT** /v1/tasks/todorequests/{toDoTaskId} | Update a to do request


# **external_api_to_do_tasks_create_to_do_task**
> ToDoTaskMessage external_api_to_do_tasks_create_to_do_task(to_do_task_post_message)

Create a to do request

Creates a to do task.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.to_do_task_message import ToDoTaskMessage
from buildium_sdk.models.to_do_task_post_message import ToDoTaskPostMessage
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
    api_instance = buildium_sdk.ToDoRequestsApi(api_client)
    to_do_task_post_message = buildium_sdk.ToDoTaskPostMessage() # ToDoTaskPostMessage | 

    try:
        # Create a to do request
        api_response = await api_instance.external_api_to_do_tasks_create_to_do_task(to_do_task_post_message)
        print("The response of ToDoRequestsApi->external_api_to_do_tasks_create_to_do_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToDoRequestsApi->external_api_to_do_tasks_create_to_do_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_do_task_post_message** | [**ToDoTaskPostMessage**](ToDoTaskPostMessage.md)|  | 

### Return type

[**ToDoTaskMessage**](ToDoTaskMessage.md)

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

# **external_api_to_do_tasks_get_to_do_task_by_id**
> ToDoTaskMessage external_api_to_do_tasks_get_to_do_task_by_id(to_do_task_id)

Retrieve a to do request

Retrieves a to do task.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.to_do_task_message import ToDoTaskMessage
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
    api_instance = buildium_sdk.ToDoRequestsApi(api_client)
    to_do_task_id = 56 # int | The to do task identifier

    try:
        # Retrieve a to do request
        api_response = await api_instance.external_api_to_do_tasks_get_to_do_task_by_id(to_do_task_id)
        print("The response of ToDoRequestsApi->external_api_to_do_tasks_get_to_do_task_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToDoRequestsApi->external_api_to_do_tasks_get_to_do_task_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_do_task_id** | **int**| The to do task identifier | 

### Return type

[**ToDoTaskMessage**](ToDoTaskMessage.md)

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

# **external_api_to_do_tasks_get_to_do_tasks**
> List[ToDoTaskMessage] external_api_to_do_tasks_get_to_do_tasks(entitytype=entitytype, entityid=entityid, statuses=statuses, unitid=unitid, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, duedatefrom=duedatefrom, duedateto=duedateto, taskcategoryid=taskcategoryid, priorities=priorities, assignedtoid=assignedtoid, tasktitle=tasktitle, orderby=orderby, offset=offset, limit=limit)

Retrieve all to do requests

Retrieves a list of to do tasks.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.to_do_task_message import ToDoTaskMessage
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
    api_instance = buildium_sdk.ToDoRequestsApi(api_client)
    entitytype = 'entitytype_example' # str | Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated. (optional)
    entityid = 56 # int | Filters results to any task associated with the specified entity id value. The value must be of the type specified in the `EntityType` field. (optional)
    statuses = ['statuses_example'] # List[str] | Filters results by the status of the task. If no status is specified, tasks with any status will be returned. (optional)
    unitid = 56 # int | Filters results to any task associated with the unit identifier. (optional)
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
        # Retrieve all to do requests
        api_response = await api_instance.external_api_to_do_tasks_get_to_do_tasks(entitytype=entitytype, entityid=entityid, statuses=statuses, unitid=unitid, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, duedatefrom=duedatefrom, duedateto=duedateto, taskcategoryid=taskcategoryid, priorities=priorities, assignedtoid=assignedtoid, tasktitle=tasktitle, orderby=orderby, offset=offset, limit=limit)
        print("The response of ToDoRequestsApi->external_api_to_do_tasks_get_to_do_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToDoRequestsApi->external_api_to_do_tasks_get_to_do_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitytype** | **str**| Specifies the type of entity that the &#x60;EntityId&#x60; field refers to. This field is required if the &#x60;EntityId&#x60; field is populated. | [optional] 
 **entityid** | **int**| Filters results to any task associated with the specified entity id value. The value must be of the type specified in the &#x60;EntityType&#x60; field. | [optional] 
 **statuses** | [**List[str]**](str.md)| Filters results by the status of the task. If no status is specified, tasks with any status will be returned. | [optional] 
 **unitid** | **int**| Filters results to any task associated with the unit identifier. | [optional] 
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

[**List[ToDoTaskMessage]**](ToDoTaskMessage.md)

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

# **external_api_to_do_tasks_update_to_do_task**
> ToDoTaskMessage external_api_to_do_tasks_update_to_do_task(to_do_task_id, to_do_task_put_message)

Update a to do request

Updates a to do task


<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.to_do_task_message import ToDoTaskMessage
from buildium_sdk.models.to_do_task_put_message import ToDoTaskPutMessage
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
    api_instance = buildium_sdk.ToDoRequestsApi(api_client)
    to_do_task_id = 56 # int | The to do task identifier.
    to_do_task_put_message = buildium_sdk.ToDoTaskPutMessage() # ToDoTaskPutMessage | 

    try:
        # Update a to do request
        api_response = await api_instance.external_api_to_do_tasks_update_to_do_task(to_do_task_id, to_do_task_put_message)
        print("The response of ToDoRequestsApi->external_api_to_do_tasks_update_to_do_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToDoRequestsApi->external_api_to_do_tasks_update_to_do_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_do_task_id** | **int**| The to do task identifier. | 
 **to_do_task_put_message** | [**ToDoTaskPutMessage**](ToDoTaskPutMessage.md)|  | 

### Return type

[**ToDoTaskMessage**](ToDoTaskMessage.md)

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

