from rest_framework import serializers  
from core.models.project import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'type',
            'author',
            'created_time'
        ]

        read_only_fields=['created_time']
        
    def create_project(self, validated_data) : 
        project = Project.objects.create(**validated_data)
        return project 