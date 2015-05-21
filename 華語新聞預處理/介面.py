# -*- coding: utf-8 -*-
from 華語新聞預處理.models import 華語新聞表格
from django.shortcuts import redirect, render


from 華語新聞預處理.models import 華語新聞
from 文章.斷詞翻譯 import 斷詞

def 全部新聞(request):
	return render(request, '華語新聞/全部新聞.html', {
		'會使用的新聞': 華語新聞.objects.filter(狀態='猶未使用').order_by('-上尾修改時間')[:20],
		'用過的新聞': 華語新聞.objects.exclude(狀態='猶未使用').order_by('-上尾修改時間')[:20],
	})
	
def 加新聞(request):
	if request.method == 'POST':  # If the form has been submitted...
		新聞表格 = 華語新聞表格(request.POST)  # A form bound to the POST data
		if 新聞表格.is_valid():
			新聞=新聞表格.save()
			if 新聞.斷詞標題 == '':
				try:
					新聞.斷詞標題 = 斷詞(新聞.原本內容)
				except:
					pass
			if 新聞.斷詞內容 == '':
				try:
					新聞.斷詞內容 = 斷詞(新聞.原本內容)
				except:
					pass
			新聞.save()
			return redirect('新聞首頁')
	else:
		新聞表格 = 華語新聞表格()
	return render(request, '華語新聞/加新聞.html', {
		'新聞表格': 新聞表格,
	})
	
def 看新聞(request, pk):
	return render(request, '華語新聞/看新聞.html', {
		'新聞': 華語新聞.objects.get(pk=pk),
		'其他狀態': ['使用','傷長','語句無順',],
	})
	
def 設定新聞狀態(request, pk, 狀態):
	新聞=華語新聞.objects.get(pk=pk)
	新聞.狀態=狀態
	新聞.save()
	return redirect('新聞首頁')

