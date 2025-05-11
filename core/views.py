from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializer import UserSerializer
# Create your views here.

User = get_user_model()

class UserViewSet(ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
