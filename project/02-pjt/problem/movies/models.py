from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=255, unique=True)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    popularity = models.FloatField()
    budget = models.IntegerField()
    revenue = models.IntegerField()
    runtime = models.IntegerField()
    # Genre 클래스의 genre 정보 다대다 참조
    genres = models.ManyToManyField(Genre)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # review = models.TextField(primary_key=True)
    author = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.FloatField()

class Cast(models.Model):
    # cast = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    character = models.CharField(max_length=255)
    order = models.IntegerField()
