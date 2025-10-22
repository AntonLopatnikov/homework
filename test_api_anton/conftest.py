import pytest
from endpoints.create_post import CreatePost
from endpoints.update_post import UpdatePost

@pytest.fixture()
def create_post_endpoint():
    return CreatePost()

@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()