from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        TodoItem.objects.create(title=title)
    return redirect('todo_list')

def complete_todo(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def delete_completed(request):
    TodoItem.objects.filter(completed=True).delete()
    return redirect('todo_list')
