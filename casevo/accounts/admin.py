from django.contrib import admin

from casevo.accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'number', 'blz', 'currency')
    search_fields = ['identifier']


admin.site.register(Account, AccountAdmin)
