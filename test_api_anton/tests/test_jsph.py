import pytest

TEST_DATA = [
    {"title": "my title","body": "baras","userId": 1},
    {"title": "my tittle","body": "barasss","userId": 2}
]

NEGATIVE_DATA = [
    {"title": ["my title"],"body": "baras","userId": 1},
    {"title": {"my tittle": ''},"body": "baras","userId": 2},
]

@pytest.mark.parametrize("data",TEST_DATA)
def test_post(create_post_endpoint,data):
    create_post_endpoint.create_new_post(body=data)
    create_post_endpoint.check_that_status_is_201()
    create_post_endpoint.check_response_title_is_correct(data['title'])


@pytest.mark.parametrize("data",NEGATIVE_DATA)
def test_post_negative_data(create_post_endpoint,data):
    create_post_endpoint.create_new_post(body=data)
    create_post_endpoint.check_that_status_is_201()
    #create_post_endpoint.check_bad_request()
    create_post_endpoint.check_response_title_is_correct(data['title'])


def test_put_a_post(update_post_endpoint):
    body = {
        "title": "foof",
        "body": "bar42",
        "userId": 1,
    }
    update_post_endpoint.make_changes_in_post(42,body)
    update_post_endpoint.check_that_status_is_201()
    update_post_endpoint.check_response_title_is_correct(body['title'])

