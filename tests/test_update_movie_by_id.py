class TestUpdateMovieById:
    # 404 ошибка при выполнении запроса. Тот же при дёргании из сваггера.

    def test_update_movie_by_id(self, api_manager, new_movie, updated_data, created_movie):
        api_manager.movies_api.edit_movie(created_movie, updated_data)

        response = api_manager.movies_api.get_movie_by_id(created_movie)
        response_data = response.json()

        for field in updated_data:
            assert response_data[field] == updated_data[field]

        for field in new_movie:
            if field not in updated_data:
                assert response_data[field] == new_movie[field], f"Изменилось поле {field}"
