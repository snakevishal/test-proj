from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^all/post/$', views.PostApi.as_view({"get": "get_post"}), name='get_post'), 
    url(r'^specific/post/(?P<id>[0-9]+)/$', views.PostApi.as_view({"get": "specific_post"}), name='specific_post'),
    url(r'^create/$', views.PostApi.as_view({"post": "create_post"}), name='create_post'),
    url(r'^update/(?P<id>[0-9]+)/$', views.PostApi.as_view({"put": "update_post"}), name='update_post'),
    url(r'^delete/(?P<id>[0-9]+)/$', views.PostApi.as_view({"delete": "delete_post"}), name='delete_post'),
    
    
]