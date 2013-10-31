from django.db import models

from currencies.models import Currency


class Account(models.Model):
    identifier = models.CharField(max_length=255)
    number = models.CharField(max_length=100)
    blz = models.CharField(max_length=100)
    currency = models.ForeignKey(Currency, default=0)

    class Meta:
        unique_together = [('number', 'blz')]

    def __unicode__(self):
        return u'%s' % (self.identifier)
