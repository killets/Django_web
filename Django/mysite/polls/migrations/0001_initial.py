# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='请输入公告内容', max_length=200)),
            ],
        ),
    ]