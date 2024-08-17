from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import UserRegisterserializer
from django.contrib.auth.models import User
from rest_framework import status


class UserRegisterView(APIView):
    def post(self, request):
        ser_data = UserRegisterserializer(data=request.POST)
        if ser_data.is_valid():
            # User.objects.create_user(
            #     username=ser_data.validated_data['username'],
            #     email=ser_data.validated_data['email'],
            #     password=ser_data.validated_data['password'],

                
            # )
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)               #اظلاعات خود کاربر که ثبت نام کرده را به خود کاربر نمایش می دهد همون  اطلاعات که کاربر ارسال کرده بود را بر می گرداند
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
            