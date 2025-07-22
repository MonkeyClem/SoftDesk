from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from core.permissions.permissions import IsContributorForProject, IsProjectAuthorForContributor
from .serializer import UserSerializer
from .serializers.project import ProjectSerializer
from .serializers.contributor import ContributorSerializer
from rest_framework import permissions
from core.models.issue import Issue
from core.models import Contributor, Comment, Project
from core.serializers.issue import IssueSerializer
from .serializers.comment import CommentSerializer
from rest_framework.exceptions import PermissionDenied
from .permissions import IsCommentAuthorOrReadOnly

User = get_user_model()
class UserViewSet(ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Seul l'auteur peut modifier ou supprimer le projet.
    Tous les contributeurs peuvent lire.
    """

    def has_object_permission(self, request, view, obj):
        # Lecture : autorisé à tous les contributeurs
        if request.method in permissions.SAFE_METHODS:
            return True
        # Écriture : seulement l'auteur
        return obj.author == request.user

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

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

class ContributorViewSet(ModelViewSet): 
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectAuthorForContributor]

    def get_queryset(self):
        user = self.request.user
        return Contributor.objects.filter(project__author=user)

    def perform_create(self, serializer) : 
        project = serializer.validated_data["project"]
        if project.author != self.request.user:
            raise PermissionDenied("Only the project author can add contributors.")
        serializer.save()
    
class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, IsContributorForProject]

    def get_queryset(self):
        user = self.request.user
        project_ids = Contributor.objects.filter(user=user).values_list('project_id', flat=True)
        return Issue.objects.filter(project__id__in=project_ids).order_by("-created_time")
    
    def perform_create(self, serializer) : 
        print("\n \n  Perfom Create Isue \n \n")
        user = self.request.user
        project = serializer.validated_data['project']
        assignee = serializer.validated_data['assignee']

        if not Contributor.objects.filter(user=user, project=project):
            raise PermissionDenied("Only a contributor can create issues for a project")

        if assignee and not Contributor.objects.filter(user=assignee, project=project).exists():
            raise PermissionDenied("The assignee must be a contributor of this project.")

        serializer.save(author=self.request.user)



class CommentViewSet(ModelViewSet): 
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsCommentAuthorOrReadOnly]

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


