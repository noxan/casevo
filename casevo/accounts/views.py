from django.views.generic import ListView

from casevo.accounts.models import Account


class AccountListView(ListView):
    model = Account
