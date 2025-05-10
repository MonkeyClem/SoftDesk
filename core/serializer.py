from rest_framework import serializers  
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
            'age',
            'can_be_contacted',
            'can_data_be_shared',
        ]
        extraKwargs = {'password' : {'write_only' : True}}

    def create_user(self, validated_data) : 
        user = User.objects.create_user(**validated_data) 
        return user 