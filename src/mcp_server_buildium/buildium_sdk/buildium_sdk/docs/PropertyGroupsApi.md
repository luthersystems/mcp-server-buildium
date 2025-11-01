# buildium_sdk.PropertyGroupsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_property_groups_create_property_group**](PropertyGroupsApi.md#external_api_property_groups_create_property_group) | **POST** /v1/propertygroups | Create a property group
[**external_api_property_groups_get_property_group_by_id**](PropertyGroupsApi.md#external_api_property_groups_get_property_group_by_id) | **GET** /v1/propertygroups/{propertyGroupId} | Retrieve a property group
[**external_api_property_groups_get_property_groups**](PropertyGroupsApi.md#external_api_property_groups_get_property_groups) | **GET** /v1/propertygroups | Retrieve all property groups
[**external_api_property_groups_update_property_group**](PropertyGroupsApi.md#external_api_property_groups_update_property_group) | **PUT** /v1/propertygroups/{propertyGroupId} | Update a property group


# **external_api_property_groups_create_property_group**
> PropertyGroupMessage external_api_property_groups_create_property_group(property_group_post_message)

Create a property group

Creates a property group.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units or</span> - `View` `Edit`
            <span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.property_group_message import PropertyGroupMessage
from buildium_sdk.models.property_group_post_message import PropertyGroupPostMessage
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
    api_instance = buildium_sdk.PropertyGroupsApi(api_client)
    property_group_post_message = buildium_sdk.PropertyGroupPostMessage() # PropertyGroupPostMessage | 

    try:
        # Create a property group
        api_response = await api_instance.external_api_property_groups_create_property_group(property_group_post_message)
        print("The response of PropertyGroupsApi->external_api_property_groups_create_property_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyGroupsApi->external_api_property_groups_create_property_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_group_post_message** | [**PropertyGroupPostMessage**](PropertyGroupPostMessage.md)|  | 

### Return type

[**PropertyGroupMessage**](PropertyGroupMessage.md)

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

# **external_api_property_groups_get_property_group_by_id**
> PropertyGroupMessage external_api_property_groups_get_property_group_by_id(property_group_id)

Retrieve a property group

Retrieves a property group.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units or</span> - `View`
            <span class="permissionBlock">Associations > Associations and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.property_group_message import PropertyGroupMessage
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
    api_instance = buildium_sdk.PropertyGroupsApi(api_client)
    property_group_id = 56 # int | 

    try:
        # Retrieve a property group
        api_response = await api_instance.external_api_property_groups_get_property_group_by_id(property_group_id)
        print("The response of PropertyGroupsApi->external_api_property_groups_get_property_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyGroupsApi->external_api_property_groups_get_property_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_group_id** | **int**|  | 

### Return type

[**PropertyGroupMessage**](PropertyGroupMessage.md)

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

# **external_api_property_groups_get_property_groups**
> List[PropertyGroupMessage] external_api_property_groups_get_property_groups(propertyids=propertyids, nameordescription=nameordescription, orderby=orderby, offset=offset, limit=limit)

Retrieve all property groups

Retrieves all property groups.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units or</span> - `View`
            
<span class="permissionBlock">Associations > Associations and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.property_group_message import PropertyGroupMessage
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
    api_instance = buildium_sdk.PropertyGroupsApi(api_client)
    propertyids = [56] # List[int] | Filters results to property groups that contain any of the specified property ids. (optional)
    nameordescription = 'nameordescription_example' # str | Filters results to any property group whose name or description contains the specified value. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all property groups
        api_response = await api_instance.external_api_property_groups_get_property_groups(propertyids=propertyids, nameordescription=nameordescription, orderby=orderby, offset=offset, limit=limit)
        print("The response of PropertyGroupsApi->external_api_property_groups_get_property_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyGroupsApi->external_api_property_groups_get_property_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **propertyids** | [**List[int]**](int.md)| Filters results to property groups that contain any of the specified property ids. | [optional] 
 **nameordescription** | **str**| Filters results to any property group whose name or description contains the specified value. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[PropertyGroupMessage]**](PropertyGroupMessage.md)

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

# **external_api_property_groups_update_property_group**
> PropertyGroupMessage external_api_property_groups_update_property_group(property_group_id, property_group_put_message)

Update a property group

Updates a property group. A property group can only be updated by the user that created it.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units or</span> - `View` `Edit`
            <span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.property_group_message import PropertyGroupMessage
from buildium_sdk.models.property_group_put_message import PropertyGroupPutMessage
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
    api_instance = buildium_sdk.PropertyGroupsApi(api_client)
    property_group_id = 56 # int | 
    property_group_put_message = buildium_sdk.PropertyGroupPutMessage() # PropertyGroupPutMessage | 

    try:
        # Update a property group
        api_response = await api_instance.external_api_property_groups_update_property_group(property_group_id, property_group_put_message)
        print("The response of PropertyGroupsApi->external_api_property_groups_update_property_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyGroupsApi->external_api_property_groups_update_property_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_group_id** | **int**|  | 
 **property_group_put_message** | [**PropertyGroupPutMessage**](PropertyGroupPutMessage.md)|  | 

### Return type

[**PropertyGroupMessage**](PropertyGroupMessage.md)

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

