from django.contrib import admin

# Register your models here.

from .models import todo

# Register model with the admin
admin.site.register(todo)
