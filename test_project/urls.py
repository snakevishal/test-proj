"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import TemplateView



urlpatterns = [
    # path('',TemplateView.as_view(template_name = "blog/index.html")),
    # path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(('testapp.urls', 'singup'),namespace='singup')),
    path('api/v1/post/', include(('post.urls', 'post'),namespace='post')),
    path('accounts/', include('allauth.urls')),
    path('',TemplateView.as_view(template_name = "blog/index.html")),
 
]
