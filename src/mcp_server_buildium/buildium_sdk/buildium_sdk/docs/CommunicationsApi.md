# buildium_sdk.CommunicationsApi

All URIs are relative to *https://api.buildium.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_api_announcement_properties_get_announcement_properties**](CommunicationsApi.md#external_api_announcement_properties_get_announcement_properties) | **GET** /v1/communications/announcements/{announcementId}/properties | Retrieve all announcement properties
[**external_api_announcements_create_announcement**](CommunicationsApi.md#external_api_announcements_create_announcement) | **POST** /v1/communications/announcements | Create an announcement
[**external_api_announcements_expiration_expire_announcement**](CommunicationsApi.md#external_api_announcements_expiration_expire_announcement) | **POST** /v1/communications/announcements/{announcementId}/expirationrequest | Expire an announcement
[**external_api_announcements_get_all_announcements**](CommunicationsApi.md#external_api_announcements_get_all_announcements) | **GET** /v1/communications/announcements | Retrieve all announcements
[**external_api_announcements_get_announcement_by_id**](CommunicationsApi.md#external_api_announcements_get_announcement_by_id) | **GET** /v1/communications/announcements/{announcementId} | Retrieve an announcement
[**external_api_email_recipients_get_email_recipients**](CommunicationsApi.md#external_api_email_recipients_get_email_recipients) | **GET** /v1/communications/emails/{emailId}/recipients | Retrieve all email recipients
[**external_api_emails_get_email_by_id**](CommunicationsApi.md#external_api_emails_get_email_by_id) | **GET** /v1/communications/emails/{emailId} | Retrieve an email
[**external_api_emails_get_emails**](CommunicationsApi.md#external_api_emails_get_emails) | **GET** /v1/communications/emails | Retrieve all emails
[**external_api_emails_write_create_email**](CommunicationsApi.md#external_api_emails_write_create_email) | **POST** /v1/communications/emails | Send an email
[**external_api_mailing_templates_get_mailing_templates**](CommunicationsApi.md#external_api_mailing_templates_get_mailing_templates) | **GET** /v1/communications/templates | Retrieve all communication templates
[**external_api_mailing_templates_get_mailing_templates_by_id**](CommunicationsApi.md#external_api_mailing_templates_get_mailing_templates_by_id) | **GET** /v1/communications/templates/{templateId} | Retrieve a communication template
[**external_api_phone_logs_create_phone_log**](CommunicationsApi.md#external_api_phone_logs_create_phone_log) | **POST** /v1/communications/phonelogs | Create a phone log
[**external_api_phone_logs_get_phone_log_by_id**](CommunicationsApi.md#external_api_phone_logs_get_phone_log_by_id) | **GET** /v1/communications/phonelogs/{phoneLogId} | Retrieve a phone log
[**external_api_phone_logs_get_phone_logs**](CommunicationsApi.md#external_api_phone_logs_get_phone_logs) | **GET** /v1/communications/phonelogs | Retrieve all phone logs
[**external_api_phone_logs_update_phone_log**](CommunicationsApi.md#external_api_phone_logs_update_phone_log) | **PUT** /v1/communications/phonelogs/{phoneLogId} | Update a phone log


# **external_api_announcement_properties_get_announcement_properties**
> List[PropertyMessage] external_api_announcement_properties_get_announcement_properties(announcement_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all announcement properties

Retrieves a list of association and/or rental properties whose residents received the announcement. An empty response collection indicates that the announcement was sent to all properties at the time of its creation.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Announcements</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.property_message import PropertyMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    announcement_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all announcement properties
        api_response = await api_instance.external_api_announcement_properties_get_announcement_properties(announcement_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of CommunicationsApi->external_api_announcement_properties_get_announcement_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_announcement_properties_get_announcement_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **announcement_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[PropertyMessage]**](PropertyMessage.md)

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

# **external_api_announcements_create_announcement**
> AnnouncementMessage external_api_announcements_create_announcement(announcement_post_message)

Create an announcement

Creates and publishes an announcement.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Announcements</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.announcement_message import AnnouncementMessage
from buildium_sdk.models.announcement_post_message import AnnouncementPostMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    announcement_post_message = buildium_sdk.AnnouncementPostMessage() # AnnouncementPostMessage | 

    try:
        # Create an announcement
        api_response = await api_instance.external_api_announcements_create_announcement(announcement_post_message)
        print("The response of CommunicationsApi->external_api_announcements_create_announcement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_announcements_create_announcement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **announcement_post_message** | [**AnnouncementPostMessage**](AnnouncementPostMessage.md)|  | 

### Return type

[**AnnouncementMessage**](AnnouncementMessage.md)

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
**409** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_announcements_expiration_expire_announcement**
> external_api_announcements_expiration_expire_announcement(announcement_id)

Expire an announcement

Removes the announcement from the Resident Center immediately.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Announcements</span> - `View` `Edit`

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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    announcement_id = 56 # int | 

    try:
        # Expire an announcement
        await api_instance.external_api_announcements_expiration_expire_announcement(announcement_id)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_announcements_expiration_expire_announcement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **announcement_id** | **int**|  | 

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
**204** | NoContent |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_announcements_get_all_announcements**
> List[AnnouncementMessage] external_api_announcements_get_all_announcements(announcementdatefrom=announcementdatefrom, announcementdateto=announcementdateto, entityid=entityid, entitytype=entitytype, senderid=senderid, orderby=orderby, offset=offset, limit=limit)

Retrieve all announcements

Retrieves all announcements.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Announcements</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.announcement_message import AnnouncementMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    announcementdatefrom = '2013-10-20' # date | Filters results to any announcements created on or after the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    announcementdateto = '2013-10-20' # date | Filters results to any announcements created on or before the specified date. The value must be formatted as YYYY-MM-DD. (optional)
    entityid = 56 # int | Filters results to any announcement associated with the specified entity id value. The value must be of the type specified in the `EntityType` field. (optional)
    entitytype = 'entitytype_example' # str | Specifies the type of entity that the `EntityId` field refers to. This field is required if the `EntityId` field is provided. (optional)
    senderid = 56 # int | Unique identifier of the user that published the announcement. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all announcements
        api_response = await api_instance.external_api_announcements_get_all_announcements(announcementdatefrom=announcementdatefrom, announcementdateto=announcementdateto, entityid=entityid, entitytype=entitytype, senderid=senderid, orderby=orderby, offset=offset, limit=limit)
        print("The response of CommunicationsApi->external_api_announcements_get_all_announcements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_announcements_get_all_announcements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **announcementdatefrom** | **date**| Filters results to any announcements created on or after the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **announcementdateto** | **date**| Filters results to any announcements created on or before the specified date. The value must be formatted as YYYY-MM-DD. | [optional] 
 **entityid** | **int**| Filters results to any announcement associated with the specified entity id value. The value must be of the type specified in the &#x60;EntityType&#x60; field. | [optional] 
 **entitytype** | **str**| Specifies the type of entity that the &#x60;EntityId&#x60; field refers to. This field is required if the &#x60;EntityId&#x60; field is provided. | [optional] 
 **senderid** | **int**| Unique identifier of the user that published the announcement. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[AnnouncementMessage]**](AnnouncementMessage.md)

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

# **external_api_announcements_get_announcement_by_id**
> AnnouncementMessage external_api_announcements_get_announcement_by_id(announcement_id)

Retrieve an announcement

Retrieves an announcement.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Announcements</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.announcement_message import AnnouncementMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    announcement_id = 56 # int | 

    try:
        # Retrieve an announcement
        api_response = await api_instance.external_api_announcements_get_announcement_by_id(announcement_id)
        print("The response of CommunicationsApi->external_api_announcements_get_announcement_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_announcements_get_announcement_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **announcement_id** | **int**|  | 

### Return type

[**AnnouncementMessage**](AnnouncementMessage.md)

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

# **external_api_email_recipients_get_email_recipients**
> List[EmailRecipientMessage] external_api_email_recipients_get_email_recipients(email_id, orderby=orderby, offset=offset, limit=limit)

Retrieve all email recipients

Retrieves all email recipients.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Email</span> - `View`
            

<h4>Optional Permissions:</h4>
            The following permissions are optional, but results with a missing permission will be filtered out.
            
<span class="permissionBlock">Maintenance > Vendors</span> - `View` In order to retrieve recipients that are Vendors, you must have this permission.
            
<span class="permissionBlock">Administration > Users</span> - `View` In order to see recipients that are Staff, you must have this permission.

### Example


```python
import buildium_sdk
from buildium_sdk.models.email_recipient_message import EmailRecipientMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    email_id = 56 # int | 
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all email recipients
        api_response = await api_instance.external_api_email_recipients_get_email_recipients(email_id, orderby=orderby, offset=offset, limit=limit)
        print("The response of CommunicationsApi->external_api_email_recipients_get_email_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_email_recipients_get_email_recipients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **int**|  | 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[EmailRecipientMessage]**](EmailRecipientMessage.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_emails_get_email_by_id**
> EmailMessage external_api_emails_get_email_by_id(email_id)

Retrieve an email

Retrieves the content of an email. System generated emails are not included. To retrieve the recipients of the email see the [Retrieve all email recipients](#tag/Communications/operation/ExternalApiEmailRecipients_GetEmailRecipients) endpoint.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Emails</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.email_message import EmailMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    email_id = 56 # int | 

    try:
        # Retrieve an email
        api_response = await api_instance.external_api_emails_get_email_by_id(email_id)
        print("The response of CommunicationsApi->external_api_emails_get_email_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_emails_get_email_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **int**|  | 

### Return type

[**EmailMessage**](EmailMessage.md)

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

# **external_api_emails_get_emails**
> List[EmailMessage] external_api_emails_get_emails(sentdatetimefrom, sentdatetimeto, subject=subject, recipientnameoremail=recipientnameoremail, senderuserid=senderuserid, orderby=orderby, offset=offset, limit=limit)

Retrieve all emails

Retrieves all emails. System generated emails are not included.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Communication > Emails</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.email_message import EmailMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    sentdatetimefrom = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any emails whose sent date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 90 days.
    sentdatetimeto = '2013-10-20T19:20:30+01:00' # datetime | Filters results to any emails whose sent date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 90 days.
    subject = 'subject_example' # str | Filters results to any email whose subject *contains* the specified value. (optional)
    recipientnameoremail = 'recipientnameoremail_example' # str | Filters results to any email with a recipient whose name or email address *contains* the specified value. (optional)
    senderuserid = 56 # int | Filters results to only emails that were sent by the specified user identifier. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all emails
        api_response = await api_instance.external_api_emails_get_emails(sentdatetimefrom, sentdatetimeto, subject=subject, recipientnameoremail=recipientnameoremail, senderuserid=senderuserid, orderby=orderby, offset=offset, limit=limit)
        print("The response of CommunicationsApi->external_api_emails_get_emails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_emails_get_emails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sentdatetimefrom** | **datetime**| Filters results to any emails whose sent date and time are greater than or equal to the specified value. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 90 days. | 
 **sentdatetimeto** | **datetime**| Filters results to any emails whose sent date and time are less than or equal to the specified value. The value must be formatted as YYYY-MM-DDTHH:MM:SSZ. The maximum date range is 90 days. | 
 **subject** | **str**| Filters results to any email whose subject *contains* the specified value. | [optional] 
 **recipientnameoremail** | **str**| Filters results to any email with a recipient whose name or email address *contains* the specified value. | [optional] 
 **senderuserid** | **int**| Filters results to only emails that were sent by the specified user identifier. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[EmailMessage]**](EmailMessage.md)

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

# **external_api_emails_write_create_email**
> external_api_emails_write_create_email(email_post_message)

Send an email

Sends an email to one or more recipients using the specified email template. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Communication > Emails</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.email_post_message import EmailPostMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    email_post_message = buildium_sdk.EmailPostMessage() # EmailPostMessage | 

    try:
        # Send an email
        await api_instance.external_api_emails_write_create_email(email_post_message)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_emails_write_create_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_post_message** | [**EmailPostMessage**](EmailPostMessage.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Sent email. |  -  |
**400** | Unable to process the request due to malformed request syntax or invalid parameters. |  -  |
**401** | The API key couldn&#39;t be authorized. |  -  |
**403** | The supplied credentials don&#39;t have permissions to access the resource. |  -  |
**404** | Resource not found. |  -  |
**415** | The Content-Type header on the request is missing or contains an unsupported value. |  -  |
**422** | The request data could not be used to fulfill the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_api_mailing_templates_get_mailing_templates**
> List[MailingTemplateMessage] external_api_mailing_templates_get_mailing_templates(orderby=orderby, offset=offset, limit=limit)

Retrieve all communication templates

Retrieves all mailing and email templates. A template is a tool in Buildium that allows you to create "mail merge" templates for emails and postal mailings to easily send common messages to residents, rental owners and vendors. 
            

<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Mailing Templates</span> - `View`
            
<h4>Optional Permissions:</h4><span class="permissionBlock">Rentals > Tenants</span> - `View`
            
<span class="permissionBlock">Rentals > Property Rental owners</span> - `View`
            
<span class="permissionBlock">Associations > Association owners and tenants</span> - `View`
            
<span class="permissionBlock">Maintenance > Vendors</span> - `View`
            
<span class="permissionBlock">Rentals > Applicants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.mailing_template_message import MailingTemplateMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all communication templates
        api_response = await api_instance.external_api_mailing_templates_get_mailing_templates(orderby=orderby, offset=offset, limit=limit)
        print("The response of CommunicationsApi->external_api_mailing_templates_get_mailing_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_mailing_templates_get_mailing_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[MailingTemplateMessage]**](MailingTemplateMessage.md)

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

# **external_api_mailing_templates_get_mailing_templates_by_id**
> MailingTemplateMessage external_api_mailing_templates_get_mailing_templates_by_id(template_id)

Retrieve a communication template

Retrieves a communication template. A template is a tool in Buildium that allows you to create "mail merge" templates for emails and postal mailings to easily send common messages to residents, rental owners and vendors.
            

<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Mailing Templates</span> - `View`
            
<h4>Optional Permissions:</h4><span class="permissionBlock">Rentals > Tenants</span> - `View`
            
<span class="permissionBlock">Rentals > Property Rental owners</span> - `View`
            
<span class="permissionBlock">Associations > Association owners and tenants</span> - `View`
            
<span class="permissionBlock">Maintenance > Vendors</span> - `View`
            
<span class="permissionBlock">Rentals > Applicants</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.mailing_template_message import MailingTemplateMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    template_id = 56 # int | 

    try:
        # Retrieve a communication template
        api_response = await api_instance.external_api_mailing_templates_get_mailing_templates_by_id(template_id)
        print("The response of CommunicationsApi->external_api_mailing_templates_get_mailing_templates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_mailing_templates_get_mailing_templates_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**|  | 

### Return type

[**MailingTemplateMessage**](MailingTemplateMessage.md)

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

# **external_api_phone_logs_create_phone_log**
> PhoneLogMessage external_api_phone_logs_create_phone_log(phone_log_post_message)

Create a phone log

Creates a phone log.


<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Timelines (Phone Logs)</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.phone_log_message import PhoneLogMessage
from buildium_sdk.models.phone_log_post_message import PhoneLogPostMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    phone_log_post_message = buildium_sdk.PhoneLogPostMessage() # PhoneLogPostMessage | 

    try:
        # Create a phone log
        api_response = await api_instance.external_api_phone_logs_create_phone_log(phone_log_post_message)
        print("The response of CommunicationsApi->external_api_phone_logs_create_phone_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_phone_logs_create_phone_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_log_post_message** | [**PhoneLogPostMessage**](PhoneLogPostMessage.md)|  | 

### Return type

[**PhoneLogMessage**](PhoneLogMessage.md)

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

# **external_api_phone_logs_get_phone_log_by_id**
> PhoneLogMessage external_api_phone_logs_get_phone_log_by_id(phone_log_id)

Retrieve a phone log

Retrieves a specific phone log.


<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Timelines (Phone Logs)</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.phone_log_message import PhoneLogMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    phone_log_id = 56 # int | The phone log identifier

    try:
        # Retrieve a phone log
        api_response = await api_instance.external_api_phone_logs_get_phone_log_by_id(phone_log_id)
        print("The response of CommunicationsApi->external_api_phone_logs_get_phone_log_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_phone_logs_get_phone_log_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_log_id** | **int**| The phone log identifier | 

### Return type

[**PhoneLogMessage**](PhoneLogMessage.md)

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

# **external_api_phone_logs_get_phone_logs**
> List[PhoneLogMessage] external_api_phone_logs_get_phone_logs(fromdate=fromdate, todate=todate, loggedbystaffuserids=loggedbystaffuserids, subject=subject, participantentityid=participantentityid, participantentitytype=participantentitytype, unitagreementid=unitagreementid, unitagreementtype=unitagreementtype, orderby=orderby, offset=offset, limit=limit)

Retrieve all phone logs

Retrieves all phone logs.


<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Timelines (Phone Logs)</span> - `View`

### Example


```python
import buildium_sdk
from buildium_sdk.models.phone_log_message import PhoneLogMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    fromdate = '2013-10-20' # date | Filters results to any phone log whose call date is greater than or equal to the specified value. (optional)
    todate = '2013-10-20' # date | Filters results to any phone log whose call date is less than or equal to the specified value. (optional)
    loggedbystaffuserids = [56] # List[int] | Filters results to any phone log that was logged by staff user(s). (optional)
    subject = 'subject_example' # str | Filters results to any phone log whose subject *contains* the specified value. (optional)
    participantentityid = 56 # int | Filters results to any phone logs that match the participant identifier. Note, if a value is provided in this field the `ParticipantEntityType` must also be provided. (optional)
    participantentitytype = 'participantentitytype_example' # str | Filters results to any phone log with the specified participant type. This field is required if a value is provided for the `ParticipantEntityId` field. (optional)
    unitagreementid = 56 # int | Filters results to any phone log with the specified unit agreement identifier. Note, if a value is provided in this field the `UnitAgreementType` must also be provided. (optional)
    unitagreementtype = 'unitagreementtype_example' # str | Filters results to any phone log with the specified unit agreement type. This field is required if a value is provided for the `UnitAgreementId` field. (optional)
    orderby = 'orderby_example' # str | `orderby` indicates the field(s) and direction to sort the results in the response. See <a href=\"#section/API-Overview/Bulk-Request-Options\">Bulk Request Options</a> for more information. (optional)
    offset = 56 # int | `offset` indicates the position of the first record to return. The `offset` is zero-based and the default is 0. (optional)
    limit = 56 # int | `limit` indicates the maximum number of results to be returned in the response. `limit` can range between 1 and 1000 and the default is 50. (optional)

    try:
        # Retrieve all phone logs
        api_response = await api_instance.external_api_phone_logs_get_phone_logs(fromdate=fromdate, todate=todate, loggedbystaffuserids=loggedbystaffuserids, subject=subject, participantentityid=participantentityid, participantentitytype=participantentitytype, unitagreementid=unitagreementid, unitagreementtype=unitagreementtype, orderby=orderby, offset=offset, limit=limit)
        print("The response of CommunicationsApi->external_api_phone_logs_get_phone_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_phone_logs_get_phone_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fromdate** | **date**| Filters results to any phone log whose call date is greater than or equal to the specified value. | [optional] 
 **todate** | **date**| Filters results to any phone log whose call date is less than or equal to the specified value. | [optional] 
 **loggedbystaffuserids** | [**List[int]**](int.md)| Filters results to any phone log that was logged by staff user(s). | [optional] 
 **subject** | **str**| Filters results to any phone log whose subject *contains* the specified value. | [optional] 
 **participantentityid** | **int**| Filters results to any phone logs that match the participant identifier. Note, if a value is provided in this field the &#x60;ParticipantEntityType&#x60; must also be provided. | [optional] 
 **participantentitytype** | **str**| Filters results to any phone log with the specified participant type. This field is required if a value is provided for the &#x60;ParticipantEntityId&#x60; field. | [optional] 
 **unitagreementid** | **int**| Filters results to any phone log with the specified unit agreement identifier. Note, if a value is provided in this field the &#x60;UnitAgreementType&#x60; must also be provided. | [optional] 
 **unitagreementtype** | **str**| Filters results to any phone log with the specified unit agreement type. This field is required if a value is provided for the &#x60;UnitAgreementId&#x60; field. | [optional] 
 **orderby** | **str**| &#x60;orderby&#x60; indicates the field(s) and direction to sort the results in the response. See &lt;a href&#x3D;\&quot;#section/API-Overview/Bulk-Request-Options\&quot;&gt;Bulk Request Options&lt;/a&gt; for more information. | [optional] 
 **offset** | **int**| &#x60;offset&#x60; indicates the position of the first record to return. The &#x60;offset&#x60; is zero-based and the default is 0. | [optional] 
 **limit** | **int**| &#x60;limit&#x60; indicates the maximum number of results to be returned in the response. &#x60;limit&#x60; can range between 1 and 1000 and the default is 50. | [optional] 

### Return type

[**List[PhoneLogMessage]**](PhoneLogMessage.md)

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

# **external_api_phone_logs_update_phone_log**
> PhoneLogMessage external_api_phone_logs_update_phone_log(phone_log_id, phone_log_put_message)

Update a phone log

Update a phone log


<strong>NOTE:</strong> Any field not included in the update request will be set to either an empty string or `null` in the database depending on the field definition. 
The recommended workflow to ensure no data is inadvertently overwritten is to execute a `GET` request for the resource you're about to update and then use this response to fill any of the fields that are not being updated.


<h4>Required permission(s):</h4><span class="permissionBlock">Communications > Timelines (Phone Logs)</span> - `View` `Edit`

### Example


```python
import buildium_sdk
from buildium_sdk.models.phone_log_message import PhoneLogMessage
from buildium_sdk.models.phone_log_put_message import PhoneLogPutMessage
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
    api_instance = buildium_sdk.CommunicationsApi(api_client)
    phone_log_id = 56 # int | The phone log identifier.
    phone_log_put_message = buildium_sdk.PhoneLogPutMessage() # PhoneLogPutMessage | 

    try:
        # Update a phone log
        api_response = await api_instance.external_api_phone_logs_update_phone_log(phone_log_id, phone_log_put_message)
        print("The response of CommunicationsApi->external_api_phone_logs_update_phone_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->external_api_phone_logs_update_phone_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_log_id** | **int**| The phone log identifier. | 
 **phone_log_put_message** | [**PhoneLogPutMessage**](PhoneLogPutMessage.md)|  | 

### Return type

[**PhoneLogMessage**](PhoneLogMessage.md)

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

