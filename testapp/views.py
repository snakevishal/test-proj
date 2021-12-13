from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import User
from rest_framework import status, exceptions
from .serializers import *
from django.core.mail import send_mail
from test_project import settings
from django.contrib.auth import authenticate

from django.contrib.auth.tokens import PasswordResetTokenGenerator

import random



from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings


class UserApi(ViewSet):

    def genrate_random_num(self):
        val = random.randint(0, 100)
        return val


    def signup_process(self, request,**data):
        password = request.data["password"]
        password1 = request.data["password1"]
        email = request.data["email"]
        qs = User.objects.filter(email=email)
        response = {}
        status_code = None
        if qs.exists():
            response = {"success": False,
                        "errors": "Email Already Exists"}
            status_code = status.HTTP_406_NOT_ACCEPTABLE
            return Response(response, status=status_code)
        elif password == password1:
            
            del request.data["password1"]
            user_obj = User.objects.filter(email__iexact=email)
            
        #       pk = User.objects.create_user(**request.data).id
            verification_link = 'http://localhost:9000/verifyemail/'+ str(self.genrate_random_num())
            
            send_mail(
                "email verification",
                f'please verify the account {verification_link} ',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            response = {
                "success":True,
                "message":"verification mail is send"
,                   }
            status_code=status.HTTP_200_OK
            return Response(response, status=status_code)
        #         user_obj = User.objects.filter(id=pk).values("email")
        #         if user_obj:
        #             response = {"success": True,
        #                         "message": "The User has been created.",
        #                         'data': user_obj}
        #             status_code = status.HTTP_201_CREATED
        #     else:
        #         response = {"success": False,
        #                     "errors": serializer.errors}
        #         status_code = status.HTTP_406_NOT_ACCEPTABLE
        # elif password != password1:
        #     response = {"success": False,
        #                 "errors": "Password Must be same"}
        #     status_code = status.HTTP_406_NOT_ACCEPTABLE
        # return Response(response, status=status_code)

    # def login(self, request):
    #     email = request.data["email"]
    #     password = request.data["password"]
    #     user = authenticate(email=email,password=password)
    #     if user is not None:
    #         response = {"success": False,
    #                     "errors": "Email id not match"}
    #         status_code = status.HTTP_406_NOT_ACCEPTABLE
    #     else:
    #         response = {"success": True,
    #                     "errors": "user is login"}
    #         status_code = status.HTTP_406_NOT_ACCEPTABLE
    #     return Response(response, status=status_code)


        # try:
        #     qs = User.objects.get(email=email)
        # except:
        #     response = {"success": False,
        #                 "errors": "Email id not match"}
        #     status_code = status.HTTP_406_NOT_ACCEPTABLE
        # if not check_password(password,User.password):
        #     response = {"success": False,
        #                 "errors": "password is not match"}
        #     status_code = status.HTTP_406_NOT_ACCEPTABLE


