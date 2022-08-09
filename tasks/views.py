from django.shortcuts import render,redirect, get_object_or_404

from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

def profile(request):
    return render(request, 'tasks/profile.html')

@login_required(login_url='login')
def currenttodos(request) :
    todos = Task.objects.filter(user= request.user, datecompleted__isnull=True)
    return render(request, 'tasks/currenttodos.html', {
        "todos": todos
    })

@login_required
def createtodo(request) :
    if request.method == "GET":
        return render(request, 'tasks/createtodo.html', {
            "form": TaskForm()
        })
    else :
        try :
            form = TaskForm(request.POST)
            newtodo = form.save(commit=False)     # don't save it in the database
            newtodo.user = request.user
            newtodo.save()
            return redirect('tasks:home')
        except ValueError:
            return render(request, 'tasks/createtodo.html', {
                'form': TaskForm(),
                "error": "Title must be less than 50 characters. Try again"
            })


@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Task, pk=todo_pk, user=request.user)
    if request.method == "GET":
        form = TaskForm(instance=todo)
        return render(request, 'tasks/viewtodo.html', {
            'todo': todo,
            "form": form
        })
    else:
        try:
            form = TaskForm(request.POST, instance=todo)
            form.save()
            return redirect('tasks:home')
        except ValueError:
            return render(request, 'tasks/viewtodo.html', {
               'todo': todo,
               "form": form,
               "error": "Bad info"
           })



@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Task, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('tasks:home')


@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Task, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect('tasks:home')


@login_required
def completedtodos(request):
    todos = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks/completedtodos.html', {
        "todos": todos
    })

