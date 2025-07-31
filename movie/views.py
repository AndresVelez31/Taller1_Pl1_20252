from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html')
    #return render(request, 'home.html', {'name': 'Andres Velez'})
    searchTerm = request.GET.get('searchMovie')
    movies = Movie.objects.all()
    
def about(request):
    #return HttpResponse('<h1>About Us</h1>')
    return render(request, 'about.html')

