def post_payload(bookid):
    payload = {
    "id": bookid,
    "title": "Python AP Testing",
    "description": "Learn API automation",
    "pageCount": 250,
    "excerpt": "Testing APIs",
    "publishDate": "2026-01-01T00:00:00.000Z"
    }
    return payload


def put_payload(bookid):
    payload = {
    "id": bookid,
    "title": "Updated Python API Testing",
    "description": "Updated description",
    "pageCount": 300,
    "excerpt": "Updated excerpt",
    "publishDate": "2026-01-02T00:00:00.000Z"
    }
    return payload
