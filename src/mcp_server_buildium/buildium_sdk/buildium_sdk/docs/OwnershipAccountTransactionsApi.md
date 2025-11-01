# buildium_sdk.OwnershipAccountTransactionsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_ownership_account_auto_allocated_payment_create_ownership_account_auto_allocated_payment**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_auto_allocated_payment_create_ownership_account_auto_allocated_payment) | **POST** /v1/associations/ownershipaccounts/{ownershipAccountId}/autoallocatedpayments | Create a payment (auto allocated)
[**external_api_ownership_account_charge_recurring_transactions_create_ownership_accounts_charge_recurring_transaction**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_charge_recurring_transactions_create_ownership_accounts_charge_recurring_transaction) | **POST** /v1/associations/ownershipaccounts/{ownershipAccountId}/recurringcharges | Create a recurring charge
[**external_api_ownership_account_charge_recurring_transactions_get_ownership_accounts_charge_recurring_transaction_by_id**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_charge_recurring_transactions_get_ownership_accounts_charge_recurring_transaction_by_id) | **GET** /v1/associations/ownershipaccounts/{ownershipAccountId}/recurringcharges/{transactionId} | Retrieve a recurring charge
[**external_api_ownership_account_deposit_withholding_create_ownership_account_deposit_withholding**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_deposit_withholding_create_ownership_account_deposit_withholding) | **POST** /v1/associations/ownershipaccounts/{ownershipAccountId}/applieddeposits | Create a deposit withholding
[**external_api_ownership_account_deposit_withholding_update_ownership_account_deposit_withholding**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_deposit_withholding_update_ownership_account_deposit_withholding) | **PUT** /v1/associations/ownershipaccounts/{ownershipAccountId}/applieddeposits/{depositId} | Update a deposit withholding
[**external_api_ownership_account_ledger_charges_create_charge**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_ledger_charges_create_charge) | **POST** /v1/associations/ownershipaccounts/{ownershipAccountId}/charges | Create a charge
[**external_api_ownership_account_ledger_charges_get_all_ownership_account_charges**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_ledger_charges_get_all_ownership_account_charges) | **GET** /v1/associations/ownershipaccounts/{ownershipAccountId}/charges | Retrieve all charges
[**external_api_ownership_account_ledger_charges_get_ownership_account_charge_by_id**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_ledger_charges_get_ownership_account_charge_by_id) | **GET** /v1/associations/ownershipaccounts/{ownershipAccountId}/charges/{chargeId} | Retrieve a charge
[**external_api_ownership_account_ledger_charges_update_ownership_account_charge**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_ledger_charges_update_ownership_account_charge) | **PUT** /v1/associations/ownershipaccounts/{ownershipAccountId}/charges/{chargeId} | Update a charge
[**external_api_ownership_account_ledger_credits_create_ownership_account_credit**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_ledger_credits_create_ownership_account_credit) | **POST** /v1/associations/ownershipaccounts/{ownershipAccountId}/credits | Create a credit
[**external_api_ownership_account_ledger_payments_create_ownership_account_ledger_payment**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_ledger_payments_create_ownership_account_ledger_payment) | **POST** /v1/associations/ownershipaccounts/{ownershipAccountId}/payments | Create a payment
[**external_api_ownership_account_ledger_payments_update_ownership_account_ledger_payment**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_ledger_payments_update_ownership_account_ledger_payment) | **PUT** /v1/associations/ownershipaccounts/{ownershipAccountId}/payments/{paymentId} | Update a payment
[**external_api_ownership_account_outstanding_balances_get_ownership_account_outstanding_balances**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_outstanding_balances_get_ownership_account_outstanding_balances) | **GET** /v1/associations/ownershipaccounts/outstandingbalances | Retrieve all outstanding balances
[**external_api_ownership_account_recurring_credits_create_ownership_account_credit_recurring_transaction**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_recurring_credits_create_ownership_account_credit_recurring_transaction) | **POST** /v1/associations/ownershipaccounts/{ownershipAccountId}/recurringcredits | Create a recurring credit
[**external_api_ownership_account_recurring_credits_get_ownership_account_recurring_credit_by_id**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_recurring_credits_get_ownership_account_recurring_credit_by_id) | **GET** /v1/associations/ownershipaccounts/{ownershipAccountId}/recurringcredits/{transactionId} | Retrieve a recurring credit
[**external_api_ownership_account_recurring_payments_create_ownership_account_recurring_payment**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_recurring_payments_create_ownership_account_recurring_payment) | **POST** /v1/associations/ownershipaccounts/{ownershipAccountId}/recurringpayments | Create a recurring payment
[**external_api_ownership_account_recurring_payments_get_recurring_ownership_account_payments_by_id**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_recurring_payments_get_recurring_ownership_account_payments_by_id) | **GET** /v1/associations/ownershipaccounts/{ownershipAccountId}/recurringpayments/{paymentId} | Retrieve a recurring payment
[**external_api_ownership_account_recurring_transactions_get_association_recurring_transaction**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_recurring_transactions_get_association_recurring_transaction) | **GET** /v1/associations/ownershipaccounts/{ownershipAccountId}/recurringtransactions | Retrieve all recurring transactions
[**external_api_ownership_account_recurring_transactions_get_recurring_transactions_for_all_ownership_accounts**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_recurring_transactions_get_recurring_transactions_for_all_ownership_accounts) | **GET** /v1/associations/ownershipaccounts/recurringtransactions | Retrieve all recurring transactions for all ownership accounts
[**external_api_ownership_account_refund_create_ownership_account_refund**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_refund_create_ownership_account_refund) | **POST** /v1/associations/ownershipaccounts/{ownershipAccountId}/refunds | Create a refund
[**external_api_ownership_account_refund_get_ownership_account_refund_by_id**](OwnershipAccountTransactionsApi.md#external_api_ownership_account_refund_get_ownership_account_refund_by_id) | **GET** /v1/associations/ownershipaccounts/{ownershipAccountId}/refunds/{refundId} | Retrieve a refund
[**external_api_ownership_accounts_ledger_get_ownership_account_ledger**](OwnershipAccountTransactionsApi.md#external_api_ownership_accounts_ledger_get_ownership_account_ledger) | **GET** /v1/associations/ownershipaccounts/{ownershipAccountId}/transactions | Retrieve all transactions
[**external_api_ownership_accounts_ledger_get_ownership_account_transaction_by_id**](OwnershipAccountTransactionsApi.md#external_api_ownership_accounts_ledger_get_ownership_account_transaction_by_id) | **GET** /v1/associations/ownershipaccounts/{ownershipAccountId}/transactions/{transactionId} | Retrieve a transaction


# **external_api_ownership_account_auto_allocated_payment_create_ownership_account_auto_allocated_payment**
> OwnershipAccountTransactionMessage external_api_ownership_account_auto_allocated_payment_create_ownership_account_auto_allocated_payment(ownership_account_id, ownership_account_auto_allocated_payment_post_message)

Create a payment (auto allocated)

Creates a payment on the ownership account ledger. Note that the recorded payment will be automatically allocated to the general ledger accounts based on the payment allocation settings. These settings can be found under the Settings > Application Settings > Residents page in your account. If you'd like to specify the general ledger accounts the payment should apply to, please use the <a href="#operation/ExternalApiOwnershipAccountLedgerPayments_CreateOwnershipAccountLedgerPayment">Create a payment</a> endpoint. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_auto_allocated_payment_post_message import OwnershipAccountAutoAllocatedPaymentPostMessage
from buildium_sdk.models.ownership_account_transaction_message import OwnershipAccountTransactionMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    ownership_account_auto_allocated_payment_post_message = buildium_sdk.OwnershipAccountAutoAllocatedPaymentPostMessage() # OwnershipAccountAutoAllocatedPaymentPostMessage | 

    try:
        # Create a payment (auto allocated)
        api_response = await api_instance.external_api_ownership_account_auto_allocated_payment_create_ownership_account_auto_allocated_payment(ownership_account_id, ownership_account_auto_allocated_payment_post_message)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_auto_allocated_payment_create_ownership_account_auto_allocated_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_auto_allocated_payment_create_ownership_account_auto_allocated_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **ownership_account_auto_allocated_payment_post_message** | [**OwnershipAccountAutoAllocatedPaymentPostMessage**](OwnershipAccountAutoAllocatedPaymentPostMessage.md)|  | 

### Return type

[**OwnershipAccountTransactionMessage**](OwnershipAccountTransactionMessage.md)

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

# **external_api_ownership_account_charge_recurring_transactions_create_ownership_accounts_charge_recurring_transaction**
> OwnershipAccountChargeRecurringTransactionMessage external_api_ownership_account_charge_recurring_transactions_create_ownership_accounts_charge_recurring_transaction(ownership_account_id, charge_recurring_transaction_post_message)

Create a recurring charge

Creates a recurring charge transaction that will post automatically on the specified ownership account ledger.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.charge_recurring_transaction_post_message import ChargeRecurringTransactionPostMessage
from buildium_sdk.models.ownership_account_charge_recurring_transaction_message import OwnershipAccountChargeRecurringTransactionMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    charge_recurring_transaction_post_message = buildium_sdk.ChargeRecurringTransactionPostMessage() # ChargeRecurringTransactionPostMessage | 

    try:
        # Create a recurring charge
        api_response = await api_instance.external_api_ownership_account_charge_recurring_transactions_create_ownership_accounts_charge_recurring_transaction(ownership_account_id, charge_recurring_transaction_post_message)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_charge_recurring_transactions_create_ownership_accounts_charge_recurring_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_charge_recurring_transactions_create_ownership_accounts_charge_recurring_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **charge_recurring_transaction_post_message** | [**ChargeRecurringTransactionPostMessage**](ChargeRecurringTransactionPostMessage.md)|  | 

### Return type

[**OwnershipAccountChargeRecurringTransactionMessage**](OwnershipAccountChargeRecurringTransactionMessage.md)

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

# **external_api_ownership_account_charge_recurring_transactions_get_ownership_accounts_charge_recurring_transaction_by_id**
> OwnershipAccountChargeRecurringTransactionMessage external_api_ownership_account_charge_recurring_transactions_get_ownership_accounts_charge_recurring_transaction_by_id(ownership_account_id, transaction_id)

Retrieve a recurring charge

Retrieves a recurring charge.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_charge_recurring_transaction_message import OwnershipAccountChargeRecurringTransactionMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    transaction_id = 56 # int | 

    try:
        # Retrieve a recurring charge
        api_response = await api_instance.external_api_ownership_account_charge_recurring_transactions_get_ownership_accounts_charge_recurring_transaction_by_id(ownership_account_id, transaction_id)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_charge_recurring_transactions_get_ownership_accounts_charge_recurring_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_charge_recurring_transactions_get_ownership_accounts_charge_recurring_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **transaction_id** | **int**|  | 

### Return type

[**OwnershipAccountChargeRecurringTransactionMessage**](OwnershipAccountChargeRecurringTransactionMessage.md)

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

# **external_api_ownership_account_deposit_withholding_create_ownership_account_deposit_withholding**
> OwnershipAccountTransactionMessage external_api_ownership_account_deposit_withholding_create_ownership_account_deposit_withholding(ownership_account_id, ownership_account_deposit_withholding_post_message)

Create a deposit withholding

Withholds an association owner deposit by reallocating the funds from a liability account to an income account to cover an expense(s).
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View` `Edit`
            <span class="permissionBlock">Accounting > General Ledger Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_deposit_withholding_post_message import OwnershipAccountDepositWithholdingPostMessage
from buildium_sdk.models.ownership_account_transaction_message import OwnershipAccountTransactionMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    ownership_account_deposit_withholding_post_message = buildium_sdk.OwnershipAccountDepositWithholdingPostMessage() # OwnershipAccountDepositWithholdingPostMessage | 

    try:
        # Create a deposit withholding
        api_response = await api_instance.external_api_ownership_account_deposit_withholding_create_ownership_account_deposit_withholding(ownership_account_id, ownership_account_deposit_withholding_post_message)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_deposit_withholding_create_ownership_account_deposit_withholding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_deposit_withholding_create_ownership_account_deposit_withholding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **ownership_account_deposit_withholding_post_message** | [**OwnershipAccountDepositWithholdingPostMessage**](OwnershipAccountDepositWithholdingPostMessage.md)|  | 

### Return type

[**OwnershipAccountTransactionMessage**](OwnershipAccountTransactionMessage.md)

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

# **external_api_ownership_account_deposit_withholding_update_ownership_account_deposit_withholding**
> OwnershipAccountTransactionMessage external_api_ownership_account_deposit_withholding_update_ownership_account_deposit_withholding(ownership_account_id, deposit_id, ownership_account_deposit_withholding_put_message)

Update a deposit withholding

Updates an ownership account deposit withholding.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View` `Edit`
            <span class="permissionBlock">Accounting > General Ledger Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_deposit_withholding_put_message import OwnershipAccountDepositWithholdingPutMessage
from buildium_sdk.models.ownership_account_transaction_message import OwnershipAccountTransactionMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    deposit_id = 56 # int | 
    ownership_account_deposit_withholding_put_message = buildium_sdk.OwnershipAccountDepositWithholdingPutMessage() # OwnershipAccountDepositWithholdingPutMessage | 

    try:
        # Update a deposit withholding
        api_response = await api_instance.external_api_ownership_account_deposit_withholding_update_ownership_account_deposit_withholding(ownership_account_id, deposit_id, ownership_account_deposit_withholding_put_message)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_deposit_withholding_update_ownership_account_deposit_withholding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_deposit_withholding_update_ownership_account_deposit_withholding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **deposit_id** | **int**|  | 
 **ownership_account_deposit_withholding_put_message** | [**OwnershipAccountDepositWithholdingPutMessage**](OwnershipAccountDepositWithholdingPutMessage.md)|  | 

### Return type

[**OwnershipAccountTransactionMessage**](OwnershipAccountTransactionMessage.md)

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

# **external_api_ownership_account_ledger_charges_create_charge**
> OwnershipAccountTransactionMessage external_api_ownership_account_ledger_charges_create_charge(ownership_account_id, ownership_account_ledger_charge_post_message)

Create a charge

Creates a ledger charge.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View` `Edit`

<span class="permissionBlock">Accounting > Bills</span> - `View` `Edit` In order to associate the charge to a bill using the BillId property, you must have this permission.

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_ledger_charge_post_message import OwnershipAccountLedgerChargePostMessage
from buildium_sdk.models.ownership_account_transaction_message import OwnershipAccountTransactionMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | The ownership account identifier.
    ownership_account_ledger_charge_post_message = buildium_sdk.OwnershipAccountLedgerChargePostMessage() # OwnershipAccountLedgerChargePostMessage | 

    try:
        # Create a charge
        api_response = await api_instance.external_api_ownership_account_ledger_charges_create_charge(ownership_account_id, ownership_account_ledger_charge_post_message)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_charges_create_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_charges_create_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**| The ownership account identifier. | 
 **ownership_account_ledger_charge_post_message** | [**OwnershipAccountLedgerChargePostMessage**](OwnershipAccountLedgerChargePostMessage.md)|  | 

### Return type

[**OwnershipAccountTransactionMessage**](OwnershipAccountTransactionMessage.md)

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

# **external_api_ownership_account_ledger_charges_get_all_ownership_account_charges**
> List[OwnershipAccountLedgerChargeMessage] external_api_ownership_account_ledger_charges_get_all_ownership_account_charges(ownership_account_id, transactiondatefrom=transactiondatefrom, transactiondateto=transactiondateto, billids=billids, orderby=orderby, offset=offset, limit=limit)

Retrieve all charges

Retrieves all ledger charges for a specific ownership account.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_ledger_charge_message import OwnershipAccountLedgerChargeMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    transactiondatefrom = '2013-10-20' # date | Filters results to any lease transaction whose start date is greater than or equal to the specified value. (optional)
    transactiondateto = '2013-10-20' # date | Filters results to any lease transaction whose end date is less than or equal to the specified value. (optional)
    billids = [56] # List[int] | Filters results to any charge that has been associated to the indicated bill ids. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all charges
        api_response = await api_instance.external_api_ownership_account_ledger_charges_get_all_ownership_account_charges(ownership_account_id, transactiondatefrom=transactiondatefrom, transactiondateto=transactiondateto, billids=billids, orderby=orderby, offset=offset, limit=limit)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_charges_get_all_ownership_account_charges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_charges_get_all_ownership_account_charges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **transactiondatefrom** | **date**| Filters results to any lease transaction whose start date is greater than or equal to the specified value. | [optional] 
 **transactiondateto** | **date**| Filters results to any lease transaction whose end date is less than or equal to the specified value. | [optional] 
 **billids** | [**List[int]**](int.md)| Filters results to any charge that has been associated to the indicated bill ids. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[OwnershipAccountLedgerChargeMessage]**](OwnershipAccountLedgerChargeMessage.md)

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

# **external_api_ownership_account_ledger_charges_get_ownership_account_charge_by_id**
> OwnershipAccountLedgerChargeMessage external_api_ownership_account_ledger_charges_get_ownership_account_charge_by_id(ownership_account_id, charge_id)

Retrieve a charge

Retrieves a specific ownership account ledger charge.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_ledger_charge_message import OwnershipAccountLedgerChargeMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | The ownership account identifier.
    charge_id = 56 # int | 

    try:
        # Retrieve a charge
        api_response = await api_instance.external_api_ownership_account_ledger_charges_get_ownership_account_charge_by_id(ownership_account_id, charge_id)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_charges_get_ownership_account_charge_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_charges_get_ownership_account_charge_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**| The ownership account identifier. | 
 **charge_id** | **int**|  | 

### Return type

[**OwnershipAccountLedgerChargeMessage**](OwnershipAccountLedgerChargeMessage.md)

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
**404** | Lease not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_ownership_account_ledger_charges_update_ownership_account_charge**
> OwnershipAccountTransactionMessage external_api_ownership_account_ledger_charges_update_ownership_account_charge(ownership_account_id, charge_id, ownership_account_ledger_charge_put_message)

Update a charge

Updates a charge.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View` `Edit`
            


### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_ledger_charge_put_message import OwnershipAccountLedgerChargePutMessage
from buildium_sdk.models.ownership_account_transaction_message import OwnershipAccountTransactionMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | The ownership account identifier.
    charge_id = 56 # int | The charge identifier.
    ownership_account_ledger_charge_put_message = buildium_sdk.OwnershipAccountLedgerChargePutMessage() # OwnershipAccountLedgerChargePutMessage | 

    try:
        # Update a charge
        api_response = await api_instance.external_api_ownership_account_ledger_charges_update_ownership_account_charge(ownership_account_id, charge_id, ownership_account_ledger_charge_put_message)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_charges_update_ownership_account_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_charges_update_ownership_account_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**| The ownership account identifier. | 
 **charge_id** | **int**| The charge identifier. | 
 **ownership_account_ledger_charge_put_message** | [**OwnershipAccountLedgerChargePutMessage**](OwnershipAccountLedgerChargePutMessage.md)|  | 

### Return type

[**OwnershipAccountTransactionMessage**](OwnershipAccountTransactionMessage.md)

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

# **external_api_ownership_account_ledger_credits_create_ownership_account_credit**
> OwnershipAccountTransactionMessage external_api_ownership_account_ledger_credits_create_ownership_account_credit(ownership_account_id, ownership_account_credit_post_message)

Create a credit

Creates a ledger credit.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_credit_post_message import OwnershipAccountCreditPostMessage
from buildium_sdk.models.ownership_account_transaction_message import OwnershipAccountTransactionMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    ownership_account_credit_post_message = buildium_sdk.OwnershipAccountCreditPostMessage() # OwnershipAccountCreditPostMessage | 

    try:
        # Create a credit
        api_response = await api_instance.external_api_ownership_account_ledger_credits_create_ownership_account_credit(ownership_account_id, ownership_account_credit_post_message)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_credits_create_ownership_account_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_credits_create_ownership_account_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **ownership_account_credit_post_message** | [**OwnershipAccountCreditPostMessage**](OwnershipAccountCreditPostMessage.md)|  | 

### Return type

[**OwnershipAccountTransactionMessage**](OwnershipAccountTransactionMessage.md)

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

# **external_api_ownership_account_ledger_payments_create_ownership_account_ledger_payment**
> OwnershipAccountTransactionMessage external_api_ownership_account_ledger_payments_create_ownership_account_ledger_payment(ownership_account_id, ownership_account_ledger_payment_post_message)

Create a payment

Creates a ledger payment.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_ledger_payment_post_message import OwnershipAccountLedgerPaymentPostMessage
from buildium_sdk.models.ownership_account_transaction_message import OwnershipAccountTransactionMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    ownership_account_ledger_payment_post_message = buildium_sdk.OwnershipAccountLedgerPaymentPostMessage() # OwnershipAccountLedgerPaymentPostMessage | 

    try:
        # Create a payment
        api_response = await api_instance.external_api_ownership_account_ledger_payments_create_ownership_account_ledger_payment(ownership_account_id, ownership_account_ledger_payment_post_message)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_payments_create_ownership_account_ledger_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_payments_create_ownership_account_ledger_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **ownership_account_ledger_payment_post_message** | [**OwnershipAccountLedgerPaymentPostMessage**](OwnershipAccountLedgerPaymentPostMessage.md)|  | 

### Return type

[**OwnershipAccountTransactionMessage**](OwnershipAccountTransactionMessage.md)

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

# **external_api_ownership_account_ledger_payments_update_ownership_account_ledger_payment**
> OwnershipAccountTransactionMessage external_api_ownership_account_ledger_payments_update_ownership_account_ledger_payment(ownership_account_id, payment_id, ownership_account_ledger_payment_put_message)

Update a payment

Updates a ledger payment. Each line item must have a unique general ledger account identifier. PaymentMethod, Date, Memo, and the total Amount cannot be changed for payments with a PaymentMethod of `BuildiumEFT`, `BuildiumCC` or `RetailCash`.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_ledger_payment_put_message import OwnershipAccountLedgerPaymentPutMessage
from buildium_sdk.models.ownership_account_transaction_message import OwnershipAccountTransactionMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    payment_id = 56 # int | 
    ownership_account_ledger_payment_put_message = buildium_sdk.OwnershipAccountLedgerPaymentPutMessage() # OwnershipAccountLedgerPaymentPutMessage | 

    try:
        # Update a payment
        api_response = await api_instance.external_api_ownership_account_ledger_payments_update_ownership_account_ledger_payment(ownership_account_id, payment_id, ownership_account_ledger_payment_put_message)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_payments_update_ownership_account_ledger_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_ledger_payments_update_ownership_account_ledger_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **payment_id** | **int**|  | 
 **ownership_account_ledger_payment_put_message** | [**OwnershipAccountLedgerPaymentPutMessage**](OwnershipAccountLedgerPaymentPutMessage.md)|  | 

### Return type

[**OwnershipAccountTransactionMessage**](OwnershipAccountTransactionMessage.md)

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

# **external_api_ownership_account_outstanding_balances_get_ownership_account_outstanding_balances**
> List[OwnershipAccountOutstandingBalanceMessage] external_api_ownership_account_outstanding_balances_get_ownership_account_outstanding_balances(associationid=associationid, ownershipaccountstatuses=ownershipaccountstatuses, ownershipaccountids=ownershipaccountids, pastdueemail=pastdueemail, balanceduration=balanceduration, orderby=orderby, offset=offset, limit=limit)

Retrieve all outstanding balances

Retrieves a list of ownership account outstanding balances.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Outstanding Balances</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_outstanding_balance_message import OwnershipAccountOutstandingBalanceMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    associationid = 56 # int | Association unique identifier (optional)
    ownershipaccountstatuses = ['ownershipaccountstatuses_example'] # List[str] | List of ownership account statuses (optional)
    ownershipaccountids = [56] # List[int] | List of ownership account ids (optional)
    pastdueemail = 'pastdueemail_example' # str | Status of notification of outstanding balances (optional)
    balanceduration = 'balanceduration_example' # str | Duration of outstanding balances (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all outstanding balances
        api_response = await api_instance.external_api_ownership_account_outstanding_balances_get_ownership_account_outstanding_balances(associationid=associationid, ownershipaccountstatuses=ownershipaccountstatuses, ownershipaccountids=ownershipaccountids, pastdueemail=pastdueemail, balanceduration=balanceduration, orderby=orderby, offset=offset, limit=limit)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_outstanding_balances_get_ownership_account_outstanding_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_outstanding_balances_get_ownership_account_outstanding_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **associationid** | **int**| Association unique identifier | [optional] 
 **ownershipaccountstatuses** | [**List[str]**](str.md)| List of ownership account statuses | [optional] 
 **ownershipaccountids** | [**List[int]**](int.md)| List of ownership account ids | [optional] 
 **pastdueemail** | **str**| Status of notification of outstanding balances | [optional] 
 **balanceduration** | **str**| Duration of outstanding balances | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[OwnershipAccountOutstandingBalanceMessage]**](OwnershipAccountOutstandingBalanceMessage.md)

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

# **external_api_ownership_account_recurring_credits_create_ownership_account_credit_recurring_transaction**
> OwnershipAccountRecurringCreditMessage external_api_ownership_account_recurring_credits_create_ownership_account_credit_recurring_transaction(ownership_account_id, credit_recurring_transaction_post_message)

Create a recurring credit

Creates a recurring credit transaction that will post automatically on the specified ownership account ledger.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.credit_recurring_transaction_post_message import CreditRecurringTransactionPostMessage
from buildium_sdk.models.ownership_account_recurring_credit_message import OwnershipAccountRecurringCreditMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    credit_recurring_transaction_post_message = buildium_sdk.CreditRecurringTransactionPostMessage() # CreditRecurringTransactionPostMessage | 

    try:
        # Create a recurring credit
        api_response = await api_instance.external_api_ownership_account_recurring_credits_create_ownership_account_credit_recurring_transaction(ownership_account_id, credit_recurring_transaction_post_message)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_recurring_credits_create_ownership_account_credit_recurring_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_recurring_credits_create_ownership_account_credit_recurring_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **credit_recurring_transaction_post_message** | [**CreditRecurringTransactionPostMessage**](CreditRecurringTransactionPostMessage.md)|  | 

### Return type

[**OwnershipAccountRecurringCreditMessage**](OwnershipAccountRecurringCreditMessage.md)

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

# **external_api_ownership_account_recurring_credits_get_ownership_account_recurring_credit_by_id**
> OwnershipAccountRecurringCreditMessage external_api_ownership_account_recurring_credits_get_ownership_account_recurring_credit_by_id(ownership_account_id, transaction_id)

Retrieve a recurring credit

Retrieves a recurring credit.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_recurring_credit_message import OwnershipAccountRecurringCreditMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    transaction_id = 56 # int | 

    try:
        # Retrieve a recurring credit
        api_response = await api_instance.external_api_ownership_account_recurring_credits_get_ownership_account_recurring_credit_by_id(ownership_account_id, transaction_id)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_recurring_credits_get_ownership_account_recurring_credit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_recurring_credits_get_ownership_account_recurring_credit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **transaction_id** | **int**|  | 

### Return type

[**OwnershipAccountRecurringCreditMessage**](OwnershipAccountRecurringCreditMessage.md)

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

# **external_api_ownership_account_recurring_payments_create_ownership_account_recurring_payment**
> OwnershipAccountRecurringPaymentMessage external_api_ownership_account_recurring_payments_create_ownership_account_recurring_payment(ownership_account_id, payment_recurring_transaction_post_message)

Create a recurring payment

Creates a recurring payment that will post automatically on the specified ownership account ledger.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_recurring_payment_message import OwnershipAccountRecurringPaymentMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    payment_recurring_transaction_post_message = buildium_sdk.PaymentRecurringTransactionPostMessage() # PaymentRecurringTransactionPostMessage | 

    try:
        # Create a recurring payment
        api_response = await api_instance.external_api_ownership_account_recurring_payments_create_ownership_account_recurring_payment(ownership_account_id, payment_recurring_transaction_post_message)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_recurring_payments_create_ownership_account_recurring_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_recurring_payments_create_ownership_account_recurring_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **payment_recurring_transaction_post_message** | [**PaymentRecurringTransactionPostMessage**](PaymentRecurringTransactionPostMessage.md)|  | 

### Return type

[**OwnershipAccountRecurringPaymentMessage**](OwnershipAccountRecurringPaymentMessage.md)

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

# **external_api_ownership_account_recurring_payments_get_recurring_ownership_account_payments_by_id**
> OwnershipAccountRecurringPaymentMessage external_api_ownership_account_recurring_payments_get_recurring_ownership_account_payments_by_id(ownership_account_id, payment_id)

Retrieve a recurring payment

Retrieves a recurring payment.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_recurring_payment_message import OwnershipAccountRecurringPaymentMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    payment_id = 56 # int | 

    try:
        # Retrieve a recurring payment
        api_response = await api_instance.external_api_ownership_account_recurring_payments_get_recurring_ownership_account_payments_by_id(ownership_account_id, payment_id)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_recurring_payments_get_recurring_ownership_account_payments_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_recurring_payments_get_recurring_ownership_account_payments_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **payment_id** | **int**|  | 

### Return type

[**OwnershipAccountRecurringPaymentMessage**](OwnershipAccountRecurringPaymentMessage.md)

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

# **external_api_ownership_account_recurring_transactions_get_association_recurring_transaction**
> List[RecurringTransactionMessage] external_api_ownership_account_recurring_transactions_get_association_recurring_transaction(ownership_account_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all recurring transactions

Retrieves all recurring transactions for an ownership account.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View`

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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all recurring transactions
        api_response = await api_instance.external_api_ownership_account_recurring_transactions_get_association_recurring_transaction(ownership_account_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_recurring_transactions_get_association_recurring_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_recurring_transactions_get_association_recurring_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
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

# **external_api_ownership_account_recurring_transactions_get_recurring_transactions_for_all_ownership_accounts**
> List[BulkOwnershipAccountRecurringTransactionMessage] external_api_ownership_account_recurring_transactions_get_recurring_transactions_for_all_ownership_accounts(ownershipaccountids=ownershipaccountids, createddatetimefrom=createddatetimefrom, createddatetimeto=createddatetimeto, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)

Retrieve all recurring transactions for all ownership accounts

Retrieves all recurring transactions for all ownership accounts.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.bulk_ownership_account_recurring_transaction_message import BulkOwnershipAccountRecurringTransactionMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownershipaccountids = [56] # List[int] | Filters results to only include records associated with the provided ownership account Ids. (optional)
    createddatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to recurring transactions created after the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. (optional)
    createddatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to recurring transactions created before the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. (optional)
    lastupdatedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to recurring transactions last updated after the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. (optional)
    lastupdatedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to recurring transactions last updated before the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all recurring transactions for all ownership accounts
        api_response = await api_instance.external_api_ownership_account_recurring_transactions_get_recurring_transactions_for_all_ownership_accounts(ownershipaccountids=ownershipaccountids, createddatetimefrom=createddatetimefrom, createddatetimeto=createddatetimeto, lastupdatedfrom=lastupdatedfrom, lastupdatedto=lastupdatedto, orderby=orderby, offset=offset, limit=limit)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_recurring_transactions_get_recurring_transactions_for_all_ownership_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_recurring_transactions_get_recurring_transactions_for_all_ownership_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownershipaccountids** | [**List[int]**](int.md)| Filters results to only include records associated with the provided ownership account Ids. | [optional] 
 **createddatetimefrom** | **datetime**| Filters results to recurring transactions created after the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. | [optional] 
 **createddatetimeto** | **datetime**| Filters results to recurring transactions created before the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. | [optional] 
 **lastupdatedfrom** | **datetime**| Filters results to recurring transactions last updated after the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. | [optional] 
 **lastupdatedto** | **datetime**| Filters results to recurring transactions last updated before the specified value. The value must be formatted as YYYY-MM-DD HH:MM:SS. The maximum date range is 365 days. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[BulkOwnershipAccountRecurringTransactionMessage]**](BulkOwnershipAccountRecurringTransactionMessage.md)

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

# **external_api_ownership_account_refund_create_ownership_account_refund**
> OwnershipAccountRefundMessage external_api_ownership_account_refund_create_ownership_account_refund(ownership_account_id, ownership_account_refund_post_message)

Create a refund

Creates a refund.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_refund_message import OwnershipAccountRefundMessage
from buildium_sdk.models.ownership_account_refund_post_message import OwnershipAccountRefundPostMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    ownership_account_refund_post_message = buildium_sdk.OwnershipAccountRefundPostMessage() # OwnershipAccountRefundPostMessage | 

    try:
        # Create a refund
        api_response = await api_instance.external_api_ownership_account_refund_create_ownership_account_refund(ownership_account_id, ownership_account_refund_post_message)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_refund_create_ownership_account_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_refund_create_ownership_account_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **ownership_account_refund_post_message** | [**OwnershipAccountRefundPostMessage**](OwnershipAccountRefundPostMessage.md)|  | 

### Return type

[**OwnershipAccountRefundMessage**](OwnershipAccountRefundMessage.md)

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

# **external_api_ownership_account_refund_get_ownership_account_refund_by_id**
> OwnershipAccountRefundMessage external_api_ownership_account_refund_get_ownership_account_refund_by_id(ownership_account_id, refund_id)

Retrieve a refund

Retrieves a refund.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Bank Accounts</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_refund_message import OwnershipAccountRefundMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | 
    refund_id = 56 # int | 

    try:
        # Retrieve a refund
        api_response = await api_instance.external_api_ownership_account_refund_get_ownership_account_refund_by_id(ownership_account_id, refund_id)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_account_refund_get_ownership_account_refund_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_account_refund_get_ownership_account_refund_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**|  | 
 **refund_id** | **int**|  | 

### Return type

[**OwnershipAccountRefundMessage**](OwnershipAccountRefundMessage.md)

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

# **external_api_ownership_accounts_ledger_get_ownership_account_ledger**
> List[OwnershipAccountTransactionMessage] external_api_ownership_accounts_ledger_get_ownership_account_ledger(ownership_account_id, transactiondatefrom=transactiondatefrom, transactiondateto=transactiondateto, transactiontypes=transactiontypes, orderby=orderby, offset=offset, limit=limit)

Retrieve all transactions

Retrieves all ledger transactions for a specific ownership account.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_transaction_message import OwnershipAccountTransactionMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | The ownership account identifier.
    transactiondatefrom = '2013-10-20' # date | Filters results to any lease transaction whose start date is greater than or equal to the specified value. (optional)
    transactiondateto = '2013-10-20' # date | Filters results to any lease transaction whose end date is less than or equal to the specified value. (optional)
    transactiontypes = ['transactiontypes_example'] # List[str] | Filters results to any lease transaction whose lease transaction type matches the specified status. If no type is specified, lease transactions with any type will be returned. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all transactions
        api_response = await api_instance.external_api_ownership_accounts_ledger_get_ownership_account_ledger(ownership_account_id, transactiondatefrom=transactiondatefrom, transactiondateto=transactiondateto, transactiontypes=transactiontypes, orderby=orderby, offset=offset, limit=limit)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_accounts_ledger_get_ownership_account_ledger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_accounts_ledger_get_ownership_account_ledger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**| The ownership account identifier. | 
 **transactiondatefrom** | **date**| Filters results to any lease transaction whose start date is greater than or equal to the specified value. | [optional] 
 **transactiondateto** | **date**| Filters results to any lease transaction whose end date is less than or equal to the specified value. | [optional] 
 **transactiontypes** | [**List[str]**](str.md)| Filters results to any lease transaction whose lease transaction type matches the specified status. If no type is specified, lease transactions with any type will be returned. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[OwnershipAccountTransactionMessage]**](OwnershipAccountTransactionMessage.md)

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

# **external_api_ownership_accounts_ledger_get_ownership_account_transaction_by_id**
> OwnershipAccountTransactionMessage external_api_ownership_accounts_ledger_get_ownership_account_transaction_by_id(ownership_account_id, transaction_id)

Retrieve a transaction

Retrieves a specific ownership account ledger transaction.


<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.ownership_account_transaction_message import OwnershipAccountTransactionMessage
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
    api_instance = buildium_sdk.OwnershipAccountTransactionsApi(api_client)
    ownership_account_id = 56 # int | The ownership account identifier.
    transaction_id = 56 # int | The transaction identifier.

    try:
        # Retrieve a transaction
        api_response = await api_instance.external_api_ownership_accounts_ledger_get_ownership_account_transaction_by_id(ownership_account_id, transaction_id)
        print("The response of OwnershipAccountTransactionsApi->external_api_ownership_accounts_ledger_get_ownership_account_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnershipAccountTransactionsApi->external_api_ownership_accounts_ledger_get_ownership_account_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_account_id** | **int**| The ownership account identifier. | 
 **transaction_id** | **int**| The transaction identifier. | 

### Return type

[**OwnershipAccountTransactionMessage**](OwnershipAccountTransactionMessage.md)

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

