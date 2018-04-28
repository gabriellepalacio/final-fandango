from django.shortcuts import render
from fandango.models import Theater, Movie, Showtime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers

from django.urls import reverse
from django.http import JsonResponse
from . import models



def home(request):
    context = {
        'theater_count': Theater.objects.count(),
        'theaters': Theater.objects.all(),
        'movie_count': Movie.objects.count(),
        'showtime_count': Showtime.objects.count(),
    }
    return render(request, "home.html", context)

def movie_detail(request):
    movie = get_object_or_404(models.Movie, movie_id=movie_id)
    theater_objects = movie.theaters.all()
    theaters = []
    for t, theater in enumerate(theater_objects):
         theaters.append(theater.name)

    context = {
        'title' : movie.title,
        'poster' : "https://" + movie.poster,
        'theaters' : theaters,

      }
    return render(request, "detail.html", context)

def movies(request):
    filter_by = request.GET.get('filter')
    filter_val = request.GET.get('val')
    filter_breadcrumb_name = None
    filter_breadcrumb_url = None

    objects = Movie.objects.all()

    if filter_by and filter_val:
        if filter_by == 'city':
            objects = objects.filter(movie__city__iexact=filter_val)
            filter_breadcrumb_name = "City"
            #filter_breadcrumb_url = reverse("winners:countries-list")
        if filter_by == 'genre':
            objects = objects.filter(movie__genre__iexact=filter_val)
            filter_breadcrumb_name = "Genres"
            #filter_breadcrumb_url = reverse("winners:categories-list")

    return render(request, "movies.html", {
        "list_type": "Movie",
        "objects": objects,
        "filter_by": filter_by,
        "filter_val": filter_val,
        "filter_breadcrumb_name": filter_breadcrumb_name,
        #"filter_breadcrumb_url": filter_breadcrumb_url,
    })


def list_movies(request):
    filter_by = request.GET.get('filter')
    filter_val = request.GET.get('val')
    filter_breadcrumb_name = None
    filter_breadcrumb_url = None

    objects = Movie.objects.all()

    if filter_by and filter_val:
        if filter_by == 'city':
            objects = objects.filter(movie__city__iexact=filter_val)
            filter_breadcrumb_name = "City"
            #filter_breadcrumb_url = reverse("winners:countries-list")
        if filter_by == 'genre':
            objects = objects.filter(movie__genre__iexact=filter_val)
            filter_breadcrumb_name = "Genres"
            #filter_breadcrumb_url = reverse("winners:categories-list")

    return render(request, "list.html", {
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

    objects = Theater.objects.all()



    return render(request, "theater.html", {
        "list_type": "Theaters",
        "objects": objects,

    })
# from django.http import HttpResponse
# from django.core import serializers
# from django.shortcuts import render, get_object_or_404
# from django.urls import reverse
# from django.http import JsonResponse
# from . import models
#
#
# def home(request):
#     return render(request, "fandango/base.html", {
#         'theaters': models.Theater.objects.all(),
#         'movies': models.Movie.objects.all(),
#     })
#
# def list_movies(request):
#     filter_by = request.GET.get('filter')
#     filter_val = request.GET.get('val')
#     filter_breadcrumb_name = None
#     filter_breadcrumb_url = None
#
#     objects = models.Movie.objects.all()
#
#     if filter_by and filter_val:
#         if filter_by == 'city':
#             objects = objects.filter(movie__city__iexact=filter_val)
#             filter_breadcrumb_name = "City"
#             #filter_breadcrumb_url = reverse("winners:countries-list")
#         if filter_by == 'genre':
#             objects = objects.filter(movie__genre__iexact=filter_val)
#             filter_breadcrumb_name = "Genres"
#             #filter_breadcrumb_url = reverse("winners:categories-list")
#
#     return render(request, "fandango/list.html", {
#         "list_type": "Movie",
#         "objects": objects,
#         "filter_by": filter_by,
#         "filter_val": filter_val,
#         "filter_breadcrumb_name": filter_breadcrumb_name,
#         #"filter_breadcrumb_url": filter_breadcrumb_url,
#     })
#
# def list_theaters(request):
#     # filter_by = request.GET.get('filter')
#     # filter_val = request.GET.get('val')
#     # filter_breadcrumb_name = None
#     # filter_breadcrumb_url = None
#
#     objects = models.Theater.objects.all()
#
#
#
#     return render(request, "fandango/list.html", {
#         "list_type": "Theaters",
#         "objects": objects,
#
#     })
#
# def movie_detail(request, movie_id):
#       movie = get_object_or_404(models.Movie, movie_id=movie_id)
#       theater_objects = movie.theaters.all()
#       theaters = []
#       for t, theater in enumerate(theater_objects):
#           theaters.append(theater.name)
#
#       context = {
#         'title' : movie.title,
#         'poster' : "https://" + movie.poster,
#         'theaters' : theaters,
#
#       }
#       return render(request, "fandango/movie_detail.html", context)
#
# def theater_detail(request, th_id):
#       theater = get_object_or_404(models.Theater, theater_id=th_id)
#       movie_objects = theater.movie_set.all()
#       movies = []
#       for m, movie in enumerate(movie_objects):
#           movies.append(movie.title)
#
#       context = {
#         'name' : theater.name,
#         'address' : theater.address,
#         'movies' : movie_objects,
#       }
#       return render(request, "fandango/theater_detail.html", context)
# # Create your views here.
