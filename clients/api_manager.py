from clients.movies_api import MoviesApi
class ApiManager:
    def __init__(self, session, base_url):
        self.session = session
        self.movies_api = MoviesApi(session, base_url)



