from django.conf.urls import patterns, url

from casevo.transactions.views import TransactionListView


urlpatterns = patterns('',
    url(r'^$', TransactionListView.as_view(), name='list'),
)
