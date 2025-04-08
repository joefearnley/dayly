from datetime import datetime
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.http import  JsonResponse
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView
from .models import Entry
import markdown


class IndexView(TemplateView):
    template_name = 'entries/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_entries = Entry.objects.filter(user=self.request.user).order_by('-date_published');
        context['entries'] = []
    
        for entry in user_entries:
            entry.body = markdown.markdown(entry.body)
            context['entries'].append(entry)

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
            slug=form.cleaned_data['date_published'].strftime('%Y-%m-%d'),
            user=self.request.user
        )

        messages.success(self.request, 'Entry Successfully Added.')

        return HttpResponseRedirect(self.get_success_url())

class EntryUpdateView(UpdateView):
    model = Entry
    fields = ['date_published', 'body']
    template_name = 'entries/edit_entry.html'
    success_url = reverse_lazy('entries_index')


class EntryDeleteView(DeleteView):
    model = Entry
    fields = ['date_published', 'body']
    template_name = 'entries/edit_entry.html'
    success_url = reverse_lazy('entries_index')
    success_message = 'Entry successfully deleted.'


class EntryView(DetailView):
    model = Entry
    template_name = 'entries/view_entry.html'


class EntryPreviewView(View):
    def get(self, request, *args, **kwargs):
        entry_body = request.GET.get('body', '')
        entry_date = request.GET.get('date', '')

        html = markdown.markdown(entry_body)
        title = datetime.fromisoformat(entry_date).strftime('%m/%d/%Y')

        response = {
            'title': title,
            'body': html
        }

        return JsonResponse(response)
