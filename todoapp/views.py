from django.shortcuts import render
from .models import todo

def index(request):
    # ORM queries the database for all of the to-do entries.
    items = todo.objects.all()

    # Responds with passing the object items (contains info from the DB) to the
    # template index.html
    # def index(request):
    if request.method == 'add'
        items = request.POST.get('add')
        return render(request, 'todoapp/index.html', {'items': items})
