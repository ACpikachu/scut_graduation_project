'''
Date                : 2021-12-11 19:53:09
LastEditors         : 王少帅
LastEditTime        : 2021-12-11 21:41:16
FilePath            : /drf_vue_blog/comment/views.py
'''
from django.shortcuts import render

from rest_framework import viewsets

from comment.models import Comment
from comment.serializers import CommentSerializer
from comment.permissions import IsOwnerOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)