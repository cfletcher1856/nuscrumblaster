from django.views.generic.base import TemplateView
from django.http import Http404
from django.contrib.auth.models import User

from api import v1


class IndexView(TemplateView):
    template_name = 'index.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        ctx = super(ProfileView, self).get_context_data(**kwargs)

        user = User.objects.get(username=self.kwargs.get('pk', None))

        ctx.update(user=user)
        return ctx
