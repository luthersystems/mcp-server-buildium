# buildium_sdk.ApplicationTransactionsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_application_ledger_auto_allocated_payments_create_application_auto_allocated_payment**](ApplicationTransactionsApi.md#external_api_application_ledger_auto_allocated_payments_create_application_auto_allocated_payment) | **POST** /v1/applications/{applicationId}/autoallocatedpayments | Create a payment (auto allocated)
[**external_api_application_ledger_charges_create_application_ledger_charge**](ApplicationTransactionsApi.md#external_api_application_ledger_charges_create_application_ledger_charge) | **POST** /v1/applications/{applicationId}/charges | Create a charge
[**external_api_application_ledger_charges_get_application_charges**](ApplicationTransactionsApi.md#external_api_application_ledger_charges_get_application_charges) | **GET** /v1/applications/{applicationId}/charges | Retrieve all charges
[**external_api_application_ledger_charges_get_application_ledger_charge_by_id**](ApplicationTransactionsApi.md#external_api_application_ledger_charges_get_application_ledger_charge_by_id) | **GET** /v1/applications/{applicationId}/charges/{transactionId} | Retrieve a charge
[**external_api_application_ledger_charges_update_application_ledger_charge**](ApplicationTransactionsApi.md#external_api_application_ledger_charges_update_application_ledger_charge) | **PUT** /v1/applications/{applicationId}/charges/{transactionId} | Update a charge
[**external_api_application_ledger_payment_reversals_create_application_ledger_reverse_payment**](ApplicationTransactionsApi.md#external_api_application_ledger_payment_reversals_create_application_ledger_reverse_payment) | **POST** /v1/applications/{applicationId}/reversepayments | Create a payment reversal
[**external_api_application_ledger_payments_create_application_ledger_payment**](ApplicationTransactionsApi.md#external_api_application_ledger_payments_create_application_ledger_payment) | **POST** /v1/applications/{applicationId}/payments | Create a payment
[**external_api_application_ledger_payments_update_application_ledger_payment**](ApplicationTransactionsApi.md#external_api_application_ledger_payments_update_application_ledger_payment) | **PUT** /v1/applications/{applicationId}/payments/{transactionId} | Update a payment
[**external_api_application_ledger_refunds_create_application_ledger_refund**](ApplicationTransactionsApi.md#external_api_application_ledger_refunds_create_application_ledger_refund) | **POST** /v1/applications/{applicationId}/refunds | Create a refund
[**external_api_application_ledger_refunds_get_application_ledger_refund_by_id**](ApplicationTransactionsApi.md#external_api_application_ledger_refunds_get_application_ledger_refund_by_id) | **GET** /v1/applications/{applicationId}/refunds/{transactionId} | Retrieve a refund
[**external_api_application_ledger_transactions_get_application_transactions**](ApplicationTransactionsApi.md#external_api_application_ledger_transactions_get_application_transactions) | **GET** /v1/applications/{applicationId}/transactions | Retrieve all application transactions
[**external_api_application_ledger_transactions_get_lease_ledger_transaction_by_id**](ApplicationTransactionsApi.md#external_api_application_ledger_transactions_get_lease_ledger_transaction_by_id) | **GET** /v1/applications/{applicationId}/transactions/{transactionId} | Retrieve an application transaction
[**external_api_application_outstanding_balances_get_application_outstanding_balances**](ApplicationTransactionsApi.md#external_api_application_outstanding_balances_get_application_outstanding_balances) | **GET** /v1/applications/outstandingbalances | Retrieve all outstanding balances


# **external_api_application_ledger_auto_allocated_payments_create_application_auto_allocated_payment**
> ApplicationTransactionMessage external_api_application_ledger_auto_allocated_payments_create_application_auto_allocated_payment(application_id, application_auto_allocated_payment_post_message)

Create a payment (auto allocated)

Creates a payment on the application ledger. Note that the recorded payment will be automatically allocated to the general ledger accounts based on the payment allocation settings. These settings can be found under the Settings > Application Settings > Residents page in your account. If you'd like to specify the GL accounts the payment should apply to, please use the <a href="#operation/ExternalApiApplicationLedgerPayments_CreateApplicationLedgerPayment">Create a payment</a> endpoint.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_auto_allocated_payment_post_message import ApplicationAutoAllocatedPaymentPostMessage
from buildium_sdk.models.application_transaction_message import ApplicationTransactionMessage
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
    api_instance = buildium_sdk.ApplicationTransactionsApi(api_client)
    application_id = 56 # int | The application unique identifier.
    application_auto_allocated_payment_post_message = buildium_sdk.ApplicationAutoAllocatedPaymentPostMessage() # ApplicationAutoAllocatedPaymentPostMessage | 

    try:
        # Create a payment (auto allocated)
        api_response = await api_instance.external_api_application_ledger_auto_allocated_payments_create_application_auto_allocated_payment(application_id, application_auto_allocated_payment_post_message)
        print("The response of ApplicationTransactionsApi->external_api_application_ledger_auto_allocated_payments_create_application_auto_allocated_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTransactionsApi->external_api_application_ledger_auto_allocated_payments_create_application_auto_allocated_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The application unique identifier. | 
 **application_auto_allocated_payment_post_message** | [**ApplicationAutoAllocatedPaymentPostMessage**](ApplicationAutoAllocatedPaymentPostMessage.md)|  | 

### Return type

[**ApplicationTransactionMessage**](ApplicationTransactionMessage.md)

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
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_application_ledger_charges_create_application_ledger_charge**
> ApplicationTransactionMessage external_api_application_ledger_charges_create_application_ledger_charge(application_id, application_charge_post_message)

Create a charge

Creates a charge on a specific application ledger.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_charge_post_message import ApplicationChargePostMessage
from buildium_sdk.models.application_transaction_message import ApplicationTransactionMessage
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
    api_instance = buildium_sdk.ApplicationTransactionsApi(api_client)
    application_id = 56 # int | 
    application_charge_post_message = buildium_sdk.ApplicationChargePostMessage() # ApplicationChargePostMessage | 

    try:
        # Create a charge
        api_response = await api_instance.external_api_application_ledger_charges_create_application_ledger_charge(application_id, application_charge_post_message)
        print("The response of ApplicationTransactionsApi->external_api_application_ledger_charges_create_application_ledger_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTransactionsApi->external_api_application_ledger_charges_create_application_ledger_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **application_charge_post_message** | [**ApplicationChargePostMessage**](ApplicationChargePostMessage.md)|  | 

### Return type

[**ApplicationTransactionMessage**](ApplicationTransactionMessage.md)

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
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_application_ledger_charges_get_application_charges**
> List[ApplicationChargeMessage] external_api_application_ledger_charges_get_application_charges(application_id, chargeids=chargeids, transactiondatefrom=transactiondatefrom, transactiondateto=transactiondateto, orderby=orderby, offset=offset, limit=limit)

Retrieve all charges

Retrieves all the charges for a specific application.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_charge_message import ApplicationChargeMessage
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
    api_instance = buildium_sdk.ApplicationTransactionsApi(api_client)
    application_id = 56 # int | 
    chargeids = [56] # List[int] | Filters results by charge ids (optional)
    transactiondatefrom = '2013-10-20' # date | Filters results to any application transaction whose start date is greater than or equal to the specified value. (optional)
    transactiondateto = '2013-10-20' # date | Filters results to any application transaction whose end date is less than or equal to the specified value. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all charges
        api_response = await api_instance.external_api_application_ledger_charges_get_application_charges(application_id, chargeids=chargeids, transactiondatefrom=transactiondatefrom, transactiondateto=transactiondateto, orderby=orderby, offset=offset, limit=limit)
        print("The response of ApplicationTransactionsApi->external_api_application_ledger_charges_get_application_charges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTransactionsApi->external_api_application_ledger_charges_get_application_charges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **chargeids** | [**List[int]**](int.md)| Filters results by charge ids | [optional] 
 **transactiondatefrom** | **date**| Filters results to any application transaction whose start date is greater than or equal to the specified value. | [optional] 
 **transactiondateto** | **date**| Filters results to any application transaction whose end date is less than or equal to the specified value. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[ApplicationChargeMessage]**](ApplicationChargeMessage.md)

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

# **external_api_application_ledger_charges_get_application_ledger_charge_by_id**
> ApplicationChargeMessage external_api_application_ledger_charges_get_application_ledger_charge_by_id(application_id, transaction_id)

Retrieve a charge

Retrieves a specific application charge.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease Transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_charge_message import ApplicationChargeMessage
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
    api_instance = buildium_sdk.ApplicationTransactionsApi(api_client)
    application_id = 56 # int | 
    transaction_id = 56 # int | 

    try:
        # Retrieve a charge
        api_response = await api_instance.external_api_application_ledger_charges_get_application_ledger_charge_by_id(application_id, transaction_id)
        print("The response of ApplicationTransactionsApi->external_api_application_ledger_charges_get_application_ledger_charge_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTransactionsApi->external_api_application_ledger_charges_get_application_ledger_charge_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **transaction_id** | **int**|  | 

### Return type

[**ApplicationChargeMessage**](ApplicationChargeMessage.md)

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

# **external_api_application_ledger_charges_update_application_ledger_charge**
> ApplicationTransactionMessage external_api_application_ledger_charges_update_application_ledger_charge(application_id, transaction_id, application_charge_put_message)

Update a charge

Updates a charge on a specific application ledger.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_charge_put_message import ApplicationChargePutMessage
from buildium_sdk.models.application_transaction_message import ApplicationTransactionMessage
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
    api_instance = buildium_sdk.ApplicationTransactionsApi(api_client)
    application_id = 56 # int | 
    transaction_id = 56 # int | 
    application_charge_put_message = buildium_sdk.ApplicationChargePutMessage() # ApplicationChargePutMessage | 

    try:
        # Update a charge
        api_response = await api_instance.external_api_application_ledger_charges_update_application_ledger_charge(application_id, transaction_id, application_charge_put_message)
        print("The response of ApplicationTransactionsApi->external_api_application_ledger_charges_update_application_ledger_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTransactionsApi->external_api_application_ledger_charges_update_application_ledger_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **transaction_id** | **int**|  | 
 **application_charge_put_message** | [**ApplicationChargePutMessage**](ApplicationChargePutMessage.md)|  | 

### Return type

[**ApplicationTransactionMessage**](ApplicationTransactionMessage.md)

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

# **external_api_application_ledger_payment_reversals_create_application_ledger_reverse_payment**
> ApplicationTransactionMessage external_api_application_ledger_payment_reversals_create_application_ledger_reverse_payment(application_id, application_reverse_payment_post_message)

Create a payment reversal

Reverses an application ledger payment. Note, this action can only be taken on a payment that has been deposited. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`
            
<span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_reverse_payment_post_message import ApplicationReversePaymentPostMessage
from buildium_sdk.models.application_transaction_message import ApplicationTransactionMessage
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
    api_instance = buildium_sdk.ApplicationTransactionsApi(api_client)
    application_id = 56 # int | The application unique identifier.
    application_reverse_payment_post_message = buildium_sdk.ApplicationReversePaymentPostMessage() # ApplicationReversePaymentPostMessage | 

    try:
        # Create a payment reversal
        api_response = await api_instance.external_api_application_ledger_payment_reversals_create_application_ledger_reverse_payment(application_id, application_reverse_payment_post_message)
        print("The response of ApplicationTransactionsApi->external_api_application_ledger_payment_reversals_create_application_ledger_reverse_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTransactionsApi->external_api_application_ledger_payment_reversals_create_application_ledger_reverse_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The application unique identifier. | 
 **application_reverse_payment_post_message** | [**ApplicationReversePaymentPostMessage**](ApplicationReversePaymentPostMessage.md)|  | 

### Return type

[**ApplicationTransactionMessage**](ApplicationTransactionMessage.md)

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

# **external_api_application_ledger_payments_create_application_ledger_payment**
> ApplicationTransactionMessage external_api_application_ledger_payments_create_application_ledger_payment(application_id, application_payment_post_message)

Create a payment

Creates an application ledger payment.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_payment_post_message import ApplicationPaymentPostMessage
from buildium_sdk.models.application_transaction_message import ApplicationTransactionMessage
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
    api_instance = buildium_sdk.ApplicationTransactionsApi(api_client)
    application_id = 56 # int | The application unique identifier.
    application_payment_post_message = buildium_sdk.ApplicationPaymentPostMessage() # ApplicationPaymentPostMessage | 

    try:
        # Create a payment
        api_response = await api_instance.external_api_application_ledger_payments_create_application_ledger_payment(application_id, application_payment_post_message)
        print("The response of ApplicationTransactionsApi->external_api_application_ledger_payments_create_application_ledger_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTransactionsApi->external_api_application_ledger_payments_create_application_ledger_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The application unique identifier. | 
 **application_payment_post_message** | [**ApplicationPaymentPostMessage**](ApplicationPaymentPostMessage.md)|  | 

### Return type

[**ApplicationTransactionMessage**](ApplicationTransactionMessage.md)

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
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_application_ledger_payments_update_application_ledger_payment**
> ApplicationTransactionMessage external_api_application_ledger_payments_update_application_ledger_payment(application_id, transaction_id, application_payment_put_message)

Update a payment

Updates an application ledger payment. Each line item must have a unique general ledger account identifier. PaymentMethod, Date, Memo, and the total Amount cannot be changed for payments with a PaymentMethod of `BuildiumEFT`, `BuildiumCC` or `RetailCash`.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_payment_put_message import ApplicationPaymentPutMessage
from buildium_sdk.models.application_transaction_message import ApplicationTransactionMessage
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
    api_instance = buildium_sdk.ApplicationTransactionsApi(api_client)
    application_id = 56 # int | The application unique identifier.
    transaction_id = 56 # int | 
    application_payment_put_message = buildium_sdk.ApplicationPaymentPutMessage() # ApplicationPaymentPutMessage | 

    try:
        # Update a payment
        api_response = await api_instance.external_api_application_ledger_payments_update_application_ledger_payment(application_id, transaction_id, application_payment_put_message)
        print("The response of ApplicationTransactionsApi->external_api_application_ledger_payments_update_application_ledger_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTransactionsApi->external_api_application_ledger_payments_update_application_ledger_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| The application unique identifier. | 
 **transaction_id** | **int**|  | 
 **application_payment_put_message** | [**ApplicationPaymentPutMessage**](ApplicationPaymentPutMessage.md)|  | 

### Return type

[**ApplicationTransactionMessage**](ApplicationTransactionMessage.md)

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

# **external_api_application_ledger_refunds_create_application_ledger_refund**
> ApplicationRefundMessage external_api_application_ledger_refunds_create_application_ledger_refund(application_id, application_refund_post_message)

Create a refund

Creates a refund for a specific application.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_refund_message import ApplicationRefundMessage
from buildium_sdk.models.application_refund_post_message import ApplicationRefundPostMessage
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
    api_instance = buildium_sdk.ApplicationTransactionsApi(api_client)
    application_id = 56 # int | 
    application_refund_post_message = buildium_sdk.ApplicationRefundPostMessage() # ApplicationRefundPostMessage | 

    try:
        # Create a refund
        api_response = await api_instance.external_api_application_ledger_refunds_create_application_ledger_refund(application_id, application_refund_post_message)
        print("The response of ApplicationTransactionsApi->external_api_application_ledger_refunds_create_application_ledger_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTransactionsApi->external_api_application_ledger_refunds_create_application_ledger_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **application_refund_post_message** | [**ApplicationRefundPostMessage**](ApplicationRefundPostMessage.md)|  | 

### Return type

[**ApplicationRefundMessage**](ApplicationRefundMessage.md)

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

# **external_api_application_ledger_refunds_get_application_ledger_refund_by_id**
> ApplicationRefundMessage external_api_application_ledger_refunds_get_application_ledger_refund_by_id(application_id, transaction_id)

Retrieve a refund

Retrieves a specific application refund.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_refund_message import ApplicationRefundMessage
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
    api_instance = buildium_sdk.ApplicationTransactionsApi(api_client)
    application_id = 56 # int | 
    transaction_id = 56 # int | 

    try:
        # Retrieve a refund
        api_response = await api_instance.external_api_application_ledger_refunds_get_application_ledger_refund_by_id(application_id, transaction_id)
        print("The response of ApplicationTransactionsApi->external_api_application_ledger_refunds_get_application_ledger_refund_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTransactionsApi->external_api_application_ledger_refunds_get_application_ledger_refund_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **transaction_id** | **int**|  | 

### Return type

[**ApplicationRefundMessage**](ApplicationRefundMessage.md)

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

# **external_api_application_ledger_transactions_get_application_transactions**
> List[ApplicationTransactionMessage] external_api_application_ledger_transactions_get_application_transactions(application_id, ids=ids, transactiondatefrom=transactiondatefrom, transactiondateto=transactiondateto, transactiontypes=transactiontypes, orderby=orderby, offset=offset, limit=limit)

Retrieve all application transactions

Retrieves all the transactions for a specific application.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_transaction_message import ApplicationTransactionMessage
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
    api_instance = buildium_sdk.ApplicationTransactionsApi(api_client)
    application_id = 56 # int | 
    ids = [56] # List[int] | Filters results to specific transactions by their unique identifiers.  If not specified, all application transactions will be returned. (optional)
    transactiondatefrom = '2013-10-20' # date | Filters results to any application transaction whose start date is greater than or equal to the specified value.  The date must be formatted as YYYY-MM-DD (optional)
    transactiondateto = '2013-10-20' # date | Filters results to any application transaction whose end date is less than or equal to the specified value.  The date must be formatted as YYYY-MM-DD (optional)
    transactiontypes = ['transactiontypes_example'] # List[str] | Filters results to any application transaction whose application transaction type matches the specified types.  If no type is specified, application transactions with any type will be returned. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all application transactions
        api_response = await api_instance.external_api_application_ledger_transactions_get_application_transactions(application_id, ids=ids, transactiondatefrom=transactiondatefrom, transactiondateto=transactiondateto, transactiontypes=transactiontypes, orderby=orderby, offset=offset, limit=limit)
        print("The response of ApplicationTransactionsApi->external_api_application_ledger_transactions_get_application_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTransactionsApi->external_api_application_ledger_transactions_get_application_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **ids** | [**List[int]**](int.md)| Filters results to specific transactions by their unique identifiers.  If not specified, all application transactions will be returned. | [optional] 
 **transactiondatefrom** | **date**| Filters results to any application transaction whose start date is greater than or equal to the specified value.  The date must be formatted as YYYY-MM-DD | [optional] 
 **transactiondateto** | **date**| Filters results to any application transaction whose end date is less than or equal to the specified value.  The date must be formatted as YYYY-MM-DD | [optional] 
 **transactiontypes** | [**List[str]**](str.md)| Filters results to any application transaction whose application transaction type matches the specified types.  If no type is specified, application transactions with any type will be returned. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[ApplicationTransactionMessage]**](ApplicationTransactionMessage.md)

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

# **external_api_application_ledger_transactions_get_lease_ledger_transaction_by_id**
> ApplicationTransactionMessage external_api_application_ledger_transactions_get_lease_ledger_transaction_by_id(application_id, transaction_id)

Retrieve an application transaction

Retrieves a specific application transaction.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease Transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_transaction_message import ApplicationTransactionMessage
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
    api_instance = buildium_sdk.ApplicationTransactionsApi(api_client)
    application_id = 56 # int | 
    transaction_id = 56 # int | 

    try:
        # Retrieve an application transaction
        api_response = await api_instance.external_api_application_ledger_transactions_get_lease_ledger_transaction_by_id(application_id, transaction_id)
        print("The response of ApplicationTransactionsApi->external_api_application_ledger_transactions_get_lease_ledger_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTransactionsApi->external_api_application_ledger_transactions_get_lease_ledger_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**|  | 
 **transaction_id** | **int**|  | 

### Return type

[**ApplicationTransactionMessage**](ApplicationTransactionMessage.md)

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

# **external_api_application_outstanding_balances_get_application_outstanding_balances**
> List[ApplicationOutstandingBalanceMessage] external_api_application_outstanding_balances_get_application_outstanding_balances(applicationstatuses=applicationstatuses, applicationids=applicationids, orderby=orderby, offset=offset, limit=limit)

Retrieve all outstanding balances

Retrieves a list of applications that have outstanding balances. Applications with a zero or credit balance will not be returned in the results. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Outstanding Balances</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.application_outstanding_balance_message import ApplicationOutstandingBalanceMessage
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
    api_instance = buildium_sdk.ApplicationTransactionsApi(api_client)
    applicationstatuses = ['applicationstatuses_example'] # List[str] | Filters results to applications in specific statuses.  If not specified, all application outstanding balances will be returned. (optional)
    applicationids = [56] # List[int] | Filters results to specific applications by their unique identifiers.  If not specified, all application outstanding balances will be returned. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all outstanding balances
        api_response = await api_instance.external_api_application_outstanding_balances_get_application_outstanding_balances(applicationstatuses=applicationstatuses, applicationids=applicationids, orderby=orderby, offset=offset, limit=limit)
        print("The response of ApplicationTransactionsApi->external_api_application_outstanding_balances_get_application_outstanding_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTransactionsApi->external_api_application_outstanding_balances_get_application_outstanding_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationstatuses** | [**List[str]**](str.md)| Filters results to applications in specific statuses.  If not specified, all application outstanding balances will be returned. | [optional] 
 **applicationids** | [**List[int]**](int.md)| Filters results to specific applications by their unique identifiers.  If not specified, all application outstanding balances will be returned. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[ApplicationOutstandingBalanceMessage]**](ApplicationOutstandingBalanceMessage.md)

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

