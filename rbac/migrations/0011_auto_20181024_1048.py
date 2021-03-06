# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-10-24 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0010_user_flag_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='flag',
            field=models.IntegerField(default=0, help_text='\u9ed8\u8ba40,0\u4ee3\u8868\u542f\u7528,1\u4ee3\u8868\u7981\u7528'),
        ),
        migrations.AlterField(
            model_name='role',
            name='flag',
            field=models.IntegerField(default=0, help_text='\u9ed8\u8ba40,0\u4ee3\u8868\u542f\u7528,1\u4ee3\u8868\u7981\u7528'),
        ),
        migrations.AlterField(
            model_name='user',
            name='flag_delete',
            field=models.IntegerField(default=0, help_text='\u9ed8\u8ba40,0\u4ee3\u8868\u6b63\u5e38\u7528\u6237,1\u4ee3\u8868\u5df2\u5220\u9664\u7528\u6237,'),
        ),
    ]
