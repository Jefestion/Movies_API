class TestGetMovies():
    def test_get_movies(self, api_manager):
        response = api_manager.movies_api.get_movies()