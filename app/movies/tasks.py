from celery import shared_task
from time import sleep
from .models import Movie


@shared_task
def increase_ranking():
    # increase_ranking: This task increases the ranking of upcoming movies by 10 every 5 minutes. It gets a list of
    # all upcoming movies from the database, iterates over them, and adds 10 to each movie's ranking field. The
    # changes are saved back to the database.

    upcoming_movies = Movie.objects.filter(status='upcoming')
    for movie in upcoming_movies:
        movie.ranking += 10
        movie.save()


@shared_task
def add(x, y):
    # add: This task simulates a long-running task by sleeping for 5 seconds, and then returns the sum of two numbers
    # x and y. This task is used as an example to demonstrate how to define a simple task with Celery.

    sleep(5)  # Simulate a long-running task
    return x + y
