from django.contrib import admin

# Register your models here.

from models import todolist

# Register model with the admin
admin.site.register(todolist)
