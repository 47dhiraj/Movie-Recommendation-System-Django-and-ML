from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [

    path('', csrf_exempt(views.home), name="home"), 
    path('genre/<str:movie_genre>', views.home),
    path('toprating/<str:imdb_rating>', views.home),
    path('year/<int:year>', views.home),
    path('recent/<str:latest>', views.home),

]
