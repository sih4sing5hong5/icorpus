from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^新聞/', include('華語新聞預處理.網址')),
    url(r'^', include('文章.urls')),
)
