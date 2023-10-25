from rest_framework.permissions import BasePermission


class StaffPermissionViewSet(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.is_staff and view.action in ['create', 'destroy']:
            return False
        return True


class SubscriptionPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True
        else:
            if view.action in ['create', 'destroy']:
                return True
            else:
                return False

