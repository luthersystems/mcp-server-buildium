"""Offline tests: each tool sends the request Buildium expects.

The SDK's HTTP client is replaced by a recorder (see conftest.py), so these
tests need no credentials and make no network call.
"""

import json
from types import ModuleType
from typing import Any
from unittest import mock

import httpx
import pytest
from fastmcp import Client

from mcp_server_buildium.buildium_client import BuildiumClient
from mcp_server_buildium.config import BuildiumConfig
from mcp_server_buildium.server import CATEGORIES, create_server

from .conftest import Recorder

PAGE = {"offset": "0", "limit": "100"}

# tool name, arguments, HTTP method, path, query parameters
READ_TOOLS: list[tuple[str, dict[str, Any], str, str, dict[str, str]]] = [
    ("list_associations", {}, "GET", "/v1/associations", PAGE),
    ("get_association", {"association_id": 7}, "GET", "/v1/associations/7", {}),
    ("list_association_board_members", {"association_id": 7}, "GET", "/v1/associations/7/boardmembers", PAGE),
    ("list_association_ownership_accounts", {"association_id": 7}, "GET", "/v1/associations/ownershipaccounts", {"associationids": "7", **PAGE}),
    ("list_leases", {}, "GET", "/v1/leases", PAGE),
    ("get_lease", {"lease_id": 7}, "GET", "/v1/leases/7", {}),
    ("list_lease_transactions", {"lease_id": 7}, "GET", "/v1/leases/7/transactions", PAGE),
    ("list_rentals", {}, "GET", "/v1/rentals", PAGE),
    ("get_rental", {"property_id": 7}, "GET", "/v1/rentals/7", {}),
    ("list_unit_listings", {}, "GET", "/v1/rentals/units/listings", PAGE),
    ("list_applicants", {}, "GET", "/v1/applicants", PAGE),
    ("get_applicant", {"applicant_id": 7}, "GET", "/v1/applicants/7", {}),
    ("list_applicant_applications", {"applicant_id": 7}, "GET", "/v1/applicants/7/applications", PAGE),
    ("get_application", {"applicant_id": 7, "application_id": 8}, "GET", "/v1/applicants/7/applications/8", {}),
    ("list_applicant_groups", {}, "GET", "/v1/applicants/groups", PAGE),
    ("list_rental_tenants", {}, "GET", "/v1/leases/tenants", PAGE),
    ("get_rental_tenant", {"tenant_id": 7}, "GET", "/v1/leases/tenants/7", {}),
    ("list_association_tenants", {}, "GET", "/v1/associations/tenants", PAGE),
    ("list_rental_owners", {}, "GET", "/v1/rentals/owners", PAGE),
    ("get_rental_owner", {"owner_id": 7}, "GET", "/v1/rentals/owners/7", {}),
    ("list_association_owners", {}, "GET", "/v1/associations/owners", PAGE),
    ("get_association_owner", {"owner_id": 7}, "GET", "/v1/associations/owners/7", {}),
    ("list_rental_units", {}, "GET", "/v1/rentals/units", PAGE),
    ("get_rental_unit", {"unit_id": 7}, "GET", "/v1/rentals/units/7", {}),
    ("list_association_units", {}, "GET", "/v1/associations/units", PAGE),
    ("list_vendors", {}, "GET", "/v1/vendors", PAGE),
    ("get_vendor", {"vendor_id": 7}, "GET", "/v1/vendors/7", {}),
    ("list_vendor_categories", {}, "GET", "/v1/vendors/categories", PAGE),
    ("list_tasks", {}, "GET", "/v1/tasks", PAGE),
    ("get_task", {"task_id": 7}, "GET", "/v1/tasks/7", {}),
    ("list_task_categories", {}, "GET", "/v1/tasks/categories", PAGE),
    ("list_bills", {}, "GET", "/v1/bills", PAGE),
    ("get_bill", {"bill_id": 7}, "GET", "/v1/bills/7", {}),
    ("list_bill_payments", {"bill_id": 7}, "GET", "/v1/bills/7/payments", PAGE),
    ("get_bill_payment", {"bill_id": 7, "payment_id": 8}, "GET", "/v1/bills/7/payments/8", {}),
    ("list_files", {}, "GET", "/v1/files", PAGE),
    ("get_file", {"file_id": 7}, "GET", "/v1/files/7", {}),
    ("create_file_download_request", {"file_id": 7}, "POST", "/v1/files/7/downloadrequest", {}),
    ("list_file_categories", {}, "GET", "/v1/files/categories", PAGE),
    ("list_bank_accounts", {}, "GET", "/v1/bankaccounts", PAGE),
    ("get_bank_account", {"bank_account_id": 7}, "GET", "/v1/bankaccounts/7", {}),
    ("list_bank_account_transactions", {"bank_account_id": 7, "start_date": "2026-01-01", "end_date": "2026-01-31"}, "GET", "/v1/bankaccounts/7/transactions", {"startdate": "2026-01-01", "enddate": "2026-01-31", **PAGE}),
    ("get_bank_account_transaction", {"bank_account_id": 7, "transaction_id": 8}, "GET", "/v1/bankaccounts/7/transactions/8", {}),
]  # fmt: skip

# Filters the tools accept, and the query parameters Buildium expects for them.
FILTERS: list[tuple[str, dict[str, Any], dict[str, str]]] = [
    ("list_leases", {"property_id": 3, "lease_status": "Active"}, {"propertyids": "3", "leasestatuses": "Active"}),
    ("list_rental_tenants", {"property_id": 3, "unit_id": 4, "status": "Active"}, {"propertyids": "3", "unitids": "4", "leasetermstatuses": "Active"}),
    ("list_association_tenants", {"property_id": 3, "status": "Active"}, {"associationids": "3", "statuses": "Active"}),
    ("list_rental_owners", {"property_id": 3}, {"propertyids": "3"}),
    ("list_association_owners", {"property_id": 3, "status": "Active"}, {"associationids": "3", "statuses": "Active"}),
    ("list_rental_units", {"property_id": 3}, {"propertyids": "3"}),
    ("list_association_units", {"property_id": 3}, {"associationids": "3"}),
    ("list_tasks", {"task_type": "ToDo", "assigned_to_user_id": 5}, {"type": "ToDo", "assignedtoid": "5"}),
    ("list_bills", {"vendor_id": 3, "status": "Unpaid"}, {"vendorid": "3", "paidstatus": "Unpaid"}),
    ("list_applicants", {"email": "a@example.com"}, {"email": "a@example.com"}),
    ("list_lease_transactions", {"lease_id": 7, "transaction_date_from": "2026-01-01", "transaction_date_to": "2026-01-31"}, {"transactiondatefrom": "2026-01-01", "transactiondateto": "2026-01-31"}),
    ("list_files", {"entity_type": "Rental", "entity_id": 3, "category_id": 4}, {"entitytype": "Rental", "entityid": "3", "categoryid": "4"}),
]  # fmt: skip


def respond_by_path(request: httpx.Request) -> httpx.Response:
    """Answer a request for one record with an object, anything else with a list."""
    last = request.url.path.rstrip("/").split("/")[-1]
    return httpx.Response(200, json={} if last.isdigit() or request.method == "POST" else [])


async def call(
    recorded_client: tuple[BuildiumClient, Recorder], tool: str, args: dict[str, Any]
) -> tuple[Any, list[httpx.Request]]:
    client, recorder = recorded_client
    recorder.respond = respond_by_path
    async with Client(create_server(client.config, client)) as mcp:
        result = await mcp.call_tool(tool, args, raise_on_error=False)
    return result, recorder.requests


@pytest.mark.asyncio
@pytest.mark.parametrize(("tool", "args", "method", "path", "query"), READ_TOOLS)
async def test_read_tool_request(
    recorded_client: tuple[BuildiumClient, Recorder],
    tool: str,
    args: dict[str, Any],
    method: str,
    path: str,
    query: dict[str, str],
) -> None:
    result, requests = await call(recorded_client, tool, args)
    assert not result.is_error, result.content
    (request,) = requests
    assert request.method == method
    assert request.url.host == "api.buildium.com"
    assert request.url.path == path
    assert dict(request.url.params) == query
    assert isinstance(json.loads(result.content[0].text), dict)


@pytest.mark.asyncio
@pytest.mark.parametrize(("tool", "args", "query"), FILTERS)
async def test_filters(
    recorded_client: tuple[BuildiumClient, Recorder],
    tool: str,
    args: dict[str, Any],
    query: dict[str, str],
) -> None:
    result, requests = await call(recorded_client, tool, args)
    assert not result.is_error, result.content
    (request,) = requests
    assert {k: request.url.params[k] for k in query} == query


@pytest.mark.asyncio
async def test_list_leases_unit_filter_reads_every_page(
    recorded_client: tuple[BuildiumClient, Recorder],
) -> None:
    client, recorder = recorded_client

    def pages(request: httpx.Request) -> httpx.Response:
        # Two full pages and a short one; unit 4 has one lease on each.
        start = int(request.url.params["offset"])
        size = 1000 if start < 2000 else 10
        return httpx.Response(
            200, json=[{"Id": start + i, "UnitId": 4 if i == 0 else 5} for i in range(size)]
        )

    recorder.respond = pages
    async with Client(create_server(client.config, client)) as mcp:
        result = await mcp.call_tool(
            "list_leases", {"unit_id": 4, "property_id": 9, "offset": 1, "limit": 5}
        )
    body = json.loads(result.content[0].text)
    assert body["count"] == 2
    assert [(lease["Id"], lease["UnitId"]) for lease in body["leases"]] == [(1000, 4), (2000, 4)]
    assert [r.url.params["offset"] for r in recorder.requests] == ["0", "1000", "2000"]
    assert {r.url.params["propertyids"] for r in recorder.requests} == {"9"}
    assert {r.url.params["orderby"] for r in recorder.requests} == {"Id"}
    assert "unitid" not in recorder.requests[0].url.params


@pytest.mark.asyncio
@pytest.mark.parametrize("paging", [{"limit": 0}, {"offset": -1}])
async def test_list_leases_unit_filter_refuses_bad_paging(
    recorded_client: tuple[BuildiumClient, Recorder], paging: dict[str, int]
) -> None:
    result, requests = await call(recorded_client, "list_leases", {"unit_id": 4, **paging})
    assert result.is_error
    assert requests == []


@pytest.mark.asyncio
async def test_list_leases_unit_filter_gives_up_after_max_pages(
    recorded_client: tuple[BuildiumClient, Recorder],
) -> None:
    client, recorder = recorded_client
    recorder.respond = lambda _req: httpx.Response(200, json=[{"Id": 1, "UnitId": 5}] * 1000)
    async with Client(create_server(client.config, client)) as mcp:
        result = await mcp.call_tool("list_leases", {"unit_id": 4}, raise_on_error=False)
    assert result.is_error
    assert "property_id" in result.content[0].text
    assert len(recorder.requests) == 20


@pytest.mark.asyncio
async def test_list_items_use_buildium_field_names(
    recorded_client: tuple[BuildiumClient, Recorder],
) -> None:
    client, recorder = recorded_client
    recorder.respond = lambda _req: httpx.Response(200, json=[{"Id": 1, "UnitId": 4}])
    async with Client(create_server(client.config, client)) as mcp:
        result = await mcp.call_tool("list_leases", {})
    body = json.loads(result.content[0].text)
    assert body["count"] == 1
    (lease,) = body["leases"]
    assert (lease["Id"], lease["UnitId"]) == (1, 4)
    assert "unit_id" not in lease


@pytest.mark.asyncio
async def test_bank_transactions_refuse_reversed_dates(
    recorded_client: tuple[BuildiumClient, Recorder],
) -> None:
    result, requests = await call(
        recorded_client,
        "list_bank_account_transactions",
        {"bank_account_id": 7, "start_date": "2026-02-01", "end_date": "2026-01-01"},
    )
    assert result.is_error
    assert requests == []


@pytest.mark.asyncio
async def test_server_uses_the_client_config(config: BuildiumConfig) -> None:
    client = BuildiumClient(config=config.model_copy(update={"categories": "leases"}))
    try:
        async with Client(create_server(client=client)) as mcp:
            names = {tool.name for tool in await mcp.list_tools()}
    finally:
        await client.close()
    assert "list_leases" in names
    assert "list_vendors" not in names


def test_unknown_category_is_refused(config: BuildiumConfig) -> None:
    with pytest.raises(ValueError, match="bank-accounts"):
        create_server(config.model_copy(update={"categories": "leases,bank-accounts"}))


@pytest.mark.asyncio
async def test_write_tool_refuses_invalid_body(
    recorded_client: tuple[BuildiumClient, Recorder],
) -> None:
    result, requests = await call(recorded_client, "create_lease", {"lease_data": {}})
    assert result.is_error
    assert requests == []


@pytest.mark.asyncio
async def test_all_tools_registered(config: BuildiumConfig) -> None:
    async with Client(create_server(config)) as mcp:
        tools = await mcp.list_tools()
    assert len(tools) == 81
    read = {name for name, *_ in READ_TOOLS}
    assert read <= {tool.name for tool in tools}


@pytest.mark.asyncio
async def test_categories_limit_tools(config: BuildiumConfig) -> None:
    only_leases = config.model_copy(update={"categories": "leases"})
    async with Client(create_server(only_leases)) as mcp:
        names = {tool.name for tool in await mcp.list_tools()}
    assert names == {
        "list_leases",
        "get_lease",
        "create_lease",
        "update_lease",
        "list_lease_transactions",
    }
    assert set(CATEGORIES) >= {"leases"}


@pytest.mark.asyncio
async def test_write_tools_call_an_existing_sdk_method(
    config: BuildiumConfig, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Each write tool calls one SDK method with argument names it accepts.

    Every SDK API object is replaced by an autospec mock, which raises on an
    unknown method or keyword, and every request model by ``dict``, so the
    tools run without building a valid Buildium body.
    """
    from mcp_server_buildium import tools

    client = BuildiumClient(config=config)
    apis = {name: value for name, value in vars(client).items() if name.endswith("_api")}
    for name, api in apis.items():
        spec = mock.create_autospec(api, instance=True)
        for method in dir(api):
            if method.startswith("external_api_"):
                getattr(spec, method).return_value = {}
        setattr(client, name, spec)
    for module in vars(tools).values():
        if isinstance(module, ModuleType):
            for attr in list(vars(module)):
                if attr.endswith("Message"):
                    monkeypatch.setattr(module, attr, dict)

    async with Client(create_server(config, client)) as mcp:
        listed = await mcp.list_tools()
        write_tools = [t for t in listed if t.name.split("_")[0] in {"create", "update"}]
        assert len(write_tools) == 39
        for tool in write_tools:
            schema = tool.input_schema
            args: dict[str, Any] = {
                name: {} if schema["properties"][name].get("type") == "object" else 7
                for name in schema.get("required", [])
            }
            if tool.name == "create_file_download_request":
                continue  # a read: covered by READ_TOOLS
            result = await mcp.call_tool(tool.name, args, raise_on_error=False)
            assert not result.is_error, (tool.name, result.content)

    calls = [
        c
        for api in vars(client).values()
        if isinstance(api, mock.NonCallableMagicMock)
        for c in api.method_calls
    ]
    assert len(calls) == 38
