from django.shortcuts import render
from django.shortcuts import render_to_response


def index(request):
    # ORM queries the database for all of the to-do entries.
    items = todo.objects.all()

    # Responds with passing the object items (contains info from the DB) to the
    # template index.html
    return render_to_response('index.html', {'items': items})
