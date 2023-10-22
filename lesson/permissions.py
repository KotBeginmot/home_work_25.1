from rest_framework.permissions import BasePermission


class StaffPermission(BasePermission):
    def has_permission(self, request, view):

        if request.user.is_staff and view.action in ['create', 'destroy']:
            return False
        return True



class ObjPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_staff or not request.user.is_superuser:
            if obj.id in [i.id for i in request.user.lesson.all()]:
                return True
        else:
            return True
        return False

