from django.conf.urls.defaults import patterns, url, include

from nuscrumblaster.board.api import v1
from nuscrumblaster.board.views import IndexView, ProfileView

urlpatterns = patterns('',
    (r'^', include('registration.backends.default.urls')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^api/', include(v1.urls)),
    url(r'^profile/(?P<pk>[a-zA-Z0-9\-]+)/$', ProfileView.as_view(), name='profile'),
    (r'^search/', include('haystack.urls')),
)
