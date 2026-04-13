from data.payloads import post_payload
from utils.assertions import assert_status_code,assert_key
import pdb


def test_create_book(api_client,book_id):
    payload = post_payload(book_id)
    response = api_client.post("/Books",payload)

    assert_status_code(response,200)
    data = response.json()
    assert data["id"] == book_id

def test_get_book(api_client,created_book):
    #pdb.set_trace()
    created_book =1
    response = api_client.get(
        f"/Books/{created_book}"
    )
    print(response.status_code)
    print(response.text)
    assert_status_code(response, 200)

    data = response.json()

    assert_key(data,"id")

