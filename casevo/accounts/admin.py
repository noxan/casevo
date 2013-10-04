from django.contrib import admin

from casevo.accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'currency')


admin.site.register(Account, AccountAdmin)
