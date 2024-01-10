from rest_framework import permissions

class IsAuthenticated (permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class IsStoreManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'store_manager'

class IsCentralOfficeEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'central_office_employee'

class IsWarehouseEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'warehouse_employee' 