from source.movie_collection import MovieCollection


class TestMovieCollection:
    def test_get_movies_by_year_true(self, movie_collection: MovieCollection):
        expected_movies = [
            {'name': 'The Shawshank Redemption', 'rating': 9.17, 'year': 1994},
            ]
        actual_movies = movie_collection.get_movies_by_year(1994)
        assert expected_movies == actual_movies

    def test_get_movies_by_more_than_true(
                self,
                movie_collection: MovieCollection
            ):

        expected_movies = [
            {'name': 'The Shawshank Redemption', 'rating': 9.17, 'year': 1994}
            ]

        actual_movies = movie_collection.get_movies_by_more_than_rating(9.12)
        assert expected_movies == actual_movies

    def test_get_top_of_n_movies_true(self, movie_collection: MovieCollection):
        expected_movies = [
            {'name': 'The Green Mile', 'rating': 9.1, 'year': 1999},
            {'name': 'The Shawshank Redemption', 'rating': 9.17, 'year': 1994},
        ]
        actual_movies = movie_collection.get_top_of_n_movies(2)
        for i in range(1):
            assert expected_movies[i] == actual_movies[i]
