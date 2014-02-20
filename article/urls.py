from django.conf.urls import patterns, url

from article import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>\d+)/edit/$', views.edit, name='改'),
    url(r'^(?P<pk>\d+)/看/$', views.Results.as_view(), name='看'),
    
#     # ex: /polls/5/vote/
#     url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
#     url(r'^(?P<pk>\d+)/editclass/$', views.EditView.as_view(), name='editClass'),
#     # ex: /polls/5/results/
#     url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
#     url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)