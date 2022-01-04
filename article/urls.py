'''
Date                : 2021-12-06 14:49:42
LastEditors         : 王少帅
LastEditTime        : 2021-12-06 19:52:55
FilePath            : /drf_vue_blog/article/urls.py
'''
from django.urls import path
from article import views

app_name = 'article'
urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
]