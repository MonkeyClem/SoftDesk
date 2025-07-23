from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from core.permissions.permissions import IsAuthorOrReadOnly, IsContributorForProject, IsProjectAuthorForContributor
from .serializer import UserSerializer
from .serializers.contributor import ContributorSerializer
from rest_framework import permissions
from core.models.issue import Issue
from core.models import Contributor, Comment, Project
from core.serializers.issue import IssueSerializer
from .serializers.comment import CommentSerializer
from rest_framework.exceptions import PermissionDenied
from .permissions import IsCommentAuthorOrReadOnly

# User = get_user_model()
# class UserViewSet(ModelViewSet): 
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny] 


# class CommentViewSet(ModelViewSet): 
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticated, IsCommentAuthorOrReadOnly]

#     def get_queryset(self): 
#         user = self.request.user 
#         return Comment.objects.filter(issue__project__contributors__user=user).distinct()


#     def perform_create(self, serializer):
#         user = self.request.user 
#         issue = self.request.data.get("issue")
#         try:
#             issue_obj = Issue.objects.get(pk=issue)
#         except Issue.DoesNotExist:
#             raise PermissionDenied("L’issue spécifiée est introuvable.")

#         # Vérifie que l'utilisateur est contributeur du projet
#         if not issue_obj.project.contributors.filter(user=user).exists():
#             raise PermissionDenied("Vous devez être contributeur du projet pour commenter cette issue.")

#         serializer.save(author=user, issue=issue_obj)


