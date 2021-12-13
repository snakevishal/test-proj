from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rest_framework import status
from .models import *

class PostApi(ViewSet):

    def get_post(self,request):
        print(request.user)
        response = {
            "success":False,
            "message":"No data found"
        }
        status_code=status.HTTP_404_NOT_FOUND
        data = Post.objects.all().values()
        response = {
            "data":data,
            "success":True,
            "message":"data received from db"
        }
        status_code=status.HTTP_200_OK
        return Response(response,status_code)
    
    def specific_post(self,request,id):
        try:
            post_obj = Post.objects.get(id=id)
            if post_obj:
                response.update({'success': True})
                response.update({'message': 'post retrieved successfully'})
                response.update({'data': post_obj})
                status_code = status.HTTP_200_OK
        except Post.DoesNotExist:
            response = {"success": False,
                    "message": ' Sorry no task has id :{}'.format(id)}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(response, status=status_code)

    def create_post(self,request,**data):
        response = {"success": False,
                    "message": '!!! Ops something went wrong '}
        data_status = Post.objects.create(**request.data)
        if data_status:
            response.update({'success': True})
            response.update({'message': 'Post created successfully'})
            status_code = status.HTTP_201_CREATED
        return Response(response, status=status_code)

    def update_post(self,request,id,**data):
        try:
            Post.objects.get(id=id)
        except Post.DoesNotExist:
            response = {
                "success":False,
                "message":f"id {id} does not exist"
            }
            status_code = status.HTTP_404_NOT_FOUND
        else:
            Post.objects.filter(id=id).update(**request.data)
            response = {
                "success":True,
                "message":"post is update"
            }
            status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
    
    def delete_post(self,request,id):
        try:
            Post.objects.get(id=id)
        except Post.DoesNotExist:
            response = {
                "success":False,
                "message":f"id {id} does not exist"
            }
            status_code = status.HTTP_404_NOT_FOUND
        else:
            Post.objects.get(id=id).delete()
            response = {
                "success":True,
                "message":"post is delete"
            }
            status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from rest_auth.registration.views import SocialLoginView

# class FacebookLogin(SocialLoginView):

#     adapter_class = FacebookOAuth2Adapter