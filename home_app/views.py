from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.views import View
from  rest_framework.response import Response
from.models import Person, Question, Answer
from.serializers import Personserislizer, Questionserializer, Answerserializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from permisstions import IsOwnerorReadonly


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
    
    
class QuestionListView(APIView):
    def get(self, request):
        
        questions = Question.objects.all()
        srz_data = Questionserializer(instance=questions, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)
    
      
class QuestionCreateView(APIView):
    
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        srz_data = Questionserializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class QuestionUpdateView(APIView):
    permission_classes =[IsOwnerorReadonly,]
    
    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        srz_data = Questionserializer(instance=question, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class QuestionDeleteView(APIView):
     permission_classes =[IsOwnerorReadonly,]
     
     def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message': 'question deleted'}, status=status.HTTP_200_OK)
    
    
        


        
        
