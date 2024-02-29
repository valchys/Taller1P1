from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    json_file_path = 'movie/management/commands/movies.json'
    with open(json_file_path, 'r') as file:
        movies = json.load(file)

    for i in range(100):
        movie=movies[i]
        exist = Movie.objects.filter(title = movie['title'],
                                     image = 'movie/images/default.jpg',
                                     genre = movie['genre'],
                                     year = movie['year'])
        