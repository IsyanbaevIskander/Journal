from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from core import models


def get_films(request):
    films = models.Film.objects.all()
    context = {'films': films,
               'title': 'Список фильмов',
                }
    return render(request, template_name='films/get_films.html', context=context)


def get_genres(request):
    genres = models.Genre.objects.all()
    context = {'title': 'Жанры',
               'genres': genres,
               }
    return render(request, template_name='films/get_genres.html', context=context)


def get_actors(request):
    actors = models.Actor.objects.all()
    context = {'title': 'Актёры',
               'actors': actors,
                }
    return render(request, template_name='films/get_actors.html', context=context)


def get_directors(request):
    directors = models.Director.objects.all()
    context = {'title': 'Режиссёры',
               'directors': directors,
                }
    return render(request, template_name='films/get_directors.html', context=context)


def get_one_genre(request, genre_id):
    genre = models.Genre.objects.get(pk=genre_id)
    films = models.Film.objects.all()
    genre_films = []
    for i in films:
        for j in i.genres.values_list('genre'):
            if genre.genre in j:
                genre_films.append(i)

    context = {'title': genre.genre,
               'films': genre_films,
               }
    return render(request, template_name='films/genre.html', context=context)


def get_one_actor(request, actor_id):
    actor = models.Actor.objects.get(pk=actor_id)
    films = models.Film.objects.all()
    actor_films = []
    for i in films:
        for j in i.actors.values_list('id'):
            print(j)
            if actor_id in j:
                actor_films.append(i)

    context = {'actor': actor,
               'films': actor_films,
               }
    return render(request, template_name='films/actor.html', context=context)


def get_one_director(request, director_id):
    director = models.Director.objects.get(pk=director_id)
    films = models.Film.objects.all()
    director_films = models.Film.objects.filter(director__exact=director)

    context = {'director': director,
               'films': director_films,
               }
    return render(request, template_name='films/director.html', context=context)


def get_one_film(request, film_id):
    film = models.Film.objects.get(pk=film_id)
    context = {'film': film}
    return render(request, template_name='films/film.html', context=context)