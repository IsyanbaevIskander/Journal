from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from core import models


def get_films(request):
    films = models.Film.objects.all()
    return render(request, template_name='films/get_films.html', context={'films': films, 'title': 'Список фильмов'})
