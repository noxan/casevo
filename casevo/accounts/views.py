from django.views.generic import UpdateView, ListView
from django.core.urlresolvers import reverse_lazy

from casevo.accounts.models import Account


class AccountListView(ListView):
    def get_queryset(self):
        return Account.objects.select_related('transactions_out', 'transactions_in').all()


class AccountUpdateView(UpdateView):
    model = Account
    template_name = 'accounts/account_update.html'
    success_url = reverse_lazy('accounts:list')
