from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from core.serializer import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.exceptions import PermissionDenied

User = get_user_model()
class UserViewSet(ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 

    def get_queryset(self):
        return User.objects.filter(accept_to_share_data=True)

    def destroy(self, request, *args, **kwargs):
        # Empêche la suppression d'autres comptes
        if int(kwargs["pk"]) != request.user.id:
            raise PermissionDenied("Vous ne pouvez supprimer que votre propre compte.")
        return super().destroy(request, *args, **kwargs)
