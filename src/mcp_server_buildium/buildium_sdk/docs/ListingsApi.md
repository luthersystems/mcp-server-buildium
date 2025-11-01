# buildium_sdk.ListingsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_listing_contacts_create_listing_contact**](ListingsApi.md#external_api_listing_contacts_create_listing_contact) | **POST** /v1/rentals/units/listingcontacts | Create a listing contact
[**external_api_listing_contacts_get_all_listing_contacts**](ListingsApi.md#external_api_listing_contacts_get_all_listing_contacts) | **GET** /v1/rentals/units/listingcontacts | Retrieve all listing contacts
[**external_api_listing_contacts_get_listing_contact_by_id**](ListingsApi.md#external_api_listing_contacts_get_listing_contact_by_id) | **GET** /v1/rentals/units/listingcontacts/{listingContactId} | Retrieve a listing contact
[**external_api_listing_contacts_update_listing_contact**](ListingsApi.md#external_api_listing_contacts_update_listing_contact) | **PUT** /v1/rentals/units/listingcontacts/{listingContactId} | Update a listing contact
[**external_api_listings_delist_unit**](ListingsApi.md#external_api_listings_delist_unit) | **DELETE** /v1/rentals/units/{unitId}/listing | Delete a listing
[**external_api_listings_get_listing_for_unit_async**](ListingsApi.md#external_api_listings_get_listing_for_unit_async) | **GET** /v1/rentals/units/{unitId}/listing | Retrieve a listing
[**external_api_listings_get_listings_async**](ListingsApi.md#external_api_listings_get_listings_async) | **GET** /v1/rentals/units/listings | Retrieve all listings
[**external_api_listings_upsert_listings_async**](ListingsApi.md#external_api_listings_upsert_listings_async) | **PUT** /v1/rentals/units/{unitId}/listing | Create/Update a listing


# **external_api_listing_contacts_create_listing_contact**
> ListingContactMessage external_api_listing_contacts_create_listing_contact(listing_contact_save_message)

Create a listing contact

Create a listing contact. Note, at least one contact field (phone number, email or website) is required for the listing contact.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Listings</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.listing_contact_message import ListingContactMessage
from buildium_sdk.models.listing_contact_save_message import ListingContactSaveMessage
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
    api_instance = buildium_sdk.ListingsApi(api_client)
    listing_contact_save_message = buildium_sdk.ListingContactSaveMessage() # ListingContactSaveMessage | 

    try:
        # Create a listing contact
        api_response = await api_instance.external_api_listing_contacts_create_listing_contact(listing_contact_save_message)
        print("The response of ListingsApi->external_api_listing_contacts_create_listing_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->external_api_listing_contacts_create_listing_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_contact_save_message** | [**ListingContactSaveMessage**](ListingContactSaveMessage.md)|  | 

### Return type

[**ListingContactMessage**](ListingContactMessage.md)

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
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_listing_contacts_get_all_listing_contacts**
> List[ListingContactMessage] external_api_listing_contacts_get_all_listing_contacts(orderby=orderby, offset=offset, limit=limit)

Retrieve all listing contacts

Retrieves all listing contacts.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Listings</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.listing_contact_message import ListingContactMessage
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
    api_instance = buildium_sdk.ListingsApi(api_client)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all listing contacts
        api_response = await api_instance.external_api_listing_contacts_get_all_listing_contacts(orderby=orderby, offset=offset, limit=limit)
        print("The response of ListingsApi->external_api_listing_contacts_get_all_listing_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->external_api_listing_contacts_get_all_listing_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[ListingContactMessage]**](ListingContactMessage.md)

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

# **external_api_listing_contacts_get_listing_contact_by_id**
> ListingContactMessage external_api_listing_contacts_get_listing_contact_by_id(listing_contact_id)

Retrieve a listing contact

Retrieves a specific listing contact.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Listings</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.listing_contact_message import ListingContactMessage
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
    api_instance = buildium_sdk.ListingsApi(api_client)
    listing_contact_id = 56 # int | The listing contact identifier.

    try:
        # Retrieve a listing contact
        api_response = await api_instance.external_api_listing_contacts_get_listing_contact_by_id(listing_contact_id)
        print("The response of ListingsApi->external_api_listing_contacts_get_listing_contact_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->external_api_listing_contacts_get_listing_contact_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_contact_id** | **int**| The listing contact identifier. | 

### Return type

[**ListingContactMessage**](ListingContactMessage.md)

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

# **external_api_listing_contacts_update_listing_contact**
> ListingContactMessage external_api_listing_contacts_update_listing_contact(listing_contact_id, listing_contact_save_message)

Update a listing contact

Update a listing contact. Note, at least one contact field (phone number, email or website) is required for the listing contact.


<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Listings</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.listing_contact_message import ListingContactMessage
from buildium_sdk.models.listing_contact_save_message import ListingContactSaveMessage
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
    api_instance = buildium_sdk.ListingsApi(api_client)
    listing_contact_id = 56 # int | The listing contact identifier.
    listing_contact_save_message = buildium_sdk.ListingContactSaveMessage() # ListingContactSaveMessage | 

    try:
        # Update a listing contact
        api_response = await api_instance.external_api_listing_contacts_update_listing_contact(listing_contact_id, listing_contact_save_message)
        print("The response of ListingsApi->external_api_listing_contacts_update_listing_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->external_api_listing_contacts_update_listing_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_contact_id** | **int**| The listing contact identifier. | 
 **listing_contact_save_message** | [**ListingContactSaveMessage**](ListingContactSaveMessage.md)|  | 

### Return type

[**ListingContactMessage**](ListingContactMessage.md)

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
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_listings_delist_unit**
> external_api_listings_delist_unit(unit_id)

Delete a listing

Deleting a listing will immediately remove it from your Buildium public website. The listing will also be removed
from any syndicated sites within 24-48 hours.

Listings manually created on craigslist using the Buildium
guided tool will not be removed. The listing must be removed using craigslist's tools provided in your craigslist account.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Listings</span> - `View` `Edit` `Delete`

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
    api_instance = buildium_sdk.ListingsApi(api_client)
    unit_id = 56 # int | The rental property unit identifier.

    try:
        # Delete a listing
        await api_instance.external_api_listings_delist_unit(unit_id)
    except Exception as e:
        print("Exception when calling ListingsApi->external_api_listings_delist_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**| The rental property unit identifier. | 

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

# **external_api_listings_get_listing_for_unit_async**
> ListingMessage external_api_listings_get_listing_for_unit_async(unit_id)

Retrieve a listing

Retrieves a specific listing.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Listings</span> - `View`

<span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.listing_message import ListingMessage
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
    api_instance = buildium_sdk.ListingsApi(api_client)
    unit_id = 56 # int | The rental unit identifier.

    try:
        # Retrieve a listing
        api_response = await api_instance.external_api_listings_get_listing_for_unit_async(unit_id)
        print("The response of ListingsApi->external_api_listings_get_listing_for_unit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->external_api_listings_get_listing_for_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**| The rental unit identifier. | 

### Return type

[**ListingMessage**](ListingMessage.md)

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

# **external_api_listings_get_listings_async**
> List[ListingMessage] external_api_listings_get_listings_async(entitytype=entitytype, entityid=entityid, orderby=orderby, offset=offset, limit=limit)

Retrieve all listings

Retrieves all listings.


<span class="permissionBlock">Rentals > Listings</span> - `View`

<span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.listing_message import ListingMessage
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
    api_instance = buildium_sdk.ListingsApi(api_client)
    entitytype = 'entitytype_example' # str | Specifies the type of entity that `EntityId` refers to. (optional)
    entityid = 56 # int | Filters results to only listings that are associated with the specified entity id value. The id must be of the type specified in `EntityType` property. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all listings
        api_response = await api_instance.external_api_listings_get_listings_async(entitytype=entitytype, entityid=entityid, orderby=orderby, offset=offset, limit=limit)
        print("The response of ListingsApi->external_api_listings_get_listings_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->external_api_listings_get_listings_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitytype** | **str**| Specifies the type of entity that &#x60;EntityId&#x60; refers to. | [optional] 
 **entityid** | **int**| Filters results to only listings that are associated with the specified entity id value. The id must be of the type specified in &#x60;EntityType&#x60; property. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[ListingMessage]**](ListingMessage.md)

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

# **external_api_listings_upsert_listings_async**
> ListingMessage external_api_listings_upsert_listings_async(unit_id, listing_put_message)

Create/Update a listing

This endpoint can be used to both *create* and *update* a listing. If no listing exists for the unit one will be created, otherwise the existing listing will be updated. A unit can only ever have one active listing. 
 


Upon creation the listing will post immediately to your Buildium public website, and will post to the selected syndicated sites within 24-48 hours. Updates to the listing will appear immediately in your Buildium public website and propagated to syndicated sites within 24-48 hours. 



Note, the listing will automatically pull in the information, features, and media that exists for the property and unit details. 


<span class="permissionBlock">Rentals > Listings</span> - `View` `Edit`

<span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.listing_message import ListingMessage
from buildium_sdk.models.listing_put_message import ListingPutMessage
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
    api_instance = buildium_sdk.ListingsApi(api_client)
    unit_id = 56 # int | 
    listing_put_message = buildium_sdk.ListingPutMessage() # ListingPutMessage | 

    try:
        # Create/Update a listing
        api_response = await api_instance.external_api_listings_upsert_listings_async(unit_id, listing_put_message)
        print("The response of ListingsApi->external_api_listings_upsert_listings_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListingsApi->external_api_listings_upsert_listings_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
 **listing_put_message** | [**ListingPutMessage**](ListingPutMessage.md)|  | 

### Return type

[**ListingMessage**](ListingMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  * Location - The location to retrieve the created resource. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

