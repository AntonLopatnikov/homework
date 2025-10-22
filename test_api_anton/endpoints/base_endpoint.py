import allure

class Endpoint:
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = None
    js = None
    headers = {'Content-Type': 'application/json'}

    @allure.step("check title")
    def check_response_title_is_correct(self, title):
        assert self.js['title'] == title

    @allure.step("check that response is 201")
    def check_that_status_is_201(self):
        assert self.response.status_code == 201

