import requests
import allure
import pytest


@pytest.fixture(scope ='session')
def hello():
    print('hello')
    yield
    print('bye')

@allure.feature('posts')
@allure.story('get posts')
def get_one_post(new_post_id, hello):
    with allure.step(f'run get request for post with id {new_post_id}'):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    with allure.step(f'check post id is {new_post_id}'):
        assert response == {11}

@allure.feature('posts')
@allure.story('get posts')
def get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100


@allure.feature('posts')
@allure.story('manipulate posts')
def add_post():
    with allure.step('prepare teest data'):
        body = {
            "title": "foo",
            "body": "bar",
            "userId": 1,
        }
        headers = {"Content-Type": "application/json"}
    with allure.step('run request to create a post'):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
    with allure.step('check response code is 201'):
        assert response.status_code == 201
    with allure.step('check id of create post is 101'):
        assert response.json()['id'] == 101

@allure.feature('example')
@allure.story('equals')
@pytest.mark.parametrize('logins', [1, 2, 3,4])
def one(logins):
    assert 1 == 1

# pytest -v --alluredir=allure-results
# pytest -vs
# pytest -v -n auto
# allure serve allure-results
# allure generate -c  allure-results -o allure-report
#  allure generate --clean