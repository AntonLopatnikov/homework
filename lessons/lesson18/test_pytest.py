import pytest
import requests
import pytest

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

@pytest.fixture(scope ='session')
def hello():
    print('hello')
    yield
    print('bye')

def test_get_one_post(new_post_id, hello):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert response['id'] == new_post_id


def test_get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100

def test_add_post():
    body = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )

    assert response.status_code == 201
    assert response.json()['id'] == 101

def test_one():
    assert 1 == 1

def test_two():
    assert 1 == 1

def test_three():
    assert 1 == 1