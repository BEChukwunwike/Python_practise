from django.shortcuts import render
from django import forms

tasks = ['Cook', 'Read', 'Sleep']

class AddTaskForm(forms.Form):
    task = forms.CharField(label="Add new task here")
    
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
    
def add(request):
    return render(request, 'tasks/add.html', {
        'form': AddTaskForm()
    })