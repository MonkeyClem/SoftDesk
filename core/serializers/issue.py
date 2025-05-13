from rest_framework import serializers
from core.models import Issue  # adapte ce chemin selon ta structure

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'description',
            'tag',
            'priority',
            'status',
            'project',
            'author',
            'assignee',
            'created_time',
        ]
        read_only_fields = ['author', 'created_time']
