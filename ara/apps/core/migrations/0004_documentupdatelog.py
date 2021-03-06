# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-18 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_documentvote'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentUpdateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 시간')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='삭제 시간')),
                ('previous_document', django_mysql.models.JSONField(default=dict, verbose_name='수정 이전 문서')),
                ('created_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='update_logs', to='core.Document', verbose_name='수정 대상 문서')),
            ],
            options={
                'verbose_name': '문서 수정 내역',
                'verbose_name_plural': '문서 수정 내역',
            },
        ),
    ]
