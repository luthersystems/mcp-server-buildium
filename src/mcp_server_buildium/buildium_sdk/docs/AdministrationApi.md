# buildium_sdk.AdministrationApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_account_info_get_account_info**](AdministrationApi.md#external_api_account_info_get_account_info) | **GET** /v1/administration/account | Retrieve account info
[**external_api_accounting_lock_period_get_accounting_lock_period_settings**](AdministrationApi.md#external_api_accounting_lock_period_get_accounting_lock_period_settings) | **GET** /v1/administration/accountinglockperiod | Retrieve accounting lock periods
[**external_api_partial_payment_global_settings_get_global_partial_payment_settings**](AdministrationApi.md#external_api_partial_payment_global_settings_get_global_partial_payment_settings) | **GET** /v1/administration/residentsettings/partialpaymentsettings | Retrieve the partial payment settings for residents
[**external_api_partial_payment_global_settings_patch_global_partial_payment_settings**](AdministrationApi.md#external_api_partial_payment_global_settings_patch_global_partial_payment_settings) | **PATCH** /v1/administration/residentsettings/partialpaymentsettings | Update the partial payment settings for residents
[**external_api_user_roles_get_all_user_roles**](AdministrationApi.md#external_api_user_roles_get_all_user_roles) | **GET** /v1/userroles | Retrieve all user roles
[**external_api_user_roles_get_user_role_by_id**](AdministrationApi.md#external_api_user_roles_get_user_role_by_id) | **GET** /v1/userroles/{userRoleId} | Retrieve a user role
[**external_api_users_get_all_users**](AdministrationApi.md#external_api_users_get_all_users) | **GET** /v1/users | Retrieve all users
[**external_api_users_get_user_by_id**](AdministrationApi.md#external_api_users_get_user_by_id) | **GET** /v1/users/{userId} | Retrieve a user


# **external_api_account_info_get_account_info**
> AccountInfoMessage external_api_account_info_get_account_info()

Retrieve account info

Retrieves information related to the Buildium account. 


<h4>Required permission(s):</h4><span class="permissionBlock">Administration > Account Information</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.account_info_message import AccountInfoMessage
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
    api_instance = buildium_sdk.AdministrationApi(api_client)

    try:
        # Retrieve account info
        api_response = await api_instance.external_api_account_info_get_account_info()
        print("The response of AdministrationApi->external_api_account_info_get_account_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdministrationApi->external_api_account_info_get_account_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountInfoMessage**](AccountInfoMessage.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_accounting_lock_period_get_accounting_lock_period_settings**
> AccountingLockPeriodMessage external_api_accounting_lock_period_get_accounting_lock_period_settings()

Retrieve accounting lock periods

Retrieves accounting lock periods.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Administration > Application Settings</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.accounting_lock_period_message import AccountingLockPeriodMessage
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
    api_instance = buildium_sdk.AdministrationApi(api_client)

    try:
        # Retrieve accounting lock periods
        api_response = await api_instance.external_api_accounting_lock_period_get_accounting_lock_period_settings()
        print("The response of AdministrationApi->external_api_accounting_lock_period_get_accounting_lock_period_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdministrationApi->external_api_accounting_lock_period_get_accounting_lock_period_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountingLockPeriodMessage**](AccountingLockPeriodMessage.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_partial_payment_global_settings_get_global_partial_payment_settings**
> PartialPaymentSettingsMessage external_api_partial_payment_global_settings_get_global_partial_payment_settings()

Retrieve the partial payment settings for residents

Retrieves the partial payment settings for residents.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Administration > Application Settings</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.partial_payment_settings_message import PartialPaymentSettingsMessage
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
    api_instance = buildium_sdk.AdministrationApi(api_client)

    try:
        # Retrieve the partial payment settings for residents
        api_response = await api_instance.external_api_partial_payment_global_settings_get_global_partial_payment_settings()
        print("The response of AdministrationApi->external_api_partial_payment_global_settings_get_global_partial_payment_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdministrationApi->external_api_partial_payment_global_settings_get_global_partial_payment_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PartialPaymentSettingsMessage**](PartialPaymentSettingsMessage.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_partial_payment_global_settings_patch_global_partial_payment_settings**
> PartialPaymentSettingsMessage external_api_partial_payment_global_settings_patch_global_partial_payment_settings(partial_payment_settings_patch_message)

Update the partial payment settings for residents

Updates the partial payment settings for residents.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Administration > Application Settings</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.partial_payment_settings_message import PartialPaymentSettingsMessage
from buildium_sdk.models.partial_payment_settings_patch_message import PartialPaymentSettingsPatchMessage
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
    api_instance = buildium_sdk.AdministrationApi(api_client)
    partial_payment_settings_patch_message = buildium_sdk.PartialPaymentSettingsPatchMessage() # PartialPaymentSettingsPatchMessage | <span>Represents the structure of the data that can be provided to a <a target=\"_blank\" href=\"https://datatracker.ietf.org/doc/html/rfc6902\">JSON patch document</a> as path values via <a target=\"_blank\" href=\"https://datatracker.ietf.org/doc/html/rfc6901/\">JSON pointer</a> syntax.</span>

    try:
        # Update the partial payment settings for residents
        api_response = await api_instance.external_api_partial_payment_global_settings_patch_global_partial_payment_settings(partial_payment_settings_patch_message)
        print("The response of AdministrationApi->external_api_partial_payment_global_settings_patch_global_partial_payment_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdministrationApi->external_api_partial_payment_global_settings_patch_global_partial_payment_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partial_payment_settings_patch_message** | [**PartialPaymentSettingsPatchMessage**](PartialPaymentSettingsPatchMessage.md)| &lt;span&gt;Represents the structure of the data that can be provided to a &lt;a target&#x3D;\&quot;_blank\&quot; href&#x3D;\&quot;https://datatracker.ietf.org/doc/html/rfc6902\&quot;&gt;JSON patch document&lt;/a&gt; as path values via &lt;a target&#x3D;\&quot;_blank\&quot; href&#x3D;\&quot;https://datatracker.ietf.org/doc/html/rfc6901/\&quot;&gt;JSON pointer&lt;/a&gt; syntax.&lt;/span&gt; | 

### Return type

[**PartialPaymentSettingsMessage**](PartialPaymentSettingsMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_user_roles_get_all_user_roles**
> List[UserRoleMessage] external_api_user_roles_get_all_user_roles(orderby=orderby, offset=offset, limit=limit)

Retrieve all user roles

Retrieves a list of user roles.


<h4>Required permission(s):</h4><span class="permissionBlock">Administration > User Roles</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.user_role_message import UserRoleMessage
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
    api_instance = buildium_sdk.AdministrationApi(api_client)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all user roles
        api_response = await api_instance.external_api_user_roles_get_all_user_roles(orderby=orderby, offset=offset, limit=limit)
        print("The response of AdministrationApi->external_api_user_roles_get_all_user_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdministrationApi->external_api_user_roles_get_all_user_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[UserRoleMessage]**](UserRoleMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Total-Count - The total number of records available in the overall result set of the request. <br>  |
**400** | BadRequest |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials do not have permissions to access the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_user_roles_get_user_role_by_id**
> UserRoleMessage external_api_user_roles_get_user_role_by_id(user_role_id)

Retrieve a user role

Retrieve a specific user role.


<h4>Required permission(s):</h4><span class="permissionBlock">Administration > User Roles</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.user_role_message import UserRoleMessage
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
    api_instance = buildium_sdk.AdministrationApi(api_client)
    user_role_id = 56 # int | The user role identifier.

    try:
        # Retrieve a user role
        api_response = await api_instance.external_api_user_roles_get_user_role_by_id(user_role_id)
        print("The response of AdministrationApi->external_api_user_roles_get_user_role_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdministrationApi->external_api_user_roles_get_user_role_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_role_id** | **int**| The user role identifier. | 

### Return type

[**UserRoleMessage**](UserRoleMessage.md)

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
**403** | The supplied credentials do not have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_users_get_all_users**
> List[UserMessage] external_api_users_get_all_users(roleids=roleids, usertypes=usertypes, status=status, name=name, email=email, orderby=orderby, offset=offset, limit=limit)

Retrieve all users

Retrieves a list of users.


<h4>Required permission(s):</h4><span class="permissionBlock">Administration > Users</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.user_message import UserMessage
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
    api_instance = buildium_sdk.AdministrationApi(api_client)
    roleids = [56] # List[int] | Describes the role of the user. (optional)
    usertypes = ['usertypes_example'] # List[str] | Describes the user type of the user. (optional)
    status = 'status_example' # str | Filters results by the status of the user. If no status is specified both `active` and `inactive` staff members will be returned. (optional)
    name = 'name_example' # str | Filters results to only records whose name *contains* the specified value. (optional)
    email = 'email_example' # str | Filters results to only records whose email *contains* the specified value. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all users
        api_response = await api_instance.external_api_users_get_all_users(roleids=roleids, usertypes=usertypes, status=status, name=name, email=email, orderby=orderby, offset=offset, limit=limit)
        print("The response of AdministrationApi->external_api_users_get_all_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdministrationApi->external_api_users_get_all_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roleids** | [**List[int]**](int.md)| Describes the role of the user. | [optional] 
 **usertypes** | [**List[str]**](str.md)| Describes the user type of the user. | [optional] 
 **status** | **str**| Filters results by the status of the user. If no status is specified both &#x60;active&#x60; and &#x60;inactive&#x60; staff members will be returned. | [optional] 
 **name** | **str**| Filters results to only records whose name *contains* the specified value. | [optional] 
 **email** | **str**| Filters results to only records whose email *contains* the specified value. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[UserMessage]**](UserMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Total-Count - The total number of records available in the overall result set of the request. <br>  |
**400** | BadRequest |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials do not have permissions to access the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_users_get_user_by_id**
> UserMessage external_api_users_get_user_by_id(user_id)

Retrieve a user

Retrieve a specific user.


<h4>Required permission(s):</h4><span class="permissionBlock">Administration > Users</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.user_message import UserMessage
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
    api_instance = buildium_sdk.AdministrationApi(api_client)
    user_id = 56 # int | The user identifier.

    try:
        # Retrieve a user
        api_response = await api_instance.external_api_users_get_user_by_id(user_id)
        print("The response of AdministrationApi->external_api_users_get_user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdministrationApi->external_api_users_get_user_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user identifier. | 

### Return type

[**UserMessage**](UserMessage.md)

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
**403** | The supplied credentials do not have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

