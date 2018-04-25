from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from . import models


def home(request):
    return render(request, "movie/home.html", {
        'theaters': models.Theater.objects.all(),
        'movie': models.Movie.objects.all(),
    })

def list_movies(request):
    filter_by = request.GET.get('filter')
    filter_val = request.GET.get('val')
    filter_breadcrumb_name = None
    filter_breadcrumb_url = None

    objects = models.Movie.objects.all()

    if filter_by and filter_val:
        if filter_by == 'city':
            objects = objects.filter(movie__city__iexact=filter_val)
            filter_breadcrumb_name = "City"
            #filter_breadcrumb_url = reverse("winners:countries-list")
        if filter_by == 'genre':
            objects = objects.filter(movie__genre__iexact=filter_val)
            filter_breadcrumb_name = "Genres"
            #filter_breadcrumb_url = reverse("winners:categories-list")

    return render(request, "movies/list.html", {
        "list_type": "Movie",
        "objects": objects,
        "filter_by": filter_by,
        "filter_val": filter_val,
        "filter_breadcrumb_name": filter_breadcrumb_name,
        #"filter_breadcrumb_url": filter_breadcrumb_url,
    })

def list_theaters(request):
    # filter_by = request.GET.get('filter')
    # filter_val = request.GET.get('val')
    # filter_breadcrumb_name = None
    # filter_breadcrumb_url = None

    objects = models.Theater.objects.all()

    # if filter_by and filter_val:
    #     if filter_by == 'city':
    #         objects = objects.filter(movie__city__iexact=filter_val)
    #         filter_breadcrumb_name = "City"
    #         #filter_breadcrumb_url = reverse("winners:countries-list")
    #     if filter_by == 'movie':
    #         for o in objects:
    #             if o.movie_set
    #         objects = objects.filter(movie__genre__iexact=filter_val)
    #         filter_breadcrumb_name = "Genres"
            #filter_breadcrumb_url = reverse("winners:categories-list")

    return render(request, "movie/list.html", {
        "list_type": "Theaters",
        "objects": objects,
        # "filter_by": filter_by,
        # "filter_val": filter_val,
        # "filter_breadcrumb_name": filter_breadcrumb_name,
        # "filter_breadcrumb_url": filter_breadcrumb_url,
    })

def movie_detail(request, movie_id):
      movie = get_object_or_404(models.Movie, movie_id=movie_id)
      theater_objects = movie.theaters.all()
      theaters = []
      for t, theater in enumerate(theater_objects):
          theaters.append(theater.name)

      context = {
        'title' : movie.title,
        'poster' : "https://" + movie.poster,
        'theaters' : theaters,
        'rating' : movie.rating,
      }
      return render(request, "movie/movie_detail.html", context)

# Create your views here.
