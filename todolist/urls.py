"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

# admin.autodiscover()

urlpatterns = [
    # Allow us to access the admin page
    url(r'^admin/', admin.site.urls),
    # match all URL patterns and route them to the todoapp
    # and let the app handle it with it's own urls.py
    url(r'', include('todoapp.urls')),
    # Delet items
    url(r'^delete_todo/', views.delete_todo, todo='delete_todo')
]
