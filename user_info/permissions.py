'''
Date                : 2021-12-12 18:27:35
LastEditors         : 王少帅
LastEditTime        : 2021-12-12 18:51:45
FilePath            : /drf_vue_blog/user_info/permissions.py
'''
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSelfOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj == request.user