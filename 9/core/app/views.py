from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Todo

def show_task(request):
    tasks = Todo.objects.all()
    return render(request, 'show.html', {'tasks':tasks})

def delete_task(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.delete()
    return redirect(reverse('tasks'))

def complete_task(request, task_id):
    task = Todo.objects.filter(id=task_id).update(completed = True)
    return redirect(reverse('tasks'))

def home(request):
    return render(request, 'home.html')