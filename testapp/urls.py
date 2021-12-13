# from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [

    path('singup/', views.UserApi.as_view({"post": "signup_process"}), name='singup'),
]