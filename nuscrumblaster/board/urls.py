from django.conf.urls.defaults import patterns, url, include

from nuscrumblaster.board.api import v1
from nuscrumblaster.board.views import IndexView

urlpatterns = patterns('',
    (r'^', include('registration.backends.default.urls')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^api/', include(v1.urls)),
)
