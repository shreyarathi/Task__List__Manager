"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include 

#admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('accounts/', include('allauth.urls')),
    path('todo/', include('todo.urls')),
    path('todo/',include('django.contrib.auth.urls')),
    #can also add myapp urls directly here rather than including, but this method is useful for multiple application
    # can add directly in url '/about' but for include '/myapp/about'
]
