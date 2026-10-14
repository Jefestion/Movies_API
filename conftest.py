import random
import string

import requests
import pytest
from clients.api_manager import ApiManager
from config.base_urls import MOVIES_BASE_URL
from clients.auth_api import AuthApi


@pytest.fixture(scope="session")
def http_session():
    http_session = requests.Session()

    yield http_session
    http_session.close()


@pytest.fixture(scope="session")
def auth_session(http_session):
    auth_api = AuthApi(http_session)
    response = auth_api.admin_login()
    token = response.json()["accessToken"]
    http_session.headers.update({
        "Authorization": f"Bearer {token}"
    })

    return http_session


@pytest.fixture(scope="session")
def api_manager(auth_session):
    return ApiManager(auth_session, MOVIES_BASE_URL)


@pytest.fixture(scope="function")
def movies_params():
    return {
        "pageSize": 10,
        "page": 1,
        "minPrice": 1,
        "maxPrice": 1000,
        "locations": "MSK",
        "published": True,
        "genreId": 7,
        "createdAt": "asc"
    }


@pytest.fixture(scope="function")
def new_movie():
    return {
        "name": ''.join(random.choices(string.ascii_letters, k=7)),
        "imageUrl": f"https://image.url",
        "price": random.randint(1, 1000),
        "description": "Описание фильма",
        "location": random.choice(["MSK", "SPB"]),
        "published": True,
        "genreId": random.choice([186, 1469, 7, 10, 9])
    }


@pytest.fixture(scope="function")
def created_movie(auth_session, new_movie, api_manager):
    disposable_movie = api_manager.movies_api.create_movie(new_movie)


@pytest.fixture(scope="function")
def refactored_data():
    return {
        "name": 'forcibly renamed',
        "imageUrl": f"https://refactored.data",
        "price": 999,
        "description": "Описание фильма после PATCH"
    }
