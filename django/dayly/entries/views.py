from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
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
    fields = ['date_published', 'body']
    template_name = 'entries/add_entry.html'
    success_url = reverse_lazy('entries_index')

    def form_valid(self, form):
        self.object = Entry.objects.create(
            date_published=form.cleaned_data['date_published'],
            body=form.cleaned_data['body'],
            user=self.request.user
        )

        messages.success(self.request, 'Entry Added Successfully.')

        return HttpResponseRedirect(self.get_success_url())

class EntryUpdateView(UpdateView):
    model = Entry
    fields = ['date_published', 'body']
    template_name = 'entries/edit_entry.html'
