from django.test import TestCase
from movies.models import Movie


class MovieModelTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(
            name='The Shawshank Redemption',
            protagonists='Tim Robbins, Morgan Freeman',
            poster='posters/shawshank_redemption.jpg',
            start_date='1994-09-23 00:00:00',
            status='Released',
            ranking=9.3,
        )

    def test_movie_name(self):
        movie = Movie.objects.get(name='The Shawshank Redemption')
        self.assertEqual(movie.name, 'The Shawshank Redemption')

    def test_movie_protagonists(self):
        movie = Movie.objects.get(name='The Shawshank Redemption')
        self.assertEqual(movie.protagonists, 'Tim Robbins, Morgan Freeman')

    def test_movie_poster(self):
        movie = Movie.objects.get(name='The Shawshank Redemption')
        self.assertEqual(movie.poster, 'posters/shawshank_redemption.jpg')

    def test_movie_start_date(self):
        movie = Movie.objects.get(name='The Shawshank Redemption')
        expected_start_date = '1994-09-23 00:00'
        self.assertEqual(movie.start_date.strftime('%Y-%m-%d %H:%M'), expected_start_date)

    def test_movie_status(self):
        movie = Movie.objects.get(name='The Shawshank Redemption')
        self.assertEqual(movie.status, 'Released')

    def test_movie_ranking(self):
        movie = Movie.objects.get(name='The Shawshank Redemption')
        self.assertEqual(movie.ranking, 9)
