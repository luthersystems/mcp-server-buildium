"""Shared helpers that turn SDK responses into tool results."""

from typing import Any


def to_result(result: Any, list_key: str | None = None) -> dict[str, Any]:
    """Convert an SDK response into the dictionary a tool returns.

    A model becomes its dictionary. A list (the SDK's paged endpoints return
    one) becomes ``{list_key: [...], "count": n}``. An empty response (204)
    becomes ``{}``.

    Args:
        result: The SDK response.
        list_key: The key a list response is returned under.

    Returns:
        The tool result.
    """
    if hasattr(result, "to_dict"):
        converted: dict[str, Any] = result.to_dict()
        return converted
    if isinstance(result, dict):
        return result
    if result is None:
        return {}
    if isinstance(result, list):
        return {list_key or "items": result, "count": len(result)}
    raise TypeError(f"unexpected Buildium response type: {type(result).__name__}")
