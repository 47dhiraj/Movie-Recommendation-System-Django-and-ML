from django.shortcuts import render, redirect
import json                           
from django.http import JsonResponse  
from recommendation.models import Movie
from django.core.cache import cache
import pandas as pd
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def home(request, movie_genre=None, imdb_rating=None, year=None, latest=None):

    if request.method == 'POST':
        query = json.loads(request.body).get('searchText')  
        movies = Movie.objects.filter(Q(title__icontains=query)).distinct()
        data = movies.values()  
        return JsonResponse(list(data),safe=False)  

    query = request.GET.get('searchvalue')
    if query:
        movies = Movie.objects.filter(Q(title__icontains=query)).distinct()
        context = {'movies': movies}
        return render(request, 'home/index.html', context)

    if movie_genre:
        if movie_genre == 'Action' or movie_genre == 'Animation' or movie_genre == 'Comedy' or movie_genre == 'Crime' or movie_genre == 'Horror' or movie_genre == 'Sci-Fi' or movie_genre == 'War' or movie_genre == 'Action Sci-Fi' or movie_genre == 'Comedy Crime' or movie_genre == 'Drama Thriller':
            movies_all = Movie.objects.filter(genre=movie_genre)
        else:
            return redirect('home')

    elif imdb_rating:
        movies_all = Movie.objects.filter(Q(imdbrating__gte=8.0))

    elif year:
        if year == 2016 or year == 2015 or year == 2014 or year == 2013 or year == 2012 or year == 2011:
            movies_all = Movie.objects.filter(year=year)
        else:
            return redirect('home')
    else:
        movies_all = Movie.objects.filter(year=2016)

    page = request.GET.get('page', 1)
    paginator = Paginator(movies_all, 12)
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)


    context = {'movies': movies}
    return render(request, 'home/index.html', context)
