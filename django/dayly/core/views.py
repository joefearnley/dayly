from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
            if self.request.user.is_authenticated:
                return HttpResponseRedirect(reverse('entries_index'))

            return super().get(request, *args, **kwargs)