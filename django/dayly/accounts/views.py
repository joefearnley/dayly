from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .forms import AccountUpdateForm


class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = AccountUpdateForm
    template_name = 'accounts/edit_account.html'
    success_url = reverse_lazy('account-edit')
    success_message = _('Account updated successfully')

    def get_object(self):
        return self.request.user