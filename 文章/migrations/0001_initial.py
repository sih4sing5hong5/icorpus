# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='何澤政文章',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('頭一擺翻譯時間', models.DateField(auto_now_add=True)),
                ('上尾修改時間', models.DateField(auto_now=True)),
                ('分類', models.CharField(max_length=100)),
                ('原本標題', models.CharField(max_length=255)),
                ('原本內容', models.TextField()),
                ('斷詞標題', models.CharField(blank=True, max_length=255)),
                ('斷詞內容', models.TextField(blank=True)),
                ('教羅標題', models.CharField(blank=True, max_length=255)),
                ('教羅內容', models.TextField(blank=True)),
            ],
        ),
    ]
