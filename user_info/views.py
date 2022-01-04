'''
Date                : 2021-12-12 18:39:40
LastEditors         : 王少帅
LastEditTime        : 2021-12-13 11:12:14
FilePath            : /drf_vue_blog/user_info/views.py
'''
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from user_info.serializers import UserRegisterSerializer
from user_info.permissions import IsSelfOrReadOnly


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly, IsSelfOrReadOnly]

        return super().get_permissions()