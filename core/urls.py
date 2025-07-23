from rest_framework.routers import DefaultRouter
from core.views.comment import CommentViewSet
from core.views.project import ProjectViewSet
from core.views.issue import IssueViewSet
from core.views.contributor import ContributorViewSet
from core.views.user import UserViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'contributors', ContributorViewSet, basename='contributor')
router.register(r'issues', IssueViewSet, basename='issue')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
