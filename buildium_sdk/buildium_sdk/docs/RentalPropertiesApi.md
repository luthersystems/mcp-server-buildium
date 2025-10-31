# buildium_sdk.RentalPropertiesApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_rental_epay_settings_get_e_pay_settings_for_rental_property**](RentalPropertiesApi.md#external_api_rental_epay_settings_get_e_pay_settings_for_rental_property) | **GET** /v1/rentals/{propertyId}/epaysettings | Retrieve ePay settings
[**external_api_rental_epay_settings_update_e_pay_settings_for_rental**](RentalPropertiesApi.md#external_api_rental_epay_settings_update_e_pay_settings_for_rental) | **PUT** /v1/rentals/{propertyId}/epaysettings | Update ePay settings
[**external_api_rental_features_get_features_by_rental_property_id**](RentalPropertiesApi.md#external_api_rental_features_get_features_by_rental_property_id) | **GET** /v1/rentals/{propertyId}/amenities | Retrieve all amenities
[**external_api_rental_features_update_rental_features**](RentalPropertiesApi.md#external_api_rental_features_update_rental_features) | **PUT** /v1/rentals/{propertyId}/amenities | Update amenities
[**external_api_rental_image_download_requests_get_rental_image_download_url_by_id**](RentalPropertiesApi.md#external_api_rental_image_download_requests_get_rental_image_download_url_by_id) | **POST** /v1/rentals/{propertyId}/images/{imageId}/downloadrequests | Download a property image
[**external_api_rental_image_order_reorder_rental_images**](RentalPropertiesApi.md#external_api_rental_image_order_reorder_rental_images) | **PUT** /v1/rentals/{propertyId}/images/order | Update property image order
[**external_api_rental_image_upload_requests_create_upload_file_request_async**](RentalPropertiesApi.md#external_api_rental_image_upload_requests_create_upload_file_request_async) | **POST** /v1/rentals/{propertyId}/images/uploadrequests | Upload a rental image
[**external_api_rental_image_video_link_requests_create_video_link_request**](RentalPropertiesApi.md#external_api_rental_image_video_link_requests_create_video_link_request) | **POST** /v1/rentals/{propertyId}/images/videolinkrequests | Create an image for a rental using a video link
[**external_api_rental_images_delete_rental_image**](RentalPropertiesApi.md#external_api_rental_images_delete_rental_image) | **DELETE** /v1/rentals/{propertyId}/images/{imageId} | Delete a property image
[**external_api_rental_images_get_rental_image_by_id**](RentalPropertiesApi.md#external_api_rental_images_get_rental_image_by_id) | **GET** /v1/rentals/{propertyId}/images/{imageId} | Retrieve a property image
[**external_api_rental_images_get_rental_images**](RentalPropertiesApi.md#external_api_rental_images_get_rental_images) | **GET** /v1/rentals/{propertyId}/images | Retrieve all property images
[**external_api_rental_images_update_rental_image**](RentalPropertiesApi.md#external_api_rental_images_update_rental_image) | **PUT** /v1/rentals/{propertyId}/images/{imageId} | Update a property image
[**external_api_rental_notes_create_rental_property_note**](RentalPropertiesApi.md#external_api_rental_notes_create_rental_property_note) | **POST** /v1/rentals/{propertyId}/notes | Create a note
[**external_api_rental_notes_get_rental_note_by_note_id**](RentalPropertiesApi.md#external_api_rental_notes_get_rental_note_by_note_id) | **GET** /v1/rentals/{propertyId}/notes/{noteId} | Retrieve a note
[**external_api_rental_notes_get_rental_notes**](RentalPropertiesApi.md#external_api_rental_notes_get_rental_notes) | **GET** /v1/rentals/{propertyId}/notes | Retrieve all notes
[**external_api_rental_notes_update_rental_property_note**](RentalPropertiesApi.md#external_api_rental_notes_update_rental_property_note) | **PUT** /v1/rentals/{propertyId}/notes/{noteId} | Update a note
[**external_api_rental_preferred_vendors_get_rental_preferred_vendors**](RentalPropertiesApi.md#external_api_rental_preferred_vendors_get_rental_preferred_vendors) | **GET** /v1/rentals/{propertyId}/vendors | Retrieve all preferred vendors
[**external_api_rental_preferred_vendors_update_rental_preferred_vendors**](RentalPropertiesApi.md#external_api_rental_preferred_vendors_update_rental_preferred_vendors) | **PUT** /v1/rentals/{propertyId}/vendors | Update preferred vendors
[**external_api_rentals_active_status_inactivate_rental_property**](RentalPropertiesApi.md#external_api_rentals_active_status_inactivate_rental_property) | **POST** /v1/rentals/{propertyId}/inactivationrequest | Inactivate a property
[**external_api_rentals_active_status_reactivate_rental_property**](RentalPropertiesApi.md#external_api_rentals_active_status_reactivate_rental_property) | **POST** /v1/rentals/{propertyId}/reactivationrequest | Reactivate a property
[**external_api_rentals_create_rental_property**](RentalPropertiesApi.md#external_api_rentals_create_rental_property) | **POST** /v1/rentals | Create a property
[**external_api_rentals_get_all_rentals**](RentalPropertiesApi.md#external_api_rentals_get_all_rentals) | **GET** /v1/rentals | Retrieve all properties
[**external_api_rentals_get_rental_by_id**](RentalPropertiesApi.md#external_api_rentals_get_rental_by_id) | **GET** /v1/rentals/{propertyId} | Retrieve a property
[**external_api_rentals_update_rental_property**](RentalPropertiesApi.md#external_api_rentals_update_rental_property) | **PUT** /v1/rentals/{propertyId} | Update a property


# **external_api_rental_epay_settings_get_e_pay_settings_for_rental_property**
> EPaySettingsMessage external_api_rental_epay_settings_get_e_pay_settings_for_rental_property(property_id)

Retrieve ePay settings

Retrieves ePay settings for a rental property.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 

    try:
        # Retrieve ePay settings
        api_response = await api_instance.external_api_rental_epay_settings_get_e_pay_settings_for_rental_property(property_id)
        print("The response of RentalPropertiesApi->external_api_rental_epay_settings_get_e_pay_settings_for_rental_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_epay_settings_get_e_pay_settings_for_rental_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 

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
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_rental_epay_settings_update_e_pay_settings_for_rental**
> EPaySettingsMessage external_api_rental_epay_settings_update_e_pay_settings_for_rental(property_id, e_pay_settings_put_message)

Update ePay settings

Updates ePay settings for a rental property.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    e_pay_settings_put_message = buildium_sdk.EPaySettingsPutMessage() # EPaySettingsPutMessage | 

    try:
        # Update ePay settings
        api_response = await api_instance.external_api_rental_epay_settings_update_e_pay_settings_for_rental(property_id, e_pay_settings_put_message)
        print("The response of RentalPropertiesApi->external_api_rental_epay_settings_update_e_pay_settings_for_rental:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_epay_settings_update_e_pay_settings_for_rental: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
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

# **external_api_rental_features_get_features_by_rental_property_id**
> RentalFeaturesMessage external_api_rental_features_get_features_by_rental_property_id(property_id)

Retrieve all amenities

Retrieve all the amenities for a rental property.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_features_message import RentalFeaturesMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 

    try:
        # Retrieve all amenities
        api_response = await api_instance.external_api_rental_features_get_features_by_rental_property_id(property_id)
        print("The response of RentalPropertiesApi->external_api_rental_features_get_features_by_rental_property_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_features_get_features_by_rental_property_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 

### Return type

[**RentalFeaturesMessage**](RentalFeaturesMessage.md)

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

# **external_api_rental_features_update_rental_features**
> RentalFeaturesMessage external_api_rental_features_update_rental_features(property_id, rental_features_put_message)

Update amenities

Updates the amenities for a rental property.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_features_message import RentalFeaturesMessage
from buildium_sdk.models.rental_features_put_message import RentalFeaturesPutMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    rental_features_put_message = buildium_sdk.RentalFeaturesPutMessage() # RentalFeaturesPutMessage | 

    try:
        # Update amenities
        api_response = await api_instance.external_api_rental_features_update_rental_features(property_id, rental_features_put_message)
        print("The response of RentalPropertiesApi->external_api_rental_features_update_rental_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_features_update_rental_features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
 **rental_features_put_message** | [**RentalFeaturesPutMessage**](RentalFeaturesPutMessage.md)|  | 

### Return type

[**RentalFeaturesMessage**](RentalFeaturesMessage.md)

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

# **external_api_rental_image_download_requests_get_rental_image_download_url_by_id**
> FileDownloadMessage external_api_rental_image_download_requests_get_rental_image_download_url_by_id(property_id, image_id)

Download a property image

Use this endpoint to create a temporary URL that can be used to download a property image. This URL expires after 5 minutes.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_download_message import FileDownloadMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    image_id = 56 # int | 

    try:
        # Download a property image
        api_response = await api_instance.external_api_rental_image_download_requests_get_rental_image_download_url_by_id(property_id, image_id)
        print("The response of RentalPropertiesApi->external_api_rental_image_download_requests_get_rental_image_download_url_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_image_download_requests_get_rental_image_download_url_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
 **image_id** | **int**|  | 

### Return type

[**FileDownloadMessage**](FileDownloadMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - The location to retrieve the created resource. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_rental_image_order_reorder_rental_images**
> List[RentalImageMessage] external_api_rental_image_order_reorder_rental_images(property_id, image_reorder_request_put_message)

Update property image order

Updates the image display order within the Buildium web application and in any associated rental listings.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.image_reorder_request_put_message import ImageReorderRequestPutMessage
from buildium_sdk.models.rental_image_message import RentalImageMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    image_reorder_request_put_message = buildium_sdk.ImageReorderRequestPutMessage() # ImageReorderRequestPutMessage | 

    try:
        # Update property image order
        api_response = await api_instance.external_api_rental_image_order_reorder_rental_images(property_id, image_reorder_request_put_message)
        print("The response of RentalPropertiesApi->external_api_rental_image_order_reorder_rental_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_image_order_reorder_rental_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
 **image_reorder_request_put_message** | [**ImageReorderRequestPutMessage**](ImageReorderRequestPutMessage.md)|  | 

### Return type

[**List[RentalImageMessage]**](RentalImageMessage.md)

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

# **external_api_rental_image_upload_requests_create_upload_file_request_async**
> FileUploadTicketMessage external_api_rental_image_upload_requests_create_upload_file_request_async(property_id, listing_entity_file_post_message)

Upload a rental image

Uploads an image and associates it to the specified rental record.
            

Uploading a file requires making two API requests. Each step is outlined below.
            

<strong>Step 1 - Save file metadata</strong>

            The first step in the file upload process is to submit the file metadata to `/v1/rentals/{rentalId}/images/uploadrequests`. The response of this call will contain a URL and a collection of form data that will be used in step 2 to generate the request for the file binary upload.
            

<strong>NOTE:</strong> The response data will expire after 5 minutes. The file metadata will not be saved in the Buildium system if step 2 of this process is not completed successfully.
            

<strong>Step 2 - Upload the file binary</strong>

            Uploading the file binary will require using the response from step 1 to form a POST request to the Buildium file provider. Follow these steps to create the request:
            

            1. Form a POST request using the value of the `BucketUrl` property as the URL. 
            


            2. Set the `Content-Type` header to `multipart/form-data`.
            


            3. Copy the fields from the `FormData`  property to this request as form-data key/value pairs.
            
<strong>NOTE:</strong> These values must added to the request form-data in the order they were received in the response.
            


            4. Lastly create a form-data key named `file` and set the value to the file binary.
            
<strong>NOTE:</strong> This must be the last field in the form-data list.
            

This image shows what the POST request should look like if you're using Postman:
            <img src="file-upload-example.png" />


            5. Send the POST request! A successful request will return with a `204 - NO CONTENT` HTTP response code. For any failure responses, please refer to <a target="_blank" href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#RESTErrorResponses">AWS documentation</a> on REST error responses.
            

<strong>NOTE:</strong> The file identifier is not generated in this response. To retrieve the file identifier, call `/v1/files` and pass the `PhysicalFileName` value received from the response of this endpoint into the `physicalfilenames` query parameter.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_upload_ticket_message import FileUploadTicketMessage
from buildium_sdk.models.listing_entity_file_post_message import ListingEntityFilePostMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    listing_entity_file_post_message = buildium_sdk.ListingEntityFilePostMessage() # ListingEntityFilePostMessage | 

    try:
        # Upload a rental image
        api_response = await api_instance.external_api_rental_image_upload_requests_create_upload_file_request_async(property_id, listing_entity_file_post_message)
        print("The response of RentalPropertiesApi->external_api_rental_image_upload_requests_create_upload_file_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_image_upload_requests_create_upload_file_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
 **listing_entity_file_post_message** | [**ListingEntityFilePostMessage**](ListingEntityFilePostMessage.md)|  | 

### Return type

[**FileUploadTicketMessage**](FileUploadTicketMessage.md)

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

# **external_api_rental_image_video_link_requests_create_video_link_request**
> RentalImageMessage external_api_rental_image_video_link_requests_create_video_link_request(property_id, video_link_request_post_message)

Create an image for a rental using a video link

Creates an image for a rental using a video link.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_image_message import RentalImageMessage
from buildium_sdk.models.video_link_request_post_message import VideoLinkRequestPostMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    video_link_request_post_message = buildium_sdk.VideoLinkRequestPostMessage() # VideoLinkRequestPostMessage | 

    try:
        # Create an image for a rental using a video link
        api_response = await api_instance.external_api_rental_image_video_link_requests_create_video_link_request(property_id, video_link_request_post_message)
        print("The response of RentalPropertiesApi->external_api_rental_image_video_link_requests_create_video_link_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_image_video_link_requests_create_video_link_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
 **video_link_request_post_message** | [**VideoLinkRequestPostMessage**](VideoLinkRequestPostMessage.md)|  | 

### Return type

[**RentalImageMessage**](RentalImageMessage.md)

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

# **external_api_rental_images_delete_rental_image**
> external_api_rental_images_delete_rental_image(property_id, image_id)

Delete a property image

Deletes a rental property image.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit` `Delete`

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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    image_id = 56 # int | 

    try:
        # Delete a property image
        await api_instance.external_api_rental_images_delete_rental_image(property_id, image_id)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_images_delete_rental_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
 **image_id** | **int**|  | 

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

# **external_api_rental_images_get_rental_image_by_id**
> RentalImageMessage external_api_rental_images_get_rental_image_by_id(property_id, image_id)

Retrieve a property image

Retrieves a rental property image.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_image_message import RentalImageMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    image_id = 56 # int | 

    try:
        # Retrieve a property image
        api_response = await api_instance.external_api_rental_images_get_rental_image_by_id(property_id, image_id)
        print("The response of RentalPropertiesApi->external_api_rental_images_get_rental_image_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_images_get_rental_image_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
 **image_id** | **int**|  | 

### Return type

[**RentalImageMessage**](RentalImageMessage.md)

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

# **external_api_rental_images_get_rental_images**
> List[RentalImageMessage] external_api_rental_images_get_rental_images(property_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all property images

Retrieves all images for a rental property. Note this endpoint will only return file metadata such as file names and descriptions. To download files make requests to the [Download File](#tag/Rental-Properties/operation/ExternalApiRentalImageDownloadRequests_GetRentalImageDownloadUrlById) endpoint.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_image_message import RentalImageMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all property images
        api_response = await api_instance.external_api_rental_images_get_rental_images(property_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of RentalPropertiesApi->external_api_rental_images_get_rental_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_images_get_rental_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[RentalImageMessage]**](RentalImageMessage.md)

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

# **external_api_rental_images_update_rental_image**
> RentalImageMessage external_api_rental_images_update_rental_image(property_id, image_id, rental_image_put_message)

Update a property image

Updates a rental property image.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_image_message import RentalImageMessage
from buildium_sdk.models.rental_image_put_message import RentalImagePutMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    image_id = 56 # int | 
    rental_image_put_message = buildium_sdk.RentalImagePutMessage() # RentalImagePutMessage | 

    try:
        # Update a property image
        api_response = await api_instance.external_api_rental_images_update_rental_image(property_id, image_id, rental_image_put_message)
        print("The response of RentalPropertiesApi->external_api_rental_images_update_rental_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_images_update_rental_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
 **image_id** | **int**|  | 
 **rental_image_put_message** | [**RentalImagePutMessage**](RentalImagePutMessage.md)|  | 

### Return type

[**RentalImageMessage**](RentalImageMessage.md)

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

# **external_api_rental_notes_create_rental_property_note**
> NoteMessage external_api_rental_notes_create_rental_property_note(property_id, note_post_message)

Create a note

Creates a note.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    note_post_message = buildium_sdk.NotePostMessage() # NotePostMessage | 

    try:
        # Create a note
        api_response = await api_instance.external_api_rental_notes_create_rental_property_note(property_id, note_post_message)
        print("The response of RentalPropertiesApi->external_api_rental_notes_create_rental_property_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_notes_create_rental_property_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
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

# **external_api_rental_notes_get_rental_note_by_note_id**
> NoteMessage external_api_rental_notes_get_rental_note_by_note_id(property_id, note_id)

Retrieve a note

Retrieves a note.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    note_id = 56 # int | 

    try:
        # Retrieve a note
        api_response = await api_instance.external_api_rental_notes_get_rental_note_by_note_id(property_id, note_id)
        print("The response of RentalPropertiesApi->external_api_rental_notes_get_rental_note_by_note_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_notes_get_rental_note_by_note_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
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

# **external_api_rental_notes_get_rental_notes**
> List[NoteMessage] external_api_rental_notes_get_rental_notes(property_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)

Retrieve all notes

Retrieves all notes.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    updateddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    updateddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    lastupdatedbyuserid = 56 # int | Filters results to only notes that were last updated by the specified user identifier. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all notes
        api_response = await api_instance.external_api_rental_notes_get_rental_notes(property_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)
        print("The response of RentalPropertiesApi->external_api_rental_notes_get_rental_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_notes_get_rental_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
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

# **external_api_rental_notes_update_rental_property_note**
> NoteMessage external_api_rental_notes_update_rental_property_note(property_id, note_id, note_put_message)

Update a note

Updates a note.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    note_id = 56 # int | 
    note_put_message = buildium_sdk.NotePutMessage() # NotePutMessage | 

    try:
        # Update a note
        api_response = await api_instance.external_api_rental_notes_update_rental_property_note(property_id, note_id, note_put_message)
        print("The response of RentalPropertiesApi->external_api_rental_notes_update_rental_property_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_notes_update_rental_property_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
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

# **external_api_rental_preferred_vendors_get_rental_preferred_vendors**
> List[RentalPreferredVendorMessage] external_api_rental_preferred_vendors_get_rental_preferred_vendors(property_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all preferred vendors

Retrieves all preferred vendors.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`
            
<span class="permissionBlock">Maintenance > Vendors</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_preferred_vendor_message import RentalPreferredVendorMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all preferred vendors
        api_response = await api_instance.external_api_rental_preferred_vendors_get_rental_preferred_vendors(property_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of RentalPropertiesApi->external_api_rental_preferred_vendors_get_rental_preferred_vendors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_preferred_vendors_get_rental_preferred_vendors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[RentalPreferredVendorMessage]**](RentalPreferredVendorMessage.md)

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

# **external_api_rental_preferred_vendors_update_rental_preferred_vendors**
> List[RentalPreferredVendorMessage] external_api_rental_preferred_vendors_update_rental_preferred_vendors(property_id, rental_preferred_vendor_put_message)

Update preferred vendors

Updates preferred vendors.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`
            
<span class="permissionBlock">Maintenance > Vendors</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_preferred_vendor_message import RentalPreferredVendorMessage
from buildium_sdk.models.rental_preferred_vendor_put_message import RentalPreferredVendorPutMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    rental_preferred_vendor_put_message = buildium_sdk.RentalPreferredVendorPutMessage() # RentalPreferredVendorPutMessage | 

    try:
        # Update preferred vendors
        api_response = await api_instance.external_api_rental_preferred_vendors_update_rental_preferred_vendors(property_id, rental_preferred_vendor_put_message)
        print("The response of RentalPropertiesApi->external_api_rental_preferred_vendors_update_rental_preferred_vendors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rental_preferred_vendors_update_rental_preferred_vendors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
 **rental_preferred_vendor_put_message** | [**RentalPreferredVendorPutMessage**](RentalPreferredVendorPutMessage.md)|  | 

### Return type

[**List[RentalPreferredVendorMessage]**](RentalPreferredVendorMessage.md)

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

# **external_api_rentals_active_status_inactivate_rental_property**
> external_api_rentals_active_status_inactivate_rental_property(property_id)

Inactivate a property

Inactivates a rental property and all associated units. Any associated property's owners that have no remaining active properties will be inactivated.
            

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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 

    try:
        # Inactivate a property
        await api_instance.external_api_rentals_active_status_inactivate_rental_property(property_id)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rentals_active_status_inactivate_rental_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 

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
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_rentals_active_status_reactivate_rental_property**
> external_api_rentals_active_status_reactivate_rental_property(property_id)

Reactivate a property

Reactivates a rental property and all associated units. Any inactive rental owners assigned to this property will also be reactivated.
            

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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 

    try:
        # Reactivate a property
        await api_instance.external_api_rentals_active_status_reactivate_rental_property(property_id)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rentals_active_status_reactivate_rental_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 

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
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_rentals_create_rental_property**
> RentalMessage external_api_rentals_create_rental_property(rental_property_post_message)

Create a property

Creates a new rental property.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_message import RentalMessage
from buildium_sdk.models.rental_property_post_message import RentalPropertyPostMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    rental_property_post_message = buildium_sdk.RentalPropertyPostMessage() # RentalPropertyPostMessage | 

    try:
        # Create a property
        api_response = await api_instance.external_api_rentals_create_rental_property(rental_property_post_message)
        print("The response of RentalPropertiesApi->external_api_rentals_create_rental_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rentals_create_rental_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_property_post_message** | [**RentalPropertyPostMessage**](RentalPropertyPostMessage.md)|  | 

### Return type

[**RentalMessage**](RentalMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - The location to retrieve the created resource. <br>  * Link - Contains the location of the unit created for the rental property. <br>  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_rentals_get_all_rentals**
> List[RentalMessage] external_api_rentals_get_all_rentals(location=location, types=types, subtypes=subtypes, status=status, rentalownerids=rentalownerids, propertyids=propertyids, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)

Retrieve all properties

Retrieves a list of rental properties.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_message import RentalMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    location = 'location_example' # str | Filters results to only rental properties whose city or state *contains* the specified value. (optional)
    types = ['types_example'] # List[str] | Filters results by the rental type. If no type is provided all types will be returned. (optional)
    subtypes = ['subtypes_example'] # List[str] | Filters results by the sub type of the rental property. If no sub type is specified all sub types will be returned. (optional)
    status = 'status_example' # str | Filters results by the status of the rental property. If no status is specified both `active` and `inactive` rental properties will be returned. (optional)
    rentalownerids = [56] # List[int] | Filters results to only rental properties whose RentalOwnerId matches the specified Id. (optional)
    propertyids = [56] # List[int] | Filters results to only rental properties units whose Rental matches the specified Id. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any rental properties that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any rental properties that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all properties
        api_response = await api_instance.external_api_rentals_get_all_rentals(location=location, types=types, subtypes=subtypes, status=status, rentalownerids=rentalownerids, propertyids=propertyids, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)
        print("The response of RentalPropertiesApi->external_api_rentals_get_all_rentals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rentals_get_all_rentals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Filters results to only rental properties whose city or state *contains* the specified value. | [optional] 
 **types** | [**List[str]**](str.md)| Filters results by the rental type. If no type is provided all types will be returned. | [optional] 
 **subtypes** | [**List[str]**](str.md)| Filters results by the sub type of the rental property. If no sub type is specified all sub types will be returned. | [optional] 
 **status** | **str**| Filters results by the status of the rental property. If no status is specified both &#x60;active&#x60; and &#x60;inactive&#x60; rental properties will be returned. | [optional] 
 **rentalownerids** | [**List[int]**](int.md)| Filters results to only rental properties whose RentalOwnerId matches the specified Id. | [optional] 
 **propertyids** | [**List[int]**](int.md)| Filters results to only rental properties units whose Rental matches the specified Id. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to any rental properties that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to any rental properties that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[RentalMessage]**](RentalMessage.md)

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

# **external_api_rentals_get_rental_by_id**
> RentalMessage external_api_rentals_get_rental_by_id(property_id)

Retrieve a property

Retrieve a specific rental property.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_message import RentalMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | The rental property identifier.

    try:
        # Retrieve a property
        api_response = await api_instance.external_api_rentals_get_rental_by_id(property_id)
        print("The response of RentalPropertiesApi->external_api_rentals_get_rental_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rentals_get_rental_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**| The rental property identifier. | 

### Return type

[**RentalMessage**](RentalMessage.md)

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

# **external_api_rentals_update_rental_property**
> RentalMessage external_api_rentals_update_rental_property(property_id, rental_property_put_message)

Update a property

Updates a rental property.


<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_message import RentalMessage
from buildium_sdk.models.rental_property_put_message import RentalPropertyPutMessage
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
    api_instance = buildium_sdk.RentalPropertiesApi(api_client)
    property_id = 56 # int | 
    rental_property_put_message = buildium_sdk.RentalPropertyPutMessage() # RentalPropertyPutMessage | 

    try:
        # Update a property
        api_response = await api_instance.external_api_rentals_update_rental_property(property_id, rental_property_put_message)
        print("The response of RentalPropertiesApi->external_api_rentals_update_rental_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalPropertiesApi->external_api_rentals_update_rental_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**|  | 
 **rental_property_put_message** | [**RentalPropertyPutMessage**](RentalPropertyPutMessage.md)|  | 

### Return type

[**RentalMessage**](RentalMessage.md)

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

