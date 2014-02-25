from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^文章/', include('文章.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
