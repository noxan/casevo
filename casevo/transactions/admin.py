from django.contrib import admin

from casevo.transactions.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'source', 'target', 'value')


admin.site.register(Transaction, TransactionAdmin)
