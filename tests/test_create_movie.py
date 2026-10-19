class TestCreateMovie:
    def test_create_movie(self, api_manager, new_movie, movie_cleanup):
        response = api_manager.movies_api.create_movie(new_movie)
        response_data = response.json()

        movie_cleanup.append(response_data["id"])

        assert isinstance(response_data["id"], int)
        assert response_data["id"] > 0
        for field in ("name", "price", "description", "location", "published", "genreId", "imageUrl"):
            assert response_data[field] == new_movie[field], f"Поле {field} не совпадает"

    def test_create_movie_same_name(self, api_manager, new_movie, movie_cleanup):
        created_movie = api_manager.movies_api.create_movie(new_movie)
        movie_cleanup.append(created_movie.json()["id"])

        duplicate_movie = new_movie.copy()
        duplicate_movie["price"] += 100

        response = api_manager.movies_api.create_movie(
            duplicate_movie,
            expected_status=409
        )

        assert response.json()["message"] == "Фильм с таким названием уже существует"

    def test_create_movie_empty_name(self, auth_session, api_manager, movie_empty_name):
        response = api_manager.movies_api.create_movie(
            movie_empty_name,
            expected_status=400
        )
        # Cообщение при 400 не соответствует прописанному а API (ОР: "Неверные параметры")
        assert response.json()["message"] == ['name should not be empty'], "Сообщение ошибки не соответствует API"
