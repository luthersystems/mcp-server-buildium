"""Tests for configuration loading and validation."""

import pytest
from pydantic import ValidationError

from mcp_server_buildium.config import DEFAULT_BASE_URL, BuildiumConfig

from .conftest import TEST_SECRET


@pytest.fixture(autouse=True)
def _no_buildium_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep BUILDIUM_* variables from the shell out of these tests."""
    import os

    for name in [n for n in os.environ if n.startswith("BUILDIUM_")]:
        monkeypatch.delenv(name)


def make(**kwargs: object) -> BuildiumConfig:
    values: dict[str, object] = {"client_id": "id", "client_secret": TEST_SECRET}
    values.update(kwargs)
    return BuildiumConfig(_env_file=None, **values)  # type: ignore[arg-type]


def test_secret_is_not_in_repr(config: BuildiumConfig) -> None:
    assert TEST_SECRET not in repr(config)
    assert TEST_SECRET not in str(config.model_dump())


@pytest.mark.parametrize("value", ["", "   "])
def test_empty_base_url_uses_default(value: str) -> None:
    assert make(base_url=value).base_url == DEFAULT_BASE_URL


@pytest.mark.parametrize(
    "value",
    [
        "http://api.buildium.com",
        "ftp://api.buildium.com",
        "api.buildium.com",
        "https://",
        "https://user:pass@api.buildium.com",
        "https://api.buildium.com?x=1",
    ],
)
def test_base_url_must_be_plain_https(value: str) -> None:
    with pytest.raises(ValidationError):
        make(base_url=value)


def test_errors_do_not_echo_the_secret(monkeypatch: pytest.MonkeyPatch) -> None:
    # A missing client ID with the secret set used to print the secret in
    # the error's input_value.
    monkeypatch.setenv("BUILDIUM_CLIENT_SECRET", TEST_SECRET)
    with pytest.raises(ValidationError) as excinfo:
        BuildiumConfig(_env_file=None)
    assert TEST_SECRET not in str(excinfo.value)


def test_errors_do_not_echo_a_base_url_password() -> None:
    with pytest.raises(ValidationError) as excinfo:
        make(base_url="https://user:hunter2@api.buildium.com")
    assert "hunter2" not in str(excinfo.value)


def test_sandbox_base_url_is_accepted() -> None:
    assert make(base_url="https://apisandbox.buildium.com/").base_url == (
        "https://apisandbox.buildium.com/"
    )


@pytest.mark.parametrize("field", ["client_id", "client_secret"])
def test_empty_credentials_are_refused(field: str) -> None:
    with pytest.raises(ValidationError):
        make(**{field: ""})


def test_categories() -> None:
    assert make().get_enabled_categories() is None
    assert make(categories="").is_category_enabled("leases")
    cfg = make(categories=" Leases, rentals ,")
    assert cfg.get_enabled_categories() == {"leases", "rentals"}
    assert cfg.is_category_enabled("LEASES")
    assert not cfg.is_category_enabled("bills")


@pytest.mark.parametrize("value", [None, "", " ", ",", " , "])
def test_blank_categories_mean_all(value: str | None) -> None:
    assert make(categories=value).get_enabled_categories() is None


def test_categories_are_normalized() -> None:
    assert make(categories=" Leases, ,vendors ").get_enabled_categories() == {"leases", "vendors"}
