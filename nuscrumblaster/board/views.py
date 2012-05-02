from django.views.generic.base import TemplateView
from django.http import Http404

from api import v1


class IndexView(TemplateView):
    template_name = 'index.html'
