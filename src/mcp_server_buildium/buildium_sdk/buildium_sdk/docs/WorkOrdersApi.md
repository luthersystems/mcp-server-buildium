# buildium_sdk.WorkOrdersApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_work_orders_create_work_order**](WorkOrdersApi.md#external_api_work_orders_create_work_order) | **POST** /v1/workorders | Create a work order
[**external_api_work_orders_get_all_work_orders**](WorkOrdersApi.md#external_api_work_orders_get_all_work_orders) | **GET** /v1/workorders | Retrieve all work orders
[**external_api_work_orders_get_work_order_by_id**](WorkOrdersApi.md#external_api_work_orders_get_work_order_by_id) | **GET** /v1/workorders/{workOrderId} | Retrieve a work order
[**external_api_work_orders_update_work_order**](WorkOrdersApi.md#external_api_work_orders_update_work_order) | **PUT** /v1/workorders/{workOrderId} | Update a work order


# **external_api_work_orders_create_work_order**
> WorkOrderMessage external_api_work_orders_create_work_order(work_order_post_message)

Create a work order

Creates a work order.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Work Orders</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.work_order_message import WorkOrderMessage
from buildium_sdk.models.work_order_post_message import WorkOrderPostMessage
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
    api_instance = buildium_sdk.WorkOrdersApi(api_client)
    work_order_post_message = buildium_sdk.WorkOrderPostMessage() # WorkOrderPostMessage | 

    try:
        # Create a work order
        api_response = await api_instance.external_api_work_orders_create_work_order(work_order_post_message)
        print("The response of WorkOrdersApi->external_api_work_orders_create_work_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkOrdersApi->external_api_work_orders_create_work_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_order_post_message** | [**WorkOrderPostMessage**](WorkOrderPostMessage.md)|  | 

### Return type

[**WorkOrderMessage**](WorkOrderMessage.md)

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

# **external_api_work_orders_get_all_work_orders**
> List[WorkOrderMessage] external_api_work_orders_get_all_work_orders(entitytype=entitytype, entityid=entityid, statuses=statuses, type=type, unitid=unitid, unitagreementid=unitagreementid, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, duedatefrom=duedatefrom, duedateto=duedateto, taskcategoryid=taskcategoryid, priorities=priorities, assignedtoid=assignedtoid, vendorids=vendorids, amountfrom=amountfrom, amountto=amountto, isbilled=isbilled, title=title, taskids=taskids, orderby=orderby, offset=offset, limit=limit)

Retrieve all work orders

Retrieves a list of work orders.


<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Work Orders</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.work_order_message import WorkOrderMessage
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
    api_instance = buildium_sdk.WorkOrdersApi(api_client)
    entitytype = 'entitytype_example' # str | Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is populated. (optional)
    entityid = 56 # int | Filters results to any work order associated with the specified entity id value. The value must be of the type specified in the `EntityType` field. (optional)
    statuses = ['statuses_example'] # List[str] | Filters results by the status of the task associated with the work order. If no status is specified, work orders with any status will be returned. (optional)
    type = 'type_example' # str | Filters results to any work order with an associated task with the task type specified. (optional)
    unitid = 56 # int | Filters results to any work order associated with the unit identifier. (optional)
    unitagreementid = 56 # int | Filters results to any work order associated with the unit agreement identifier specified. (optional)
    lastupdatedfrom = '2013-10-20' # date | Filters results to any work orders were updated on or after the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    lastupdatedto = '2013-10-20' # date | Filters results to any work orders were updated on or before the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    duedatefrom = '2013-10-20' # date | Filters results to any work orders with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    duedateto = '2013-10-20' # date | Filters results to any work orders with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    taskcategoryid = 56 # int | Filters results to any work orders with the specified task category identifier. (optional)
    priorities = ['priorities_example'] # List[str] | Filters results to any work orders whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned. (optional)
    assignedtoid = 56 # int | Filters results to any work orders that have been assigned to the specified staff user identifier. (optional)
    vendorids = [56] # List[int] | Filters results to any work orders that have been assigned to the specified vendor identifier. (optional)
    amountfrom = 3.4 # float | Filters results to any work orders whose total amounts are equal or greater than the specified amount. (optional)
    amountto = 3.4 # float | Filters results to any work orders whose total amounts are equal or less than the specified amount. (optional)
    isbilled = True # bool | Filters results to work orders that have an associated bill. (optional)
    title = 'title_example' # str | Filters results to any work orders whose title *contains* the specified value. (optional)
    taskids = [56] # List[int] | Filters results to work orders that have an associated to a task in the specified list. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all work orders
        api_response = await api_instance.external_api_work_orders_get_all_work_orders(entitytype=entitytype, entityid=entityid, statuses=statuses, type=type, unitid=unitid, unitagreementid=unitagreementid, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, duedatefrom=duedatefrom, duedateto=duedateto, taskcategoryid=taskcategoryid, priorities=priorities, assignedtoid=assignedtoid, vendorids=vendorids, amountfrom=amountfrom, amountto=amountto, isbilled=isbilled, title=title, taskids=taskids, orderby=orderby, offset=offset, limit=limit)
        print("The response of WorkOrdersApi->external_api_work_orders_get_all_work_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkOrdersApi->external_api_work_orders_get_all_work_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitytype** | **str**| Specifies the type of entity that the &#x60;EntityId&#x60; field refers to. This field is required if the &#x60;EntityId&#x60; field is populated. | [optional] 
 **entityid** | **int**| Filters results to any work order associated with the specified entity id value. The value must be of the type specified in the &#x60;EntityType&#x60; field. | [optional] 
 **statuses** | [**List[str]**](str.md)| Filters results by the status of the task associated with the work order. If no status is specified, work orders with any status will be returned. | [optional] 
 **type** | **str**| Filters results to any work order with an associated task with the task type specified. | [optional] 
 **unitid** | **int**| Filters results to any work order associated with the unit identifier. | [optional] 
 **unitagreementid** | **int**| Filters results to any work order associated with the unit agreement identifier specified. | [optional] 
 **lastupdatedfrom** | **date**| Filters results to any work orders were updated on or after the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **lastupdatedto** | **date**| Filters results to any work orders were updated on or before the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **duedatefrom** | **date**| Filters results to any work orders with a due date on or after the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **duedateto** | **date**| Filters results to any work orders with a due date on or before the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **taskcategoryid** | **int**| Filters results to any work orders with the specified task category identifier. | [optional] 
 **priorities** | [**List[str]**](str.md)| Filters results to any work orders whose priority matches the specified values. If no priority is specified, tasks with any priority will be returned. | [optional] 
 **assignedtoid** | **int**| Filters results to any work orders that have been assigned to the specified staff user identifier. | [optional] 
 **vendorids** | [**List[int]**](int.md)| Filters results to any work orders that have been assigned to the specified vendor identifier. | [optional] 
 **amountfrom** | **float**| Filters results to any work orders whose total amounts are equal or greater than the specified amount. | [optional] 
 **amountto** | **float**| Filters results to any work orders whose total amounts are equal or less than the specified amount. | [optional] 
 **isbilled** | **bool**| Filters results to work orders that have an associated bill. | [optional] 
 **title** | **str**| Filters results to any work orders whose title *contains* the specified value. | [optional] 
 **taskids** | [**List[int]**](int.md)| Filters results to work orders that have an associated to a task in the specified list. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[WorkOrderMessage]**](WorkOrderMessage.md)

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

# **external_api_work_orders_get_work_order_by_id**
> WorkOrderMessage external_api_work_orders_get_work_order_by_id(work_order_id)

Retrieve a work order

Retrieves a specific work order.


<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Work Orders</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.work_order_message import WorkOrderMessage
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
    api_instance = buildium_sdk.WorkOrdersApi(api_client)
    work_order_id = 56 # int | 

    try:
        # Retrieve a work order
        api_response = await api_instance.external_api_work_orders_get_work_order_by_id(work_order_id)
        print("The response of WorkOrdersApi->external_api_work_orders_get_work_order_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkOrdersApi->external_api_work_orders_get_work_order_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_order_id** | **int**|  | 

### Return type

[**WorkOrderMessage**](WorkOrderMessage.md)

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

# **external_api_work_orders_update_work_order**
> WorkOrderMessage external_api_work_orders_update_work_order(work_order_id, work_order_put_message)

Update a work order

Updates a work order.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Work Orders</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.work_order_message import WorkOrderMessage
from buildium_sdk.models.work_order_put_message import WorkOrderPutMessage
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
    api_instance = buildium_sdk.WorkOrdersApi(api_client)
    work_order_id = 56 # int | 
    work_order_put_message = buildium_sdk.WorkOrderPutMessage() # WorkOrderPutMessage | 

    try:
        # Update a work order
        api_response = await api_instance.external_api_work_orders_update_work_order(work_order_id, work_order_put_message)
        print("The response of WorkOrdersApi->external_api_work_orders_update_work_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkOrdersApi->external_api_work_orders_update_work_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_order_id** | **int**|  | 
 **work_order_put_message** | [**WorkOrderPutMessage**](WorkOrderPutMessage.md)|  | 

### Return type

[**WorkOrderMessage**](WorkOrderMessage.md)

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

