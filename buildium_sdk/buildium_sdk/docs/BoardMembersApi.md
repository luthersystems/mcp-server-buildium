# buildium_sdk.BoardMembersApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_association_board_members_create_board_member**](BoardMembersApi.md#external_api_association_board_members_create_board_member) | **POST** /v1/associations/{associationId}/boardmembers | Create a board member
[**external_api_association_board_members_delete_board_member**](BoardMembersApi.md#external_api_association_board_members_delete_board_member) | **DELETE** /v1/associations/{associationId}/boardmembers/{boardMemberId} | Delete a board member
[**external_api_association_board_members_get_all_association_board_members**](BoardMembersApi.md#external_api_association_board_members_get_all_association_board_members) | **GET** /v1/associations/{associationId}/boardmembers | Retrieve all board members
[**external_api_association_board_members_get_association_board_member_by_id**](BoardMembersApi.md#external_api_association_board_members_get_association_board_member_by_id) | **GET** /v1/associations/{associationId}/boardmembers/{boardMemberId} | Retrieve a board member
[**external_api_association_board_members_update_board_member**](BoardMembersApi.md#external_api_association_board_members_update_board_member) | **PUT** /v1/associations/{associationId}/boardmembers/{boardMemberId} | Update a board member


# **external_api_association_board_members_create_board_member**
> AssociationBoardMemberMessage external_api_association_board_members_create_board_member(association_id, association_board_member_post_message)

Create a board member

Creates a board member for a given association.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_board_member_message import AssociationBoardMemberMessage
from buildium_sdk.models.association_board_member_post_message import AssociationBoardMemberPostMessage
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
    api_instance = buildium_sdk.BoardMembersApi(api_client)
    association_id = 56 # int | 
    association_board_member_post_message = buildium_sdk.AssociationBoardMemberPostMessage() # AssociationBoardMemberPostMessage | 

    try:
        # Create a board member
        api_response = await api_instance.external_api_association_board_members_create_board_member(association_id, association_board_member_post_message)
        print("The response of BoardMembersApi->external_api_association_board_members_create_board_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardMembersApi->external_api_association_board_members_create_board_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
 **association_board_member_post_message** | [**AssociationBoardMemberPostMessage**](AssociationBoardMemberPostMessage.md)|  | 

### Return type

[**AssociationBoardMemberMessage**](AssociationBoardMemberMessage.md)

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

# **external_api_association_board_members_delete_board_member**
> external_api_association_board_members_delete_board_member(association_id, board_member_id)

Delete a board member

Deletes a board member. Note, this is a hard delete from the database and data can not be restored. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View` `Edit` `Delete`

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
    api_instance = buildium_sdk.BoardMembersApi(api_client)
    association_id = 56 # int | 
    board_member_id = 56 # int | 

    try:
        # Delete a board member
        await api_instance.external_api_association_board_members_delete_board_member(association_id, board_member_id)
    except Exception as e:
        print("Exception when calling BoardMembersApi->external_api_association_board_members_delete_board_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
 **board_member_id** | **int**|  | 

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

# **external_api_association_board_members_get_all_association_board_members**
> List[AssociationBoardMemberMessage] external_api_association_board_members_get_all_association_board_members(association_id, statuses=statuses, boardpositiontypes=boardpositiontypes, createddatetimeto=createddatetimeto, createddatetimefrom=createddatetimefrom, orderby=orderby, offset=offset, limit=limit)

Retrieve all board members

Retrieves all association board members.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_board_member_message import AssociationBoardMemberMessage
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
    api_instance = buildium_sdk.BoardMembersApi(api_client)
    association_id = 56 # int | 
    statuses = ['statuses_example'] # List[str] | Filters results to only records whose status is equal to the specified values. (optional)
    boardpositiontypes = ['boardpositiontypes_example'] # List[str] | Filters results to only records whose board position type is equal to the specified values. (optional)
    createddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only records that were created before this date. Must be formatted as `YYYY-MM-DD`. (optional)
    createddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only records that were created after this date. Must be formatted as `YYYY-MM-DD`. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all board members
        api_response = await api_instance.external_api_association_board_members_get_all_association_board_members(association_id, statuses=statuses, boardpositiontypes=boardpositiontypes, createddatetimeto=createddatetimeto, createddatetimefrom=createddatetimefrom, orderby=orderby, offset=offset, limit=limit)
        print("The response of BoardMembersApi->external_api_association_board_members_get_all_association_board_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardMembersApi->external_api_association_board_members_get_all_association_board_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
 **statuses** | [**List[str]**](str.md)| Filters results to only records whose status is equal to the specified values. | [optional] 
 **boardpositiontypes** | [**List[str]**](str.md)| Filters results to only records whose board position type is equal to the specified values. | [optional] 
 **createddatetimeto** | **datetime**| Filters results to only records that were created before this date. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
 **createddatetimefrom** | **datetime**| Filters results to only records that were created after this date. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[AssociationBoardMemberMessage]**](AssociationBoardMemberMessage.md)

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

# **external_api_association_board_members_get_association_board_member_by_id**
> AssociationBoardMemberMessage external_api_association_board_members_get_association_board_member_by_id(association_id, board_member_id)

Retrieve a board member

Retrieves an association board member.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_board_member_message import AssociationBoardMemberMessage
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
    api_instance = buildium_sdk.BoardMembersApi(api_client)
    association_id = 56 # int | 
    board_member_id = 56 # int | 

    try:
        # Retrieve a board member
        api_response = await api_instance.external_api_association_board_members_get_association_board_member_by_id(association_id, board_member_id)
        print("The response of BoardMembersApi->external_api_association_board_members_get_association_board_member_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardMembersApi->external_api_association_board_members_get_association_board_member_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
 **board_member_id** | **int**|  | 

### Return type

[**AssociationBoardMemberMessage**](AssociationBoardMemberMessage.md)

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

# **external_api_association_board_members_update_board_member**
> AssociationBoardMemberMessage external_api_association_board_members_update_board_member(association_id, board_member_id, association_board_member_put_message)

Update a board member

Updates a board member for a given association.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Association owners and tenants</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.association_board_member_message import AssociationBoardMemberMessage
from buildium_sdk.models.association_board_member_put_message import AssociationBoardMemberPutMessage
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
    api_instance = buildium_sdk.BoardMembersApi(api_client)
    association_id = 56 # int | 
    board_member_id = 56 # int | 
    association_board_member_put_message = buildium_sdk.AssociationBoardMemberPutMessage() # AssociationBoardMemberPutMessage | 

    try:
        # Update a board member
        api_response = await api_instance.external_api_association_board_members_update_board_member(association_id, board_member_id, association_board_member_put_message)
        print("The response of BoardMembersApi->external_api_association_board_members_update_board_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardMembersApi->external_api_association_board_members_update_board_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
 **board_member_id** | **int**|  | 
 **association_board_member_put_message** | [**AssociationBoardMemberPutMessage**](AssociationBoardMemberPutMessage.md)|  | 

### Return type

[**AssociationBoardMemberMessage**](AssociationBoardMemberMessage.md)

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

