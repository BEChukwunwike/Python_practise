from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, name=None):
    if name:
        name = name.capitalize()
    return render(request, 'hello/index.html', {
        'name': name
    })