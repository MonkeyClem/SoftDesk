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

    def validate(self, data):
        user = data['user']
        project = data['project']
        role = data['role']

        if Contributor.objects.filter(user=user, project=project).exists():
            raise serializers.ValidationError("Cet utilisateur est déjà contributeur de ce projet.")

        if role == Contributor.AUTHOR:
            if Contributor.objects.filter(project=project, role=Contributor.AUTHOR).exists():
                raise serializers.ValidationError("Ce projet a déjà un auteur.")

        return data

    def create(self, validated_data):
        return Contributor.objects.create(**validated_data)



