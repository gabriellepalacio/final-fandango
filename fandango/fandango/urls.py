from django.urls import path

from . import views

app_name='fandango'
urlpatterns = [
    path('', views.home, name='home'),
    path('movie/', views.list_movies, name='movies-list'),
    path('theaters/', views.list_theaters, name='theaters-list'),
    path('movie/<int:movie_id>/', views.movie_detail, name="movie-details"),
    path('theaters/<slug:th_id>/', views.theater_detail, name="theater-details"),
    path('api/<slug:slug>/', views.api, name='api'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]
