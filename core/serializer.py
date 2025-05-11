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
            'accept_to_share_data',
        ]
        extra_kwargs = {'password' : {'write_only' : True}}

    def create_user(self, validated_data) : 
        user = User.objects.create_user(**validated_data) 
        return user 