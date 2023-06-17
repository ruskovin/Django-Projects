from django.shortcuts import redirect, render, HttpResponseRedirect
from . import forms
from .models import Task
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.


def todolist_home(request):
    if request.method == 'POST':
        form = forms.AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'tasks': Task.objects.all(),
        'form': forms.AddTaskForm,
    }
    return render(request, 'task-list.html', context)


def task_detail(request, id):
    context = {
        'task': Task.objects.get(id=id)
    }

    return render(request, 'task-detail.html', context)


def status_update(request, id):
    task = Task.objects.get(id=id)
    task.set_status()
    Task.objects.filter(id=id).update(status = task.status)
    return redirect('home')


def delete_task(request: any, id: int):
    Task.objects.get(id=id).delete()
    return redirect('home')


def update_task(request: any, id: int):
    task = Task.objects.get(id=id)
    form = forms.AddTaskForm(instance=task)
    if request.method == 'POST':
        f = forms.AddTaskForm(request.POST, instance=task)
        f.save()
        return redirect('home')
    context = {
        'task': task,
        'form': form
    }
    return render(request, 'update-task.html', context)
