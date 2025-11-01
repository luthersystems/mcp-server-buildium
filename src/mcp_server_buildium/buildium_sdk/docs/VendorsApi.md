# buildium_sdk.VendorsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_vendor_categories_create_vendor_category**](VendorsApi.md#external_api_vendor_categories_create_vendor_category) | **POST** /v1/vendors/categories | Create a vendor category
[**external_api_vendor_categories_get_all_vendor_categories**](VendorsApi.md#external_api_vendor_categories_get_all_vendor_categories) | **GET** /v1/vendors/categories | Retrieve all vendor categories
[**external_api_vendor_categories_get_vendor_category_by_id**](VendorsApi.md#external_api_vendor_categories_get_vendor_category_by_id) | **GET** /v1/vendors/categories/{vendorCategoryId} | Retrieve a vendor category
[**external_api_vendor_categories_update_vendor_category**](VendorsApi.md#external_api_vendor_categories_update_vendor_category) | **PUT** /v1/vendors/categories/{vendorCategoryId} | Update a vendor category
[**external_api_vendor_credits_get_vendor_credit**](VendorsApi.md#external_api_vendor_credits_get_vendor_credit) | **GET** /v1/vendors/{vendorId}/credits/{vendorCreditId} | Retrieve a credit
[**external_api_vendor_credits_write_create_vendor_credit**](VendorsApi.md#external_api_vendor_credits_write_create_vendor_credit) | **POST** /v1/vendors/{vendorId}/credits | Create a credit
[**external_api_vendor_notes_create_vendor_note**](VendorsApi.md#external_api_vendor_notes_create_vendor_note) | **POST** /v1/vendors/{vendorId}/notes | Create a note
[**external_api_vendor_notes_get_vendor_note_by_note_id**](VendorsApi.md#external_api_vendor_notes_get_vendor_note_by_note_id) | **GET** /v1/vendors/{vendorId}/notes/{noteId} | Retrieve a note
[**external_api_vendor_notes_get_vendor_notes**](VendorsApi.md#external_api_vendor_notes_get_vendor_notes) | **GET** /v1/vendors/{vendorId}/notes | Retrieve all notes
[**external_api_vendor_notes_update_vendor_note**](VendorsApi.md#external_api_vendor_notes_update_vendor_note) | **PUT** /v1/vendors/{vendorId}/notes/{noteId} | Update a note
[**external_api_vendor_refunds_get_vendor_refund**](VendorsApi.md#external_api_vendor_refunds_get_vendor_refund) | **GET** /v1/vendors/{vendorId}/refunds/{vendorRefundId} | Retrieve a refund
[**external_api_vendor_refunds_write_create_vendor_refund**](VendorsApi.md#external_api_vendor_refunds_write_create_vendor_refund) | **POST** /v1/vendors/{vendorId}/refunds | Create a refund
[**external_api_vendor_transactions_get_all_vendor_transactions**](VendorsApi.md#external_api_vendor_transactions_get_all_vendor_transactions) | **GET** /v1/vendors/{vendorId}/transactions | Retrieve all transactions
[**external_api_vendors_create_vendor**](VendorsApi.md#external_api_vendors_create_vendor) | **POST** /v1/vendors | Create a vendor
[**external_api_vendors_get_all_vendors**](VendorsApi.md#external_api_vendors_get_all_vendors) | **GET** /v1/vendors | Retrieve all vendors
[**external_api_vendors_get_vendor_by_id**](VendorsApi.md#external_api_vendors_get_vendor_by_id) | **GET** /v1/vendors/{vendorId} | Retrieve a vendor
[**external_api_vendors_update_vendor**](VendorsApi.md#external_api_vendors_update_vendor) | **PUT** /v1/vendors/{vendorId} | Update a vendor


# **external_api_vendor_categories_create_vendor_category**
> VendorCategoryMessage external_api_vendor_categories_create_vendor_category(vendor_category_save_message)

Create a vendor category

Creates a vendor category.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.vendor_category_message import VendorCategoryMessage
from buildium_sdk.models.vendor_category_save_message import VendorCategorySaveMessage
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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_category_save_message = buildium_sdk.VendorCategorySaveMessage() # VendorCategorySaveMessage | 

    try:
        # Create a vendor category
        api_response = await api_instance.external_api_vendor_categories_create_vendor_category(vendor_category_save_message)
        print("The response of VendorsApi->external_api_vendor_categories_create_vendor_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendor_categories_create_vendor_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_category_save_message** | [**VendorCategorySaveMessage**](VendorCategorySaveMessage.md)|  | 

### Return type

[**VendorCategoryMessage**](VendorCategoryMessage.md)

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

# **external_api_vendor_categories_get_all_vendor_categories**
> List[VendorCategoryMessage] external_api_vendor_categories_get_all_vendor_categories(orderby=orderby, offset=offset, limit=limit)

Retrieve all vendor categories

Retrieves a list of vendor categories.


<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.vendor_category_message import VendorCategoryMessage
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
    api_instance = buildium_sdk.VendorsApi(api_client)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all vendor categories
        api_response = await api_instance.external_api_vendor_categories_get_all_vendor_categories(orderby=orderby, offset=offset, limit=limit)
        print("The response of VendorsApi->external_api_vendor_categories_get_all_vendor_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendor_categories_get_all_vendor_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[VendorCategoryMessage]**](VendorCategoryMessage.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_vendor_categories_get_vendor_category_by_id**
> VendorCategoryMessage external_api_vendor_categories_get_vendor_category_by_id(vendor_category_id)

Retrieve a vendor category

Retrieves a specific vendor category.


<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.vendor_category_message import VendorCategoryMessage
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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_category_id = 56 # int | The vendor category identifier.

    try:
        # Retrieve a vendor category
        api_response = await api_instance.external_api_vendor_categories_get_vendor_category_by_id(vendor_category_id)
        print("The response of VendorsApi->external_api_vendor_categories_get_vendor_category_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendor_categories_get_vendor_category_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_category_id** | **int**| The vendor category identifier. | 

### Return type

[**VendorCategoryMessage**](VendorCategoryMessage.md)

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

# **external_api_vendor_categories_update_vendor_category**
> VendorCategoryMessage external_api_vendor_categories_update_vendor_category(vendor_category_id, vendor_category_save_message)

Update a vendor category

Updates a vendor category.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.vendor_category_message import VendorCategoryMessage
from buildium_sdk.models.vendor_category_save_message import VendorCategorySaveMessage
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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_category_id = 56 # int | 
    vendor_category_save_message = buildium_sdk.VendorCategorySaveMessage() # VendorCategorySaveMessage | 

    try:
        # Update a vendor category
        api_response = await api_instance.external_api_vendor_categories_update_vendor_category(vendor_category_id, vendor_category_save_message)
        print("The response of VendorsApi->external_api_vendor_categories_update_vendor_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendor_categories_update_vendor_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_category_id** | **int**|  | 
 **vendor_category_save_message** | [**VendorCategorySaveMessage**](VendorCategorySaveMessage.md)|  | 

### Return type

[**VendorCategoryMessage**](VendorCategoryMessage.md)

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

# **external_api_vendor_credits_get_vendor_credit**
> VendorCreditMessage external_api_vendor_credits_get_vendor_credit(vendor_id, vendor_credit_id)

Retrieve a credit

Retrieves a credit.
             

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.vendor_credit_message import VendorCreditMessage
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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_id = 56 # int | 
    vendor_credit_id = 56 # int | 

    try:
        # Retrieve a credit
        api_response = await api_instance.external_api_vendor_credits_get_vendor_credit(vendor_id, vendor_credit_id)
        print("The response of VendorsApi->external_api_vendor_credits_get_vendor_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendor_credits_get_vendor_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**|  | 
 **vendor_credit_id** | **int**|  | 

### Return type

[**VendorCreditMessage**](VendorCreditMessage.md)

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

# **external_api_vendor_credits_write_create_vendor_credit**
> VendorCreditMessage external_api_vendor_credits_write_create_vendor_credit(vendor_id, vendor_credit_post_message)

Create a credit

Creates a credit.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.vendor_credit_message import VendorCreditMessage
from buildium_sdk.models.vendor_credit_post_message import VendorCreditPostMessage
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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_id = 56 # int | 
    vendor_credit_post_message = buildium_sdk.VendorCreditPostMessage() # VendorCreditPostMessage | 

    try:
        # Create a credit
        api_response = await api_instance.external_api_vendor_credits_write_create_vendor_credit(vendor_id, vendor_credit_post_message)
        print("The response of VendorsApi->external_api_vendor_credits_write_create_vendor_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendor_credits_write_create_vendor_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**|  | 
 **vendor_credit_post_message** | [**VendorCreditPostMessage**](VendorCreditPostMessage.md)|  | 

### Return type

[**VendorCreditMessage**](VendorCreditMessage.md)

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

# **external_api_vendor_notes_create_vendor_note**
> NoteMessage external_api_vendor_notes_create_vendor_note(vendor_id, note_post_message)

Create a note

Creates a vendor note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View` `Edit`

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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_id = 56 # int | 
    note_post_message = buildium_sdk.NotePostMessage() # NotePostMessage | 

    try:
        # Create a note
        api_response = await api_instance.external_api_vendor_notes_create_vendor_note(vendor_id, note_post_message)
        print("The response of VendorsApi->external_api_vendor_notes_create_vendor_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendor_notes_create_vendor_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**|  | 
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

# **external_api_vendor_notes_get_vendor_note_by_note_id**
> NoteMessage external_api_vendor_notes_get_vendor_note_by_note_id(vendor_id, note_id)

Retrieve a note

Retrieves a vendor note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View`

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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_id = 56 # int | 
    note_id = 56 # int | 

    try:
        # Retrieve a note
        api_response = await api_instance.external_api_vendor_notes_get_vendor_note_by_note_id(vendor_id, note_id)
        print("The response of VendorsApi->external_api_vendor_notes_get_vendor_note_by_note_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendor_notes_get_vendor_note_by_note_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**|  | 
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

# **external_api_vendor_notes_get_vendor_notes**
> List[NoteMessage] external_api_vendor_notes_get_vendor_notes(vendor_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)

Retrieve all notes

Retrieves all vendor notes.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View`

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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_id = 56 # int | 
    updateddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    updateddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    lastupdatedbyuserid = 56 # int | Filters results to only notes that were last updated by the specified user identifier. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all notes
        api_response = await api_instance.external_api_vendor_notes_get_vendor_notes(vendor_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)
        print("The response of VendorsApi->external_api_vendor_notes_get_vendor_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendor_notes_get_vendor_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**|  | 
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

# **external_api_vendor_notes_update_vendor_note**
> NoteMessage external_api_vendor_notes_update_vendor_note(vendor_id, note_id, note_put_message)

Update a note

Updates a vendor note.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View` `Edit`

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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_id = 56 # int | 
    note_id = 56 # int | 
    note_put_message = buildium_sdk.NotePutMessage() # NotePutMessage | 

    try:
        # Update a note
        api_response = await api_instance.external_api_vendor_notes_update_vendor_note(vendor_id, note_id, note_put_message)
        print("The response of VendorsApi->external_api_vendor_notes_update_vendor_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendor_notes_update_vendor_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**|  | 
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

# **external_api_vendor_refunds_get_vendor_refund**
> VendorRefundMessage external_api_vendor_refunds_get_vendor_refund(vendor_id, vendor_refund_id)

Retrieve a refund

Retrieves a refund.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.vendor_refund_message import VendorRefundMessage
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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_id = 56 # int | 
    vendor_refund_id = 56 # int | 

    try:
        # Retrieve a refund
        api_response = await api_instance.external_api_vendor_refunds_get_vendor_refund(vendor_id, vendor_refund_id)
        print("The response of VendorsApi->external_api_vendor_refunds_get_vendor_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendor_refunds_get_vendor_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**|  | 
 **vendor_refund_id** | **int**|  | 

### Return type

[**VendorRefundMessage**](VendorRefundMessage.md)

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

# **external_api_vendor_refunds_write_create_vendor_refund**
> VendorRefundMessage external_api_vendor_refunds_write_create_vendor_refund(vendor_id, vendor_refund_post_message)

Create a refund

Creates a refund.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View` `Edit`
            <span class="permissionBlock">Accounting > Bank Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.vendor_refund_message import VendorRefundMessage
from buildium_sdk.models.vendor_refund_post_message import VendorRefundPostMessage
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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_id = 56 # int | 
    vendor_refund_post_message = buildium_sdk.VendorRefundPostMessage() # VendorRefundPostMessage | 

    try:
        # Create a refund
        api_response = await api_instance.external_api_vendor_refunds_write_create_vendor_refund(vendor_id, vendor_refund_post_message)
        print("The response of VendorsApi->external_api_vendor_refunds_write_create_vendor_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendor_refunds_write_create_vendor_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**|  | 
 **vendor_refund_post_message** | [**VendorRefundPostMessage**](VendorRefundPostMessage.md)|  | 

### Return type

[**VendorRefundMessage**](VendorRefundMessage.md)

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

# **external_api_vendor_transactions_get_all_vendor_transactions**
> List[VendorTransactionMessage] external_api_vendor_transactions_get_all_vendor_transactions(transactiondatefrom, transactiondateto, vendor_id, transactiontypes=transactiontypes, referencenumber=referencenumber, memo=memo, orderby=orderby, offset=offset, limit=limit)

Retrieve all transactions

Retrieves all transactions for a given vendor.


<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View`

<span class="permissionBlock">Accounting > General Ledger Transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.vendor_transaction_message import VendorTransactionMessage
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
    api_instance = buildium_sdk.VendorsApi(api_client)
    transactiondatefrom = '2013-10-20' # date | Filters results to any vendor transaction whose entry date that is greater than or equal to the specified value. The maximum date range is 365 days.
    transactiondateto = '2013-10-20' # date | Filters results to any vendor transaction whose entry date is less than or equal to the specified value. The maximum date range is 365 days.
    vendor_id = 56 # int | 
    transactiontypes = ['transactiontypes_example'] # List[str] | Filters results to any vendor transaction whose vendor transaction type matches the specified status. If no type is specified, vendor transactions with any type will be returned. (optional)
    referencenumber = 'referencenumber_example' # str | Filters results to vendor transaction whose reference number contains the specified value. The reference number cannot exceed 40 characters. (optional)
    memo = 'memo_example' # str | Filters results to vendor transaction whose memo contains the specified value. The memo cannot exceed 40 characters. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all transactions
        api_response = await api_instance.external_api_vendor_transactions_get_all_vendor_transactions(transactiondatefrom, transactiondateto, vendor_id, transactiontypes=transactiontypes, referencenumber=referencenumber, memo=memo, orderby=orderby, offset=offset, limit=limit)
        print("The response of VendorsApi->external_api_vendor_transactions_get_all_vendor_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendor_transactions_get_all_vendor_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactiondatefrom** | **date**| Filters results to any vendor transaction whose entry date that is greater than or equal to the specified value. The maximum date range is 365 days. | 
 **transactiondateto** | **date**| Filters results to any vendor transaction whose entry date is less than or equal to the specified value. The maximum date range is 365 days. | 
 **vendor_id** | **int**|  | 
 **transactiontypes** | [**List[str]**](str.md)| Filters results to any vendor transaction whose vendor transaction type matches the specified status. If no type is specified, vendor transactions with any type will be returned. | [optional] 
 **referencenumber** | **str**| Filters results to vendor transaction whose reference number contains the specified value. The reference number cannot exceed 40 characters. | [optional] 
 **memo** | **str**| Filters results to vendor transaction whose memo contains the specified value. The memo cannot exceed 40 characters. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[VendorTransactionMessage]**](VendorTransactionMessage.md)

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

# **external_api_vendors_create_vendor**
> VendorMessage external_api_vendors_create_vendor(vendor_post_message)

Create a vendor

Creates a vendor.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.vendor_message import VendorMessage
from buildium_sdk.models.vendor_post_message import VendorPostMessage
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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_post_message = buildium_sdk.VendorPostMessage() # VendorPostMessage | 

    try:
        # Create a vendor
        api_response = await api_instance.external_api_vendors_create_vendor(vendor_post_message)
        print("The response of VendorsApi->external_api_vendors_create_vendor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendors_create_vendor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_post_message** | [**VendorPostMessage**](VendorPostMessage.md)|  | 

### Return type

[**VendorMessage**](VendorMessage.md)

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

# **external_api_vendors_get_all_vendors**
> List[VendorMessage] external_api_vendors_get_all_vendors(status=status, email=email, website=website, name=name, insuranceexpiration=insuranceexpiration, phone=phone, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)

Retrieve all vendors

Retrieves a list of vendors.


<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.vendor_message import VendorMessage
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
    api_instance = buildium_sdk.VendorsApi(api_client)
    status = 'status_example' # str | Filters results by the status of the vendor. If no status is specified both `active` and `inactive` vendors will be returned. (optional)
    email = 'email_example' # str | Filters results to any vendor whose email *contains* the specified value. (optional)
    website = 'website_example' # str | Filters results to any vendor whose website *contains* the specified value. (optional)
    name = 'name_example' # str | Filters results to any vendor whose name *contains* the specified value. (optional)
    insuranceexpiration = 'insuranceexpiration_example' # str | Filters results to any vendor whose insurance will expire in the specified date range. (optional)
    phone = 'phone_example' # str | Filters results to any vendor who has a phone number that *contains* the specified value. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any vendors that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any vendors that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all vendors
        api_response = await api_instance.external_api_vendors_get_all_vendors(status=status, email=email, website=website, name=name, insuranceexpiration=insuranceexpiration, phone=phone, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)
        print("The response of VendorsApi->external_api_vendors_get_all_vendors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendors_get_all_vendors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filters results by the status of the vendor. If no status is specified both &#x60;active&#x60; and &#x60;inactive&#x60; vendors will be returned. | [optional] 
 **email** | **str**| Filters results to any vendor whose email *contains* the specified value. | [optional] 
 **website** | **str**| Filters results to any vendor whose website *contains* the specified value. | [optional] 
 **name** | **str**| Filters results to any vendor whose name *contains* the specified value. | [optional] 
 **insuranceexpiration** | **str**| Filters results to any vendor whose insurance will expire in the specified date range. | [optional] 
 **phone** | **str**| Filters results to any vendor who has a phone number that *contains* the specified value. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to any vendors that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to any vendors that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[VendorMessage]**](VendorMessage.md)

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

# **external_api_vendors_get_vendor_by_id**
> VendorMessage external_api_vendors_get_vendor_by_id(vendor_id)

Retrieve a vendor

Retrieve a specific vendor.


<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.vendor_message import VendorMessage
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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_id = 56 # int | The vendor identifier.

    try:
        # Retrieve a vendor
        api_response = await api_instance.external_api_vendors_get_vendor_by_id(vendor_id)
        print("The response of VendorsApi->external_api_vendors_get_vendor_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendors_get_vendor_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| The vendor identifier. | 

### Return type

[**VendorMessage**](VendorMessage.md)

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

# **external_api_vendors_update_vendor**
> VendorMessage external_api_vendors_update_vendor(vendor_id, vendor_put_message)

Update a vendor

Updates a vendor.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Maintenance > Vendors</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.vendor_message import VendorMessage
from buildium_sdk.models.vendor_put_message import VendorPutMessage
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
    api_instance = buildium_sdk.VendorsApi(api_client)
    vendor_id = 56 # int | 
    vendor_put_message = buildium_sdk.VendorPutMessage() # VendorPutMessage | 

    try:
        # Update a vendor
        api_response = await api_instance.external_api_vendors_update_vendor(vendor_id, vendor_put_message)
        print("The response of VendorsApi->external_api_vendors_update_vendor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->external_api_vendors_update_vendor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**|  | 
 **vendor_put_message** | [**VendorPutMessage**](VendorPutMessage.md)|  | 

### Return type

[**VendorMessage**](VendorMessage.md)

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

