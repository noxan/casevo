from django.views.generic import ListView

from casevo.transactions.models import Transaction


class TransactionListView(ListView):
    model = Transaction
