class TestGetMovies:
    def test_get_movies(self, api_manager, movies_params):
        response = api_manager.movies_api.get_movies(movies_params)
        response_data = response.json()
        assert "movies" in response_data
        assert isinstance(response_data["movies"], list)
        assert len(response_data["movies"]) > 0
        assert response_data["page"] == movies_params["page"]
        assert response_data["pageSize"] == movies_params["pageSize"]
        assert isinstance(response_data["count"], int)

        assert isinstance(response_data["pageCount"], int)

        for movie in response_data["movies"]:
            assert isinstance(movie["id"], int)
            assert isinstance(movie["name"], str)
            assert isinstance(movie["price"], (int, float))
            assert isinstance(movie["published"], bool)
            assert isinstance(movie["genre"], dict)
            assert isinstance(movie["genre"]["name"], str)
        print(response_data)

    def test_get_movies_check_location_msk(self, api_manager, movies_params):
        response = api_manager.movies_api.get_movies(movies_params)
        response_data = response.json()
        for movie in response_data["movies"]:
            assert movie["location"] == "MSK"
        assert response_data["movies"], "Список фильмов пуст"

    def test_get_movies_check_location_spb(self, api_manager, movies_params):
        params = movies_params.copy()
        params["locations"] = "SPB"
        response = api_manager.movies_api.get_movies(params)
        response_data = response.json()
        for movie in response_data["movies"]:
            assert movie["location"] == "SPB"
        assert response_data["movies"], "Список фильмов пуст"

    def test_get_movies_wrong_params(self, api_manager, wrong_movies_params):
        response = api_manager.movies_api.get_movies(wrong_movies_params, expected_status=400)
        response_data = response.json()
        assert response_data["statusCode"] == 400
        assert response_data["message"] == "minPrice must be less than maxPrice"
