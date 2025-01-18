from django.views.generic import TemplateView
from .models import Entry


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entries'] = Entry.objects.all()[:5]
        return context
