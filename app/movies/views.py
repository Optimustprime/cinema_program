from django.shortcuts import render
from movies.serializers import (MovieSerializer)
from .models import Movie
from rest_framework import viewsets


# Create your views here.

class MovieListView(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-ranking') # Sort by ranking in descending order
    serializer_class = MovieSerializer

    # def get_extra_actions(self):
    #     extra_actions = {}
    #     return extra_actions