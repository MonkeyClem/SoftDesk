from django.conf import settings
from django.db import models
from core.models.project import Project

class Contributor(models.Model): 
    AUTHOR = 'AUTHOR'
    CONTRIBUTOR = 'CONTRIBUTOR'

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

    role = models.CharField(max_length=20, choices=ROLES, default=CONTRIBUTOR)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'project')  # ✅ Empêche les doublons
        verbose_name = "Contributor"
        verbose_name_plural = "Contributors"

    def __str__(self):
        return f"{self.user.username} → {self.project.title} ({self.role})"
