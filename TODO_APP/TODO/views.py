from django.shortcuts import render, redirect

from .models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos':todos})

def add(request):
    if request.method == 'GET':
        title = request.GET['title']
        todos = Todo(title=title)
        todos.save()

        print(request.GET)
    return redirect('/')


def delete(request, id):
    if request.method == 'GET':
        todos = Todo.objects.get(id=id)
        todos.delete()

    return redirect('/')
