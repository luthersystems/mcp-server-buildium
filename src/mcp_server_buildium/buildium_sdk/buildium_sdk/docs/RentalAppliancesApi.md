# buildium_sdk.RentalAppliancesApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_rental_appliance_service_history_create_rental_appliance_service_history**](RentalAppliancesApi.md#external_api_rental_appliance_service_history_create_rental_appliance_service_history) | **POST** /v1/rentals/appliances/{applianceId}/servicehistory | Create a service history
[**external_api_rental_appliance_service_history_get_rental_appliance_service_history**](RentalAppliancesApi.md#external_api_rental_appliance_service_history_get_rental_appliance_service_history) | **GET** /v1/rentals/appliances/{applianceId}/servicehistory | Retrieve all service history
[**external_api_rental_appliance_service_history_get_rental_appliance_service_history_by_id**](RentalAppliancesApi.md#external_api_rental_appliance_service_history_get_rental_appliance_service_history_by_id) | **GET** /v1/rentals/appliances/{applianceId}/servicehistory/{serviceHistoryId} | Retrieve a service history
[**external_api_rental_appliances_create_rental_appliance**](RentalAppliancesApi.md#external_api_rental_appliances_create_rental_appliance) | **POST** /v1/rentals/appliances | Create an appliance
[**external_api_rental_appliances_delete_rental_appliances**](RentalAppliancesApi.md#external_api_rental_appliances_delete_rental_appliances) | **DELETE** /v1/rentals/appliances/{applianceId} | Delete an appliance
[**external_api_rental_appliances_get_rental_appliance_by_id**](RentalAppliancesApi.md#external_api_rental_appliances_get_rental_appliance_by_id) | **GET** /v1/rentals/appliances/{applianceId} | Retrieve an appliance
[**external_api_rental_appliances_get_rental_appliances**](RentalAppliancesApi.md#external_api_rental_appliances_get_rental_appliances) | **GET** /v1/rentals/appliances | Retrieve all appliances
[**external_api_rental_appliances_update_rental_appliance**](RentalAppliancesApi.md#external_api_rental_appliances_update_rental_appliance) | **PUT** /v1/rentals/appliances/{applianceId} | Update an appliance


# **external_api_rental_appliance_service_history_create_rental_appliance_service_history**
> RentalApplianceServiceHistoryMessage external_api_rental_appliance_service_history_create_rental_appliance_service_history(appliance_id, rental_appliance_service_history_post_message)

Create a service history

Creates a service history record for an appliance.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_appliance_service_history_message import RentalApplianceServiceHistoryMessage
from buildium_sdk.models.rental_appliance_service_history_post_message import RentalApplianceServiceHistoryPostMessage
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
    api_instance = buildium_sdk.RentalAppliancesApi(api_client)
    appliance_id = 56 # int | 
    rental_appliance_service_history_post_message = buildium_sdk.RentalApplianceServiceHistoryPostMessage() # RentalApplianceServiceHistoryPostMessage | 

    try:
        # Create a service history
        api_response = await api_instance.external_api_rental_appliance_service_history_create_rental_appliance_service_history(appliance_id, rental_appliance_service_history_post_message)
        print("The response of RentalAppliancesApi->external_api_rental_appliance_service_history_create_rental_appliance_service_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalAppliancesApi->external_api_rental_appliance_service_history_create_rental_appliance_service_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_id** | **int**|  | 
 **rental_appliance_service_history_post_message** | [**RentalApplianceServiceHistoryPostMessage**](RentalApplianceServiceHistoryPostMessage.md)|  | 

### Return type

[**RentalApplianceServiceHistoryMessage**](RentalApplianceServiceHistoryMessage.md)

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

# **external_api_rental_appliance_service_history_get_rental_appliance_service_history**
> List[RentalApplianceServiceHistoryMessage] external_api_rental_appliance_service_history_get_rental_appliance_service_history(appliance_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all service history

Retrieves all of the service history records for an appliance.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_appliance_service_history_message import RentalApplianceServiceHistoryMessage
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
    api_instance = buildium_sdk.RentalAppliancesApi(api_client)
    appliance_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all service history
        api_response = await api_instance.external_api_rental_appliance_service_history_get_rental_appliance_service_history(appliance_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of RentalAppliancesApi->external_api_rental_appliance_service_history_get_rental_appliance_service_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalAppliancesApi->external_api_rental_appliance_service_history_get_rental_appliance_service_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[RentalApplianceServiceHistoryMessage]**](RentalApplianceServiceHistoryMessage.md)

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

# **external_api_rental_appliance_service_history_get_rental_appliance_service_history_by_id**
> RentalApplianceServiceHistoryMessage external_api_rental_appliance_service_history_get_rental_appliance_service_history_by_id(appliance_id, service_history_id)

Retrieve a service history

Retrieves a specific service history record for a given appliance.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_appliance_service_history_message import RentalApplianceServiceHistoryMessage
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
    api_instance = buildium_sdk.RentalAppliancesApi(api_client)
    appliance_id = 56 # int | 
    service_history_id = 56 # int | 

    try:
        # Retrieve a service history
        api_response = await api_instance.external_api_rental_appliance_service_history_get_rental_appliance_service_history_by_id(appliance_id, service_history_id)
        print("The response of RentalAppliancesApi->external_api_rental_appliance_service_history_get_rental_appliance_service_history_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalAppliancesApi->external_api_rental_appliance_service_history_get_rental_appliance_service_history_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_id** | **int**|  | 
 **service_history_id** | **int**|  | 

### Return type

[**RentalApplianceServiceHistoryMessage**](RentalApplianceServiceHistoryMessage.md)

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

# **external_api_rental_appliances_create_rental_appliance**
> RentalApplianceMessage external_api_rental_appliances_create_rental_appliance(rental_appliance_post_message)

Create an appliance

Creates a rental property appliance.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_appliance_message import RentalApplianceMessage
from buildium_sdk.models.rental_appliance_post_message import RentalAppliancePostMessage
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
    api_instance = buildium_sdk.RentalAppliancesApi(api_client)
    rental_appliance_post_message = buildium_sdk.RentalAppliancePostMessage() # RentalAppliancePostMessage | 

    try:
        # Create an appliance
        api_response = await api_instance.external_api_rental_appliances_create_rental_appliance(rental_appliance_post_message)
        print("The response of RentalAppliancesApi->external_api_rental_appliances_create_rental_appliance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalAppliancesApi->external_api_rental_appliances_create_rental_appliance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_appliance_post_message** | [**RentalAppliancePostMessage**](RentalAppliancePostMessage.md)|  | 

### Return type

[**RentalApplianceMessage**](RentalApplianceMessage.md)

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

# **external_api_rental_appliances_delete_rental_appliances**
> external_api_rental_appliances_delete_rental_appliances(appliance_id)

Delete an appliance

Deletes an appliance.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

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
    api_instance = buildium_sdk.RentalAppliancesApi(api_client)
    appliance_id = 56 # int | 

    try:
        # Delete an appliance
        await api_instance.external_api_rental_appliances_delete_rental_appliances(appliance_id)
    except Exception as e:
        print("Exception when calling RentalAppliancesApi->external_api_rental_appliances_delete_rental_appliances: %s\n" % e)
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

# **external_api_rental_appliances_get_rental_appliance_by_id**
> RentalApplianceMessage external_api_rental_appliances_get_rental_appliance_by_id(appliance_id)

Retrieve an appliance

Retrieves a rental appliance.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_appliance_message import RentalApplianceMessage
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
    api_instance = buildium_sdk.RentalAppliancesApi(api_client)
    appliance_id = 56 # int | 

    try:
        # Retrieve an appliance
        api_response = await api_instance.external_api_rental_appliances_get_rental_appliance_by_id(appliance_id)
        print("The response of RentalAppliancesApi->external_api_rental_appliances_get_rental_appliance_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalAppliancesApi->external_api_rental_appliances_get_rental_appliance_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_id** | **int**|  | 

### Return type

[**RentalApplianceMessage**](RentalApplianceMessage.md)

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

# **external_api_rental_appliances_get_rental_appliances**
> List[RentalApplianceMessage] external_api_rental_appliances_get_rental_appliances(propertyids=propertyids, unitids=unitids, orderby=orderby, offset=offset, limit=limit)

Retrieve all appliances

Retrieves all rental appliances.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_appliance_message import RentalApplianceMessage
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
    api_instance = buildium_sdk.RentalAppliancesApi(api_client)
    propertyids = [56] # List[int] | Filters results to appliances associated to any of the specified rental property identifiers. (optional)
    unitids = [56] # List[int] | Filters results to appliances associated to any of the specified rental unit identifiers. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all appliances
        api_response = await api_instance.external_api_rental_appliances_get_rental_appliances(propertyids=propertyids, unitids=unitids, orderby=orderby, offset=offset, limit=limit)
        print("The response of RentalAppliancesApi->external_api_rental_appliances_get_rental_appliances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalAppliancesApi->external_api_rental_appliances_get_rental_appliances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **propertyids** | [**List[int]**](int.md)| Filters results to appliances associated to any of the specified rental property identifiers. | [optional] 
 **unitids** | [**List[int]**](int.md)| Filters results to appliances associated to any of the specified rental unit identifiers. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[RentalApplianceMessage]**](RentalApplianceMessage.md)

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

# **external_api_rental_appliances_update_rental_appliance**
> RentalApplianceMessage external_api_rental_appliances_update_rental_appliance(appliance_id, rental_appliance_put_message)

Update an appliance

Updates a rental appliance.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_appliance_message import RentalApplianceMessage
from buildium_sdk.models.rental_appliance_put_message import RentalAppliancePutMessage
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
    api_instance = buildium_sdk.RentalAppliancesApi(api_client)
    appliance_id = 56 # int | 
    rental_appliance_put_message = buildium_sdk.RentalAppliancePutMessage() # RentalAppliancePutMessage | 

    try:
        # Update an appliance
        api_response = await api_instance.external_api_rental_appliances_update_rental_appliance(appliance_id, rental_appliance_put_message)
        print("The response of RentalAppliancesApi->external_api_rental_appliances_update_rental_appliance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalAppliancesApi->external_api_rental_appliances_update_rental_appliance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_id** | **int**|  | 
 **rental_appliance_put_message** | [**RentalAppliancePutMessage**](RentalAppliancePutMessage.md)|  | 

### Return type

[**RentalApplianceMessage**](RentalApplianceMessage.md)

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

