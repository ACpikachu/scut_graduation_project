'''
Date                : 2021-12-06 15:01:58
LastEditors         : 王少帅
LastEditTime        : 2021-12-06 18:16:52
FilePath            : /drf_vue_blog/article/admin.py
'''

from django.contrib import admin
from .models import Article

admin.site.register(Article)