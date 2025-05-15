# Register your models here.
from django.contrib import admin
from .models import User, Issue, Comment, Contributor, Project

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)
admin.site.register(Contributor)
