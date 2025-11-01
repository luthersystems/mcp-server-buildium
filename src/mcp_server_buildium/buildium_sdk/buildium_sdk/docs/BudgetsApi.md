# buildium_sdk.BudgetsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_budgets_create_budget_async**](BudgetsApi.md#external_api_budgets_create_budget_async) | **POST** /v1/budgets | Create a budget
[**external_api_budgets_get_budget_by_id**](BudgetsApi.md#external_api_budgets_get_budget_by_id) | **GET** /v1/budgets/{budgetId} | Retrieve a budget
[**external_api_budgets_get_budgets**](BudgetsApi.md#external_api_budgets_get_budgets) | **GET** /v1/budgets | Retrieve all budgets
[**external_api_budgets_update_budget**](BudgetsApi.md#external_api_budgets_update_budget) | **PUT** /v1/budgets/{budgetId} | Update a budget


# **external_api_budgets_create_budget_async**
> BudgetMessage external_api_budgets_create_budget_async(budget_post_message)

Create a budget

Creates a budget.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Budgets</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.budget_message import BudgetMessage
from buildium_sdk.models.budget_post_message import BudgetPostMessage
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
    api_instance = buildium_sdk.BudgetsApi(api_client)
    budget_post_message = buildium_sdk.BudgetPostMessage() # BudgetPostMessage | 

    try:
        # Create a budget
        api_response = await api_instance.external_api_budgets_create_budget_async(budget_post_message)
        print("The response of BudgetsApi->external_api_budgets_create_budget_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->external_api_budgets_create_budget_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_post_message** | [**BudgetPostMessage**](BudgetPostMessage.md)|  | 

### Return type

[**BudgetMessage**](BudgetMessage.md)

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

# **external_api_budgets_get_budget_by_id**
> BudgetMessage external_api_budgets_get_budget_by_id(budget_id)

Retrieve a budget

Retrieves a budget.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Budgets</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.budget_message import BudgetMessage
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
    api_instance = buildium_sdk.BudgetsApi(api_client)
    budget_id = 56 # int | 

    try:
        # Retrieve a budget
        api_response = await api_instance.external_api_budgets_get_budget_by_id(budget_id)
        print("The response of BudgetsApi->external_api_budgets_get_budget_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->external_api_budgets_get_budget_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **int**|  | 

### Return type

[**BudgetMessage**](BudgetMessage.md)

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

# **external_api_budgets_get_budgets**
> List[BudgetMessage] external_api_budgets_get_budgets(propertyids=propertyids, fiscalyear=fiscalyear, name=name, orderby=orderby, offset=offset, limit=limit)

Retrieve all budgets

Retrieves all budgets.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Budgets</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.budget_message import BudgetMessage
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
    api_instance = buildium_sdk.BudgetsApi(api_client)
    propertyids = [56] # List[int] | Filters results to any budget associated to any of the specified set of property ids. (optional)
    fiscalyear = 56 # int | Filters results to any budgets that end in the given fiscal year. FiscalYear must be a positive number. (optional)
    name = 'name_example' # str | Filters results to any budgets whose name *contains* the specified value. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all budgets
        api_response = await api_instance.external_api_budgets_get_budgets(propertyids=propertyids, fiscalyear=fiscalyear, name=name, orderby=orderby, offset=offset, limit=limit)
        print("The response of BudgetsApi->external_api_budgets_get_budgets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->external_api_budgets_get_budgets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **propertyids** | [**List[int]**](int.md)| Filters results to any budget associated to any of the specified set of property ids. | [optional] 
 **fiscalyear** | **int**| Filters results to any budgets that end in the given fiscal year. FiscalYear must be a positive number. | [optional] 
 **name** | **str**| Filters results to any budgets whose name *contains* the specified value. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BudgetMessage]**](BudgetMessage.md)

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

# **external_api_budgets_update_budget**
> BudgetMessage external_api_budgets_update_budget(budget_id, budget_put_message)

Update a budget

Updates a budget.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Budgets</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.budget_message import BudgetMessage
from buildium_sdk.models.budget_put_message import BudgetPutMessage
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
    api_instance = buildium_sdk.BudgetsApi(api_client)
    budget_id = 56 # int | 
    budget_put_message = buildium_sdk.BudgetPutMessage() # BudgetPutMessage | 

    try:
        # Update a budget
        api_response = await api_instance.external_api_budgets_update_budget(budget_id, budget_put_message)
        print("The response of BudgetsApi->external_api_budgets_update_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->external_api_budgets_update_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **int**|  | 
 **budget_put_message** | [**BudgetPutMessage**](BudgetPutMessage.md)|  | 

### Return type

[**BudgetMessage**](BudgetMessage.md)

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

