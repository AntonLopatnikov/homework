import requests
import allure

@allure.story("getting a post")
def test_one_post(new_post_id):
    print('test')
    with allure.step(f'Run get request for post{new_post_id}'):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    with allure.step(f'Check that post id is {new_post_id}'):
        assert response == {11}


@allure.story("create a new post")
def test_new_post():
    with allure.step('prepare test data'):
        body = {
            "title": "foo",
            "body": "bar",
            "userId": 1,
        }
        headers = {"Content-Type": "application/json"}
    with allure.step('Run a request to create a new post'):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json = body,
               headers = headers
        )
    with allure.step('check post body'):
        assert response.status_code == 201
        assert response.json()['title'] == 'foo'
        assert response.json()['body'] == 'bar'
        assert response.json()['userId'] == 1



@allure.story("updating the post")
def test_put_a_post():
    body = {
        "title": "foof",
        "body": "bar42",
        "userId": 1,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/42',
        json=body,
        headers=headers
    ).json()
    assert response['title'] == 'foof'
    assert response['body'] == 'bar42'


@allure.story("partial update of the post")
def test_patch_a_post():
    body = {
        "body": "bar",
        "userId": 7,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f'https://jsonplaceholder.typicode.com/posts/42',
        json=body,
        headers=headers
    ).json()
    print(f"PATCH response: {response}")

@allure.story("delete a post")
def test_delete_a_post():
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/42')
    assert response.status_code == 200, f"Delete failed with status {response.status_code}"

# pytest -v lessons/lesson18 --alluredir=allure-results
# allure generate -c allure-results -o allure-reports