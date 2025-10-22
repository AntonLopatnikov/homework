import requests
import allure

@allure.feature('posts')
@allure.story('manipulate posts')
def test_delete(new_post_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}')