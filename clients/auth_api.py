from custom_requester.custom_requester import CustomRequester
from config.base_urls import AUTH_BASE_URL
from config.admin_creds import ADMIN_CREDS

LOGIN = '/login'


class AuthApi(CustomRequester):
    def __init__(self, session):
        super().__init__(session=session, base_url=AUTH_BASE_URL)

    def admin_login(self):
        return self.send_request(
            method="POST",
            endpoint=LOGIN,
            data=ADMIN_CREDS,
            expected_status=201,
        )
