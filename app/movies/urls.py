from django.urls import path, include
from rest_framework import routers
from .views import MovieListView

router = routers.DefaultRouter()
router.register(r'movies', MovieListView, basename='movie')

urlpatterns = [
    path('', include(router.urls)),
]
