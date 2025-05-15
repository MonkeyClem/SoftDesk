from rest_framework import serializers  
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer) : 
    can_be_contacted = serializers.BooleanField(required = True)
    accept_to_share_data = serializers.BooleanField(required = True)
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
        extra_kwargs = {'password' : {'write_only' : True}, 'email' : {'required' : True }}

    def create(self, validated_data) : 
        user = User.objects.create_user(**validated_data) 
        user.set_password(validated_data["password"])
        user.save()
        return user
        