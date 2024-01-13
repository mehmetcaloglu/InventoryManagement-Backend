from rest_framework import permissions

class IsAuthenticated (permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class IsStoreManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class IsCentralOfficeEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class IsWarehouseEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated