from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializer import UserSerializer
from .serializers.project import ProjectSerializer
from .serializers.contributor import ContributorSerializer
from rest_framework import permissions
from core.models.issue import Issue
from core.serializers.issue import IssueSerializer
from .serializers.comment import CommentSerializer
from rest_framework.exceptions import PermissionDenied
from .permissions import isCommentAuthorOrReadOnly
from models import Project, Contributor, Issue, Comment

## TO DO : See why the import certain serializers does not work
from serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
# Create your views here.

User = get_user_model()

class UserViewSet(ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    
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
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    def perform_create(self, serializer) : 
        project = serializer.validated_data["project"]
        if project.author != self.request.user:
            raise PermissionDenied("Only the project author can add contributors.")
        serializer.save()
    
class IssueViewSet(ModelViewSet):
    # queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]
    # def perform_create(self, serializer):
    #     print("Perfom Create running")
    #     try :
    #         serializer.save(author=self.request.user)
    #     except Exception as e:
    #         print("\n \n \nSAVE FAILED:", e, "\n \n")
    #         raise

    def get_queryset(self):
        user = self.request.user
        project_ids = Contributor.objects.filter(user=user).values_list('project_id', flat=True)
        return Issue.objects.filter(project__id__in=project_ids).order_by("-created_time")
    
    def perform_create(self, serializer) : 
        print("\n \n \n \n Perfom Create running")
        user = self.request.user
        project = serializer.validated_data['project']
        assignee = serializer.validated_data['assignee']

        if not Contributor.objects.filter(user=user, project = project): 
            raise PermissionDenied("Only a contributor can create issues for a project")
        
        if assignee and not Contributor.objects.filter(user=assignee, project=project).exists() : 
            raise PermissionDenied("The assignee must be a contributor of this project.")
        
        serializer.save(author = self.request.user)
        
     

class CommentViewSet(ModelViewSet): 
    # queryset = Comment.objects.all()
    def get_queryset(self): 
        user = self.request.user 
        return Comment.objects.filter(issue__project__contributors__user=user).distinct()

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, isCommentAuthorOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user 
        # issue = serializer.validated_data.get("issue")
        issue = self.request.data.get("issue")
        # is_contributor = issue.project.contributors.filter(user = user)
        # if not is_contributor : 
        #     PermissionDenied("Only contributors can add comment")
        # On vérifie que l'issue existe
        try:
            issue_obj = Issue.objects.get(pk=issue)
        except Issue.DoesNotExist:
            raise PermissionDenied("L’issue spécifiée est introuvable.")

        # Vérifie que l'utilisateur est contributeur du projet
        if not issue_obj.project.contributors.filter(user=user).exists():
            raise PermissionDenied("Vous devez être contributeur du projet pour commenter cette issue.")

        serializer.save(author=user, issue=issue_obj)

        # serializer.save(author=User.objects.first())  

