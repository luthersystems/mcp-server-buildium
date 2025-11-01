# buildium_sdk.RentalOwnerRequestsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_rental_owner_request_tasks_create_rental_owner_request_task**](RentalOwnerRequestsApi.md#external_api_rental_owner_request_tasks_create_rental_owner_request_task) | **POST** /v1/tasks/rentalownerrequests | Create a rental owner request
[**external_api_rental_owner_request_tasks_get_all_rental_owner_request_tasks**](RentalOwnerRequestsApi.md#external_api_rental_owner_request_tasks_get_all_rental_owner_request_tasks) | **GET** /v1/tasks/rentalownerrequests | Retrieve all rental owner requests
[**external_api_rental_owner_request_tasks_get_rental_owner_request_task_by_id**](RentalOwnerRequestsApi.md#external_api_rental_owner_request_tasks_get_rental_owner_request_task_by_id) | **GET** /v1/tasks/rentalownerrequests/{rentalOwnerRequestTaskId} | Retrieve a rental owner request
[**external_api_rental_owner_request_tasks_get_rental_owner_request_task_contribution_data**](RentalOwnerRequestsApi.md#external_api_rental_owner_request_tasks_get_rental_owner_request_task_contribution_data) | **GET** /v1/tasks/rentalownerrequests/{rentalOwnerRequestTaskId}/contributiondata | Retrieve rental owner contribution request
[**external_api_rental_owner_request_tasks_update_rental_owner_request_task**](RentalOwnerRequestsApi.md#external_api_rental_owner_request_tasks_update_rental_owner_request_task) | **PUT** /v1/tasks/rentalownerrequests/{rentalOwnerRequestTaskId} | Update a rental owner request
[**external_api_rental_owner_request_tasks_update_rental_owner_request_task_contribution_data**](RentalOwnerRequestsApi.md#external_api_rental_owner_request_tasks_update_rental_owner_request_task_contribution_data) | **PUT** /v1/tasks/rentalownerrequests/{rentalOwnerRequestTaskId}/contributiondata | Update a rental owner contribution request


# **external_api_rental_owner_request_tasks_create_rental_owner_request_task**
> RentalOwnerRequestTaskMessage external_api_rental_owner_request_tasks_create_rental_owner_request_task(rental_owner_request_task_post_message)

Create a rental owner request

Creates a rental owner request.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_owner_request_task_message import RentalOwnerRequestTaskMessage
from buildium_sdk.models.rental_owner_request_task_post_message import RentalOwnerRequestTaskPostMessage
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
    api_instance = buildium_sdk.RentalOwnerRequestsApi(api_client)
    rental_owner_request_task_post_message = buildium_sdk.RentalOwnerRequestTaskPostMessage() # RentalOwnerRequestTaskPostMessage | 

    try:
        # Create a rental owner request
        api_response = await api_instance.external_api_rental_owner_request_tasks_create_rental_owner_request_task(rental_owner_request_task_post_message)
        print("The response of RentalOwnerRequestsApi->external_api_rental_owner_request_tasks_create_rental_owner_request_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnerRequestsApi->external_api_rental_owner_request_tasks_create_rental_owner_request_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_owner_request_task_post_message** | [**RentalOwnerRequestTaskPostMessage**](RentalOwnerRequestTaskPostMessage.md)|  | 

### Return type

[**RentalOwnerRequestTaskMessage**](RentalOwnerRequestTaskMessage.md)

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

# **external_api_rental_owner_request_tasks_get_all_rental_owner_request_tasks**
> List[RentalOwnerRequestTaskMessage] external_api_rental_owner_request_tasks_get_all_rental_owner_request_tasks(entitytype=entitytype, entityid=entityid, statuses=statuses, unitid=unitid, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, duedatefrom=duedatefrom, duedateto=duedateto, taskcategoryid=taskcategoryid, priorities=priorities, assignedtoid=assignedtoid, tasktitle=tasktitle)

Retrieve all rental owner requests

Retrieves all rental owner requests.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_owner_request_task_message import RentalOwnerRequestTaskMessage
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
    api_instance = buildium_sdk.RentalOwnerRequestsApi(api_client)
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

    try:
        # Retrieve all rental owner requests
        api_response = await api_instance.external_api_rental_owner_request_tasks_get_all_rental_owner_request_tasks(entitytype=entitytype, entityid=entityid, statuses=statuses, unitid=unitid, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, duedatefrom=duedatefrom, duedateto=duedateto, taskcategoryid=taskcategoryid, priorities=priorities, assignedtoid=assignedtoid, tasktitle=tasktitle)
        print("The response of RentalOwnerRequestsApi->external_api_rental_owner_request_tasks_get_all_rental_owner_request_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnerRequestsApi->external_api_rental_owner_request_tasks_get_all_rental_owner_request_tasks: %s\n" % e)
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

### Return type

[**List[RentalOwnerRequestTaskMessage]**](RentalOwnerRequestTaskMessage.md)

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

# **external_api_rental_owner_request_tasks_get_rental_owner_request_task_by_id**
> RentalOwnerRequestTaskMessage external_api_rental_owner_request_tasks_get_rental_owner_request_task_by_id(rental_owner_request_task_id)

Retrieve a rental owner request

Retrieves a specific rental owner request.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_owner_request_task_message import RentalOwnerRequestTaskMessage
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
    api_instance = buildium_sdk.RentalOwnerRequestsApi(api_client)
    rental_owner_request_task_id = 56 # int | The rental owner request identifier.

    try:
        # Retrieve a rental owner request
        api_response = await api_instance.external_api_rental_owner_request_tasks_get_rental_owner_request_task_by_id(rental_owner_request_task_id)
        print("The response of RentalOwnerRequestsApi->external_api_rental_owner_request_tasks_get_rental_owner_request_task_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnerRequestsApi->external_api_rental_owner_request_tasks_get_rental_owner_request_task_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_owner_request_task_id** | **int**| The rental owner request identifier. | 

### Return type

[**RentalOwnerRequestTaskMessage**](RentalOwnerRequestTaskMessage.md)

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

# **external_api_rental_owner_request_tasks_get_rental_owner_request_task_contribution_data**
> RentalOwnerContributionDataMessage external_api_rental_owner_request_tasks_get_rental_owner_request_task_contribution_data(rental_owner_request_task_id)

Retrieve rental owner contribution request

Retrieves the contribution details for a rental owner contribution request.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_owner_contribution_data_message import RentalOwnerContributionDataMessage
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
    api_instance = buildium_sdk.RentalOwnerRequestsApi(api_client)
    rental_owner_request_task_id = 56 # int | The rental owner request identifier.

    try:
        # Retrieve rental owner contribution request
        api_response = await api_instance.external_api_rental_owner_request_tasks_get_rental_owner_request_task_contribution_data(rental_owner_request_task_id)
        print("The response of RentalOwnerRequestsApi->external_api_rental_owner_request_tasks_get_rental_owner_request_task_contribution_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnerRequestsApi->external_api_rental_owner_request_tasks_get_rental_owner_request_task_contribution_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_owner_request_task_id** | **int**| The rental owner request identifier. | 

### Return type

[**RentalOwnerContributionDataMessage**](RentalOwnerContributionDataMessage.md)

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
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_rental_owner_request_tasks_update_rental_owner_request_task**
> RentalOwnerRequestTaskMessage external_api_rental_owner_request_tasks_update_rental_owner_request_task(rental_owner_request_task_id, rental_owner_request_task_put_message)

Update a rental owner request

Updates a rental owner request.


<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_owner_request_task_message import RentalOwnerRequestTaskMessage
from buildium_sdk.models.rental_owner_request_task_put_message import RentalOwnerRequestTaskPutMessage
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
    api_instance = buildium_sdk.RentalOwnerRequestsApi(api_client)
    rental_owner_request_task_id = 56 # int | The rental owner request identifier.
    rental_owner_request_task_put_message = buildium_sdk.RentalOwnerRequestTaskPutMessage() # RentalOwnerRequestTaskPutMessage | 

    try:
        # Update a rental owner request
        api_response = await api_instance.external_api_rental_owner_request_tasks_update_rental_owner_request_task(rental_owner_request_task_id, rental_owner_request_task_put_message)
        print("The response of RentalOwnerRequestsApi->external_api_rental_owner_request_tasks_update_rental_owner_request_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnerRequestsApi->external_api_rental_owner_request_tasks_update_rental_owner_request_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_owner_request_task_id** | **int**| The rental owner request identifier. | 
 **rental_owner_request_task_put_message** | [**RentalOwnerRequestTaskPutMessage**](RentalOwnerRequestTaskPutMessage.md)|  | 

### Return type

[**RentalOwnerRequestTaskMessage**](RentalOwnerRequestTaskMessage.md)

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

# **external_api_rental_owner_request_tasks_update_rental_owner_request_task_contribution_data**
> RentalOwnerContributionDataMessage external_api_rental_owner_request_tasks_update_rental_owner_request_task_contribution_data(rental_owner_request_task_id, rental_owner_contribution_data_put_message)

Update a rental owner contribution request

Updates the contribution details for a rental owner contribution request.


<h4>Required permission(s):</h4><span class="permissionBlock">Tasks > Tasks</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_owner_contribution_data_message import RentalOwnerContributionDataMessage
from buildium_sdk.models.rental_owner_contribution_data_put_message import RentalOwnerContributionDataPutMessage
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
    api_instance = buildium_sdk.RentalOwnerRequestsApi(api_client)
    rental_owner_request_task_id = 56 # int | The rental owner request identifier.
    rental_owner_contribution_data_put_message = buildium_sdk.RentalOwnerContributionDataPutMessage() # RentalOwnerContributionDataPutMessage | 

    try:
        # Update a rental owner contribution request
        api_response = await api_instance.external_api_rental_owner_request_tasks_update_rental_owner_request_task_contribution_data(rental_owner_request_task_id, rental_owner_contribution_data_put_message)
        print("The response of RentalOwnerRequestsApi->external_api_rental_owner_request_tasks_update_rental_owner_request_task_contribution_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalOwnerRequestsApi->external_api_rental_owner_request_tasks_update_rental_owner_request_task_contribution_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_owner_request_task_id** | **int**| The rental owner request identifier. | 
 **rental_owner_contribution_data_put_message** | [**RentalOwnerContributionDataPutMessage**](RentalOwnerContributionDataPutMessage.md)|  | 

### Return type

[**RentalOwnerContributionDataMessage**](RentalOwnerContributionDataMessage.md)

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

