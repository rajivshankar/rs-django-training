# myproject/movies/views.py
# -*- coding: UTF-8 -*-


from django.shortcuts import render
from .models import Genre
from .models import Director
from .models import Actor
from .models import Movie, RATING_CHOICES
from .forms import MovieFilterForm

def movie_list(request):
    qs = Movie.objects.order_by('title')
    
    form = MovieFilterForm(data=request.REQUEST)
    
    facets = {
        'selected':{},
        'categories':{
            'genres':Genre.objects.all(),
            'directors':Director.objects.all(),
            'actors':Actor.objects.all(),
            'ratings':RATING_CHOICES
        },
    }
    
    if form.is_valid():
        genre = form.cleaned_data['genre']
        if genre:
            facets['selected']['genre'] = genre
            qs = qs.filter(genres=genre).distinct()
        
        director = form.cleaned_data['director']
        if director:
            facets['selected']['director'] = director
            qs = qs.filter(directors=director).distinct()
        
        actor = form.cleaned_data['actor']
        if actor:
            facets['selected']['actor'] = actor
            qs = qs.filter(actors=actor).distinct()
        
        rating = form.cleaned_data['rating']
        if rating:
            facets['selected']['rating'] = \
                (int(rating), dict(RATING_CHOICES)[int(rating)])
            qs = qs.filter(rating=rating).distinct()
        
    context = {
       'form':form,
       'facets':facets,
       'object_list':qs,
    }
    
    return render(request, 'movies/movie_list.html', context)