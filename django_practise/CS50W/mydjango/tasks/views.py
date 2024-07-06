from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.http import HttpResponseRedirect

class AddTaskForm(forms.Form):
    task = forms.CharField(label="Add new task here")
    
# Create your views here.
def index(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session['tasks']
    })
    
def add(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks'] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, 'tasks/add.html', {
                'form': form
            })
            
    return render(request, 'tasks/add.html', {
        'form': AddTaskForm()
    })