from django.conf.urls import patterns, url

from 文章 import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^文章/$', views.index),
    url(r'^登入', views.登入, name='登入'),
    url(r'^登出$', views.登出, name='登出'),
    # ex: /polls/5/
    url(r'^(?P<pk>\d+)/看文章/$', views.看文章, name='看文章'),
    url(r'^(?P<pk>\d+)/全改/$', views.全改, name='全改'),
    url(r'^加新文章', views.加新文章, name='加新文章'),
    url(r'^(?P<pk>\d+)/改分類佮原文/$', views.改分類佮原文, name='改分類佮原文'),
    url(r'^(?P<pk>\d+)/改國語斷詞/$', views.改國語斷詞, name='改國語斷詞'),
    url(r'^(?P<pk>\d+)/改閩南語翻譯/$', views.改閩南語翻譯, name='改閩南語翻譯'),
    
    url(r'^揣文章$', views.揣文章, name='揣文章'),
    
    url(r'^.*$', views.index, name='首頁'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
#     url(r'^(?P<pk>\d+)/editclass/$', views.EditView.as_view(), name='editClass'),
#     # ex: /polls/5/results/
#     url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
#     url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)