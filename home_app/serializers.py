from rest_framework import serializers 
from .models import Question, Answer
from .custom_relational_fields import UserEmailNameRelatinalField


class Personserislizer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
    
class Questionserializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)
   
    
    class Meta:
        model = Question
        fields = '__all__'
        
    def get_answers(self, obj):
        result = obj.answers.all()
        return Answerserializer(instance=result, many=True).data
    
        
class Answerserializer(serializers.ModelSerializer):
    class Meta:
        
        model = Answer
        fields = '__all__'
    