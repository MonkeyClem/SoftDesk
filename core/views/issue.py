from core.models.contributor import Contributor
from core.models.issue import Issue
from core.permissions.permissions import IsContributorForProject
from core.serializers.issue import IssueSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsContributorForProject]

    def get_queryset(self):
        user = self.request.user
        project_ids = Contributor.objects.filter(user=user).values_list('project_id', flat=True)
        return Issue.objects.filter(project__id__in=project_ids).order_by("-created_time")
    
    def perform_create(self, serializer) : 
        user = self.request.user
        project = serializer.validated_data['project']
        assignee = serializer.validated_data['assignee']

        if not Contributor.objects.filter(user=user, project=project):
            raise PermissionDenied("Only a contributor can create issues for a project")

        if assignee and not Contributor.objects.filter(user=assignee, project=project).exists():
            raise PermissionDenied("The assignee must be a contributor of this project.")

        serializer.save(author=self.request.user)

