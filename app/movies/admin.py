from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'protagonists', 'start_date', 'status', 'ranking')
    list_filter = ('status',)
    search_fields = ('name', 'protagonists')
