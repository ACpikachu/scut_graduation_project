'''
Date                : 2021-12-06 17:52:55
LastEditors         : 王少帅
LastEditTime        : 2021-12-28 19:48:29
FilePath            : /drf_vue_blog/drf_vue_blog/urls.py
'''

"""drf_vue_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)
from article import views

from comment.views import CommentViewSet
from user_info.views import UserViewSet

router = DefaultRouter()
router.register(r'tag', views.TagViewSet)
router.register(r'article', views.ArticleViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'avatar', views.AvatarViewSet)
router.register(r'user', UserViewSet)
router.register(r'comment', CommentViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 可视化登陆入口
    path('api-auth/', include('rest_framework.urls')),
    
    # # 文章查看界面
    # path('api/article/', include('article.urls', namespace='article'))
    
    path('api/', include(router.urls)),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)