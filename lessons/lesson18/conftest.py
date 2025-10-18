import pytest
import requests


@pytest.fixture()
def new_post_id():
    body = {"title": "foo","body": "bar","userId": 1,}
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('post deleted')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')