# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-30 11:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app01', '0003_user_profile_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='QQgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('members_limit', models.IntegerField(default=200)),
                ('brief', models.TextField(default='nothing.......', max_length=1024)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_admins', to='app01.User_Profile')),
                ('founder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.User_Profile')),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_members', to='app01.User_Profile')),
            ],
        ),
    ]
