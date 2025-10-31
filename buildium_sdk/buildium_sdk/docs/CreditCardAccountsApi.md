# buildium_sdk.CreditCardAccountsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_credit_card_accounts_update_credit_card_account**](CreditCardAccountsApi.md#external_api_credit_card_accounts_update_credit_card_account) | **PUT** /v1/creditcardaccounts/{creditCardAccountId} | Update a credit card account


# **external_api_credit_card_accounts_update_credit_card_account**
> CreditCardAccountMessage external_api_credit_card_accounts_update_credit_card_account(credit_card_account_id, credit_card_account_put_message)

Update a credit card account

Updates a credit card account.
            

<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Accounting > Banking</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.credit_card_account_message import CreditCardAccountMessage
from buildium_sdk.models.credit_card_account_put_message import CreditCardAccountPutMessage
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
    api_instance = buildium_sdk.CreditCardAccountsApi(api_client)
    credit_card_account_id = 56 # int | 
    credit_card_account_put_message = buildium_sdk.CreditCardAccountPutMessage() # CreditCardAccountPutMessage | 

    try:
        # Update a credit card account
        api_response = await api_instance.external_api_credit_card_accounts_update_credit_card_account(credit_card_account_id, credit_card_account_put_message)
        print("The response of CreditCardAccountsApi->external_api_credit_card_accounts_update_credit_card_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditCardAccountsApi->external_api_credit_card_accounts_update_credit_card_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_card_account_id** | **int**|  | 
 **credit_card_account_put_message** | [**CreditCardAccountPutMessage**](CreditCardAccountPutMessage.md)|  | 

### Return type

[**CreditCardAccountMessage**](CreditCardAccountMessage.md)

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

