# buildium_sdk.AssociationMeterReadingsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_association_delete_meter_reading_details_delete_meter_reading_details_for_association**](AssociationMeterReadingsApi.md#external_api_association_delete_meter_reading_details_delete_meter_reading_details_for_association) | **DELETE** /v1/associations/{associationId}/meterreadings/summary | Delete meter reading details for a given date
[**external_api_association_meter_reading_details_get_association_meter_reading_details_async**](AssociationMeterReadingsApi.md#external_api_association_meter_reading_details_get_association_meter_reading_details_async) | **GET** /v1/associations/{associationId}/meterreadings/summary | Retrieve all meter reading details
[**external_api_association_meter_reading_details_upsert_upsert_association_meter_reading_details_async**](AssociationMeterReadingsApi.md#external_api_association_meter_reading_details_upsert_upsert_association_meter_reading_details_async) | **PUT** /v1/associations/{associationId}/meterreadings/summary | Create/Update meter reading details
[**external_api_association_meter_readings_read_get_meter_readings_for_association**](AssociationMeterReadingsApi.md#external_api_association_meter_readings_read_get_meter_readings_for_association) | **GET** /v1/associations/{associationId}/meterreadings | Retrieve all meter readings


# **external_api_association_delete_meter_reading_details_delete_meter_reading_details_for_association**
> external_api_association_delete_meter_reading_details_delete_meter_reading_details_for_association(association_id, readingdate, metertype)

Delete meter reading details for a given date

Delete meter reading details for an association for a given date.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Ownership account transactions</span> - `View` `Edit` `Delete`

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
    api_instance = buildium_sdk.AssociationMeterReadingsApi(api_client)
    association_id = 56 # int | 
    readingdate = '2013-10-20' # date | Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.
    metertype = 'metertype_example' # str | Filters results to the specified meter type.

    try:
        # Delete meter reading details for a given date
        await api_instance.external_api_association_delete_meter_reading_details_delete_meter_reading_details_for_association(association_id, readingdate, metertype)
    except Exception as e:
        print("Exception when calling AssociationMeterReadingsApi->external_api_association_delete_meter_reading_details_delete_meter_reading_details_for_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
 **readingdate** | **date**| Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD. | 
 **metertype** | **str**| Filters results to the specified meter type. | 

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

# **external_api_association_meter_reading_details_get_association_meter_reading_details_async**
> MeterReadingDetailsMessage external_api_association_meter_reading_details_get_association_meter_reading_details_async(association_id, readingdate, metertype)

Retrieve all meter reading details

Retrieves all meter reading details for an association.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.meter_reading_details_message import MeterReadingDetailsMessage
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
    api_instance = buildium_sdk.AssociationMeterReadingsApi(api_client)
    association_id = 56 # int | 
    readingdate = '2013-10-20' # date | Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD.
    metertype = 'metertype_example' # str | Filters results to the specified meter type.

    try:
        # Retrieve all meter reading details
        api_response = await api_instance.external_api_association_meter_reading_details_get_association_meter_reading_details_async(association_id, readingdate, metertype)
        print("The response of AssociationMeterReadingsApi->external_api_association_meter_reading_details_get_association_meter_reading_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationMeterReadingsApi->external_api_association_meter_reading_details_get_association_meter_reading_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
 **readingdate** | **date**| Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD. | 
 **metertype** | **str**| Filters results to the specified meter type. | 

### Return type

[**MeterReadingDetailsMessage**](MeterReadingDetailsMessage.md)

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

# **external_api_association_meter_reading_details_upsert_upsert_association_meter_reading_details_async**
> MeterReadingDetailsMessage external_api_association_meter_reading_details_upsert_upsert_association_meter_reading_details_async(association_id, meter_reading_details_put_message, readingdate=readingdate, metertype=metertype)

Create/Update meter reading details

This endpoint can be used to both create and update a meter reading detail for an association.
            <ul><li>There can only be one meter reading detail for a given combination of MeterType and ReadingDate for an association</li><li>If you are updating an existing meter reading detail, use the query parameters to specify the existing meter reading detail to update.</li><li>If you are creating a new meter reading detail, do not pass any query parameters.</li><li>When adding a new item to the Details array, leave out the `Id` field.</li><li>When updating an existing item in the Details array, the `Id` field of the existing item must be included.</li></ul>

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.meter_reading_details_message import MeterReadingDetailsMessage
from buildium_sdk.models.meter_reading_details_put_message import MeterReadingDetailsPutMessage
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
    api_instance = buildium_sdk.AssociationMeterReadingsApi(api_client)
    association_id = 56 # int | 
    meter_reading_details_put_message = buildium_sdk.MeterReadingDetailsPutMessage() # MeterReadingDetailsPutMessage | 
    readingdate = '2013-10-20' # date | Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD. (optional)
    metertype = 'metertype_example' # str | Filters results to the specified meter type. (optional)

    try:
        # Create/Update meter reading details
        api_response = await api_instance.external_api_association_meter_reading_details_upsert_upsert_association_meter_reading_details_async(association_id, meter_reading_details_put_message, readingdate=readingdate, metertype=metertype)
        print("The response of AssociationMeterReadingsApi->external_api_association_meter_reading_details_upsert_upsert_association_meter_reading_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationMeterReadingsApi->external_api_association_meter_reading_details_upsert_upsert_association_meter_reading_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
 **meter_reading_details_put_message** | [**MeterReadingDetailsPutMessage**](MeterReadingDetailsPutMessage.md)|  | 
 **readingdate** | **date**| Filters results to any meter readings whose entry date is equal to the specified value. The value must be formatted as YYYY-MM-DD. | [optional] 
 **metertype** | **str**| Filters results to the specified meter type. | [optional] 

### Return type

[**MeterReadingDetailsMessage**](MeterReadingDetailsMessage.md)

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
**409** | There is a request conflict with the current state of the target resource. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_association_meter_readings_read_get_meter_readings_for_association**
> List[MeterReadingMessage] external_api_association_meter_readings_read_get_meter_readings_for_association(association_id, readingdatefrom, readingdateto, metertypes=metertypes, orderby=orderby, offset=offset, limit=limit)

Retrieve all meter readings

Retrieves all meter readings for an association.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Associations > Associations and units</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.meter_reading_message import MeterReadingMessage
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
    api_instance = buildium_sdk.AssociationMeterReadingsApi(api_client)
    association_id = 56 # int | 
    readingdatefrom = '2013-10-20' # date | Filters results to any meter readings whose entry date that is greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days.
    readingdateto = '2013-10-20' # date | Filters results to any meter readings whose entry date is less than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days.
    metertypes = ['metertypes_example'] # List[str] | Filters results to the specified meter types. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all meter readings
        api_response = await api_instance.external_api_association_meter_readings_read_get_meter_readings_for_association(association_id, readingdatefrom, readingdateto, metertypes=metertypes, orderby=orderby, offset=offset, limit=limit)
        print("The response of AssociationMeterReadingsApi->external_api_association_meter_readings_read_get_meter_readings_for_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationMeterReadingsApi->external_api_association_meter_readings_read_get_meter_readings_for_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_id** | **int**|  | 
 **readingdatefrom** | **date**| Filters results to any meter readings whose entry date that is greater than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days. | 
 **readingdateto** | **date**| Filters results to any meter readings whose entry date is less than or equal to the specified value. The value must be formatted as YYYY-MM-DD. The maximum date range is 365 days. | 
 **metertypes** | [**List[str]**](str.md)| Filters results to the specified meter types. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[MeterReadingMessage]**](MeterReadingMessage.md)

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

