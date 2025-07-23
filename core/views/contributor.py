
from core import permissions
from rest_framework.permissions import IsAuthenticated
from core.models.contributor import Contributor
from core.permissions.permissions import IsProjectAuthorForContributor
from core.serializers.contributor import ContributorSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied


class ContributorViewSet(ModelViewSet): 
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsProjectAuthorForContributor]

    def get_queryset(self):
        user = self.request.user
        return Contributor.objects.filter(project__author=user)

    def perform_create(self, serializer) : 
        project = serializer.validated_data["project"]
        if project.author != self.request.user:
            raise PermissionDenied("Only the project author can add contributors.")
        serializer.save()
    
