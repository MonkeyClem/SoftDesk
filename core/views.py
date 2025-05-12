from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializer import UserSerializer
from .models.project import Project
from .models.contributor import Contributor
from .serializers.project import ProjectSerializer
from .serializers.contributor import ContributorSerializer
# Create your views here.

User = get_user_model()

class UserViewSet(ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ContributorViewSet(ModelViewSet): 
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    