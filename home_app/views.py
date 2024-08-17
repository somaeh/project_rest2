from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.views import View
from  rest_framework.response import Response
from.models import Person, Question, Answer
from.serializers import Personserislizer, Questionserializer, Answerserializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

# @api_view(['GET'])
# def home(request):
#     return Response({'name':'haval'})
    
    
    
class Home(APIView):
    # permission_classes = [IsAuthenticated,]
    permission_classes = [IsAdminUser,]
    
    def get(self, request):
        
        person = Person.objects.all()
        
        ser_data = Personserislizer(instance=person, many=True)
        
                                
        return Response(data=ser_data.data)
    
    
    
    # def post(self, request):
    #     name = request.data['name']
    #     return Response({'name': name})
    
    
class QuestionView(APIView):
    def get(self, request):
        
        questions = Question.objects.all()
        serz_data = Questionserializer(instance=questions, many=True)
        return Response(serz_data.data, status=status.HTTP_200_OK)
        
        
