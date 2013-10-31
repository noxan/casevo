from django.conf.urls import patterns, url

from casevo.accounts.views import AccountListView


urlpatterns = patterns('',
    url(r'^$', AccountListView.as_view(), name='list'),
)
