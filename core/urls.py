from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
# router.register(r'projects', ProjectViewSet, basename="project")
# router.register(r'contributors', ContributorViewSet, basename="contributor")
# router.register(r'issues', IssueViewSet, basename='issue')
# router.register(r'comments', CommentViewSet, basename='comment')

# urlpatterns = router.urls


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    ProjectViewSet,
    ContributorViewSet,
    IssueViewSet,
    CommentViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'contributors', ContributorViewSet, basename='contributor')
router.register(r'issues', IssueViewSet, basename='issue')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
