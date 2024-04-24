from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'favorite_movie':'범죄도시',
        'movie_list' : ['범죄도시','극한직업','기생충','아바타']
    }
    return render(request, 'movies/index.html', context)