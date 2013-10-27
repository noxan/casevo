from django.db import models

from casevo.accounts.models import Account


class Transaction(models.Model):
    date = models.DateField()
    source = models.ForeignKey(Account, related_name='transactions_out')
    target = models.ForeignKey(Account, related_name='transactions_in')
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    description = models.TextField()

    class Meta:
        unique_together = (('date', 'source', 'target', 'value', 'description'),)

    def __unicode__(self):
        return u'%s' % (self.date)
