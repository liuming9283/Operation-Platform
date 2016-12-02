#-*- coding:utf8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userinfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()

    def __unicode__(self):
        return self.username

class host(models.Model):
    """
    这张表本来定义了9个字段，但是有一个是外键，Django中，外键的字段会单独建立一张表，还有一个manytomany字段，这个manytomany
    字段会单独生成一张表，不在这个表中有所体现
    """
    name = models.CharField(max_length=64, unique=True)    #字段唯一，不能重复
    ip_addr = models.GenericIPAddressField(unique=True)    #IPv4和IPv6都支持    IPAddress只支持IPv4
    port = models.IntegerField(default=22)

    system_type_choice = (
        ("linux", "LINUX"),
        ("win32", "Windows")
    )       #元祖中，第一个字段为数据库中实际存储的内容，第二个字段为Django页面上显示的内容
    system_type = models.CharField(choices=system_type_choice, max_length=32)
    enable = models.BooleanField(default=True)
    idc = models.ForeignKey("IDC")   #外键，多对一关系，对应IDC表
    groups = models.ManyToManyField("HostGroup")  #对应HostGroup表，数据关联类型有三种：一对一，多对一，多对多
    online_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)   #每当用户创建一台主机，自动加入创建的日期

    def __unicode__(self):
        return self.name

class IDC(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name

class HostGroup(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name

class User_Profile(models.Model):
    user = models.OneToOneField(User)       #与Django自带的用户表一对一关联，实现继承
    name = models.CharField(max_length=64, unique=True)
    host_group = models.ManyToManyField("HostGroup", blank=True, null=True)   #关联组
    hosts = models.ManyToManyField("host", blank=True, null=True)   #关联主机

    friends = models.ManyToManyField('self', blank=True, related_name='my_friends')  #进行自关联需要指定related_name，与这个字段区分开
                                                                                    #symmetrical=False指定了非对称关系，默认为对称关系

    def __unicode__(self):
        return self.name
