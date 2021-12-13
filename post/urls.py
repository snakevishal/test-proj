# from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [

    path('all/post/', views.PostApi.as_view({"get": "get_post"}), name='get_post'), 
    path('specific/post/', views.PostApi.as_view({"get": "specific_post"}), name='specific_post'),
    path('create', views.PostApi.as_view({"post": "create_post"}), name='create_post'),
    path('update/<id>', views.PostApi.as_view({"put": "update_post"}), name='update_post'),
    path('delete/<id>/', views.PostApi.as_view({"delete": "delete_post"}), name='delete_post'),
    
    
]