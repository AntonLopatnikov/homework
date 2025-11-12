import requests


def all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100, 'not all posts returned'


def one_post():
    post_id = new_post()
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    assert response['id'] == post_id



def new_post():
    body = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json = body,
        headers = headers
    )

    return response.json()['id']

def clear(post_id):
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

def put_a_post():
    post_id = new_post()
    body = {
        "title": "foof",
        "body": "bar42",
        "userId": 1,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json = body,
        headers = headers
    ).json()
    assert response['title'] == 'foof', 'title is incorrect'
    clear(post_id)


def patch_a_post():
    post_id = new_post()
    body = {
        "body": "bar",
        "userId": 7,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json = body,
        headers = headers
    ).json()
    clear(post_id)

def delete_a_post():
    post_id = new_post()
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print(response.json())
    print(response.status_code)

