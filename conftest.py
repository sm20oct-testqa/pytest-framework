import pytest
from utils.api_clients import APIclient
from data.payloads import post_payload


@pytest.fixture
def api_client():
    return APIclient()

@pytest.fixture
def book_id():
    return 201

@pytest.fixture
def created_book(api_client, book_id):

    payload = post_payload(book_id)

    response = api_client.post(
        "/Books",
        payload
    )

    assert response.status_code == 200

    return book_id