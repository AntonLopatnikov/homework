import unittest
import requests
import sys

class TestPostApi(unittest.TestCase):

    def setUp(self):
        print('test')
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
        self.post_id = response.json()['id']
        print(f'post created:{self.post_id}')

    def tearDown(self) -> None:
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        print(f'post deleted:{self.post_id}')

    @unittest.skip
    def test_get_one_post(self):
        print('test')
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
        self.assertEqual(response['id'] ,self.post_id)



class testindependent(unittest.TestCase):

    def test_get_all_posts(self):
        print('test')
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100)

    def test_add_post(self):
        print('test')
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
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 101)



