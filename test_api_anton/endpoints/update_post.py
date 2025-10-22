from endpoints.base_endpoint import Endpoint
import requests
import allure


class UpdatePost(Endpoint):

    @allure.step("Update a post")
    def make_changes_in_post(self,post_id,body,headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}',
            json=body,
            headers=headers
        )
        self.js = self.response.json()
        return self.response

    allure.step('check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400

