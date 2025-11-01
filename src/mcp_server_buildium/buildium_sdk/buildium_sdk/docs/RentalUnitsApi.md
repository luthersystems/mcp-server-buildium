# buildium_sdk.RentalUnitsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_rental_unit_amenities_get_features_for_rental_unit_by_id**](RentalUnitsApi.md#external_api_rental_unit_amenities_get_features_for_rental_unit_by_id) | **GET** /v1/rentals/units/{unitId}/amenities | Retrieve all amenities
[**external_api_rental_unit_amenities_update_rental_unit_features**](RentalUnitsApi.md#external_api_rental_unit_amenities_update_rental_unit_features) | **PUT** /v1/rentals/units/{unitId}/amenities | Update amenities
[**external_api_rental_unit_image_download_requests_get_rental_unit_image_download_url_by_id**](RentalUnitsApi.md#external_api_rental_unit_image_download_requests_get_rental_unit_image_download_url_by_id) | **POST** /v1/rentals/units/{unitId}/images/{imageId}/downloadrequests | Download a unit image
[**external_api_rental_unit_image_order_reorder_rental_unit_images**](RentalUnitsApi.md#external_api_rental_unit_image_order_reorder_rental_unit_images) | **PUT** /v1/rentals/units/{unitId}/images/order | Update unit image order
[**external_api_rental_unit_image_upload_requests_create_upload_file_request_async**](RentalUnitsApi.md#external_api_rental_unit_image_upload_requests_create_upload_file_request_async) | **POST** /v1/rentals/units/{unitId}/images/uploadrequests | Upload a unit image
[**external_api_rental_unit_image_video_link_requests_create_unit_video_link_request**](RentalUnitsApi.md#external_api_rental_unit_image_video_link_requests_create_unit_video_link_request) | **POST** /v1/rentals/units/{unitId}/images/videolinkrequests | Create an image for a unit using a video link
[**external_api_rental_unit_images_delete_rental_unit_image**](RentalUnitsApi.md#external_api_rental_unit_images_delete_rental_unit_image) | **DELETE** /v1/rentals/units/{unitId}/images/{imageId} | Delete a unit image
[**external_api_rental_unit_images_get_rental_unit_image_by_id**](RentalUnitsApi.md#external_api_rental_unit_images_get_rental_unit_image_by_id) | **GET** /v1/rentals/units/{unitId}/images/{imageId} | Retrieve a unit image
[**external_api_rental_unit_images_get_rental_unit_images**](RentalUnitsApi.md#external_api_rental_unit_images_get_rental_unit_images) | **GET** /v1/rentals/units/{unitId}/images | Retrieve all unit images
[**external_api_rental_unit_images_update_rental_unit_image**](RentalUnitsApi.md#external_api_rental_unit_images_update_rental_unit_image) | **PUT** /v1/rentals/units/{unitId}/images/{imageId} | Update a unit image
[**external_api_rental_unit_notes_create_rental_unit_note**](RentalUnitsApi.md#external_api_rental_unit_notes_create_rental_unit_note) | **POST** /v1/rentals/units/{unitId}/notes | Create a note
[**external_api_rental_unit_notes_get_rental_unit_note_by_note_id**](RentalUnitsApi.md#external_api_rental_unit_notes_get_rental_unit_note_by_note_id) | **GET** /v1/rentals/units/{unitId}/notes/{noteId} | Retrieve a note
[**external_api_rental_unit_notes_get_rental_unit_notes**](RentalUnitsApi.md#external_api_rental_unit_notes_get_rental_unit_notes) | **GET** /v1/rentals/units/{unitId}/notes | Retrieve all notes
[**external_api_rental_unit_notes_update_note_for_rental_unit**](RentalUnitsApi.md#external_api_rental_unit_notes_update_note_for_rental_unit) | **PUT** /v1/rentals/units/{unitId}/notes/{noteId} | Update a note
[**external_api_rental_units_create_rental_unit**](RentalUnitsApi.md#external_api_rental_units_create_rental_unit) | **POST** /v1/rentals/units | Create a unit
[**external_api_rental_units_get_all_rental_units**](RentalUnitsApi.md#external_api_rental_units_get_all_rental_units) | **GET** /v1/rentals/units | Retrieve all units
[**external_api_rental_units_get_rental_unit_by_id**](RentalUnitsApi.md#external_api_rental_units_get_rental_unit_by_id) | **GET** /v1/rentals/units/{unitId} | Retrieve a unit
[**external_api_rental_units_update_rental_unit**](RentalUnitsApi.md#external_api_rental_units_update_rental_unit) | **PUT** /v1/rentals/units/{unitId} | Update a unit


# **external_api_rental_unit_amenities_get_features_for_rental_unit_by_id**
> RentalUnitFeaturesMessage external_api_rental_unit_amenities_get_features_for_rental_unit_by_id(unit_id)

Retrieve all amenities

Retrieves all amenities for a rental unit.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_unit_features_message import RentalUnitFeaturesMessage
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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 

    try:
        # Retrieve all amenities
        api_response = await api_instance.external_api_rental_unit_amenities_get_features_for_rental_unit_by_id(unit_id)
        print("The response of RentalUnitsApi->external_api_rental_unit_amenities_get_features_for_rental_unit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_amenities_get_features_for_rental_unit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 

### Return type

[**RentalUnitFeaturesMessage**](RentalUnitFeaturesMessage.md)

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

# **external_api_rental_unit_amenities_update_rental_unit_features**
> RentalUnitFeaturesMessage external_api_rental_unit_amenities_update_rental_unit_features(unit_id, rental_unit_features_put_message)

Update amenities

Updates the amenities for a rental unit.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_unit_features_message import RentalUnitFeaturesMessage
from buildium_sdk.models.rental_unit_features_put_message import RentalUnitFeaturesPutMessage
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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 
    rental_unit_features_put_message = buildium_sdk.RentalUnitFeaturesPutMessage() # RentalUnitFeaturesPutMessage | 

    try:
        # Update amenities
        api_response = await api_instance.external_api_rental_unit_amenities_update_rental_unit_features(unit_id, rental_unit_features_put_message)
        print("The response of RentalUnitsApi->external_api_rental_unit_amenities_update_rental_unit_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_amenities_update_rental_unit_features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
 **rental_unit_features_put_message** | [**RentalUnitFeaturesPutMessage**](RentalUnitFeaturesPutMessage.md)|  | 

### Return type

[**RentalUnitFeaturesMessage**](RentalUnitFeaturesMessage.md)

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

# **external_api_rental_unit_image_download_requests_get_rental_unit_image_download_url_by_id**
> FileDownloadMessage external_api_rental_unit_image_download_requests_get_rental_unit_image_download_url_by_id(unit_id, image_id)

Download a unit image

Use this endpoint to create a temporary URL that can be used to download a unit image. This URL expires after 5 minutes.
            

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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 
    image_id = 56 # int | 

    try:
        # Download a unit image
        api_response = await api_instance.external_api_rental_unit_image_download_requests_get_rental_unit_image_download_url_by_id(unit_id, image_id)
        print("The response of RentalUnitsApi->external_api_rental_unit_image_download_requests_get_rental_unit_image_download_url_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_image_download_requests_get_rental_unit_image_download_url_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
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

# **external_api_rental_unit_image_order_reorder_rental_unit_images**
> List[RentalUnitImageMessage] external_api_rental_unit_image_order_reorder_rental_unit_images(unit_id, image_reorder_request_put_message)

Update unit image order

Updates the image display order within the Buildium web application and in any associated rental listings.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.image_reorder_request_put_message import ImageReorderRequestPutMessage
from buildium_sdk.models.rental_unit_image_message import RentalUnitImageMessage
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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 
    image_reorder_request_put_message = buildium_sdk.ImageReorderRequestPutMessage() # ImageReorderRequestPutMessage | 

    try:
        # Update unit image order
        api_response = await api_instance.external_api_rental_unit_image_order_reorder_rental_unit_images(unit_id, image_reorder_request_put_message)
        print("The response of RentalUnitsApi->external_api_rental_unit_image_order_reorder_rental_unit_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_image_order_reorder_rental_unit_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
 **image_reorder_request_put_message** | [**ImageReorderRequestPutMessage**](ImageReorderRequestPutMessage.md)|  | 

### Return type

[**List[RentalUnitImageMessage]**](RentalUnitImageMessage.md)

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

# **external_api_rental_unit_image_upload_requests_create_upload_file_request_async**
> FileUploadTicketMessage external_api_rental_unit_image_upload_requests_create_upload_file_request_async(unit_id, listing_entity_file_post_message)

Upload a unit image

Uploads an image and associates it to the specified unit record.
            

Uploading a file requires making two API requests. Each step is outlined below.
            

<strong>Step 1 - Save file metadata</strong>

            The first step in the file upload process is to submit the file metadata to `/v1/rentals/units/{unitId:int}/images/uploadrequests`. The response of this call will contain a URL and a collection of form data that will be used in step 2 to generate the request for the file binary upload.
            

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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 
    listing_entity_file_post_message = buildium_sdk.ListingEntityFilePostMessage() # ListingEntityFilePostMessage | 

    try:
        # Upload a unit image
        api_response = await api_instance.external_api_rental_unit_image_upload_requests_create_upload_file_request_async(unit_id, listing_entity_file_post_message)
        print("The response of RentalUnitsApi->external_api_rental_unit_image_upload_requests_create_upload_file_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_image_upload_requests_create_upload_file_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
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

# **external_api_rental_unit_image_video_link_requests_create_unit_video_link_request**
> RentalUnitImageMessage external_api_rental_unit_image_video_link_requests_create_unit_video_link_request(unit_id, video_link_request_post_message)

Create an image for a unit using a video link

Creates an image for a rental unit using a video link.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_unit_image_message import RentalUnitImageMessage
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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 
    video_link_request_post_message = buildium_sdk.VideoLinkRequestPostMessage() # VideoLinkRequestPostMessage | 

    try:
        # Create an image for a unit using a video link
        api_response = await api_instance.external_api_rental_unit_image_video_link_requests_create_unit_video_link_request(unit_id, video_link_request_post_message)
        print("The response of RentalUnitsApi->external_api_rental_unit_image_video_link_requests_create_unit_video_link_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_image_video_link_requests_create_unit_video_link_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
 **video_link_request_post_message** | [**VideoLinkRequestPostMessage**](VideoLinkRequestPostMessage.md)|  | 

### Return type

[**RentalUnitImageMessage**](RentalUnitImageMessage.md)

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

# **external_api_rental_unit_images_delete_rental_unit_image**
> external_api_rental_unit_images_delete_rental_unit_image(unit_id, image_id)

Delete a unit image

Deletes a unit image.
            

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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 
    image_id = 56 # int | 

    try:
        # Delete a unit image
        await api_instance.external_api_rental_unit_images_delete_rental_unit_image(unit_id, image_id)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_images_delete_rental_unit_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
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

# **external_api_rental_unit_images_get_rental_unit_image_by_id**
> RentalUnitImageMessage external_api_rental_unit_images_get_rental_unit_image_by_id(unit_id, image_id)

Retrieve a unit image

Retrieves a unit image.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_unit_image_message import RentalUnitImageMessage
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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 
    image_id = 56 # int | 

    try:
        # Retrieve a unit image
        api_response = await api_instance.external_api_rental_unit_images_get_rental_unit_image_by_id(unit_id, image_id)
        print("The response of RentalUnitsApi->external_api_rental_unit_images_get_rental_unit_image_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_images_get_rental_unit_image_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
 **image_id** | **int**|  | 

### Return type

[**RentalUnitImageMessage**](RentalUnitImageMessage.md)

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

# **external_api_rental_unit_images_get_rental_unit_images**
> List[RentalUnitImageMessage] external_api_rental_unit_images_get_rental_unit_images(unit_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all unit images

Retrieves all images for a unit. Note this endpoint will only return file metadata such as file names and descriptions. To download files make requests to the [Download File](#tag/Rental-Units/operation/ExternalApiRentalUnitImageDownloadRequests_GetRentalUnitImageDownloadUrlById) endpoint.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_unit_image_message import RentalUnitImageMessage
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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all unit images
        api_response = await api_instance.external_api_rental_unit_images_get_rental_unit_images(unit_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of RentalUnitsApi->external_api_rental_unit_images_get_rental_unit_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_images_get_rental_unit_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[RentalUnitImageMessage]**](RentalUnitImageMessage.md)

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

# **external_api_rental_unit_images_update_rental_unit_image**
> RentalImageMessage external_api_rental_unit_images_update_rental_unit_image(unit_id, image_id, rental_unit_image_put_message)

Update a unit image

Updates a unit image.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_image_message import RentalImageMessage
from buildium_sdk.models.rental_unit_image_put_message import RentalUnitImagePutMessage
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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 
    image_id = 56 # int | 
    rental_unit_image_put_message = buildium_sdk.RentalUnitImagePutMessage() # RentalUnitImagePutMessage | 

    try:
        # Update a unit image
        api_response = await api_instance.external_api_rental_unit_images_update_rental_unit_image(unit_id, image_id, rental_unit_image_put_message)
        print("The response of RentalUnitsApi->external_api_rental_unit_images_update_rental_unit_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_images_update_rental_unit_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
 **image_id** | **int**|  | 
 **rental_unit_image_put_message** | [**RentalUnitImagePutMessage**](RentalUnitImagePutMessage.md)|  | 

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

# **external_api_rental_unit_notes_create_rental_unit_note**
> NoteMessage external_api_rental_unit_notes_create_rental_unit_note(unit_id, note_post_message)

Create a note

Creates a rental unit note.
            

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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 
    note_post_message = buildium_sdk.NotePostMessage() # NotePostMessage | 

    try:
        # Create a note
        api_response = await api_instance.external_api_rental_unit_notes_create_rental_unit_note(unit_id, note_post_message)
        print("The response of RentalUnitsApi->external_api_rental_unit_notes_create_rental_unit_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_notes_create_rental_unit_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
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

# **external_api_rental_unit_notes_get_rental_unit_note_by_note_id**
> NoteMessage external_api_rental_unit_notes_get_rental_unit_note_by_note_id(unit_id, note_id)

Retrieve a note

Retrieves a rental unit note.
            

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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 
    note_id = 56 # int | 

    try:
        # Retrieve a note
        api_response = await api_instance.external_api_rental_unit_notes_get_rental_unit_note_by_note_id(unit_id, note_id)
        print("The response of RentalUnitsApi->external_api_rental_unit_notes_get_rental_unit_note_by_note_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_notes_get_rental_unit_note_by_note_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
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

# **external_api_rental_unit_notes_get_rental_unit_notes**
> List[NoteMessage] external_api_rental_unit_notes_get_rental_unit_notes(unit_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)

Retrieve all notes

Retrieves all rental unit notes.
            

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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 
    updateddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    updateddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any note whose updated date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. (optional)
    lastupdatedbyuserid = 56 # int | Filters results to only notes that were last updated by the specified user identifier. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all notes
        api_response = await api_instance.external_api_rental_unit_notes_get_rental_unit_notes(unit_id, updateddatetimefrom=updateddatetimefrom, updateddatetimeto=updateddatetimeto, lastupdatedbyuserid=lastupdatedbyuserid, orderby=orderby, offset=offset, limit=limit)
        print("The response of RentalUnitsApi->external_api_rental_unit_notes_get_rental_unit_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_notes_get_rental_unit_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
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

# **external_api_rental_unit_notes_update_note_for_rental_unit**
> NoteMessage external_api_rental_unit_notes_update_note_for_rental_unit(unit_id, note_id, note_put_message)

Update a note

Updates a rental unit note.
            

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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | 
    note_id = 56 # int | 
    note_put_message = buildium_sdk.NotePutMessage() # NotePutMessage | 

    try:
        # Update a note
        api_response = await api_instance.external_api_rental_unit_notes_update_note_for_rental_unit(unit_id, note_id, note_put_message)
        print("The response of RentalUnitsApi->external_api_rental_unit_notes_update_note_for_rental_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_unit_notes_update_note_for_rental_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**|  | 
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

# **external_api_rental_units_create_rental_unit**
> RentalUnitMessage external_api_rental_units_create_rental_unit(rental_units_post_message)

Create a unit

Creates a rental unit.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_unit_message import RentalUnitMessage
from buildium_sdk.models.rental_units_post_message import RentalUnitsPostMessage
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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    rental_units_post_message = buildium_sdk.RentalUnitsPostMessage() # RentalUnitsPostMessage | 

    try:
        # Create a unit
        api_response = await api_instance.external_api_rental_units_create_rental_unit(rental_units_post_message)
        print("The response of RentalUnitsApi->external_api_rental_units_create_rental_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_units_create_rental_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_units_post_message** | [**RentalUnitsPostMessage**](RentalUnitsPostMessage.md)|  | 

### Return type

[**RentalUnitMessage**](RentalUnitMessage.md)

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

# **external_api_rental_units_get_all_rental_units**
> List[RentalUnitMessage] external_api_rental_units_get_all_rental_units(propertyids=propertyids, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)

Retrieve all units

Retrieves a list of rental property units.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_unit_message import RentalUnitMessage
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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    propertyids = [56] # List[int] | Filters results to rental units that belong to the specified set of property ids. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any rental units that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any rental units that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all units
        api_response = await api_instance.external_api_rental_units_get_all_rental_units(propertyids=propertyids, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)
        print("The response of RentalUnitsApi->external_api_rental_units_get_all_rental_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_units_get_all_rental_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **propertyids** | [**List[int]**](int.md)| Filters results to rental units that belong to the specified set of property ids. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to any rental units that were updated on or after the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to any rental units that were updated on or before the specified date. The value must be in UTC and formatted as YYYY-MM-DDTHH:MM:SSZ. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[RentalUnitMessage]**](RentalUnitMessage.md)

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

# **external_api_rental_units_get_rental_unit_by_id**
> RentalUnitMessage external_api_rental_units_get_rental_unit_by_id(unit_id)

Retrieve a unit

Retrieves a specific rental property unit.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_unit_message import RentalUnitMessage
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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | The rental unit identifier.

    try:
        # Retrieve a unit
        api_response = await api_instance.external_api_rental_units_get_rental_unit_by_id(unit_id)
        print("The response of RentalUnitsApi->external_api_rental_units_get_rental_unit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_units_get_rental_unit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**| The rental unit identifier. | 

### Return type

[**RentalUnitMessage**](RentalUnitMessage.md)

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

# **external_api_rental_units_update_rental_unit**
> RentalUnitMessage external_api_rental_units_update_rental_unit(unit_id, rental_unit_put_message)

Update a unit

Updates a rental unit.


<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Rental properties and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.rental_unit_message import RentalUnitMessage
from buildium_sdk.models.rental_unit_put_message import RentalUnitPutMessage
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
    api_instance = buildium_sdk.RentalUnitsApi(api_client)
    unit_id = 56 # int | The identifier of the unit to update.
    rental_unit_put_message = buildium_sdk.RentalUnitPutMessage() # RentalUnitPutMessage | 

    try:
        # Update a unit
        api_response = await api_instance.external_api_rental_units_update_rental_unit(unit_id, rental_unit_put_message)
        print("The response of RentalUnitsApi->external_api_rental_units_update_rental_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RentalUnitsApi->external_api_rental_units_update_rental_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **int**| The identifier of the unit to update. | 
 **rental_unit_put_message** | [**RentalUnitPutMessage**](RentalUnitPutMessage.md)|  | 

### Return type

[**RentalUnitMessage**](RentalUnitMessage.md)

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

