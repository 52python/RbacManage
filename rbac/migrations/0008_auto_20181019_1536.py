# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-10-19 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0007_auto_20181019_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=32, unique=True, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(unique=True, verbose_name='\u624b\u673a\u53f7\u7801'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32, unique=True, verbose_name='\u7528\u6237\u540d'),
        ),
    ]
