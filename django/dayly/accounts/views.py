from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .forms import AccountUpdateForm


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AccountUpdateForm
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'accounts/edit_account.html'
    success_url = reverse_lazy('account-edit')

    def get_object(self):
        return self.request.user