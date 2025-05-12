from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, ContributorViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'projects', ProjectViewSet, basename="project")
router.register(r'contributors', ContributorViewSet, basename="contributor")

urlpatterns = router.urls
