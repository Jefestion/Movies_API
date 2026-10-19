class TestGetMovieById:

    def test_get_movie_by_id(self, api_manager, new_movie, created_movie):
        response = api_manager.movies_api.get_movie_by_id(created_movie)
        response_data = response.json()

        assert response_data["id"] == created_movie
        for field in new_movie:
            assert response_data[field] == new_movie[field]

    def test_get_movie_by_nonexistent_id(self, api_manager):
        response = api_manager.movies_api.get_movie_by_id(-1,
                                                          expected_status=404)
        response_data = response.json()
        assert response_data["statusCode"] == 404
        assert response_data["message"] == "Фильм не найден", "Сообщение ошибки не соответствует API"