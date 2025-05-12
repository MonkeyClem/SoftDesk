from rest_framework import serializers  

from core.models.contributor import Contributor

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = [
            'id',
            'user',
            'project',
            'role',
            'created_time',
        ]
        read_only_fields = ['created_time']

    def create(self, validated_data):
        contributor = Contributor.objects.create(**validated_data)
        return contributor
