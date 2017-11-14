# -*- coding: utf-8 -*-
import json

from django.core.management.base import BaseCommand
from 文章.models import 何澤政文章
from 文章.轉出 import 對應資料


class Command(BaseCommand):

    def handle(self, *args, **參數):
        全部文章 = []
        for 文章 in 何澤政文章.objects.order_by('pk'):
            全部文章.append(對應資料(文章))
        with open('icorpus.json', 'w') as 檔案:
            json.dump(
                全部文章, 檔案,
                ensure_ascii=False, sort_keys=True, indent=2,
            )
