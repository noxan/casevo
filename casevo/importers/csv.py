from datetime import datetime
from decimal import Decimal

from currencies.models import Currency

from casevo.accounts.models import Account
from casevo.transactions.models import Transaction


# "source";"date";"valuta date";"type";"title";"target";"target nummer";"target blz";"value";"currency";"info"
def parse_csv(text):
    default_curreny = Currency.objects.get(is_default=True)
    lines = text.replace('\r', '').split('\n')
    for line in lines:
        fields = line.replace('"', '').split(';')

        currency, created = Currency.objects.get_or_create(code=fields[9], defaults={'name': fields[9], 'factor': 1})

        source, created = Account.objects.get_or_create(identifier=fields[0], defaults={'currency': default_curreny})
        target, created = Account.objects.get_or_create(identifier=fields[5], defaults={'currency': currency})

        transaction = Transaction()
        transaction.date = datetime.strptime(fields[2], '%d.%m.%y').date()
        transaction.source = source
        transaction.target = target
        transaction.value = Decimal(fields[8].strip().replace('-', '').replace(',', '.'))
        transaction.description = fields[4]
        transaction.save()