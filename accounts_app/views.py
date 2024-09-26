from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import UserRegisterserializer
from accounts_app.serializers import Userserializers
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

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
    
    
class UserViewSet(viewsets.ViewSet):
    Permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    
    def list(self, request):            # retern allusername informations
        serz_data = Userserializers(instance=self.queryset, many=True)
        return Response(serz_data.data)
        
        
    def retrieve(self, request, pk=None):    #only return one object
        user = get_object_or_404(self.queryset, pk=pk)
        serz_data = Userserializers(instance=user)
        return Response(data=serz_data.data)
    
    def partial_update(self, request, pk=None):
        
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({'permitions denide': 'you are not woner'})
        srez_data = Userserializers(instance=user, data=request.POSt, partial=True)
        if srez_data.is_valid():
            srez_data.save()
            return Response(data=srez_data.data)
        return Response(data=srez_data.errors)
        
        
    
    def destroy(self, request, pk=None):
       user = get_object_or_404(self.queryset, pk=pk)
       if user != request.user:
           return Response({'permitions denide': 'you are ont owner'})
       user.is_active = False
       user.save()
       return Response({'message': 'user deactivaded'})