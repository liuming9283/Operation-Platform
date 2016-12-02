from __future__ import unicode_literals

from django.db import models
from app01 import models as my_models

# Create your models here.

class QQgroup(models.Model):
    name = models.CharField(max_length=64)
    founder = models.ForeignKey(my_models.User_Profile)
    admin = models.ForeignKey(my_models.User_Profile, related_name='group_admins')
    members = models.ForeignKey(my_models.User_Profile, related_name='group_members')
    members_limit = models.IntegerField(default=200)
    brief = models.TextField(max_length=1024, default="nothing.......")
    def __unicode__(self):
        return self.name