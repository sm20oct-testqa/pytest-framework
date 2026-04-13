def assert_status_code(response,expected_code):
    assert response.status_code == expected_code

def assert_key(response_json,key):
    assert key in response_json
