from __future__ import annotations

import requests
from tests.test_configs import base_url


def _get_headers(cookie: str | None = None) -> dict:
    """Формируем заголовки с кукой, если она передана."""
    if cookie:
        return {"Cookie": f"cart={cookie};"}
    return {}


def _request(method: str, path: str, *, params=None, json=None, cookie=None):
    """Унифицированный метод для запросов."""
    url = f"{base_url}{path}"
    headers = _get_headers(cookie)
    return requests.request(method, url, params=params, json=json, headers=headers or None)


def get_active_items():
    return _request("GET", "/web/client/events/active")


def get_item(item_slug: str):
    return _request("GET", f"/web/client/moderated-offers/{item_slug}")


def search_items(item_name: str):
    return _request("POST", "/web/client/search/full-text", json={"query": item_name})


def get_cart(cookie: str | None = None):
    return _request("GET", "/web/client/cart/view-cart/duplicate", cookie=cookie)


def add_to_cart(cookie: str, offer_id: str, condition_id: int, quantity: int = 1):
    body = {
        "moderated_offer_id": offer_id,
        "condition_id": condition_id,
        "quantity": quantity,
    }
    return _request("POST", "/web/client/cart/moderated-items", json=body, cookie=cookie)