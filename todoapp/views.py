from django.shortcuts import render
from .models import todo


def index(request):
    # ORM queries the database for all of the to-do entries.

    if request.method == 'POST':
        # Get the data from the form
        name = request.POST.get('name')
        description = request.POST.get('description')
        # add the data to the database
        items = todo.objects.create(task_name=name, task_description=description)

    # Gets the todos we need from the database
    items = todo.objects.all()
    # render the page with the todos list
    return render(request, 'todoapp/index.html', {'items': items})


def delete_todo(request):
    if request.method == 'POST':
        # get the id for the task
        id = request.POST.get("id")
        # delete the data
        todo.objects.get(id=id).delete()
        # Gets the todos we need from the database
        items = todo.objects.all()
        # render the page with the todos list
        return render(request, 'todoapp/index.html', {'items': items})
