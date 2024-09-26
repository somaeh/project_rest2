from rest_framework import serializers
from django.contrib.auth.models import User

#required یعنی پر کردن این فیلدها اجباری است

def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('admin cant be in email')
    
class UserRegisterserializer(serializers.ModelSerializer):
    # username = serializers.CharField(required=True)
    # email = serializers.EmailField(required=True, validators=[clean_email])
    # password = serializers.CharField(required=True, write_only=True)
    # password2 = serializers.CharField(required=True,  write_only=True)
    password2 = serializers.CharField(write_only =True, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
    extra_kwargs = {
        'password': {'write_only':True},
        'email':{'validators':(clean_email,)}
    }
    
    def create(self, validated_data):   # کاربر را ایجاد می کنیم
        del validated_data['password2']
        return User.objects.create_user(**validated_data)
        
    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('you canit writ admin')
        return value
    
    
    # def validate_password(self, data):
    #     if data['password'] != data['password2']:
    #         raise serializers.ValidationError('password must match')
    #     return data
    
    
class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'