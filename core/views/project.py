from core.models.contributor import Contributor
from core.models.project import Project
from core.permissions.permissions import IsAuthorOrReadOnly
from core.serializers.project import ProjectSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(
            contributors__user=user
        ).distinct()
    
    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(
            user=self.request.user,
            project=project,
            role=Contributor.AUTHOR
        )