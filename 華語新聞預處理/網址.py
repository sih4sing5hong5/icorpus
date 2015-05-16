# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


from 華語新聞預處理.介面 import 加新聞
from 華語新聞預處理.介面 import 全部新聞
from 華語新聞預處理.介面 import 看新聞
from 華語新聞預處理.介面 import 設定新聞狀態

urlpatterns = patterns('',
	
	url(r'^$', 全部新聞,name='新聞首頁'),
	url(r'^加新聞$', 加新聞,name='加新聞'),
	url(r'^看新聞/(?P<pk>\d+)$', 看新聞,name='看新聞'),
	url(r'^設定新聞狀態/(?P<pk>\d+)/(?P<狀態>.+)/$', 設定新聞狀態,name='設定新聞狀態'),
	url(r'^', 全部新聞,name='新聞首頁'),
	
)