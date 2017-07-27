# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-27 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_face', models.CharField(max_length=300)),
                ('first_choice', models.CharField(max_length=50)),
                ('second_choice', models.CharField(max_length=50)),
                ('third_choice', models.CharField(max_length=50)),
                ('fourth_choice', models.CharField(max_length=50)),
                ('difficulty', models.IntegerField()),
            ],
        ),
    ]
