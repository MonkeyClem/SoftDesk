from django.db import models
from django.conf import settings
from .project import Project
from.contributor import Contributor
from .user import User

class Issue(models.Model) : 

    class Tag(models.TextChoices) : 
        BUG = 'BUG', 'Bug'
        FEATURE = 'FEATURE', 'Feature'
        TASK = 'TASK', 'TASK'

    class Priority(models.TextChoices) :
        LOW = 'LOW', 'Low', 
        MEDIUM = 'MEDIUM', 'Medium', 
        HIGH = 'HIGH', 'High'

    class Status(models.TextChoices) : 
        TODO = 'TODO', 'To Do', 
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress',
        FINISHED = 'FINISHED', 'Finished'


#  Un contributeur qui travaille sur un projet doit pouvoir créer des Issues
# (tâches/problèmes). Ces issues permettent de planifier des fonctionnalités à
# mettre en œuvre ou des bugs à régler dans un projet donné.
# - Lors de la création de l’issue, le contributeur doit pouvoir la nommer et ajouter
# une description. Il doit aussi pouvoir assigner l’issue à un autre contributeur s’il
# le souhaite. Attention, seuls les contributeurs du projet correspondant à l’issue
# sont sélectionnables
    title = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=1024, blank=False)
    tag = models.CharField(max_length=16 , choices=Tag.choices, default=Tag.TASK)
    priority = models.CharField(max_length=16, choices=Priority.choices)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.TODO)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="issues")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="created_issues")
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='assigned_issues')

    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - status : {self.status}"