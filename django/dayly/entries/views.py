from django.views.generic import TemplateView, CreateView, UpdateView
from .models import Entry


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entries'] = Entry.objects.all()[:5]
        return context


class EntryCreateView(CreateView):
    model = Entry
    fields = ['title', 'body']
    template_name = 'entries/add_entry.html'


class EntryUpdateView(UpdateView):
    model = Entry
    fields = ['title', 'body']
    template_name = 'entries/edit_entry.html'
