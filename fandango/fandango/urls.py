

from django.urls import path
from django.contrib import admin
from . import views

app_name = 'fandango'

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.list_movies, name='movies-list'),
    path('admin/', admin.site.urls),
    path('movies/<int:movie_id>/', views.list_movies, name="movie-details"),
]

# from django.urls import path
# from django.contrib import admin
# from . import views
#
# app_name = 'fandango'
# urlpatterns = [
#     path('', views.home, name='home')
# ]
