# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-18 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
        ('core', '0002_auto_20170316_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 시간')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='삭제 시간')),
                ('is_up', models.BooleanField(verbose_name='투표 내용')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='session.UserProfile', verbose_name='작성자')),
                ('created_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='core.Document', verbose_name='상위 문서')),
            ],
            options={
                'verbose_name': '문서 투표',
                'verbose_name_plural': '문서 투표',
            },
        ),
    ]