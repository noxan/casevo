from django.views.generic import ListView

from casevo.transactions.models import Transaction


class TransactionListView(ListView):
    def get_queryset(self):
        return Transaction.objects.select_related().all()
