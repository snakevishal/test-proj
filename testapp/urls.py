from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^singup/$', views.UserApi.as_view({"post": "signup_process"}), name='singup'),
]