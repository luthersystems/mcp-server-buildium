# buildium_sdk.BillsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_bill_file_download_requests_download_bill_file**](BillsApi.md#external_api_bill_file_download_requests_download_bill_file) | **POST** /v1/bills/{billId}/files/{fileId}/downloadrequest | Download a bill file
[**external_api_bill_file_uploads_create_upload_file_request**](BillsApi.md#external_api_bill_file_uploads_create_upload_file_request) | **POST** /v1/bills/{billId}/files/uploadrequests | Upload a bill file
[**external_api_bill_payments_read_get_bill_payment_by_id**](BillsApi.md#external_api_bill_payments_read_get_bill_payment_by_id) | **GET** /v1/bills/{billId}/payments/{paymentId} | Retrieve a bill payment
[**external_api_bill_payments_read_get_bill_payments**](BillsApi.md#external_api_bill_payments_read_get_bill_payments) | **GET** /v1/bills/{billId}/payments | Retrieve all bill payments
[**external_api_bill_payments_write_create_bill_payment**](BillsApi.md#external_api_bill_payments_write_create_bill_payment) | **POST** /v1/bills/{billId}/payments | Create a bill payment
[**external_api_bill_payments_write_create_multiple_bill_payments**](BillsApi.md#external_api_bill_payments_write_create_multiple_bill_payments) | **POST** /v1/bills/payments | Create a payment for multiple bills with one check
[**external_api_bills_create_bill**](BillsApi.md#external_api_bills_create_bill) | **POST** /v1/bills | Create a bill
[**external_api_bills_files_delete_bill_file**](BillsApi.md#external_api_bills_files_delete_bill_file) | **DELETE** /v1/bills/{billId}/files/{fileId} | Delete a bill file
[**external_api_bills_files_get_all_files_for_bill**](BillsApi.md#external_api_bills_files_get_all_files_for_bill) | **GET** /v1/bills/{billId}/files | Retrieve all files for a bill
[**external_api_bills_files_get_bill_file_by_id**](BillsApi.md#external_api_bills_files_get_bill_file_by_id) | **GET** /v1/bills/{billId}/files/{fileId} | Retrieve a file for a bill
[**external_api_bills_get_bill_by_id**](BillsApi.md#external_api_bills_get_bill_by_id) | **GET** /v1/bills/{billId} | Retrieve a bill
[**external_api_bills_get_bills_async**](BillsApi.md#external_api_bills_get_bills_async) | **GET** /v1/bills | Retrieve all bills
[**external_api_bills_patch_bill**](BillsApi.md#external_api_bills_patch_bill) | **PATCH** /v1/bills/{billId} | Update a bill
[**external_api_bills_update_bill**](BillsApi.md#external_api_bills_update_bill) | **PUT** /v1/bills/{billId} | Update a bill


# **external_api_bill_file_download_requests_download_bill_file**
> FileDownloadMessage external_api_bill_file_download_requests_download_bill_file(bill_id, file_id)

Download a bill file

Downloads a specific file associated to the bill.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View`

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
    api_instance = buildium_sdk.BillsApi(api_client)
    bill_id = 56 # int | 
    file_id = 56 # int | 

    try:
        # Download a bill file
        api_response = await api_instance.external_api_bill_file_download_requests_download_bill_file(bill_id, file_id)
        print("The response of BillsApi->external_api_bill_file_download_requests_download_bill_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bill_file_download_requests_download_bill_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_id** | **int**|  | 
 **file_id** | **int**|  | 

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
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bill_file_uploads_create_upload_file_request**
> FileUploadTicketMessage external_api_bill_file_uploads_create_upload_file_request(bill_id, file_name_post_message)

Upload a bill file

Uploads a file and associates it to the specified bill record.


Uploading a file requires making two API requests. Each step is outlined below.


<strong>Step 1 - Save file metadata</strong>

The first step in the file upload process is to submit the file metadata to `/v1/bills/{billId:int}/files/uploadrequests`. The response of this call will contain a URL and a collection of form data that will be used in step 2 to generate the request for the file binary upload.


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


<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.file_name_post_message import FileNamePostMessage
from buildium_sdk.models.file_upload_ticket_message import FileUploadTicketMessage
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
    api_instance = buildium_sdk.BillsApi(api_client)
    bill_id = 56 # int | 
    file_name_post_message = buildium_sdk.FileNamePostMessage() # FileNamePostMessage | 

    try:
        # Upload a bill file
        api_response = await api_instance.external_api_bill_file_uploads_create_upload_file_request(bill_id, file_name_post_message)
        print("The response of BillsApi->external_api_bill_file_uploads_create_upload_file_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bill_file_uploads_create_upload_file_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_id** | **int**|  | 
 **file_name_post_message** | [**FileNamePostMessage**](FileNamePostMessage.md)|  | 

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
**409** | There is a request conflict with the current state of the target resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bill_payments_read_get_bill_payment_by_id**
> BillPaymentMessage external_api_bill_payments_read_get_bill_payment_by_id(bill_id, payment_id)

Retrieve a bill payment

Retrieves specific bill payment.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bill_payment_message import BillPaymentMessage
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
    api_instance = buildium_sdk.BillsApi(api_client)
    bill_id = 56 # int | 
    payment_id = 56 # int | 

    try:
        # Retrieve a bill payment
        api_response = await api_instance.external_api_bill_payments_read_get_bill_payment_by_id(bill_id, payment_id)
        print("The response of BillsApi->external_api_bill_payments_read_get_bill_payment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bill_payments_read_get_bill_payment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_id** | **int**|  | 
 **payment_id** | **int**|  | 

### Return type

[**BillPaymentMessage**](BillPaymentMessage.md)

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

# **external_api_bill_payments_read_get_bill_payments**
> List[BillPaymentMessage] external_api_bill_payments_read_get_bill_payments(bill_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all bill payments

Retrieves a list of bill payments for a specific bill.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bill_payment_message import BillPaymentMessage
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
    api_instance = buildium_sdk.BillsApi(api_client)
    bill_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all bill payments
        api_response = await api_instance.external_api_bill_payments_read_get_bill_payments(bill_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of BillsApi->external_api_bill_payments_read_get_bill_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bill_payments_read_get_bill_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BillPaymentMessage]**](BillPaymentMessage.md)

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

# **external_api_bill_payments_write_create_bill_payment**
> BillPaymentMessage external_api_bill_payments_write_create_bill_payment(bill_id, bill_payment_post_message)

Create a bill payment

Creates a bill payment.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View` `Edit`
            <span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bill_payment_message import BillPaymentMessage
from buildium_sdk.models.bill_payment_post_message import BillPaymentPostMessage
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
    api_instance = buildium_sdk.BillsApi(api_client)
    bill_id = 56 # int | 
    bill_payment_post_message = buildium_sdk.BillPaymentPostMessage() # BillPaymentPostMessage | 

    try:
        # Create a bill payment
        api_response = await api_instance.external_api_bill_payments_write_create_bill_payment(bill_id, bill_payment_post_message)
        print("The response of BillsApi->external_api_bill_payments_write_create_bill_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bill_payments_write_create_bill_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_id** | **int**|  | 
 **bill_payment_post_message** | [**BillPaymentPostMessage**](BillPaymentPostMessage.md)|  | 

### Return type

[**BillPaymentMessage**](BillPaymentMessage.md)

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

# **external_api_bill_payments_write_create_multiple_bill_payments**
> BillPaymentMessage external_api_bill_payments_write_create_multiple_bill_payments(multiple_bill_payments_post_message)

Create a payment for multiple bills with one check

Creates a payment for multiple bills with one check.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View` `Edit`
            <span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bill_payment_message import BillPaymentMessage
from buildium_sdk.models.multiple_bill_payments_post_message import MultipleBillPaymentsPostMessage
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
    api_instance = buildium_sdk.BillsApi(api_client)
    multiple_bill_payments_post_message = buildium_sdk.MultipleBillPaymentsPostMessage() # MultipleBillPaymentsPostMessage | 

    try:
        # Create a payment for multiple bills with one check
        api_response = await api_instance.external_api_bill_payments_write_create_multiple_bill_payments(multiple_bill_payments_post_message)
        print("The response of BillsApi->external_api_bill_payments_write_create_multiple_bill_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bill_payments_write_create_multiple_bill_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multiple_bill_payments_post_message** | [**MultipleBillPaymentsPostMessage**](MultipleBillPaymentsPostMessage.md)|  | 

### Return type

[**BillPaymentMessage**](BillPaymentMessage.md)

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

# **external_api_bills_create_bill**
> BillMessage external_api_bills_create_bill(bill_post_message)

Create a bill

Creates a bill.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bill_message import BillMessage
from buildium_sdk.models.bill_post_message import BillPostMessage
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
    api_instance = buildium_sdk.BillsApi(api_client)
    bill_post_message = buildium_sdk.BillPostMessage() # BillPostMessage | 

    try:
        # Create a bill
        api_response = await api_instance.external_api_bills_create_bill(bill_post_message)
        print("The response of BillsApi->external_api_bills_create_bill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bills_create_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_post_message** | [**BillPostMessage**](BillPostMessage.md)|  | 

### Return type

[**BillMessage**](BillMessage.md)

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

# **external_api_bills_files_delete_bill_file**
> external_api_bills_files_delete_bill_file(bill_id, file_id)

Delete a bill file

Deletes the specified file from a bill. The file will be permanently deleted from the Buildium platform and can not be recovered.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View` `Edit` `Delete`

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
    api_instance = buildium_sdk.BillsApi(api_client)
    bill_id = 56 # int | 
    file_id = 56 # int | 

    try:
        # Delete a bill file
        await api_instance.external_api_bills_files_delete_bill_file(bill_id, file_id)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bills_files_delete_bill_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_id** | **int**|  | 
 **file_id** | **int**|  | 

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

# **external_api_bills_files_get_all_files_for_bill**
> List[BillFileMessage] external_api_bills_files_get_all_files_for_bill(bill_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all files for a bill

Retrieves the metadata for all files associated to the specified bill. To download the actual file view the [Download a bill file](#tag/Bills/operation/ExternalApiBillFileDownloadRequests_DownloadBillFile).
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bill_file_message import BillFileMessage
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
    api_instance = buildium_sdk.BillsApi(api_client)
    bill_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all files for a bill
        api_response = await api_instance.external_api_bills_files_get_all_files_for_bill(bill_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of BillsApi->external_api_bills_files_get_all_files_for_bill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bills_files_get_all_files_for_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BillFileMessage]**](BillFileMessage.md)

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

# **external_api_bills_files_get_bill_file_by_id**
> BillFileMessage external_api_bills_files_get_bill_file_by_id(bill_id, file_id)

Retrieve a file for a bill

Retrieves the metadata for a specific file associated with the specified bill.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bill_file_message import BillFileMessage
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
    api_instance = buildium_sdk.BillsApi(api_client)
    bill_id = 56 # int | 
    file_id = 56 # int | 

    try:
        # Retrieve a file for a bill
        api_response = await api_instance.external_api_bills_files_get_bill_file_by_id(bill_id, file_id)
        print("The response of BillsApi->external_api_bills_files_get_bill_file_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bills_files_get_bill_file_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_id** | **int**|  | 
 **file_id** | **int**|  | 

### Return type

[**BillFileMessage**](BillFileMessage.md)

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

# **external_api_bills_get_bill_by_id**
> BillMessage external_api_bills_get_bill_by_id(bill_id)

Retrieve a bill

Retrieves a single bill.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bill_message import BillMessage
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
    api_instance = buildium_sdk.BillsApi(api_client)
    bill_id = 56 # int | 

    try:
        # Retrieve a bill
        api_response = await api_instance.external_api_bills_get_bill_by_id(bill_id)
        print("The response of BillsApi->external_api_bills_get_bill_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bills_get_bill_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_id** | **int**|  | 

### Return type

[**BillMessage**](BillMessage.md)

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

# **external_api_bills_get_bills_async**
> List[BillMessage] external_api_bills_get_bills_async(entityid=entityid, entitytype=entitytype, vendorid=vendorid, referencenumber=referencenumber, paidstatus=paidstatus, frompaiddate=frompaiddate, topaiddate=topaiddate, approvalstatuses=approvalstatuses, orderby=orderby, offset=offset, limit=limit)

Retrieve all bills

Retrieves a list of bills.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bill_message import BillMessage
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
    api_instance = buildium_sdk.BillsApi(api_client)
    entityid = 56 # int | Filters results to any bill containing line items associated with the specified entity identifier. This filter is used in conjunction with the `EntityType` field which must be set to the type of entity this identifier references. (optional)
    entitytype = 'entitytype_example' # str | Specifies the type of entity that `EntityId` refers to. This field is required if `EntityId` is specified. (optional)
    vendorid = 56 # int | Filters results to bills associated with a specific vendor. (optional)
    referencenumber = 'referencenumber_example' # str | Filters results to bills whose reference number contains the specified value. (optional)
    paidstatus = 'paidstatus_example' # str | Filters results by the bill's paid status. If no status is specified, bills with any status will be returned. (optional)
    frompaiddate = '2013-10-20' # date | Filters results to any bill whose paid date is greater than or equal to the specified value. (optional)
    topaiddate = '2013-10-20' # date | Filters results to any bill whose paid date is less than or equal to the specified value. (optional)
    approvalstatuses = ['approvalstatuses_example'] # List[str] | Filters the results to bills matching the specified approval statuses. If no approval status is specified, bills with any status will be returned. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all bills
        api_response = await api_instance.external_api_bills_get_bills_async(entityid=entityid, entitytype=entitytype, vendorid=vendorid, referencenumber=referencenumber, paidstatus=paidstatus, frompaiddate=frompaiddate, topaiddate=topaiddate, approvalstatuses=approvalstatuses, orderby=orderby, offset=offset, limit=limit)
        print("The response of BillsApi->external_api_bills_get_bills_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bills_get_bills_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entityid** | **int**| Filters results to any bill containing line items associated with the specified entity identifier. This filter is used in conjunction with the &#x60;EntityType&#x60; field which must be set to the type of entity this identifier references. | [optional] 
 **entitytype** | **str**| Specifies the type of entity that &#x60;EntityId&#x60; refers to. This field is required if &#x60;EntityId&#x60; is specified. | [optional] 
 **vendorid** | **int**| Filters results to bills associated with a specific vendor. | [optional] 
 **referencenumber** | **str**| Filters results to bills whose reference number contains the specified value. | [optional] 
 **paidstatus** | **str**| Filters results by the bill&#39;s paid status. If no status is specified, bills with any status will be returned. | [optional] 
 **frompaiddate** | **date**| Filters results to any bill whose paid date is greater than or equal to the specified value. | [optional] 
 **topaiddate** | **date**| Filters results to any bill whose paid date is less than or equal to the specified value. | [optional] 
 **approvalstatuses** | [**List[str]**](str.md)| Filters the results to bills matching the specified approval statuses. If no approval status is specified, bills with any status will be returned. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BillMessage]**](BillMessage.md)

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

# **external_api_bills_patch_bill**
> BillMessage external_api_bills_patch_bill(bill_id, bill_patch_message)

Update a bill

Updates a bill.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bill_message import BillMessage
from buildium_sdk.models.bill_patch_message import BillPatchMessage
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
    api_instance = buildium_sdk.BillsApi(api_client)
    bill_id = 56 # int | 
    bill_patch_message = buildium_sdk.BillPatchMessage() # BillPatchMessage | <span>Represents the structure of the data that can be provided to a <a target=\"_blank\" href=\"https://datatracker.ietf.org/doc/html/rfc6902\">JSON patch document</a> as path values via <a target=\"_blank\" href=\"https://datatracker.ietf.org/doc/html/rfc6901/\">JSON pointer</a> syntax.</span>

    try:
        # Update a bill
        api_response = await api_instance.external_api_bills_patch_bill(bill_id, bill_patch_message)
        print("The response of BillsApi->external_api_bills_patch_bill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bills_patch_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_id** | **int**|  | 
 **bill_patch_message** | [**BillPatchMessage**](BillPatchMessage.md)| &lt;span&gt;Represents the structure of the data that can be provided to a &lt;a target&#x3D;\&quot;_blank\&quot; href&#x3D;\&quot;https://datatracker.ietf.org/doc/html/rfc6902\&quot;&gt;JSON patch document&lt;/a&gt; as path values via &lt;a target&#x3D;\&quot;_blank\&quot; href&#x3D;\&quot;https://datatracker.ietf.org/doc/html/rfc6901/\&quot;&gt;JSON pointer&lt;/a&gt; syntax.&lt;/span&gt; | 

### Return type

[**BillMessage**](BillMessage.md)

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
**409** | There is a request conflict with the current state of the target resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_bills_update_bill**
> BillMessage external_api_bills_update_bill(bill_id, bill_put_message)

Update a bill

Use this operation to update any of the writable fields of an existing bill resource. When updating this resource keep the following in mind: 
<ul><li>Writable fields omitted from the request or that do not have a value in the request message are set to `NULL`. If you do not want to update the field, submit the original field value.</li><li>When a bill has an existing payment any edits to the line items that change the total bill amount must result in the new total bill amount being equal to or greater than the amount paid.</li><li>When adding a new line item leave the `LineItem.Id` field empty.</li><li>You cannot update a bill that has a pending EFT associated with it.</li></ul>

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bills</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bill_message import BillMessage
from buildium_sdk.models.bill_put_message import BillPutMessage
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
    api_instance = buildium_sdk.BillsApi(api_client)
    bill_id = 56 # int | 
    bill_put_message = buildium_sdk.BillPutMessage() # BillPutMessage | 

    try:
        # Update a bill
        api_response = await api_instance.external_api_bills_update_bill(bill_id, bill_put_message)
        print("The response of BillsApi->external_api_bills_update_bill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsApi->external_api_bills_update_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_id** | **int**|  | 
 **bill_put_message** | [**BillPutMessage**](BillPutMessage.md)|  | 

### Return type

[**BillMessage**](BillMessage.md)

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
**409** | There is a request conflict with the current state of the target resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

