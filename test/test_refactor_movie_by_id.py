class TestRefactorMovieById:
    #404 ошибка при выполнении запроса. Тот же при дёргании из сваггера.
    def test_refactor_movie_by_id(self, api_manager, new_movie, refactored_data):
        created_movie_to_refactor = api_manager.movies_api.create_movie(new_movie)
        new_movie_id = created_movie_to_refactor.json()["id"]
        api_manager.movies_api.get_movie_by_id(new_movie_id)
        api_manager.movies_api.edit_movie(new_movie_id, refactored_data)
        response = api_manager.movies_api.get_movie_by_id(new_movie_id)
        response_data = response.json()
        for field in refactored_data:
            assert response_data[field] == refactored_data[field]