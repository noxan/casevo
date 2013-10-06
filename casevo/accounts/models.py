from django.db import models

from currencies.models import Currency


class Account(models.Model):
    identifier = models.CharField(max_length=255, unique=True)
    currency = models.ForeignKey(Currency, default=0)

    def __unicode__(self):
        return self.identifier
