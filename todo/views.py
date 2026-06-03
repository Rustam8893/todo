from django.shortcuts import render,redirect
from .models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('index')
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('index')
    return render(request, 'edit.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

def change_status(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')
