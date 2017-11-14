from django.http import HttpResponse
from 文章.models import 何澤政文章
import json
from 文章.文章整理 import 文章整理
__文章整理 = 文章整理()


def 轉網頁(物件):
    return HttpResponse(json.dumps(物件))


def 全部文號(request):
    文號 = []
    for 文章 in 何澤政文章.objects.order_by('pk'):
        文號.append(文章.pk)
    return 轉網頁(文號)


def 揣翻譯對應(request, pk):
    文章 = 何澤政文章.objects.get(pk=pk)
    return 轉網頁(對應資料(文章))


def 對應資料(文章):
    國語 = __文章整理.轉文章空白(文章.斷詞標題 + '\n' + 文章.斷詞內容)
    閩南語 = __文章整理.轉文章空白(文章.教羅標題 + '\n' + 文章.教羅內容)
    return {
        '文號': 文章.pk, '日期': str(文章.上尾修改時間),
        '華語': 國語, '閩南語': 閩南語
    }
