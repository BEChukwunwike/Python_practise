from django.shortcuts import render
tasks = ['Cook', 'Read', 'Sleep']

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
    
def add(request):
    return render(request, 'task/add.html')