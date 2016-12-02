#-*- coding:utf-8 -*-
from django.test import TestCase
# Create your tests here.
# 要允许此模块需要配置环境变量，否则只能在python manage.py test的shell中执行
import models

# models.User.objects.filter(id=4).delete()

print models.User.objects.filter( username='webb')
if len(models.User.objects.filter( username='webb')) == 0:
    print "1111"