# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-27 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_question_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diff1count', models.IntegerField()),
                ('diff2count', models.IntegerField()),
                ('diff3count', models.IntegerField()),
                ('diff4count', models.IntegerField()),
                ('diff5count', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='course.Course')),
                ('questions', models.ManyToManyField(related_name='exams', to='course.Question')),
            ],
        ),
    ]
