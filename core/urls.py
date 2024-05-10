from django.urls import path
from core import views

urlpatterns = [
    path('', views.get_films),
    path('genres/', views.get_genres),
    path('actors/', views.get_actors),
    path('directors/', views.get_directors),
    path('genres/ <int:genre_id>/', views.get_one_genre),
    path('actors/ <int:actor_id>/', views.get_one_actor),
    path('directors/ <int:director_id>/', views.get_one_director),
    path('<int:film_id>/', views.get_one_film),
]
