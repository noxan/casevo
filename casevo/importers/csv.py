import codecs
import logging
from datetime import datetime
from decimal import Decimal

from currencies.models import Currency

from casevo.accounts.models import Account
from casevo.transactions.models import Transaction


logger = logging.getLogger(__name__)

# "source";"date";"valuta date";"type";"title";"target";"target nummer";"target blz";"value";"currency";"info"
class ImporterCSV(object):
    def __init__(self):
        self.default_curreny = Currency.objects.get(is_default=True)

    def read(self, filename, encoding='windows-1252', skip_first_line=True):
        f = codecs.open(filename, 'r', encoding)
        for line in f.readlines()[1:]:
            self.process_line(line.replace('\r', ''))

    def parse(self, text):
        lines = text.replace('\r', '').split('\n')
        for line in lines:
            self.process_line(line)

    def process_line(self, line):
        fields = line.replace('"', '').split(';')

        currency, created = Currency.objects.get_or_create(code=fields[9], defaults={'name': fields[9], 'factor': 1})

        source, created = Account.objects.get_or_create(identifier=fields[0], defaults={'currency': default_curreny})
        target, created = Account.objects.get_or_create(identifier=fields[5], defaults={'currency': currency})

        transaction_date = datetime.strptime(fields[2], '%d.%m.%y').date()
        transaction_value = Decimal(fields[8].strip().replace('-', '').replace(',', '.'))
        transaction_description = fields[4]

        transaction = Transaction()
        transaction.date = transaction_date
        transaction.source = source
        transaction.target = target
        transaction.value = transaction_value
        transaction.description = transaction_description
        transaction.save()
