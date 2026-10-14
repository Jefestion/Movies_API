class TestGetMovies:
    def test_get_movies(self, api_manager, movies_params):
        response = api_manager.movies_api.get_movies(movies_params)
        response_data = response.json()
        assert "movies" in response_data
        assert isinstance(response_data["movies"], list)

    def test_get_movies_check_location_msk(self, api_manager, movies_params):
        response = api_manager.movies_api.get_movies(movies_params)
        response_data = response.json()
        for movie in response_data["movies"]:
            assert movie["location"] == "MSK"

    def test_get_movies_check_location_spb(self, api_manager, movies_params):
        movies_params["locations"] = "SPB"
        response = api_manager.movies_api.get_movies(movies_params)
        response_data = response.json()
        for movie in response_data["movies"]:
            assert movie["location"] == "SPB"
