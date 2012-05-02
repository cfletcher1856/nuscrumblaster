from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django import template

template.add_to_builtins('django.contrib.staticfiles.templatetags.staticfiles')

admin.autodiscover()

urlpatterns = patterns('',
    (r'', include('nuscrumblaster.board.urls')),
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += staticfiles_urlpatterns()
