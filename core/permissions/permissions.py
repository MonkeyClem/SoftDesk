from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Seul l'auteur peut modifier ou supprimer le projet.
    Tous les contributeurs peuvent lire.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Écriture : seulement l'auteur
        return obj.author == request.user


class IsCommentAuthorOrReadOnly(permissions.BasePermission) :
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Pour écrire, l'utilisateur doit être l'auteur
        return obj.author == request.user

class IsProjectAuthorForContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.project.author == request.user


class IsContributorForProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.project.contributors.filter(user=user).exists()