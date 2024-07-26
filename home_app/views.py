from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.views import View
from  rest_framework.response import Response

# @api_view(['GET'])
# def home(request):
#     return Response({'name':'haval'})
    
    
    
class Home(APIView):
    def get(self, request):
        return Response({'name':'haval'})
    def post(self, request):
        name = request.data['name']
        return Response({'name': name})
