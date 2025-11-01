# buildium_sdk.LeaseTransactionsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_lease_auto_allocated_payment_create_lease_auto_allocated_payment**](LeaseTransactionsApi.md#external_api_lease_auto_allocated_payment_create_lease_auto_allocated_payment) | **POST** /v1/leases/{leaseId}/autoallocatedpayments | Create a payment (auto allocated)
[**external_api_lease_charge_recurring_transactions_create_lease_charge_recurring_transaction**](LeaseTransactionsApi.md#external_api_lease_charge_recurring_transactions_create_lease_charge_recurring_transaction) | **POST** /v1/leases/{leaseId}/recurringcharges | Create a recurring charge
[**external_api_lease_charge_recurring_transactions_get_lease_charge_recurring_transaction_by_id**](LeaseTransactionsApi.md#external_api_lease_charge_recurring_transactions_get_lease_charge_recurring_transaction_by_id) | **GET** /v1/leases/{leaseId}/recurringcharges/{transactionId} | Retrieve a recurring charge
[**external_api_lease_ledger_charges_read_get_all_charges**](LeaseTransactionsApi.md#external_api_lease_ledger_charges_read_get_all_charges) | **GET** /v1/leases/{leaseId}/charges | Retrieve all charges
[**external_api_lease_ledger_charges_read_get_charge_by_id**](LeaseTransactionsApi.md#external_api_lease_ledger_charges_read_get_charge_by_id) | **GET** /v1/leases/{leaseId}/charges/{chargeId} | Retrieve a charge
[**external_api_lease_ledger_charges_write_create_charge**](LeaseTransactionsApi.md#external_api_lease_ledger_charges_write_create_charge) | **POST** /v1/leases/{leaseId}/charges | Create a charge
[**external_api_lease_ledger_charges_write_update_lease_charge**](LeaseTransactionsApi.md#external_api_lease_ledger_charges_write_update_lease_charge) | **PUT** /v1/leases/{leaseId}/charges/{chargeId} | Update a charge
[**external_api_lease_ledger_credits_write_create_lease_credit**](LeaseTransactionsApi.md#external_api_lease_ledger_credits_write_create_lease_credit) | **POST** /v1/leases/{leaseId}/credits | Create a credit
[**external_api_lease_ledger_deposit_withholding_create_lease_ledger_deposit_withholding**](LeaseTransactionsApi.md#external_api_lease_ledger_deposit_withholding_create_lease_ledger_deposit_withholding) | **POST** /v1/leases/{leaseId}/applieddeposits | Create a deposit withholding
[**external_api_lease_ledger_deposit_withholding_update_deposit_withholding**](LeaseTransactionsApi.md#external_api_lease_ledger_deposit_withholding_update_deposit_withholding) | **PUT** /v1/leases/{leaseId}/applieddeposits/{depositId} | Update a deposit withholding
[**external_api_lease_ledger_payment_reversals_write_create_lease_reverse_payment**](LeaseTransactionsApi.md#external_api_lease_ledger_payment_reversals_write_create_lease_reverse_payment) | **POST** /v1/leases/{leaseId}/reversepayments | Create a payment reversal
[**external_api_lease_ledger_payments_write_create_payment**](LeaseTransactionsApi.md#external_api_lease_ledger_payments_write_create_payment) | **POST** /v1/leases/{leaseId}/payments | Create a payment
[**external_api_lease_ledger_payments_write_update_lease_ledger_payment**](LeaseTransactionsApi.md#external_api_lease_ledger_payments_write_update_lease_ledger_payment) | **PUT** /v1/leases/{leaseId}/payments/{paymentId} | Update a payment
[**external_api_lease_ledger_refunds_create_lease_ledger_refund**](LeaseTransactionsApi.md#external_api_lease_ledger_refunds_create_lease_ledger_refund) | **POST** /v1/leases/{leaseId}/refunds | Create a refund
[**external_api_lease_ledger_refunds_get_lease_ledger_refund_by_id**](LeaseTransactionsApi.md#external_api_lease_ledger_refunds_get_lease_ledger_refund_by_id) | **GET** /v1/leases/{leaseId}/refunds/{refundId} | Retrieve a refund
[**external_api_lease_ledger_transactions_get_lease_ledger_transaction_by_id**](LeaseTransactionsApi.md#external_api_lease_ledger_transactions_get_lease_ledger_transaction_by_id) | **GET** /v1/leases/{leaseId}/transactions/{transactionId} | Retrieve a lease transaction
[**external_api_lease_ledger_transactions_get_lease_ledgers**](LeaseTransactionsApi.md#external_api_lease_ledger_transactions_get_lease_ledgers) | **GET** /v1/leases/{leaseId}/transactions | Retrieve all lease transactions
[**external_api_lease_outstanding_balances_get_lease_outstanding_balances**](LeaseTransactionsApi.md#external_api_lease_outstanding_balances_get_lease_outstanding_balances) | **GET** /v1/leases/outstandingbalances | Retrieve all outstanding balances
[**external_api_lease_recurring_credits_create_lease_credit_recurring_transaction**](LeaseTransactionsApi.md#external_api_lease_recurring_credits_create_lease_credit_recurring_transaction) | **POST** /v1/leases/{leaseId}/recurringcredits | Create a recurring credit
[**external_api_lease_recurring_credits_get_lease_recurring_credit_by_id**](LeaseTransactionsApi.md#external_api_lease_recurring_credits_get_lease_recurring_credit_by_id) | **GET** /v1/leases/{leaseId}/recurringcredits/{transactionId} | Retrieve a recurring credit
[**external_api_lease_recurring_payments_create_lease_recurring_payment**](LeaseTransactionsApi.md#external_api_lease_recurring_payments_create_lease_recurring_payment) | **POST** /v1/leases/{leaseId}/recurringpayments | Create a recurring payment
[**external_api_lease_recurring_payments_get_recurring_lease_payments_by_id**](LeaseTransactionsApi.md#external_api_lease_recurring_payments_get_recurring_lease_payments_by_id) | **GET** /v1/leases/{leaseId}/recurringpayments/{paymentId} | Retrieve a recurring payment
[**external_api_lease_recurring_transactions_get_lease_recurring_transactions**](LeaseTransactionsApi.md#external_api_lease_recurring_transactions_get_lease_recurring_transactions) | **GET** /v1/leases/{leaseId}/recurringtransactions | Retrieve all recurring transactions
[**external_api_lease_recurring_transactions_get_recurring_transactions_for_all_leases**](LeaseTransactionsApi.md#external_api_lease_recurring_transactions_get_recurring_transactions_for_all_leases) | **GET** /v1/leases/recurringtransactions | Retrieve all recurring transactions for all leases


# **external_api_lease_auto_allocated_payment_create_lease_auto_allocated_payment**
> LeaseTransactionMessage external_api_lease_auto_allocated_payment_create_lease_auto_allocated_payment(lease_id, lease_auto_allocated_payment_post_message)

Create a payment (auto allocated)

Creates a payment on the lease ledger. Note that the recorded payment will be automatically allocated to the general ledger accounts based on the payment allocation settings. These settings can be found under the Settings > Application Settings > Residents page in your account. If you'd like to specify the GL accounts the payment should apply to, please use the <a href="#operation/ExternalApiLeaseLedgerPaymentsWrite_CreatePayment">Create a payment</a> endpoint.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_auto_allocated_payment_post_message import LeaseAutoAllocatedPaymentPostMessage
from buildium_sdk.models.lease_transaction_message import LeaseTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    lease_auto_allocated_payment_post_message = buildium_sdk.LeaseAutoAllocatedPaymentPostMessage() # LeaseAutoAllocatedPaymentPostMessage | 

    try:
        # Create a payment (auto allocated)
        api_response = await api_instance.external_api_lease_auto_allocated_payment_create_lease_auto_allocated_payment(lease_id, lease_auto_allocated_payment_post_message)
        print("The response of LeaseTransactionsApi->external_api_lease_auto_allocated_payment_create_lease_auto_allocated_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_auto_allocated_payment_create_lease_auto_allocated_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **lease_auto_allocated_payment_post_message** | [**LeaseAutoAllocatedPaymentPostMessage**](LeaseAutoAllocatedPaymentPostMessage.md)|  | 

### Return type

[**LeaseTransactionMessage**](LeaseTransactionMessage.md)

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

# **external_api_lease_charge_recurring_transactions_create_lease_charge_recurring_transaction**
> LeaseChargeRecurringTransactionMessage external_api_lease_charge_recurring_transactions_create_lease_charge_recurring_transaction(lease_id, charge_recurring_transaction_post_message)

Create a recurring charge

Creates a recurring charge transaction that will post automatically on the specified lease ledger.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.charge_recurring_transaction_post_message import ChargeRecurringTransactionPostMessage
from buildium_sdk.models.lease_charge_recurring_transaction_message import LeaseChargeRecurringTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    charge_recurring_transaction_post_message = buildium_sdk.ChargeRecurringTransactionPostMessage() # ChargeRecurringTransactionPostMessage | 

    try:
        # Create a recurring charge
        api_response = await api_instance.external_api_lease_charge_recurring_transactions_create_lease_charge_recurring_transaction(lease_id, charge_recurring_transaction_post_message)
        print("The response of LeaseTransactionsApi->external_api_lease_charge_recurring_transactions_create_lease_charge_recurring_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_charge_recurring_transactions_create_lease_charge_recurring_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **charge_recurring_transaction_post_message** | [**ChargeRecurringTransactionPostMessage**](ChargeRecurringTransactionPostMessage.md)|  | 

### Return type

[**LeaseChargeRecurringTransactionMessage**](LeaseChargeRecurringTransactionMessage.md)

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

# **external_api_lease_charge_recurring_transactions_get_lease_charge_recurring_transaction_by_id**
> LeaseChargeRecurringTransactionMessage external_api_lease_charge_recurring_transactions_get_lease_charge_recurring_transaction_by_id(lease_id, transaction_id)

Retrieve a recurring charge

Retrieves a recurring charge.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_charge_recurring_transaction_message import LeaseChargeRecurringTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    transaction_id = 56 # int | 

    try:
        # Retrieve a recurring charge
        api_response = await api_instance.external_api_lease_charge_recurring_transactions_get_lease_charge_recurring_transaction_by_id(lease_id, transaction_id)
        print("The response of LeaseTransactionsApi->external_api_lease_charge_recurring_transactions_get_lease_charge_recurring_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_charge_recurring_transactions_get_lease_charge_recurring_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **transaction_id** | **int**|  | 

### Return type

[**LeaseChargeRecurringTransactionMessage**](LeaseChargeRecurringTransactionMessage.md)

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

# **external_api_lease_ledger_charges_read_get_all_charges**
> List[LeaseChargeMessage] external_api_lease_ledger_charges_read_get_all_charges(lease_id, transactiondatefrom=transactiondatefrom, transactiondateto=transactiondateto, billids=billids, orderby=orderby, offset=offset, limit=limit)

Retrieve all charges

Retrieves all the charges for a specific lease.


<h4>Required permissions(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_charge_message import LeaseChargeMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    transactiondatefrom = '2013-10-20' # date | Filters results to any lease transaction whose start date is greater than or equal to the specified value. (optional)
    transactiondateto = '2013-10-20' # date | Filters results to any lease transaction whose end date is less than or equal to the specified value. (optional)
    billids = [56] # List[int] | Filters results to any charge that has been associated to the indicated bill ids. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all charges
        api_response = await api_instance.external_api_lease_ledger_charges_read_get_all_charges(lease_id, transactiondatefrom=transactiondatefrom, transactiondateto=transactiondateto, billids=billids, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_charges_read_get_all_charges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_charges_read_get_all_charges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **transactiondatefrom** | **date**| Filters results to any lease transaction whose start date is greater than or equal to the specified value. | [optional] 
 **transactiondateto** | **date**| Filters results to any lease transaction whose end date is less than or equal to the specified value. | [optional] 
 **billids** | [**List[int]**](int.md)| Filters results to any charge that has been associated to the indicated bill ids. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[LeaseChargeMessage]**](LeaseChargeMessage.md)

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
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_lease_ledger_charges_read_get_charge_by_id**
> LeaseChargeMessage external_api_lease_ledger_charges_read_get_charge_by_id(lease_id, charge_id)

Retrieve a charge

Retrieves a specific lease charge.


<h4>Required permissions(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_charge_message import LeaseChargeMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    charge_id = 56 # int | 

    try:
        # Retrieve a charge
        api_response = await api_instance.external_api_lease_ledger_charges_read_get_charge_by_id(lease_id, charge_id)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_charges_read_get_charge_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_charges_read_get_charge_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **charge_id** | **int**|  | 

### Return type

[**LeaseChargeMessage**](LeaseChargeMessage.md)

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
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_lease_ledger_charges_write_create_charge**
> List[LeaseTransactionMessage] external_api_lease_ledger_charges_write_create_charge(lease_id, lease_charge_post_message)

Create a charge

Creates a charge transaction on a specific lease ledger.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

<span class="permissionBlock">Accounting > Bills</span> - `View` `Edit` In order to associate the charge to a bill using the BillId property, you must have this permission.

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_charge_post_message import LeaseChargePostMessage
from buildium_sdk.models.lease_transaction_message import LeaseTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    lease_charge_post_message = buildium_sdk.LeaseChargePostMessage() # LeaseChargePostMessage | 

    try:
        # Create a charge
        api_response = await api_instance.external_api_lease_ledger_charges_write_create_charge(lease_id, lease_charge_post_message)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_charges_write_create_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_charges_write_create_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **lease_charge_post_message** | [**LeaseChargePostMessage**](LeaseChargePostMessage.md)|  | 

### Return type

[**List[LeaseTransactionMessage]**](LeaseTransactionMessage.md)

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
**404** | Lease not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_lease_ledger_charges_write_update_lease_charge**
> LeaseTransactionMessage external_api_lease_ledger_charges_write_update_lease_charge(lease_id, charge_id, lease_charge_put_message)

Update a charge

Updates a charge.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_charge_put_message import LeaseChargePutMessage
from buildium_sdk.models.lease_transaction_message import LeaseTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    charge_id = 56 # int | 
    lease_charge_put_message = buildium_sdk.LeaseChargePutMessage() # LeaseChargePutMessage | 

    try:
        # Update a charge
        api_response = await api_instance.external_api_lease_ledger_charges_write_update_lease_charge(lease_id, charge_id, lease_charge_put_message)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_charges_write_update_lease_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_charges_write_update_lease_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **charge_id** | **int**|  | 
 **lease_charge_put_message** | [**LeaseChargePutMessage**](LeaseChargePutMessage.md)|  | 

### Return type

[**LeaseTransactionMessage**](LeaseTransactionMessage.md)

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

# **external_api_lease_ledger_credits_write_create_lease_credit**
> LeaseTransactionMessage external_api_lease_ledger_credits_write_create_lease_credit(lease_id, lease_ledger_credit_post_message)

Create a credit

Creates a lease ledger credit.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_ledger_credit_post_message import LeaseLedgerCreditPostMessage
from buildium_sdk.models.lease_transaction_message import LeaseTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | The lease unique identifier.
    lease_ledger_credit_post_message = buildium_sdk.LeaseLedgerCreditPostMessage() # LeaseLedgerCreditPostMessage | 

    try:
        # Create a credit
        api_response = await api_instance.external_api_lease_ledger_credits_write_create_lease_credit(lease_id, lease_ledger_credit_post_message)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_credits_write_create_lease_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_credits_write_create_lease_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**| The lease unique identifier. | 
 **lease_ledger_credit_post_message** | [**LeaseLedgerCreditPostMessage**](LeaseLedgerCreditPostMessage.md)|  | 

### Return type

[**LeaseTransactionMessage**](LeaseTransactionMessage.md)

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

# **external_api_lease_ledger_deposit_withholding_create_lease_ledger_deposit_withholding**
> LeaseTransactionMessage external_api_lease_ledger_deposit_withholding_create_lease_ledger_deposit_withholding(lease_id, lease_ledger_deposit_withholding_post_message)

Create a deposit withholding

Withholds a resident deposit by reallocating the funds from a liability account to an income account to cover an expense(s).
           

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease Ledger</span> - `View` `Edit`
           
<span class="permissionBlock">Accounting > General Ledger Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_ledger_deposit_withholding_post_message import LeaseLedgerDepositWithholdingPostMessage
from buildium_sdk.models.lease_transaction_message import LeaseTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    lease_ledger_deposit_withholding_post_message = buildium_sdk.LeaseLedgerDepositWithholdingPostMessage() # LeaseLedgerDepositWithholdingPostMessage | 

    try:
        # Create a deposit withholding
        api_response = await api_instance.external_api_lease_ledger_deposit_withholding_create_lease_ledger_deposit_withholding(lease_id, lease_ledger_deposit_withholding_post_message)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_deposit_withholding_create_lease_ledger_deposit_withholding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_deposit_withholding_create_lease_ledger_deposit_withholding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **lease_ledger_deposit_withholding_post_message** | [**LeaseLedgerDepositWithholdingPostMessage**](LeaseLedgerDepositWithholdingPostMessage.md)|  | 

### Return type

[**LeaseTransactionMessage**](LeaseTransactionMessage.md)

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

# **external_api_lease_ledger_deposit_withholding_update_deposit_withholding**
> LeaseTransactionMessage external_api_lease_ledger_deposit_withholding_update_deposit_withholding(lease_id, deposit_id, lease_ledger_deposit_withholding_put_message)

Update a deposit withholding

Updates a resident deposit withholding.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease Ledger</span> - `View` `Edit`
            
<span class="permissionBlock">Accounting > General Ledger Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_ledger_deposit_withholding_put_message import LeaseLedgerDepositWithholdingPutMessage
from buildium_sdk.models.lease_transaction_message import LeaseTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    deposit_id = 56 # int | 
    lease_ledger_deposit_withholding_put_message = buildium_sdk.LeaseLedgerDepositWithholdingPutMessage() # LeaseLedgerDepositWithholdingPutMessage | 

    try:
        # Update a deposit withholding
        api_response = await api_instance.external_api_lease_ledger_deposit_withholding_update_deposit_withholding(lease_id, deposit_id, lease_ledger_deposit_withholding_put_message)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_deposit_withholding_update_deposit_withholding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_deposit_withholding_update_deposit_withholding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **deposit_id** | **int**|  | 
 **lease_ledger_deposit_withholding_put_message** | [**LeaseLedgerDepositWithholdingPutMessage**](LeaseLedgerDepositWithholdingPutMessage.md)|  | 

### Return type

[**LeaseTransactionMessage**](LeaseTransactionMessage.md)

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

# **external_api_lease_ledger_payment_reversals_write_create_lease_reverse_payment**
> LeaseTransactionMessage external_api_lease_ledger_payment_reversals_write_create_lease_reverse_payment(lease_id, lease_ledger_reverse_payment_post_message)

Create a payment reversal

Reverses a lease ledger payment. Note, this action can only be taken on a payment that has been deposited. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`
            
<span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_ledger_reverse_payment_post_message import LeaseLedgerReversePaymentPostMessage
from buildium_sdk.models.lease_transaction_message import LeaseTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | The lease unique identifier.
    lease_ledger_reverse_payment_post_message = buildium_sdk.LeaseLedgerReversePaymentPostMessage() # LeaseLedgerReversePaymentPostMessage | 

    try:
        # Create a payment reversal
        api_response = await api_instance.external_api_lease_ledger_payment_reversals_write_create_lease_reverse_payment(lease_id, lease_ledger_reverse_payment_post_message)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_payment_reversals_write_create_lease_reverse_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_payment_reversals_write_create_lease_reverse_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**| The lease unique identifier. | 
 **lease_ledger_reverse_payment_post_message** | [**LeaseLedgerReversePaymentPostMessage**](LeaseLedgerReversePaymentPostMessage.md)|  | 

### Return type

[**LeaseTransactionMessage**](LeaseTransactionMessage.md)

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

# **external_api_lease_ledger_payments_write_create_payment**
> LeaseTransactionMessage external_api_lease_ledger_payments_write_create_payment(lease_id, lease_ledger_payment_post_message)

Create a payment

Creates a lease ledger payment.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_ledger_payment_post_message import LeaseLedgerPaymentPostMessage
from buildium_sdk.models.lease_transaction_message import LeaseTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | The lease unique identifier.
    lease_ledger_payment_post_message = buildium_sdk.LeaseLedgerPaymentPostMessage() # LeaseLedgerPaymentPostMessage | 

    try:
        # Create a payment
        api_response = await api_instance.external_api_lease_ledger_payments_write_create_payment(lease_id, lease_ledger_payment_post_message)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_payments_write_create_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_payments_write_create_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**| The lease unique identifier. | 
 **lease_ledger_payment_post_message** | [**LeaseLedgerPaymentPostMessage**](LeaseLedgerPaymentPostMessage.md)|  | 

### Return type

[**LeaseTransactionMessage**](LeaseTransactionMessage.md)

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

# **external_api_lease_ledger_payments_write_update_lease_ledger_payment**
> LeaseTransactionMessage external_api_lease_ledger_payments_write_update_lease_ledger_payment(lease_id, payment_id, lease_ledger_payment_put_message)

Update a payment

Updates a ledger payment. Each line item must have a unique general ledger account identifier. PaymentMethod, Date, Memo, and the total Amount cannot be changed for payments with a PaymentMethod of `BuildiumEFT`, `BuildiumCC` or `RetailCash`.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_ledger_payment_put_message import LeaseLedgerPaymentPutMessage
from buildium_sdk.models.lease_transaction_message import LeaseTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    payment_id = 56 # int | 
    lease_ledger_payment_put_message = buildium_sdk.LeaseLedgerPaymentPutMessage() # LeaseLedgerPaymentPutMessage | 

    try:
        # Update a payment
        api_response = await api_instance.external_api_lease_ledger_payments_write_update_lease_ledger_payment(lease_id, payment_id, lease_ledger_payment_put_message)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_payments_write_update_lease_ledger_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_payments_write_update_lease_ledger_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **payment_id** | **int**|  | 
 **lease_ledger_payment_put_message** | [**LeaseLedgerPaymentPutMessage**](LeaseLedgerPaymentPutMessage.md)|  | 

### Return type

[**LeaseTransactionMessage**](LeaseTransactionMessage.md)

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

# **external_api_lease_ledger_refunds_create_lease_ledger_refund**
> LeaseLedgerRefundMessage external_api_lease_ledger_refunds_create_lease_ledger_refund(lease_id, lease_ledger_refund_post_message)

Create a refund

Creates a refund.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_ledger_refund_message import LeaseLedgerRefundMessage
from buildium_sdk.models.lease_ledger_refund_post_message import LeaseLedgerRefundPostMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    lease_ledger_refund_post_message = buildium_sdk.LeaseLedgerRefundPostMessage() # LeaseLedgerRefundPostMessage | 

    try:
        # Create a refund
        api_response = await api_instance.external_api_lease_ledger_refunds_create_lease_ledger_refund(lease_id, lease_ledger_refund_post_message)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_refunds_create_lease_ledger_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_refunds_create_lease_ledger_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **lease_ledger_refund_post_message** | [**LeaseLedgerRefundPostMessage**](LeaseLedgerRefundPostMessage.md)|  | 

### Return type

[**LeaseLedgerRefundMessage**](LeaseLedgerRefundMessage.md)

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

# **external_api_lease_ledger_refunds_get_lease_ledger_refund_by_id**
> LeaseLedgerRefundMessage external_api_lease_ledger_refunds_get_lease_ledger_refund_by_id(lease_id, refund_id)

Retrieve a refund

Retrieves a refund.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_ledger_refund_message import LeaseLedgerRefundMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    refund_id = 56 # int | 

    try:
        # Retrieve a refund
        api_response = await api_instance.external_api_lease_ledger_refunds_get_lease_ledger_refund_by_id(lease_id, refund_id)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_refunds_get_lease_ledger_refund_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_refunds_get_lease_ledger_refund_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **refund_id** | **int**|  | 

### Return type

[**LeaseLedgerRefundMessage**](LeaseLedgerRefundMessage.md)

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

# **external_api_lease_ledger_transactions_get_lease_ledger_transaction_by_id**
> LeaseTransactionMessage external_api_lease_ledger_transactions_get_lease_ledger_transaction_by_id(lease_id, transaction_id)

Retrieve a lease transaction

Retrieves a specific lease transaction.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease Transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_transaction_message import LeaseTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    transaction_id = 56 # int | 

    try:
        # Retrieve a lease transaction
        api_response = await api_instance.external_api_lease_ledger_transactions_get_lease_ledger_transaction_by_id(lease_id, transaction_id)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_transactions_get_lease_ledger_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_transactions_get_lease_ledger_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **transaction_id** | **int**|  | 

### Return type

[**LeaseTransactionMessage**](LeaseTransactionMessage.md)

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

# **external_api_lease_ledger_transactions_get_lease_ledgers**
> List[LeaseTransactionMessage] external_api_lease_ledger_transactions_get_lease_ledgers(lease_id, transactiondatefrom=transactiondatefrom, transactiondateto=transactiondateto, transactiontypes=transactiontypes, orderby=orderby, offset=offset, limit=limit)

Retrieve all lease transactions

Retrieves all the transactions for a specific lease.


<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_transaction_message import LeaseTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    transactiondatefrom = '2013-10-20' # date | Filters results to any lease transaction whose start date is greater than or equal to the specified value. (optional)
    transactiondateto = '2013-10-20' # date | Filters results to any lease transaction whose end date is less than or equal to the specified value. (optional)
    transactiontypes = ['transactiontypes_example'] # List[str] | Filters results to any lease transaction whose lease transaction type matches the specified status. If no type is specified, lease transactions with any type will be returned. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all lease transactions
        api_response = await api_instance.external_api_lease_ledger_transactions_get_lease_ledgers(lease_id, transactiondatefrom=transactiondatefrom, transactiondateto=transactiondateto, transactiontypes=transactiontypes, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeaseTransactionsApi->external_api_lease_ledger_transactions_get_lease_ledgers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_ledger_transactions_get_lease_ledgers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **transactiondatefrom** | **date**| Filters results to any lease transaction whose start date is greater than or equal to the specified value. | [optional] 
 **transactiondateto** | **date**| Filters results to any lease transaction whose end date is less than or equal to the specified value. | [optional] 
 **transactiontypes** | [**List[str]**](str.md)| Filters results to any lease transaction whose lease transaction type matches the specified status. If no type is specified, lease transactions with any type will be returned. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[LeaseTransactionMessage]**](LeaseTransactionMessage.md)

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

# **external_api_lease_outstanding_balances_get_lease_outstanding_balances**
> List[LeaseOutstandingBalanceMessage] external_api_lease_outstanding_balances_get_lease_outstanding_balances(entitytype=entitytype, entityid=entityid, leasestatuses=leasestatuses, leaseids=leaseids, pastdueemail=pastdueemail, balanceduration=balanceduration, evictionstatus=evictionstatus, orderby=orderby, offset=offset, limit=limit)

Retrieve all outstanding balances

Retrieves a list of leases that have outstanding balances. Leases with a zero or credit balance will not be returned in the results. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Outstanding Balances</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_outstanding_balance_message import LeaseOutstandingBalanceMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    entitytype = 'entitytype_example' # str |  (optional)
    entityid = 56 # int |  (optional)
    leasestatuses = ['leasestatuses_example'] # List[str] |  (optional)
    leaseids = [56] # List[int] |  (optional)
    pastdueemail = 'pastdueemail_example' # str |  (optional)
    balanceduration = 'balanceduration_example' # str |  (optional)
    evictionstatus = 'evictionstatus_example' # str |  (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all outstanding balances
        api_response = await api_instance.external_api_lease_outstanding_balances_get_lease_outstanding_balances(entitytype=entitytype, entityid=entityid, leasestatuses=leasestatuses, leaseids=leaseids, pastdueemail=pastdueemail, balanceduration=balanceduration, evictionstatus=evictionstatus, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeaseTransactionsApi->external_api_lease_outstanding_balances_get_lease_outstanding_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_outstanding_balances_get_lease_outstanding_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitytype** | **str**|  | [optional] 
 **entityid** | **int**|  | [optional] 
 **leasestatuses** | [**List[str]**](str.md)|  | [optional] 
 **leaseids** | [**List[int]**](int.md)|  | [optional] 
 **pastdueemail** | **str**|  | [optional] 
 **balanceduration** | **str**|  | [optional] 
 **evictionstatus** | **str**|  | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[LeaseOutstandingBalanceMessage]**](LeaseOutstandingBalanceMessage.md)

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

# **external_api_lease_recurring_credits_create_lease_credit_recurring_transaction**
> LeaseRecurringCreditMessage external_api_lease_recurring_credits_create_lease_credit_recurring_transaction(lease_id, credit_recurring_transaction_post_message)

Create a recurring credit

Creates a recurring credit transaction on the specified lease ledger. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.credit_recurring_transaction_post_message import CreditRecurringTransactionPostMessage
from buildium_sdk.models.lease_recurring_credit_message import LeaseRecurringCreditMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    credit_recurring_transaction_post_message = buildium_sdk.CreditRecurringTransactionPostMessage() # CreditRecurringTransactionPostMessage | 

    try:
        # Create a recurring credit
        api_response = await api_instance.external_api_lease_recurring_credits_create_lease_credit_recurring_transaction(lease_id, credit_recurring_transaction_post_message)
        print("The response of LeaseTransactionsApi->external_api_lease_recurring_credits_create_lease_credit_recurring_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_recurring_credits_create_lease_credit_recurring_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **credit_recurring_transaction_post_message** | [**CreditRecurringTransactionPostMessage**](CreditRecurringTransactionPostMessage.md)|  | 

### Return type

[**LeaseRecurringCreditMessage**](LeaseRecurringCreditMessage.md)

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

# **external_api_lease_recurring_credits_get_lease_recurring_credit_by_id**
> LeaseRecurringCreditMessage external_api_lease_recurring_credits_get_lease_recurring_credit_by_id(lease_id, transaction_id)

Retrieve a recurring credit

Retrieves a recurring credit.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_recurring_credit_message import LeaseRecurringCreditMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    transaction_id = 56 # int | 

    try:
        # Retrieve a recurring credit
        api_response = await api_instance.external_api_lease_recurring_credits_get_lease_recurring_credit_by_id(lease_id, transaction_id)
        print("The response of LeaseTransactionsApi->external_api_lease_recurring_credits_get_lease_recurring_credit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_recurring_credits_get_lease_recurring_credit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **transaction_id** | **int**|  | 

### Return type

[**LeaseRecurringCreditMessage**](LeaseRecurringCreditMessage.md)

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

# **external_api_lease_recurring_payments_create_lease_recurring_payment**
> LeaseRecurringPaymentMessage external_api_lease_recurring_payments_create_lease_recurring_payment(lease_id, payment_recurring_transaction_post_message)

Create a recurring payment

Creates a recurring payment that will post automatically on the specified lease ledger.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease Transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_recurring_payment_message import LeaseRecurringPaymentMessage
from buildium_sdk.models.payment_recurring_transaction_post_message import PaymentRecurringTransactionPostMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    payment_recurring_transaction_post_message = buildium_sdk.PaymentRecurringTransactionPostMessage() # PaymentRecurringTransactionPostMessage | 

    try:
        # Create a recurring payment
        api_response = await api_instance.external_api_lease_recurring_payments_create_lease_recurring_payment(lease_id, payment_recurring_transaction_post_message)
        print("The response of LeaseTransactionsApi->external_api_lease_recurring_payments_create_lease_recurring_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_recurring_payments_create_lease_recurring_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **payment_recurring_transaction_post_message** | [**PaymentRecurringTransactionPostMessage**](PaymentRecurringTransactionPostMessage.md)|  | 

### Return type

[**LeaseRecurringPaymentMessage**](LeaseRecurringPaymentMessage.md)

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

# **external_api_lease_recurring_payments_get_recurring_lease_payments_by_id**
> LeaseRecurringPaymentMessage external_api_lease_recurring_payments_get_recurring_lease_payments_by_id(lease_id, payment_id)

Retrieve a recurring payment

Retrieves a recurring payment.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease Transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.lease_recurring_payment_message import LeaseRecurringPaymentMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    payment_id = 56 # int | 

    try:
        # Retrieve a recurring payment
        api_response = await api_instance.external_api_lease_recurring_payments_get_recurring_lease_payments_by_id(lease_id, payment_id)
        print("The response of LeaseTransactionsApi->external_api_lease_recurring_payments_get_recurring_lease_payments_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_recurring_payments_get_recurring_lease_payments_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **payment_id** | **int**|  | 

### Return type

[**LeaseRecurringPaymentMessage**](LeaseRecurringPaymentMessage.md)

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

# **external_api_lease_recurring_transactions_get_lease_recurring_transactions**
> List[RecurringTransactionMessage] external_api_lease_recurring_transactions_get_lease_recurring_transactions(lease_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all recurring transactions

Retrieves all recurring transactions for a given lease.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.recurring_transaction_message import RecurringTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    lease_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all recurring transactions
        api_response = await api_instance.external_api_lease_recurring_transactions_get_lease_recurring_transactions(lease_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeaseTransactionsApi->external_api_lease_recurring_transactions_get_lease_recurring_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_recurring_transactions_get_lease_recurring_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[RecurringTransactionMessage]**](RecurringTransactionMessage.md)

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

# **external_api_lease_recurring_transactions_get_recurring_transactions_for_all_leases**
> List[BulkLeaseRecurringTransactionMessage] external_api_lease_recurring_transactions_get_recurring_transactions_for_all_leases(leaseids=leaseids, createddatetimefrom=createddatetimefrom, createddatetimeto=createddatetimeto, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)

Retrieve all recurring transactions for all leases

Retrieves all recurring transactions for all leases.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Rentals > Lease transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bulk_lease_recurring_transaction_message import BulkLeaseRecurringTransactionMessage
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
    api_instance = buildium_sdk.LeaseTransactionsApi(api_client)
    leaseids = [56] # List[int] | Filters results to only include records associated with the provided lease Ids. (optional)
    createddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to recurring transactions created after the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. (optional)
    createddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to recurring transactions created before the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to recurring transactions last updated after the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to recurring transactions last updated before the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all recurring transactions for all leases
        api_response = await api_instance.external_api_lease_recurring_transactions_get_recurring_transactions_for_all_leases(leaseids=leaseids, createddatetimefrom=createddatetimefrom, createddatetimeto=createddatetimeto, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)
        print("The response of LeaseTransactionsApi->external_api_lease_recurring_transactions_get_recurring_transactions_for_all_leases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaseTransactionsApi->external_api_lease_recurring_transactions_get_recurring_transactions_for_all_leases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaseids** | [**List[int]**](int.md)| Filters results to only include records associated with the provided lease Ids. | [optional] 
 **createddatetimefrom** | **datetime**| Filters results to recurring transactions created after the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. | [optional] 
 **createddatetimeto** | **datetime**| Filters results to recurring transactions created before the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to recurring transactions last updated after the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to recurring transactions last updated before the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BulkLeaseRecurringTransactionMessage]**](BulkLeaseRecurringTransactionMessage.md)

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

