from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=255)
    protagonists = models.TextField()
    poster = models.ImageField(upload_to='posters')
    start_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    ranking = models.IntegerField(default=0)

    def __str__(self):
        return self.name
