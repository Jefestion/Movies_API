import requests
import pytest
from clients.api_manager import ApiManager
from config.base_urls import MOVIES_BASE_URL


@pytest.fixture(scope="session")
def auth_session():
    http_session = requests.Session()
    yield http_session
    http_session.close()


@pytest.fixture(scope="session")
def api_manager(auth_session):
    return ApiManager(auth_session, MOVIES_BASE_URL)


@pytest.fixture(scope="session")
def movies_params(auth_session):
    return {
        "pageSize": 10,
        "page": 1,
        "minPrice": 1,
        "maxPrice": 1000,
        "locations": "MSK",
        "published": True,
        "genreId": 1,
        "createdAt": "asc"
    }
