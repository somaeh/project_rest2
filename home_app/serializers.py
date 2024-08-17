from rest_framework import serializers
from .models import Question, Answer


class Personserislizer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
    
class Questionserializer(serializers.ModelField):
    
    class Meta:
        model = Question
        fields = '__all__'
        
class Answerserializer(serializers.ModelSerializer):
    class Meta:
        
        model = Answer
        fields = '__all__'
    