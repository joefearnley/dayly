from django.views.generic import TemplateView, CreateView, UpdateView
from .models import Entry
from .forms import EntryForm


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

    def post(self, request, *args, **kwargs):
        form = EntryForm(request.POST)

        if form.is_valid():
            entry = form.save()
            entry.save()
            return HttpResponseRedirect(reverse_lazy('entries_index'))

        return render(request, 'entries/add_entry.html', {'form': form})

class EntryUpdateView(UpdateView):
    model = Entry
    fields = ['date_published', 'body']
    template_name = 'entries/edit_entry.html'
