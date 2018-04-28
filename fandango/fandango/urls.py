

from django.urls import path
from django.contrib import admin
from . import views

app_name = 'fandango'

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies, name='movies'),
    path('admin/', admin.site.urls),
    path('movies/<int:movie_id>/', views.list_movies, name="movie-details"),
    path('theaters/', views.list_theaters, name='theaters-list'),

]

# from django.urls import path
# from django.contrib import admin
# from . import views
#
# app_name = 'fandango'
# urlpatterns = [
#     path('', views.home, name='home')
# ]
