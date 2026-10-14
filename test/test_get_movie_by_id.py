class TestGetMovieById:

    def test_get_movie_by_id(self, api_manager, new_movie):
        created_movie_to_get = api_manager.movies_api.create_movie(new_movie)
        new_movie_id = created_movie_to_get.json()["id"]

        response = api_manager.movies_api.get_movie_by_id(new_movie_id)
        response_data = response.json()

        for field in new_movie:
            assert response_data[field] == new_movie[field]
