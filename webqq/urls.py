# -*- coding:utf-8 -*-
__author__ = 'webber'
"""
此url为二级路由使用
"""
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='chat'),
    url(r'^send_msg/$', views.send_msg, name='chat_send_msg'),
    url(r'^get_msg/$', views.get_msg, name='get_new_msg'),
]