# buildium_sdk.AppliancesApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_association_appliance_service_history_create_association_appliance_service_history**](AppliancesApi.md#external_api_association_appliance_service_history_create_association_appliance_service_history) | **POST** /v1/associations/appliances/{applianceId}/servicehistory | Create a service history
[**external_api_association_appliance_service_history_get_all_association_appliance_service_history**](AppliancesApi.md#external_api_association_appliance_service_history_get_all_association_appliance_service_history) | **GET** /v1/associations/appliances/{applianceId}/servicehistory | Retrieve all service history
[**external_api_association_appliance_service_history_get_association_appliance_service_history_by_id**](AppliancesApi.md#external_api_association_appliance_service_history_get_association_appliance_service_history_by_id) | **GET** /v1/associations/appliances/{applianceId}/servicehistory/{serviceHistoryId} | Retrieve a service history
[**external_api_association_appliances_create_association_appliance**](AppliancesApi.md#external_api_association_appliances_create_association_appliance) | **POST** /v1/associations/appliances | Create an appliance
[**external_api_association_appliances_delete_association_appliances**](AppliancesApi.md#external_api_association_appliances_delete_association_appliances) | **DELETE** /v1/associations/appliances/{applianceId} | Delete an appliance
[**external_api_association_appliances_get_association_appliance_by_id**](AppliancesApi.md#external_api_association_appliances_get_association_appliance_by_id) | **GET** /v1/associations/appliances/{applianceId} | Retrieve an appliance
[**external_api_association_appliances_get_association_appliances**](AppliancesApi.md#external_api_association_appliances_get_association_appliances) | **GET** /v1/associations/appliances | Retrieve all appliances
[**external_api_association_appliances_update_association_appliance**](AppliancesApi.md#external_api_association_appliances_update_association_appliance) | **PUT** /v1/associations/appliances/{applianceId} | Update an appliance


# **external_api_association_appliance_service_history_create_association_appliance_service_history**
> AssociationApplianceServiceHistoryMessage external_api_association_appliance_service_history_create_association_appliance_service_history(appliance_id, association_appliance_service_history_post_message)

Create a service history

Creates a service history for an appliance.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_appliance_service_history_message import AssociationApplianceServiceHistoryMessage
from buildium_sdk.models.association_appliance_service_history_post_message import AssociationApplianceServiceHistoryPostMessage
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
    api_instance = buildium_sdk.AppliancesApi(api_client)
    appliance_id = 56 # int | 
    association_appliance_service_history_post_message = buildium_sdk.AssociationApplianceServiceHistoryPostMessage() # AssociationApplianceServiceHistoryPostMessage | 

    try:
        # Create a service history
        api_response = await api_instance.external_api_association_appliance_service_history_create_association_appliance_service_history(appliance_id, association_appliance_service_history_post_message)
        print("The response of AppliancesApi->external_api_association_appliance_service_history_create_association_appliance_service_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppliancesApi->external_api_association_appliance_service_history_create_association_appliance_service_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_id** | **int**|  | 
 **association_appliance_service_history_post_message** | [**AssociationApplianceServiceHistoryPostMessage**](AssociationApplianceServiceHistoryPostMessage.md)|  | 

### Return type

[**AssociationApplianceServiceHistoryMessage**](AssociationApplianceServiceHistoryMessage.md)

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

# **external_api_association_appliance_service_history_get_all_association_appliance_service_history**
> List[AssociationApplianceServiceHistoryMessage] external_api_association_appliance_service_history_get_all_association_appliance_service_history(appliance_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all service history

Retrieves all of the service history records for an appliance.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_appliance_service_history_message import AssociationApplianceServiceHistoryMessage
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
    api_instance = buildium_sdk.AppliancesApi(api_client)
    appliance_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all service history
        api_response = await api_instance.external_api_association_appliance_service_history_get_all_association_appliance_service_history(appliance_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of AppliancesApi->external_api_association_appliance_service_history_get_all_association_appliance_service_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppliancesApi->external_api_association_appliance_service_history_get_all_association_appliance_service_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[AssociationApplianceServiceHistoryMessage]**](AssociationApplianceServiceHistoryMessage.md)

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

# **external_api_association_appliance_service_history_get_association_appliance_service_history_by_id**
> AssociationApplianceServiceHistoryMessage external_api_association_appliance_service_history_get_association_appliance_service_history_by_id(appliance_id, service_history_id)

Retrieve a service history

Retrieves a specific service history record for a given appliance.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_appliance_service_history_message import AssociationApplianceServiceHistoryMessage
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
    api_instance = buildium_sdk.AppliancesApi(api_client)
    appliance_id = 56 # int | 
    service_history_id = 56 # int | 

    try:
        # Retrieve a service history
        api_response = await api_instance.external_api_association_appliance_service_history_get_association_appliance_service_history_by_id(appliance_id, service_history_id)
        print("The response of AppliancesApi->external_api_association_appliance_service_history_get_association_appliance_service_history_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppliancesApi->external_api_association_appliance_service_history_get_association_appliance_service_history_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_id** | **int**|  | 
 **service_history_id** | **int**|  | 

### Return type

[**AssociationApplianceServiceHistoryMessage**](AssociationApplianceServiceHistoryMessage.md)

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

# **external_api_association_appliances_create_association_appliance**
> AssociationApplianceMessage external_api_association_appliances_create_association_appliance(association_appliance_post_message)

Create an appliance

Creates an association appliance.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_appliance_message import AssociationApplianceMessage
from buildium_sdk.models.association_appliance_post_message import AssociationAppliancePostMessage
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
    api_instance = buildium_sdk.AppliancesApi(api_client)
    association_appliance_post_message = buildium_sdk.AssociationAppliancePostMessage() # AssociationAppliancePostMessage | 

    try:
        # Create an appliance
        api_response = await api_instance.external_api_association_appliances_create_association_appliance(association_appliance_post_message)
        print("The response of AppliancesApi->external_api_association_appliances_create_association_appliance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppliancesApi->external_api_association_appliances_create_association_appliance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_appliance_post_message** | [**AssociationAppliancePostMessage**](AssociationAppliancePostMessage.md)|  | 

### Return type

[**AssociationApplianceMessage**](AssociationApplianceMessage.md)

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

# **external_api_association_appliances_delete_association_appliances**
> external_api_association_appliances_delete_association_appliances(appliance_id)

Delete an appliance

Deletes an associations appliance.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

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
    api_instance = buildium_sdk.AppliancesApi(api_client)
    appliance_id = 56 # int | 

    try:
        # Delete an appliance
        await api_instance.external_api_association_appliances_delete_association_appliances(appliance_id)
    except Exception as e:
        print("Exception when calling AppliancesApi->external_api_association_appliances_delete_association_appliances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_id** | **int**|  | 

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

# **external_api_association_appliances_get_association_appliance_by_id**
> AssociationApplianceMessage external_api_association_appliances_get_association_appliance_by_id(appliance_id)

Retrieve an appliance

Retrieves an association appliance by id.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_appliance_message import AssociationApplianceMessage
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
    api_instance = buildium_sdk.AppliancesApi(api_client)
    appliance_id = 56 # int | 

    try:
        # Retrieve an appliance
        api_response = await api_instance.external_api_association_appliances_get_association_appliance_by_id(appliance_id)
        print("The response of AppliancesApi->external_api_association_appliances_get_association_appliance_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppliancesApi->external_api_association_appliances_get_association_appliance_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_id** | **int**|  | 

### Return type

[**AssociationApplianceMessage**](AssociationApplianceMessage.md)

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

# **external_api_association_appliances_get_association_appliances**
> List[AssociationApplianceMessage] external_api_association_appliances_get_association_appliances(associationids=associationids, unitids=unitids, orderby=orderby, offset=offset, limit=limit)

Retrieve all appliances

Retrieves all association appliances.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_appliance_message import AssociationApplianceMessage
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
    api_instance = buildium_sdk.AppliancesApi(api_client)
    associationids = [56] # List[int] | Filters results to appliances associated to any of the specified association identifiers. (optional)
    unitids = [56] # List[int] | Filters results to appliances associated to any of the specified association unit identifiers. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all appliances
        api_response = await api_instance.external_api_association_appliances_get_association_appliances(associationids=associationids, unitids=unitids, orderby=orderby, offset=offset, limit=limit)
        print("The response of AppliancesApi->external_api_association_appliances_get_association_appliances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppliancesApi->external_api_association_appliances_get_association_appliances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **associationids** | [**List[int]**](int.md)| Filters results to appliances associated to any of the specified association identifiers. | [optional] 
 **unitids** | [**List[int]**](int.md)| Filters results to appliances associated to any of the specified association unit identifiers. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[AssociationApplianceMessage]**](AssociationApplianceMessage.md)

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

# **external_api_association_appliances_update_association_appliance**
> AssociationApplianceMessage external_api_association_appliances_update_association_appliance(appliance_id, association_appliance_put_message)

Update an appliance

Updates an association appliance.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_appliance_message import AssociationApplianceMessage
from buildium_sdk.models.association_appliance_put_message import AssociationAppliancePutMessage
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
    api_instance = buildium_sdk.AppliancesApi(api_client)
    appliance_id = 56 # int | 
    association_appliance_put_message = buildium_sdk.AssociationAppliancePutMessage() # AssociationAppliancePutMessage | 

    try:
        # Update an appliance
        api_response = await api_instance.external_api_association_appliances_update_association_appliance(appliance_id, association_appliance_put_message)
        print("The response of AppliancesApi->external_api_association_appliances_update_association_appliance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppliancesApi->external_api_association_appliances_update_association_appliance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_id** | **int**|  | 
 **association_appliance_put_message** | [**AssociationAppliancePutMessage**](AssociationAppliancePutMessage.md)|  | 

### Return type

[**AssociationApplianceMessage**](AssociationApplianceMessage.md)

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

