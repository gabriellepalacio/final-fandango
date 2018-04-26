

from django.urls import path
from django.contrib import admin
from . import views

app_name = 'fandango'

urlpatterns = [
    path('', views.home, name='home'),
    # path('movies/', views.list_movies, name='movies-list'),
    # path('theaters/', views.list_theaters, name='theaters-list'),
    # path('movies/<int:movie_id>/', views.movie_detail, name="movie-details"),
    # path('theaters/<slug:th_id>/', views.theater_detail, name="theater-details"),
    path('admin/', admin.site.urls),
]

# from django.urls import path
# from django.contrib import admin
# from . import views
#
# app_name = 'fandango'
# urlpatterns = [
#     path('', views.home, name='home')
# ]
