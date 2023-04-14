from django.shortcuts import get_object_or_404
from django.http import Http404
from ninja import Router
from .models import Movie
from .serializers import MovieSerializer

router = Router()


@router.get("/movies/")
def list_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return serializer.data


@router.get("/movies/{movie_id}/")
def get_movie(request, movie_id: int):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        raise Http404
    serializer = MovieSerializer(movie)
    return serializer.data


@router.post("/movies/")
def create_movie(request, data: dict):
    serializer = MovieSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    else:
        return serializer.errors



@router.put("/movies/{movie_id}/")
def update_movie(request, movie_id: int, data: dict):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieSerializer(movie, data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    else:
        return serializer.errors


@router.delete("/movies/{movie_id}/")
def delete_movie(request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return {"status": "ok"}
