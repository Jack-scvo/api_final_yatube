from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение,
    позволяющее неаутенфицированному пользователю только читать и,
    не дающее зарегистрированному редактировать не свои объекты.
    """
    def has_permission(self, request, view):
        return (
            (request.method in permissions.SAFE_METHODS)
            or (request.user.is_authenticated)
        )

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user or view.action == 'retrieve')
