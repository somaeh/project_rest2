from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.views import View
from  rest_framework.response import Response
from.models import Person
from.serializers import Personserislizer

# @api_view(['GET'])
# def home(request):
#     return Response({'name':'haval'})
    
    
    
class Home(APIView):
    def get(self, request):
        
        person = Person.objects.all()
        
        ser_data = Personserislizer(instance=person, many=True)
        
                                
        return Response(data=ser_data.data)
    
    
    
    # def post(self, request):
    #     name = request.data['name']
    #     return Response({'name': name})
