from rest_framework import serializers
from ..models import Comment
class CommentSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Comment 
        fields = [
            'id',
            'description',
            'author',
            'issue',
            'created_time'
        ]

        read_only_fields = ['author', 'created_time']