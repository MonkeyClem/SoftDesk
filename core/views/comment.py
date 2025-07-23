
from core.models.issue import Issue
from core.permissions import permissions
from core.serializers.comment import CommentSerializer
from rest_framework.viewsets import ModelViewSet
from core.models.comment import Comment
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

class CommentViewSet(ModelViewSet): 
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, permissions.IsCommentAuthorOrReadOnly]

    def get_queryset(self): 
        user = self.request.user 
        return Comment.objects.filter(issue__project__contributors__user=user).distinct()


    def perform_create(self, serializer):
        user = self.request.user 
        issue = self.request.data.get("issue")
        try:
            issue_obj = Issue.objects.get(pk=issue)
        except Issue.DoesNotExist:
            raise PermissionDenied("L’issue spécifiée est introuvable.")

        # Vérifie que l'utilisateur est contributeur du projet
        if not issue_obj.project.contributors.filter(user=user).exists():
            raise PermissionDenied("Vous devez être contributeur du projet pour commenter cette issue.")

        serializer.save(author=user, issue=issue_obj)


