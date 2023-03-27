from django.shortcuts import render, redirect
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-created')
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        task = Task.objects.create(title=title)
        task.save()
        return redirect('index')
    return render(request, 'todo/add_task.html')


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('index')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')
