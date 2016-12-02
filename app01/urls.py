# -*- coding:utf-8 -*-
__author__ = 'webber'
"""
此url为二级路由使用
"""
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^index/', views.index),
]