# buildium_sdk.ResidentCenterApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_resident_center_users_get_resident_center_users**](ResidentCenterApi.md#external_api_resident_center_users_get_resident_center_users) | **GET** /v1/residentCenterUsers | Retrieve all resident center users
[**external_api_retail_cash_read_get_retail_cash_user**](ResidentCenterApi.md#external_api_retail_cash_read_get_retail_cash_user) | **GET** /v1/retailcashusers/{userId}/{unitAgreementId} | Retrieve a retail cash user
[**external_api_retail_cash_read_get_retail_cash_users**](ResidentCenterApi.md#external_api_retail_cash_read_get_retail_cash_users) | **GET** /v1/retailcashusers | Retrieve all retail cash users
[**external_api_retail_cash_write_update_retail_cash_user**](ResidentCenterApi.md#external_api_retail_cash_write_update_retail_cash_user) | **PUT** /v1/retailcashusers/{userId}/{unitAgreementId} | Update a retail cash user


# **external_api_resident_center_users_get_resident_center_users**
> List[ResidentCenterUserMessage] external_api_resident_center_users_get_resident_center_users(unitagreementids=unitagreementids, userids=userids, usertypes=usertypes, residentcenteruserstatuses=residentcenteruserstatuses, isautopayenabled=isautopayenabled, orderby=orderby, offset=offset, limit=limit)

Retrieve all resident center users

Retrieves all resident center users for both rentals and associations.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Resident Center Users</span> - `View`
            
<span class="permissionBlock">Rentals > Tenants</span> - `View` is required to retrieve resident center users that are tenants.
            
<span class="permissionBlock">Associations > Association owners and tenants</span> - `View` is required to retrieve resident center users that are association owners.

### Example


```python
import buildium_sdk
from buildium_sdk.models.resident_center_user_message import ResidentCenterUserMessage
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
    api_instance = buildium_sdk.ResidentCenterApi(api_client)
    unitagreementids = [56] # List[int] | Filters results to any resident center user who is associated with the specified lease and/or association ownership account identifiers. (optional)
    userids = [56] # List[int] | Filters results to any resident center user with the specified tenant and/or association owner identifiers. (optional)
    usertypes = ['usertypes_example'] # List[str] | Filters results to any resident center user with the specified types. (optional)
    residentcenteruserstatuses = ['residentcenteruserstatuses_example'] # List[str] | Filters results to any resident center user with the specified resident center user statuses. (optional)
    isautopayenabled = True # bool | If true, filters results to any resident center users who have automatic payments scheduled for the future. If false, filters results to any resident center users  who do not have automatic payments scheduled for the future. If not provided, will not filter results based on automatic payments. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all resident center users
        api_response = await api_instance.external_api_resident_center_users_get_resident_center_users(unitagreementids=unitagreementids, userids=userids, usertypes=usertypes, residentcenteruserstatuses=residentcenteruserstatuses, isautopayenabled=isautopayenabled, orderby=orderby, offset=offset, limit=limit)
        print("The response of ResidentCenterApi->external_api_resident_center_users_get_resident_center_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResidentCenterApi->external_api_resident_center_users_get_resident_center_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unitagreementids** | [**List[int]**](int.md)| Filters results to any resident center user who is associated with the specified lease and/or association ownership account identifiers. | [optional] 
 **userids** | [**List[int]**](int.md)| Filters results to any resident center user with the specified tenant and/or association owner identifiers. | [optional] 
 **usertypes** | [**List[str]**](str.md)| Filters results to any resident center user with the specified types. | [optional] 
 **residentcenteruserstatuses** | [**List[str]**](str.md)| Filters results to any resident center user with the specified resident center user statuses. | [optional] 
 **isautopayenabled** | **bool**| If true, filters results to any resident center users who have automatic payments scheduled for the future. If false, filters results to any resident center users  who do not have automatic payments scheduled for the future. If not provided, will not filter results based on automatic payments. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[ResidentCenterUserMessage]**](ResidentCenterUserMessage.md)

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

# **external_api_retail_cash_read_get_retail_cash_user**
> RetailCashUserMessage external_api_retail_cash_read_get_retail_cash_user(user_id, unit_agreement_id)

Retrieve a retail cash user

Retrieves a retail cash user.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Tenants</span> - `View`
            OR
            <span class="permissionBlock"> Associations > Association owners and tenants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.retail_cash_user_message import RetailCashUserMessage
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
    api_instance = buildium_sdk.ResidentCenterApi(api_client)
    user_id = 56 # int | 
    unit_agreement_id = 56 # int | 

    try:
        # Retrieve a retail cash user
        api_response = await api_instance.external_api_retail_cash_read_get_retail_cash_user(user_id, unit_agreement_id)
        print("The response of ResidentCenterApi->external_api_retail_cash_read_get_retail_cash_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResidentCenterApi->external_api_retail_cash_read_get_retail_cash_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **unit_agreement_id** | **int**|  | 

### Return type

[**RetailCashUserMessage**](RetailCashUserMessage.md)

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

# **external_api_retail_cash_read_get_retail_cash_users**
> List[RetailCashUserMessage] external_api_retail_cash_read_get_retail_cash_users(entityid=entityid, entitytype=entitytype, statuses=statuses, name=name, unitaddress=unitaddress, isaccountcreated=isaccountcreated, orderby=orderby, offset=offset, limit=limit)

Retrieve all retail cash users

Retrieves all retail cash users.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Tenants</span> - `View`
            OR
            <span class="permissionBlock"> Associations > Association owners and tenants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.retail_cash_user_message import RetailCashUserMessage
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
    api_instance = buildium_sdk.ResidentCenterApi(api_client)
    entityid = 56 # int | Filters results to any users associated with the specified entity id value. The value must be of the type specified in the `EntityType` field. (optional)
    entitytype = 'entitytype_example' # str | Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is provided. (optional)
    statuses = ['statuses_example'] # List[str] | Filters results to any users whose lease is in one of the provided statuses. (optional)
    name = 'name_example' # str | Filters results to any users whose name *contains* the specified value. (optional)
    unitaddress = 'unitaddress_example' # str | Filters results to any users whose unit address *contains* the specified value. (optional)
    isaccountcreated = True # bool | Filters results to any users whose retail cash account is created. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all retail cash users
        api_response = await api_instance.external_api_retail_cash_read_get_retail_cash_users(entityid=entityid, entitytype=entitytype, statuses=statuses, name=name, unitaddress=unitaddress, isaccountcreated=isaccountcreated, orderby=orderby, offset=offset, limit=limit)
        print("The response of ResidentCenterApi->external_api_retail_cash_read_get_retail_cash_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResidentCenterApi->external_api_retail_cash_read_get_retail_cash_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entityid** | **int**| Filters results to any users associated with the specified entity id value. The value must be of the type specified in the &#x60;EntityType&#x60; field. | [optional] 
 **entitytype** | **str**| Specifies the type of entity that the &#x60;EntityId&#x60; field refers to. This field is required if the &#x60;EntityId&#x60; field is provided. | [optional] 
 **statuses** | [**List[str]**](str.md)| Filters results to any users whose lease is in one of the provided statuses. | [optional] 
 **name** | **str**| Filters results to any users whose name *contains* the specified value. | [optional] 
 **unitaddress** | **str**| Filters results to any users whose unit address *contains* the specified value. | [optional] 
 **isaccountcreated** | **bool**| Filters results to any users whose retail cash account is created. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[RetailCashUserMessage]**](RetailCashUserMessage.md)

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

# **external_api_retail_cash_write_update_retail_cash_user**
> RetailCashUserMessage external_api_retail_cash_write_update_retail_cash_user(user_id, unit_agreement_id, retail_cash_user_put_message)

Update a retail cash user

Updates a retail cash user.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Tenants</span> - `View` `Edit`
            OR
            <span class="permissionBlock"> Associations > Association owners and tenants</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.retail_cash_user_message import RetailCashUserMessage
from buildium_sdk.models.retail_cash_user_put_message import RetailCashUserPutMessage
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
    api_instance = buildium_sdk.ResidentCenterApi(api_client)
    user_id = 56 # int | 
    unit_agreement_id = 56 # int | 
    retail_cash_user_put_message = buildium_sdk.RetailCashUserPutMessage() # RetailCashUserPutMessage | 

    try:
        # Update a retail cash user
        api_response = await api_instance.external_api_retail_cash_write_update_retail_cash_user(user_id, unit_agreement_id, retail_cash_user_put_message)
        print("The response of ResidentCenterApi->external_api_retail_cash_write_update_retail_cash_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResidentCenterApi->external_api_retail_cash_write_update_retail_cash_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **unit_agreement_id** | **int**|  | 
 **retail_cash_user_put_message** | [**RetailCashUserPutMessage**](RetailCashUserPutMessage.md)|  | 

### Return type

[**RetailCashUserMessage**](RetailCashUserMessage.md)

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

