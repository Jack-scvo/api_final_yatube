from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение, не дающее зарегистрированному
    пользователю редактировать не свои объекты.
    """

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user or view.action == 'retrieve')
