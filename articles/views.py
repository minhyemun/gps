from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        #'name':'김씨',
        'variable':'김씨',
        'result':'10'
    }
    return render(request, 'articles/index.html', context)