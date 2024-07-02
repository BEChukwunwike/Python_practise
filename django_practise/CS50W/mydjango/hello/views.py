from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'Hello/index.html')

def greet(request, name):
    name = name.capitalize()
    return render(request, 'Hello/index.html',{
        'name': name
    })
    