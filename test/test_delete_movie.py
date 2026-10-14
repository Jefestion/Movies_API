class TestDeleteMovieById:
    def test_delete_movie_by_id(self, api_manager, new_movie):
        created_movie_to_delete = api_manager.movies_api.create_movie(new_movie)
        new_movie_id = created_movie_to_delete.json()["id"]

        api_manager.movies_api.delete_movie_by_id(new_movie_id)

        api_manager.movies_api.get_movie_by_id(
            new_movie_id,
            expected_status=404
        )

