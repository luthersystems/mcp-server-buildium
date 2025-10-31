# buildium_sdk.LeasesApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_lease_epay_settings_get_lease_epay_settings_by_id**](LeasesApi.md#external_api_lease_epay_settings_get_lease_epay_settings_by_id) | **GET** /v1/leases/{leaseId}/epaysettings | Retrieve ePay settings
[**external_api_lease_epay_settings_update_lease_epay_settings**](LeasesApi.md#external_api_lease_epay_settings_update_lease_epay_settings) | **PUT** /v1/leases/{leaseId}/epaysettings | Update ePay settings
[**external_api_lease_move_outs_create_move_out_data**](LeasesApi.md#external_api_lease_move_outs_create_move_out_data) | **POST** /v1/leases/{leaseId}/moveouts | Create a move out
[**external_api_lease_move_outs_get_lease_move_out_data_by_tenant_id**](LeasesApi.md#external_api_lease_move_outs_get_lease_move_out_data_by_tenant_id) | **GET** /v1/leases/{leaseId}/moveouts/{tenantId} | Retrieve a move out
[**external_api_lease_move_outs_get_lease_move_out_information_by_id**](LeasesApi.md#external_api_lease_move_outs_get_lease_move_out_information_by_id) | **GET** /v1/leases/{leaseId}/moveouts | Retrieve all move outs
[**external_api_lease_move_outs_undo_tenant_moveout**](LeasesApi.md#external_api_lease_move_outs_undo_tenant_moveout) | **DELETE** /v1/leases/{leaseId}/moveouts/{tenantId} | Delete a move out
[**external_api_lease_notes_create_lease_note**](LeasesApi.md#external_api_lease_notes_create_lease_note) | **POST** /v1/leases/{leaseId}/notes | Create a note
[**external_api_lease_notes_get_lease_note_by_note_id**](LeasesApi.md#external_api_lease_notes_get_lease_note_by_note_id) | **GET** /v1/leases/{leaseId}/notes/{noteId} | Retrieve a note
[**external_api_lease_notes_get_lease_notes**](LeasesApi.md#external_api_lease_notes_get_lease_notes) | **GET** /v1/leases/{leaseId}/notes | Retrieve all notes
[**external_api_lease_notes_update_lease_note**](LeasesApi.md#external_api_lease_notes_update_lease_note) | **PUT** /v1/leases/{leaseId}/notes/{noteId} | Update a note
[**external_api_lease_partial_payment_settings_get_lease_partial_payment_settings**](LeasesApi.md#external_api_lease_partial_payment_settings_get_lease_partial_payment_settings) | **GET** /v1/leases/{leaseId}/partialpaymentsettings | Retrieve all partial payment settings for a lease
[**external_api_lease_renewals_read_get_all_lease_renewals**](LeasesApi.md#external_api_lease_renewals_read_get_all_lease_renewals) | **GET** /v1/leases/{leaseId}/renewals | Retrieve all renewals
[**external_api_lease_renewals_read_get_all_lease_renewals_for_all_properties**](LeasesApi.md#external_api_lease_renewals_read_get_all_lease_renewals_for_all_properties) | **GET** /v1/leases/renewals | Retrieve all upcoming renewals
[**external_api_lease_renewals_read_get_lease_renewal_by_id**](LeasesApi.md#external_api_lease_renewals_read_get_lease_renewal_by_id) | **GET** /v1/leases/{leaseId}/renewals/{renewalId} | Retrieve a renewal
[**external_api_lease_renewals_read_get_lease_renewal_history**](LeasesApi.md#external_api_lease_renewals_read_get_lease_renewal_history) | **GET** /v1/leases/renewalhistory | Retrieve all lease renewal history
[**external_api_lease_renewals_write_create_lease_renewal**](LeasesApi.md#external_api_lease_renewals_write_create_lease_renewal) | **POST** /v1/leases/{leaseId}/renewals | Create a lease renewal
[**external_api_lease_rent_create_rent_schedule**](LeasesApi.md#external_api_lease_rent_create_rent_schedule) | **POST** /v1/leases/{leaseId}/rent | Create a rent schedule
[**external_api_lease_rent_get_rent**](LeasesApi.md#external_api_lease_rent_get_rent) | **GET** /v1/leases/{leaseId}/rent | Retrieve all rent schedules
[**external_api_lease_rent_get_rent_by_id**](LeasesApi.md#external_api_lease_rent_get_rent_by_id) | **GET** /v1/leases/{leaseId}/rent/{rentId} | Retrieve a rent schedule
[**external_api_lease_rent_get_rent_paged**](LeasesApi.md#external_api_lease_rent_get_rent_paged) | **GET** /v1/leases/rent | Retrieve all rent schedules
[**external_api_lease_rent_update_rent_schedule**](LeasesApi.md#external_api_lease_rent_update_rent_schedule) | **PUT** /v1/leases/{leaseId}/rent/{rentId} | Update a rent schedule
[**external_api_lease_update_partial_payment_settings_patch_lease_partial_payment_settings**](LeasesApi.md#external_api_lease_update_partial_payment_settings_patch_lease_partial_payment_settings) | **PATCH** /v1/leases/{leaseId}/partialpaymentsettings | Update partial payment settings for a lease
[**external_api_leases_create_lease**](LeasesApi.md#external_api_leases_create_lease) | **POST** /v1/leases | Create a lease
[**external_api_leases_get_lease_by_id**](LeasesApi.md#external_api_leases_get_lease_by_id) | **GET** /v1/leases/{leaseId} | Retrieve a lease
[**external_api_leases_get_leases**](LeasesApi.md#external_api_leases_get_leases) | **GET** /v1/leases | Retrieve all leases
[**external_api_leases_update_lease**](LeasesApi.md#external_api_leases_update_lease) | **PUT** /v1/leases/{leaseId} | Update a lease
[**external_api_renters_insurance_get_renters_insurance_policies**](LeasesApi.md#external_api_renters_insurance_get_renters_insurance_policies) | **GET** /v1/leases/{leaseId}/rentersinsurance | Retrieve all insurance policies
[**external_api_renters_insurance_get_renters_insurance_policy_by_id**](LeasesApi.md#external_api_renters_insurance_get_renters_insurance_policy_by_id) | **GET** /v1/leases/{leaseId}/rentersinsurance/{policyId} | Retrieve an insurance policy


# **external_api_lease_epay_settings_get_lease_epay_settings_by_id**
> EPaySettingsMessage external_api_lease_epay_settings_get_lease_epay_settings_by_id(lease_id)

Retrieve ePay settings

Retrieves ePay settings for a lease.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.e_pay_settings_message import EPaySettingsMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 

    try:
        # Retrieve ePay settings
        api_response = await api_instance.external_api_lease_epay_settings_get_lease_epay_settings_by_id(lease_id)
        print("The response of LeasesApi->external_api_lease_epay_settings_get_lease_epay_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_epay_settings_get_lease_epay_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 

### Return type

[**EPaySettingsMessage**](EPaySettingsMessage.md)

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

# **external_api_lease_epay_settings_update_lease_epay_settings**
> EPaySettingsMessage external_api_lease_epay_settings_update_lease_epay_settings(lease_id, e_pay_settings_put_message)

Update ePay settings

Updates ePay settings for a lease
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.e_pay_settings_message import EPaySettingsMessage
from buildium_sdk.models.e_pay_settings_put_message import EPaySettingsPutMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    e_pay_settings_put_message = buildium_sdk.EPaySettingsPutMessage() # EPaySettingsPutMessage | 

    try:
        # Update ePay settings
        api_response = await api_instance.external_api_lease_epay_settings_update_lease_epay_settings(lease_id, e_pay_settings_put_message)
        print("The response of LeasesApi->external_api_lease_epay_settings_update_lease_epay_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_epay_settings_update_lease_epay_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **e_pay_settings_put_message** | [**EPaySettingsPutMessage**](EPaySettingsPutMessage.md)|  | 

### Return type

[**EPaySettingsMessage**](EPaySettingsMessage.md)

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

# **external_api_lease_move_outs_create_move_out_data**
> LeaseMoveOutDataMessage external_api_lease_move_outs_create_move_out_data(lease_id, lease_move_out_data_post_message)

Create a move out

Creates move out data for a single tenant on a given lease.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View` `Edit`
            
<span class="permissionBlock">Rentals > Tenants</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_move_out_data_message import LeaseMoveOutDataMessage
from buildium_sdk.models.lease_move_out_data_post_message import LeaseMoveOutDataPostMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    lease_move_out_data_post_message = buildium_sdk.LeaseMoveOutDataPostMessage() # LeaseMoveOutDataPostMessage | 

    try:
        # Create a move out
        api_response = await api_instance.external_api_lease_move_outs_create_move_out_data(lease_id, lease_move_out_data_post_message)
        print("The response of LeasesApi->external_api_lease_move_outs_create_move_out_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_move_outs_create_move_out_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **lease_move_out_data_post_message** | [**LeaseMoveOutDataPostMessage**](LeaseMoveOutDataPostMessage.md)|  | 

### Return type

[**LeaseMoveOutDataMessage**](LeaseMoveOutDataMessage.md)

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

# **external_api_lease_move_outs_get_lease_move_out_data_by_tenant_id**
> LeaseMoveOutDataMessage external_api_lease_move_outs_get_lease_move_out_data_by_tenant_id(lease_id, tenant_id)

Retrieve a move out

Retrieves move out data for a single tenant on a given lease.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View`
            
<span class="permissionBlock">Rentals > Tenants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_move_out_data_message import LeaseMoveOutDataMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    tenant_id = 56 # int | 

    try:
        # Retrieve a move out
        api_response = await api_instance.external_api_lease_move_outs_get_lease_move_out_data_by_tenant_id(lease_id, tenant_id)
        print("The response of LeasesApi->external_api_lease_move_outs_get_lease_move_out_data_by_tenant_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_move_outs_get_lease_move_out_data_by_tenant_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **tenant_id** | **int**|  | 

### Return type

[**LeaseMoveOutDataMessage**](LeaseMoveOutDataMessage.md)

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

# **external_api_lease_move_outs_get_lease_move_out_information_by_id**
> List[LeaseMoveOutDataMessage] external_api_lease_move_outs_get_lease_move_out_information_by_id(lease_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all move outs

Retrieves a list of move out dates for a given lease.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View`
            
<span class="permissionBlock">Rentals > Tenants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_move_out_data_message import LeaseMoveOutDataMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all move outs
        api_response = await api_instance.external_api_lease_move_outs_get_lease_move_out_information_by_id(lease_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeasesApi->external_api_lease_move_outs_get_lease_move_out_information_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_move_outs_get_lease_move_out_information_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[LeaseMoveOutDataMessage]**](LeaseMoveOutDataMessage.md)

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

# **external_api_lease_move_outs_undo_tenant_moveout**
> external_api_lease_move_outs_undo_tenant_moveout(lease_id, tenant_id)

Delete a move out

Deletes move out data for a tenant on a given lease.
            

<h4>Required Permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View` `Edit`
            
<span class="permissionBlock">Rentals > Tenants</span> - `View`

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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    tenant_id = 56 # int | 

    try:
        # Delete a move out
        await api_instance.external_api_lease_move_outs_undo_tenant_moveout(lease_id, tenant_id)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_move_outs_undo_tenant_moveout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **tenant_id** | **int**|  | 

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

# **external_api_lease_notes_create_lease_note**
> NoteMessage external_api_lease_notes_create_lease_note(lease_id, note_post_message)

Create a note

Creates a lease note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.note_message import NoteMessage
from buildium_sdk.models.note_post_message import NotePostMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    note_post_message = buildium_sdk.NotePostMessage() # NotePostMessage | 

    try:
        # Create a note
        api_response = await api_instance.external_api_lease_notes_create_lease_note(lease_id, note_post_message)
        print("The response of LeasesApi->external_api_lease_notes_create_lease_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_notes_create_lease_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **note_post_message** | [**NotePostMessage**](NotePostMessage.md)|  | 

### Return type

[**NoteMessage**](NoteMessage.md)

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

# **external_api_lease_notes_get_lease_note_by_note_id**
> NoteMessage external_api_lease_notes_get_lease_note_by_note_id(lease_id, note_id)

Retrieve a note

Retrieves a lease note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.note_message import NoteMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    note_id = 56 # int | 

    try:
        # Retrieve a note
        api_response = await api_instance.external_api_lease_notes_get_lease_note_by_note_id(lease_id, note_id)
        print("The response of LeasesApi->external_api_lease_notes_get_lease_note_by_note_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_notes_get_lease_note_by_note_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **note_id** | **int**|  | 

### Return type

[**NoteMessage**](NoteMessage.md)

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

# **external_api_lease_notes_get_lease_notes**
> List[NoteMessage] external_api_lease_notes_get_lease_notes(lease_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)

Retrieve all notes

Retrieves all lease notes.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.note_message import NoteMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    updateddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    updateddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    lastupdatedbyuserid = 56 # int | Filters results to only notes that were last updated by the specified user identifier. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all notes
        api_response = await api_instance.external_api_lease_notes_get_lease_notes(lease_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeasesApi->external_api_lease_notes_get_lease_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_notes_get_lease_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **updateddatetimefrom** | **datetime**| Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. | [optional] 
 **updateddatetimeto** | **datetime**| Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. | [optional] 
 **lastupdatedbyuserid** | **int**| Filters results to only notes that were last updated by the specified user identifier. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[NoteMessage]**](NoteMessage.md)

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

# **external_api_lease_notes_update_lease_note**
> NoteMessage external_api_lease_notes_update_lease_note(lease_id, note_id, note_put_message)

Update a note

Updates a lease note.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.note_message import NoteMessage
from buildium_sdk.models.note_put_message import NotePutMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    note_id = 56 # int | 
    note_put_message = buildium_sdk.NotePutMessage() # NotePutMessage | 

    try:
        # Update a note
        api_response = await api_instance.external_api_lease_notes_update_lease_note(lease_id, note_id, note_put_message)
        print("The response of LeasesApi->external_api_lease_notes_update_lease_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_notes_update_lease_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **note_id** | **int**|  | 
 **note_put_message** | [**NotePutMessage**](NotePutMessage.md)|  | 

### Return type

[**NoteMessage**](NoteMessage.md)

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

# **external_api_lease_partial_payment_settings_get_lease_partial_payment_settings**
> PartialPaymentSettingsMessage external_api_lease_partial_payment_settings_get_lease_partial_payment_settings(lease_id)

Retrieve all partial payment settings for a lease

Retrieves partial payment settings for a lease.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View`

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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 

    try:
        # Retrieve all partial payment settings for a lease
        api_response = await api_instance.external_api_lease_partial_payment_settings_get_lease_partial_payment_settings(lease_id)
        print("The response of LeasesApi->external_api_lease_partial_payment_settings_get_lease_partial_payment_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_partial_payment_settings_get_lease_partial_payment_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 

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
**404** | Resource not found. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_lease_renewals_read_get_all_lease_renewals**
> List[LeaseRenewalMessage] external_api_lease_renewals_read_get_all_lease_renewals(lease_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all renewals

Retrieves all renewals for a specific a lease.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_renewal_message import LeaseRenewalMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all renewals
        api_response = await api_instance.external_api_lease_renewals_read_get_all_lease_renewals(lease_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeasesApi->external_api_lease_renewals_read_get_all_lease_renewals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_renewals_read_get_all_lease_renewals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[LeaseRenewalMessage]**](LeaseRenewalMessage.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_lease_renewals_read_get_all_lease_renewals_for_all_properties**
> List[LeaseRenewalMessage] external_api_lease_renewals_read_get_all_lease_renewals_for_all_properties(esignaturestatuses, propertyids=propertyids, rentalownerids=rentalownerids, orderby=orderby, offset=offset, limit=limit)

Retrieve all upcoming renewals

Retrieves all upcoming lease renewals across all rental properties. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_renewal_message import LeaseRenewalMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    esignaturestatuses = ['esignaturestatuses_example'] # List[str] | Filters result to any lease renewal with an esignature status that matches the given statuses.
    propertyids = [56] # List[int] | Filters results to only include leases whose unit belongs to the specified set of property ids. (optional)
    rentalownerids = [56] # List[int] | Filters results to any lease whose unit belongs to a property with rental owner in the specified set of rental owner ids. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all upcoming renewals
        api_response = await api_instance.external_api_lease_renewals_read_get_all_lease_renewals_for_all_properties(esignaturestatuses, propertyids=propertyids, rentalownerids=rentalownerids, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeasesApi->external_api_lease_renewals_read_get_all_lease_renewals_for_all_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_renewals_read_get_all_lease_renewals_for_all_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **esignaturestatuses** | [**List[str]**](str.md)| Filters result to any lease renewal with an esignature status that matches the given statuses. | 
 **propertyids** | [**List[int]**](int.md)| Filters results to only include leases whose unit belongs to the specified set of property ids. | [optional] 
 **rentalownerids** | [**List[int]**](int.md)| Filters results to any lease whose unit belongs to a property with rental owner in the specified set of rental owner ids. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[LeaseRenewalMessage]**](LeaseRenewalMessage.md)

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

# **external_api_lease_renewals_read_get_lease_renewal_by_id**
> LeaseRenewalMessage external_api_lease_renewals_read_get_lease_renewal_by_id(lease_id, renewal_id)

Retrieve a renewal

Retrieves a specific renewal for a given lease. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_renewal_message import LeaseRenewalMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    renewal_id = 56 # int | 

    try:
        # Retrieve a renewal
        api_response = await api_instance.external_api_lease_renewals_read_get_lease_renewal_by_id(lease_id, renewal_id)
        print("The response of LeasesApi->external_api_lease_renewals_read_get_lease_renewal_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_renewals_read_get_lease_renewal_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **renewal_id** | **int**|  | 

### Return type

[**LeaseRenewalMessage**](LeaseRenewalMessage.md)

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

# **external_api_lease_renewals_read_get_lease_renewal_history**
> List[LeaseRenewalHistoryMessage] external_api_lease_renewals_read_get_lease_renewal_history(leaseids=leaseids, createddatetimefrom=createddatetimefrom, createddatetimeto=createddatetimeto, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)

Retrieve all lease renewal history

Retrieves all lease renewal history
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_renewal_history_message import LeaseRenewalHistoryMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    leaseids = [56] # List[int] | Filters results to only include lease renewals whose renewals belongs to the specified set of lease ids. (optional)
    createddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only lease renewals that were created after this date.  The value must be in UTC and formatted as `YYYY-MM-DDTHH:MM:SSZ`. The maximum date range is 365 days. (optional)
    createddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only lease renewals that were created before this date.The value must be in UTC and formatted as `YYYY-MM-DDTHH:MM:SSZ`. The maximum date range is 365 days. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any lease renewals that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 365 days. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any lease renewals were updated on or before the specified date.The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 365 days. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all lease renewal history
        api_response = await api_instance.external_api_lease_renewals_read_get_lease_renewal_history(leaseids=leaseids, createddatetimefrom=createddatetimefrom, createddatetimeto=createddatetimeto, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeasesApi->external_api_lease_renewals_read_get_lease_renewal_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_renewals_read_get_lease_renewal_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaseids** | [**List[int]**](int.md)| Filters results to only include lease renewals whose renewals belongs to the specified set of lease ids. | [optional] 
 **createddatetimefrom** | **datetime**| Filters results to only lease renewals that were created after this date.  The value must be in UTC and formatted as &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. The maximum date range is 365 days. | [optional] 
 **createddatetimeto** | **datetime**| Filters results to only lease renewals that were created before this date.The value must be in UTC and formatted as &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. The maximum date range is 365 days. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to any lease renewals that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 365 days. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to any lease renewals were updated on or before the specified date.The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 365 days. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[LeaseRenewalHistoryMessage]**](LeaseRenewalHistoryMessage.md)

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

# **external_api_lease_renewals_write_create_lease_renewal**
> LeaseRenewalMessage external_api_lease_renewals_write_create_lease_renewal(lease_id, lease_renewal_post_message)

Create a lease renewal

Creates a lease renewal.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_renewal_message import LeaseRenewalMessage
from buildium_sdk.models.lease_renewal_post_message import LeaseRenewalPostMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    lease_renewal_post_message = buildium_sdk.LeaseRenewalPostMessage() # LeaseRenewalPostMessage | 

    try:
        # Create a lease renewal
        api_response = await api_instance.external_api_lease_renewals_write_create_lease_renewal(lease_id, lease_renewal_post_message)
        print("The response of LeasesApi->external_api_lease_renewals_write_create_lease_renewal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_renewals_write_create_lease_renewal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **lease_renewal_post_message** | [**LeaseRenewalPostMessage**](LeaseRenewalPostMessage.md)|  | 

### Return type

[**LeaseRenewalMessage**](LeaseRenewalMessage.md)

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
**409** | There is a request conflict with the current state of the target resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_lease_rent_create_rent_schedule**
> LeaseRentMessage external_api_lease_rent_create_rent_schedule(lease_id, rent_schedule_post_message)

Create a rent schedule

Creates a rent schedule.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease Transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_rent_message import LeaseRentMessage
from buildium_sdk.models.rent_schedule_post_message import RentSchedulePostMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    rent_schedule_post_message = buildium_sdk.RentSchedulePostMessage() # RentSchedulePostMessage | 

    try:
        # Create a rent schedule
        api_response = await api_instance.external_api_lease_rent_create_rent_schedule(lease_id, rent_schedule_post_message)
        print("The response of LeasesApi->external_api_lease_rent_create_rent_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_rent_create_rent_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **rent_schedule_post_message** | [**RentSchedulePostMessage**](RentSchedulePostMessage.md)|  | 

### Return type

[**LeaseRentMessage**](LeaseRentMessage.md)

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

# **external_api_lease_rent_get_rent**
> List[LeaseRentMessage] external_api_lease_rent_get_rent(lease_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all rent schedules

The rent schedule provides details (dollar amount, day of the month, etc) of the recurring charges that are applied to the lease ledger each rent cycle. A lease may have more than one rent schedule associated with it if the rent terms change within the duration of the lease.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_rent_message import LeaseRentMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all rent schedules
        api_response = await api_instance.external_api_lease_rent_get_rent(lease_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeasesApi->external_api_lease_rent_get_rent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_rent_get_rent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[LeaseRentMessage]**](LeaseRentMessage.md)

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

# **external_api_lease_rent_get_rent_by_id**
> LeaseRentMessage external_api_lease_rent_get_rent_by_id(lease_id, rent_id)

Retrieve a rent schedule

Retrieves a specific rent schedule for a lease. The rent schedule provides details (dollar amount, day of the month, etc) of the recurring charges that are applied to the lease ledger each rent cycle.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_rent_message import LeaseRentMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    rent_id = 56 # int | 

    try:
        # Retrieve a rent schedule
        api_response = await api_instance.external_api_lease_rent_get_rent_by_id(lease_id, rent_id)
        print("The response of LeasesApi->external_api_lease_rent_get_rent_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_rent_get_rent_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **rent_id** | **int**|  | 

### Return type

[**LeaseRentMessage**](LeaseRentMessage.md)

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

# **external_api_lease_rent_get_rent_paged**
> List[RentMessage] external_api_lease_rent_get_rent_paged(leaseids=leaseids, createddatetimefrom=createddatetimefrom, createddatetimeto=createddatetimeto, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)

Retrieve all rent schedules

The rent schedule provides details (dollar amount, day of the month, etc) of the recurring charges that are applied to the lease ledger each rent cycle. A lease may have more than one rent schedule associated with it if the rent terms change within the duration of the lease.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rent_message import RentMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    leaseids = [56] # List[int] | Filters results to only include rents whose lease belongs to the specified set of lease ids. (optional)
    createddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only rents that were created after this date. The value must be in UTC and formatted as `YYYY-MM-DDTHH:MM:SSZ`. The maximum date range is 365 days. (optional)
    createddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to only rents that were created before this date.The value must be in UTC and formatted as `YYYY-MM-DDTHH:MM:SSZ`. The maximum date range is 365 days. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any rents that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 365 days. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any rents were updated on or before the specified date.The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 365 days. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all rent schedules
        api_response = await api_instance.external_api_lease_rent_get_rent_paged(leaseids=leaseids, createddatetimefrom=createddatetimefrom, createddatetimeto=createddatetimeto, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeasesApi->external_api_lease_rent_get_rent_paged:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_rent_get_rent_paged: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaseids** | [**List[int]**](int.md)| Filters results to only include rents whose lease belongs to the specified set of lease ids. | [optional] 
 **createddatetimefrom** | **datetime**| Filters results to only rents that were created after this date. The value must be in UTC and formatted as &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. The maximum date range is 365 days. | [optional] 
 **createddatetimeto** | **datetime**| Filters results to only rents that were created before this date.The value must be in UTC and formatted as &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. The maximum date range is 365 days. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to any rents that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 365 days. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to any rents were updated on or before the specified date.The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 365 days. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[RentMessage]**](RentMessage.md)

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

# **external_api_lease_rent_update_rent_schedule**
> LeaseRentMessage external_api_lease_rent_update_rent_schedule(lease_id, rent_id, rent_schedule_put_message)

Update a rent schedule

Updates a rent schedule.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease Transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_rent_message import LeaseRentMessage
from buildium_sdk.models.rent_schedule_put_message import RentSchedulePutMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    rent_id = 56 # int | 
    rent_schedule_put_message = buildium_sdk.RentSchedulePutMessage() # RentSchedulePutMessage | 

    try:
        # Update a rent schedule
        api_response = await api_instance.external_api_lease_rent_update_rent_schedule(lease_id, rent_id, rent_schedule_put_message)
        print("The response of LeasesApi->external_api_lease_rent_update_rent_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_rent_update_rent_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **rent_id** | **int**|  | 
 **rent_schedule_put_message** | [**RentSchedulePutMessage**](RentSchedulePutMessage.md)|  | 

### Return type

[**LeaseRentMessage**](LeaseRentMessage.md)

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

# **external_api_lease_update_partial_payment_settings_patch_lease_partial_payment_settings**
> PartialPaymentSettingsMessage external_api_lease_update_partial_payment_settings_patch_lease_partial_payment_settings(lease_id, partial_payment_settings_patch_message)

Update partial payment settings for a lease

Updates partial payment settings for a lease.
            

<h4>Required Permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View` `Edit`
            <span class="permissionBlock">Administration > Application Settings</span> - `View` `Edit`

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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    partial_payment_settings_patch_message = buildium_sdk.PartialPaymentSettingsPatchMessage() # PartialPaymentSettingsPatchMessage | <span>Represents the structure of the data that can be provided to a <a target=\"_blank\" href=\"https://datatracker.ietf.org/doc/html/rfc6902\">JSON patch document</a> as path values via <a target=\"_blank\" href=\"https://datatracker.ietf.org/doc/html/rfc6901/\">JSON pointer</a> syntax.</span>

    try:
        # Update partial payment settings for a lease
        api_response = await api_instance.external_api_lease_update_partial_payment_settings_patch_lease_partial_payment_settings(lease_id, partial_payment_settings_patch_message)
        print("The response of LeasesApi->external_api_lease_update_partial_payment_settings_patch_lease_partial_payment_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_lease_update_partial_payment_settings_patch_lease_partial_payment_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
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
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_leases_create_lease**
> LeaseMessage external_api_leases_create_lease(lease_post_message)

Create a lease

Creates a signed lease.


<span class="permissionBlock">Rentals > Leases</span> - `View` `Edit`

<span class="permissionBlock">Rentals > Tenants</span> - `View` `Edit`

<span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

<h4>Optional Permissions:</h4>
<span class="permissionBlock">Rentals > Applicants</span> - `View` In order to add tenants to the lease using the ApplicantIds property, you must have this permission.

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_message import LeaseMessage
from buildium_sdk.models.lease_post_message import LeasePostMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_post_message = buildium_sdk.LeasePostMessage() # LeasePostMessage | 

    try:
        # Create a lease
        api_response = await api_instance.external_api_leases_create_lease(lease_post_message)
        print("The response of LeasesApi->external_api_leases_create_lease:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_leases_create_lease: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_post_message** | [**LeasePostMessage**](LeasePostMessage.md)|  | 

### Return type

[**LeaseMessage**](LeaseMessage.md)

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

# **external_api_leases_get_lease_by_id**
> LeaseMessage external_api_leases_get_lease_by_id(lease_id)

Retrieve a lease

Retrieves a specific lease.


<span class="permissionBlock">Rentals > Leases</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_message import LeaseMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | The lease identifier.

    try:
        # Retrieve a lease
        api_response = await api_instance.external_api_leases_get_lease_by_id(lease_id)
        print("The response of LeasesApi->external_api_leases_get_lease_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_leases_get_lease_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**| The lease identifier. | 

### Return type

[**LeaseMessage**](LeaseMessage.md)

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

# **external_api_leases_get_leases**
> List[LeaseMessage] external_api_leases_get_leases(propertyids=propertyids, rentalownerids=rentalownerids, unitnumber=unitnumber, tenantname=tenantname, leasedatefrom=leasedatefrom, leasedateto=leasedateto, leasetypes=leasetypes, leasestatuses=leasestatuses, createddatetimefrom=createddatetimefrom, createddatetimeto=createddatetimeto, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)

Retrieve all leases

Retrieves a list of leases.


<span class="permissionBlock">Rentals > Leases</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_message import LeaseMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    propertyids = [56] # List[int] | Filters results to any lease whose unit belongs to the specified set of property ids. (optional)
    rentalownerids = [56] # List[int] | Filters results to any lease whose unit belongs to a property with a rental owner in the specified set of rental owner ids. (optional)
    unitnumber = 'unitnumber_example' # str | Filters results to any lease whose unit number *contains* the specified value. (optional)
    tenantname = 'tenantname_example' # str | Filters results to any lease whose current tenants' names *contain* the specified value. (optional)
    leasedatefrom = '2013-10-20' # date | Filters results to any lease whose start date is greater than or equal to the specified value. (optional)
    leasedateto = '2013-10-20' # date | Filters results to any lease whose end date is less than or equal to the specified value. (optional)
    leasetypes = ['leasetypes_example'] # List[str] | Filters results to any lease whose lease type matches the specified status. If no type is specified, leases with any type will be returned. (optional)
    leasestatuses = ['leasestatuses_example'] # List[str] | Filters results to any lease whose lease term matches the specified status. If no status is specified, leases with any lease term status will be returned. (optional)
    createddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any lease whose created date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    createddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any lease whose created date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any leases that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any leases that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all leases
        api_response = await api_instance.external_api_leases_get_leases(propertyids=propertyids, rentalownerids=rentalownerids, unitnumber=unitnumber, tenantname=tenantname, leasedatefrom=leasedatefrom, leasedateto=leasedateto, leasetypes=leasetypes, leasestatuses=leasestatuses, createddatetimefrom=createddatetimefrom, createddatetimeto=createddatetimeto, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeasesApi->external_api_leases_get_leases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_leases_get_leases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **propertyids** | [**List[int]**](int.md)| Filters results to any lease whose unit belongs to the specified set of property ids. | [optional] 
 **rentalownerids** | [**List[int]**](int.md)| Filters results to any lease whose unit belongs to a property with a rental owner in the specified set of rental owner ids. | [optional] 
 **unitnumber** | **str**| Filters results to any lease whose unit number *contains* the specified value. | [optional] 
 **tenantname** | **str**| Filters results to any lease whose current tenants&#39; names *contain* the specified value. | [optional] 
 **leasedatefrom** | **date**| Filters results to any lease whose start date is greater than or equal to the specified value. | [optional] 
 **leasedateto** | **date**| Filters results to any lease whose end date is less than or equal to the specified value. | [optional] 
 **leasetypes** | [**List[str]**](str.md)| Filters results to any lease whose lease type matches the specified status. If no type is specified, leases with any type will be returned. | [optional] 
 **leasestatuses** | [**List[str]**](str.md)| Filters results to any lease whose lease term matches the specified status. If no status is specified, leases with any lease term status will be returned. | [optional] 
 **createddatetimefrom** | **datetime**| Filters results to any lease whose created date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. | [optional] 
 **createddatetimeto** | **datetime**| Filters results to any lease whose created date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to any leases that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to any leases that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[LeaseMessage]**](LeaseMessage.md)

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

# **external_api_leases_update_lease**
> LeaseMessage external_api_leases_update_lease(lease_id, lease_put_message)

Update a lease

Update a signed lease.


<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.


<span class="permissionBlock">Rentals > Leases</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_message import LeaseMessage
from buildium_sdk.models.lease_put_message import LeasePutMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    lease_put_message = buildium_sdk.LeasePutMessage() # LeasePutMessage | 

    try:
        # Update a lease
        api_response = await api_instance.external_api_leases_update_lease(lease_id, lease_put_message)
        print("The response of LeasesApi->external_api_leases_update_lease:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_leases_update_lease: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **lease_put_message** | [**LeasePutMessage**](LeasePutMessage.md)|  | 

### Return type

[**LeaseMessage**](LeaseMessage.md)

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

# **external_api_renters_insurance_get_renters_insurance_policies**
> List[RentersInsurancePolicyMessage] external_api_renters_insurance_get_renters_insurance_policies(lease_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all insurance policies

Retrieves all renters insurance policies for a lease.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.renters_insurance_policy_message import RentersInsurancePolicyMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all insurance policies
        api_response = await api_instance.external_api_renters_insurance_get_renters_insurance_policies(lease_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeasesApi->external_api_renters_insurance_get_renters_insurance_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_renters_insurance_get_renters_insurance_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[RentersInsurancePolicyMessage]**](RentersInsurancePolicyMessage.md)

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

# **external_api_renters_insurance_get_renters_insurance_policy_by_id**
> RentersInsurancePolicyMessage external_api_renters_insurance_get_renters_insurance_policy_by_id(lease_id, policy_id)

Retrieve an insurance policy

Retrieves a renters insurance policy.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Leases</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.renters_insurance_policy_message import RentersInsurancePolicyMessage
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
    api_instance = buildium_sdk.LeasesApi(api_client)
    lease_id = 56 # int | 
    policy_id = 56 # int | 

    try:
        # Retrieve an insurance policy
        api_response = await api_instance.external_api_renters_insurance_get_renters_insurance_policy_by_id(lease_id, policy_id)
        print("The response of LeasesApi->external_api_renters_insurance_get_renters_insurance_policy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeasesApi->external_api_renters_insurance_get_renters_insurance_policy_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **policy_id** | **int**|  | 

### Return type

[**RentersInsurancePolicyMessage**](RentersInsurancePolicyMessage.md)

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

