class TestCreateMovie:
    def test_create_movie(self, auth_session, api_manager, new_movie):
        response = api_manager.movies_api.create_movie(new_movie)
        response_data = response.json()

        assert response_data["id"]
        for field in ("name", "price", "description", "location", "published", "genreId", "imageUrl"):
            assert response_data[field] == new_movie[field], f"Поле {field} не совпадает"
