# buildium_sdk.ClientLeadsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_client_leads_get_client_leads**](ClientLeadsApi.md#external_api_client_leads_get_client_leads) | **GET** /v1/clientleads | Retrieve all client leads
[**external_api_client_leads_get_prospective_client**](ClientLeadsApi.md#external_api_client_leads_get_prospective_client) | **GET** /v1/clientleads/{clientLeadId} | Retrieve a client lead


# **external_api_client_leads_get_client_leads**
> List[ClientLeadMessage] external_api_client_leads_get_client_leads(leadstatuses=leadstatuses, propertytypes=propertytypes, datereceivedfrom=datereceivedfrom, datereceivedto=datereceivedto, includecreditedleads=includecreditedleads, orderby=orderby, offset=offset, limit=limit)

Retrieve all client leads

Retrieves all client leads
            


            Note: When using the `orderby` query string parameter, the only supported options are DateReceived.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Administration > All Property Management</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.client_lead_message import ClientLeadMessage
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
    api_instance = buildium_sdk.ClientLeadsApi(api_client)
    leadstatuses = ['leadstatuses_example'] # List[str] | Filters results to any client leads that are in one of the given statuses. (optional)
    propertytypes = ['propertytypes_example'] # List[str] | Filters results to any client leads that have a property in one of the given property types. (optional)
    datereceivedfrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any client leads that were received on or after the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    datereceivedto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any client leads that were received on or before the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    includecreditedleads = True # bool | This will also return client leads that were credited. By default credited leads will not be returned. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all client leads
        api_response = await api_instance.external_api_client_leads_get_client_leads(leadstatuses=leadstatuses, propertytypes=propertytypes, datereceivedfrom=datereceivedfrom, datereceivedto=datereceivedto, includecreditedleads=includecreditedleads, orderby=orderby, offset=offset, limit=limit)
        print("The response of ClientLeadsApi->external_api_client_leads_get_client_leads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientLeadsApi->external_api_client_leads_get_client_leads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leadstatuses** | [**List[str]**](str.md)| Filters results to any client leads that are in one of the given statuses. | [optional] 
 **propertytypes** | [**List[str]**](str.md)| Filters results to any client leads that have a property in one of the given property types. | [optional] 
 **datereceivedfrom** | **datetime**| Filters results to any client leads that were received on or after the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **datereceivedto** | **datetime**| Filters results to any client leads that were received on or before the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **includecreditedleads** | **bool**| This will also return client leads that were credited. By default credited leads will not be returned. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[ClientLeadMessage]**](ClientLeadMessage.md)

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

# **external_api_client_leads_get_prospective_client**
> ClientLeadMessage external_api_client_leads_get_prospective_client(client_lead_id)

Retrieve a client lead

Retrieves a specific client lead
            

<h4>Required permission(s):</h4><span class="permissionBlock">Administration > All Property Management</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.client_lead_message import ClientLeadMessage
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
    api_instance = buildium_sdk.ClientLeadsApi(api_client)
    client_lead_id = 56 # int | 

    try:
        # Retrieve a client lead
        api_response = await api_instance.external_api_client_leads_get_prospective_client(client_lead_id)
        print("The response of ClientLeadsApi->external_api_client_leads_get_prospective_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientLeadsApi->external_api_client_leads_get_prospective_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_lead_id** | **int**|  | 

### Return type

[**ClientLeadMessage**](ClientLeadMessage.md)

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

