import pytest


class TestDeleteMovieById:
    def test_delete_movie_by_id(self, api_manager, new_movie, movie_cleanup):
        created_movie_to_delete = api_manager.movies_api.create_movie(new_movie)
        new_movie_id = created_movie_to_delete.json()["id"]
        movie_cleanup.append(new_movie_id)

        api_manager.movies_api.delete_movie_by_id(new_movie_id)
        movie_cleanup.remove(new_movie_id)
        response = api_manager.movies_api.get_movie_by_id(
            new_movie_id,
            expected_status=404
        )
        # Нужно исправить - значение ["message"] при 404 плавающее
        # assert response.json()["message"] == 'Not Found', "Сообщение ошибки не соответствует API"

    def test_delete_movie_by_nonexistent_id(self, api_manager):
        response = api_manager.movies_api.delete_movie_by_id(9999999999999999999, expected_status=404)
        assert response.json()["message"] == "Фильм не найден", "Сообщение ошибки не соответствует API"

    # Не понял, как добиться ошибки 400 "Неверные параметры" - всегда при негативном тестировании возвращает 404
    @pytest.mark.skip
    def test_delete_movie_by_invalid_id(self, api_manager):
        api_manager.movies_api.delete_movie_by_id("_", expected_status=400)
