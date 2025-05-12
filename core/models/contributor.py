from django.db import models
from django.conf import settings
from .projects import Project

class Contributor(models.Model): 
    AUTHOR = 'AUTHOR'
    CONTRIBUTOR = "CONTRIBUTOR"

    ROLES = [
        (AUTHOR, "Author"),
        (CONTRIBUTOR, "Contributor")
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributions",
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="contributors"
    )

    role = models.CharField(max_length=20, choices=ROLES, default='CONTRIBUTOR')    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.project.title} - ({self.role})"