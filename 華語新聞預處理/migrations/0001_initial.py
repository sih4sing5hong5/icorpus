# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='華語新聞',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('頭一擺翻譯時間', models.DateField(auto_now_add=True)),
                ('上尾修改時間', models.DateField(auto_now=True)),
                ('原本標題', models.CharField(max_length=255)),
                ('原本內容', models.TextField()),
                ('斷詞標題', models.CharField(blank=True, max_length=255)),
                ('斷詞內容', models.TextField(blank=True)),
                ('狀態', models.CharField(default='猶未使用', choices=[('猶未使用', '猶未使用'), ('使用', '使用'), ('傷長', '傷長'), ('語句無順', '語句無順')], max_length=20)),
            ],
        ),
    ]
