# buildium_sdk.RentalTenantsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_rental_tenants_create_rental_tenant**](RentalTenantsApi.md#external_api_rental_tenants_create_rental_tenant) | **POST** /v1/leases/tenants | Create a tenant
[**external_api_rental_tenants_get_all_tenants**](RentalTenantsApi.md#external_api_rental_tenants_get_all_tenants) | **GET** /v1/leases/tenants | Retrieve all tenants
[**external_api_rental_tenants_get_tenant_by_id**](RentalTenantsApi.md#external_api_rental_tenants_get_tenant_by_id) | **GET** /v1/leases/tenants/{tenantId} | Retrieve a tenant
[**external_api_rental_tenants_update_rental_tenant**](RentalTenantsApi.md#external_api_rental_tenants_update_rental_tenant) | **PUT** /v1/leases/tenants/{tenantId} | Update a tenant
[**external_api_tenant_notes_create_tenant_note**](RentalTenantsApi.md#external_api_tenant_notes_create_tenant_note) | **POST** /v1/leases/tenants/{tenantId}/notes | Create a note
[**external_api_tenant_notes_get_all_tenant_notes**](RentalTenantsApi.md#external_api_tenant_notes_get_all_tenant_notes) | **GET** /v1/leases/tenants/{tenantId}/notes | Retrieve all notes
[**external_api_tenant_notes_get_tenant_note_by_id**](RentalTenantsApi.md#external_api_tenant_notes_get_tenant_note_by_id) | **GET** /v1/leases/tenants/{tenantId}/notes/{noteId} | Retrieve a note
[**external_api_tenant_notes_update_lease_tenant_note**](RentalTenantsApi.md#external_api_tenant_notes_update_lease_tenant_note) | **PUT** /v1/leases/tenants/{tenantId}/notes/{noteId} | Update a note


# **external_api_rental_tenants_create_rental_tenant**
> TenantMessage external_api_rental_tenants_create_rental_tenant(rental_tenant_post_message)

Create a tenant

Creates a rental tenant.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Tenants</span> - `View` `Edit`

<span class="permissionBlock">Rentals > Leases</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_tenant_post_message import RentalTenantPostMessage
from buildium_sdk.models.tenant_message import TenantMessage
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
    api_instance = buildium_sdk.RentalTenantsApi(api_client)
    rental_tenant_post_message = buildium_sdk.RentalTenantPostMessage() # RentalTenantPostMessage | 

    try:
        # Create a tenant
        api_response = await api_instance.external_api_rental_tenants_create_rental_tenant(rental_tenant_post_message)
        print("The response of RentalTenantsApi->external_api_rental_tenants_create_rental_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalTenantsApi->external_api_rental_tenants_create_rental_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_tenant_post_message** | [**RentalTenantPostMessage**](RentalTenantPostMessage.md)|  | 

### Return type

[**TenantMessage**](TenantMessage.md)

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

# **external_api_rental_tenants_get_all_tenants**
> List[TenantMessage] external_api_rental_tenants_get_all_tenants(buildingstatuses=buildingstatuses, leasetermstatuses=leasetermstatuses, unitnumber=unitnumber, name=name, phone=phone, email=email, propertyids=propertyids, rentalownerids=rentalownerids, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, unitids=unitids, orderby=orderby, offset=offset, limit=limit)

Retrieve all tenants

Retrieves a list of tenants.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Tenants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.tenant_message import TenantMessage
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
    api_instance = buildium_sdk.RentalTenantsApi(api_client)
    buildingstatuses = ['buildingstatuses_example'] # List[str] | Filters results by the status of the rental property the tenants are associated with. If no status is specified tenants in either `active` and `inactive` rental properties will be returned. (optional)
    leasetermstatuses = ['leasetermstatuses_example'] # List[str] | Filters results to any tenant whose lease term matches the specified status.  If no status is specified tenants with any lease terms status will be returned. (optional)
    unitnumber = 'unitnumber_example' # str | Filters results to any tenant whose unit number *contains* the specified value. (optional)
    name = 'name_example' # str | Filters results to any tenant whose name *contains* the specified value. (optional)
    phone = 'phone_example' # str | Filters results to any tenant whose phone number *contains* the specified value. (optional)
    email = 'email_example' # str | Filters results to any tenant whose email *contains* the specified value. (optional)
    propertyids = [56] # List[int] | Filters results to tenants whose rental unit belongs to the specified set of property ids. (optional)
    rentalownerids = [56] # List[int] | Filters results to tenants whose rental unit belongs to a property with a rental owner in the specified set of rental owner ids. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any rental tenants that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any rental tenants that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    unitids = [56] # List[int] | Filters results to only tenants associated with the specified set of unit ids. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all tenants
        api_response = await api_instance.external_api_rental_tenants_get_all_tenants(buildingstatuses=buildingstatuses, leasetermstatuses=leasetermstatuses, unitnumber=unitnumber, name=name, phone=phone, email=email, propertyids=propertyids, rentalownerids=rentalownerids, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, unitids=unitids, orderby=orderby, offset=offset, limit=limit)
        print("The response of RentalTenantsApi->external_api_rental_tenants_get_all_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalTenantsApi->external_api_rental_tenants_get_all_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buildingstatuses** | [**List[str]**](str.md)| Filters results by the status of the rental property the tenants are associated with. If no status is specified tenants in either &#x60;active&#x60; and &#x60;inactive&#x60; rental properties will be returned. | [optional] 
 **leasetermstatuses** | [**List[str]**](str.md)| Filters results to any tenant whose lease term matches the specified status.  If no status is specified tenants with any lease terms status will be returned. | [optional] 
 **unitnumber** | **str**| Filters results to any tenant whose unit number *contains* the specified value. | [optional] 
 **name** | **str**| Filters results to any tenant whose name *contains* the specified value. | [optional] 
 **phone** | **str**| Filters results to any tenant whose phone number *contains* the specified value. | [optional] 
 **email** | **str**| Filters results to any tenant whose email *contains* the specified value. | [optional] 
 **propertyids** | [**List[int]**](int.md)| Filters results to tenants whose rental unit belongs to the specified set of property ids. | [optional] 
 **rentalownerids** | [**List[int]**](int.md)| Filters results to tenants whose rental unit belongs to a property with a rental owner in the specified set of rental owner ids. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to any rental tenants that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to any rental tenants that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **unitids** | [**List[int]**](int.md)| Filters results to only tenants associated with the specified set of unit ids. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[TenantMessage]**](TenantMessage.md)

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

# **external_api_rental_tenants_get_tenant_by_id**
> TenantMessage external_api_rental_tenants_get_tenant_by_id(tenant_id)

Retrieve a tenant

Retrieve a specific tenant.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Tenants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.tenant_message import TenantMessage
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
    api_instance = buildium_sdk.RentalTenantsApi(api_client)
    tenant_id = 56 # int | The tenant identifier.

    try:
        # Retrieve a tenant
        api_response = await api_instance.external_api_rental_tenants_get_tenant_by_id(tenant_id)
        print("The response of RentalTenantsApi->external_api_rental_tenants_get_tenant_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalTenantsApi->external_api_rental_tenants_get_tenant_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**| The tenant identifier. | 

### Return type

[**TenantMessage**](TenantMessage.md)

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

# **external_api_rental_tenants_update_rental_tenant**
> TenantMessage external_api_rental_tenants_update_rental_tenant(tenant_id, rental_tenant_put_message)

Update a tenant

Updates a rental tenant.


<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Tenants</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_tenant_put_message import RentalTenantPutMessage
from buildium_sdk.models.tenant_message import TenantMessage
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
    api_instance = buildium_sdk.RentalTenantsApi(api_client)
    tenant_id = 56 # int | 
    rental_tenant_put_message = buildium_sdk.RentalTenantPutMessage() # RentalTenantPutMessage | 

    try:
        # Update a tenant
        api_response = await api_instance.external_api_rental_tenants_update_rental_tenant(tenant_id, rental_tenant_put_message)
        print("The response of RentalTenantsApi->external_api_rental_tenants_update_rental_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalTenantsApi->external_api_rental_tenants_update_rental_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**|  | 
 **rental_tenant_put_message** | [**RentalTenantPutMessage**](RentalTenantPutMessage.md)|  | 

### Return type

[**TenantMessage**](TenantMessage.md)

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

# **external_api_tenant_notes_create_tenant_note**
> NoteMessage external_api_tenant_notes_create_tenant_note(tenant_id, note_post_message)

Create a note

Creates a tenant note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Tenants</span> - `View` `Edit`

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
    api_instance = buildium_sdk.RentalTenantsApi(api_client)
    tenant_id = 56 # int | 
    note_post_message = buildium_sdk.NotePostMessage() # NotePostMessage | 

    try:
        # Create a note
        api_response = await api_instance.external_api_tenant_notes_create_tenant_note(tenant_id, note_post_message)
        print("The response of RentalTenantsApi->external_api_tenant_notes_create_tenant_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalTenantsApi->external_api_tenant_notes_create_tenant_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**|  | 
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

# **external_api_tenant_notes_get_all_tenant_notes**
> List[NoteMessage] external_api_tenant_notes_get_all_tenant_notes(tenant_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)

Retrieve all notes

Retrieves all tenant notes.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Tenants</span> - `View`

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
    api_instance = buildium_sdk.RentalTenantsApi(api_client)
    tenant_id = 56 # int | The tenant identifier.
    updateddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    updateddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    lastupdatedbyuserid = 56 # int | Filters results to only notes that were last updated by the specified user identifier. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all notes
        api_response = await api_instance.external_api_tenant_notes_get_all_tenant_notes(tenant_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)
        print("The response of RentalTenantsApi->external_api_tenant_notes_get_all_tenant_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalTenantsApi->external_api_tenant_notes_get_all_tenant_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**| The tenant identifier. | 
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

# **external_api_tenant_notes_get_tenant_note_by_id**
> NoteMessage external_api_tenant_notes_get_tenant_note_by_id(tenant_id, note_id)

Retrieve a note

Retrieves a tenant note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Tenants</span> - `View`

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
    api_instance = buildium_sdk.RentalTenantsApi(api_client)
    tenant_id = 56 # int | 
    note_id = 56 # int | 

    try:
        # Retrieve a note
        api_response = await api_instance.external_api_tenant_notes_get_tenant_note_by_id(tenant_id, note_id)
        print("The response of RentalTenantsApi->external_api_tenant_notes_get_tenant_note_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalTenantsApi->external_api_tenant_notes_get_tenant_note_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**|  | 
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

# **external_api_tenant_notes_update_lease_tenant_note**
> NoteMessage external_api_tenant_notes_update_lease_tenant_note(tenant_id, note_id, note_put_message)

Update a note

Updates a tenant note.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Tenants</span> - `View` `Edit`

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
    api_instance = buildium_sdk.RentalTenantsApi(api_client)
    tenant_id = 56 # int | 
    note_id = 56 # int | 
    note_put_message = buildium_sdk.NotePutMessage() # NotePutMessage | 

    try:
        # Update a note
        api_response = await api_instance.external_api_tenant_notes_update_lease_tenant_note(tenant_id, note_id, note_put_message)
        print("The response of RentalTenantsApi->external_api_tenant_notes_update_lease_tenant_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalTenantsApi->external_api_tenant_notes_update_lease_tenant_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**|  | 
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

