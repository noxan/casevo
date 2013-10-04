from django.db import models

from currencies.models import Currency


class Account(models.Model):
    identifier = models.CharField(max_length=255)
    currency = models.ForeignKey(Currency, default=0)
