from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from core.serializer import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()
class UserViewSet(ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 
