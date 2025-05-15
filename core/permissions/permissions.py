from rest_framework import permissions

class isCommentAuthorOrReadOnly(permissions.BasePermission) :
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Pour écrire, l'utilisateur doit être l'auteur
        return obj.author == request.user