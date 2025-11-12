import pytest
import requests

@pytest.fixture()
def new_post_id():
    body = {"title": "foo", "body": "bar", "userId": 1}
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    print(f"Created post ID: {post_id}")
    yield post_id
    # Удаление поста (cleanup)
    delete_response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print(f"Deleted post {post_id}, status: {delete_response.status_code}")

