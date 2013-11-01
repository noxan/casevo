from django.conf.urls import patterns, url

from casevo.accounts.views import AccountUpdateView, AccountListView


urlpatterns = patterns('',
    url(r'^$', AccountListView.as_view(), name='list'),
    url(r'^(?P<pk>[\d]+)/$', AccountUpdateView.as_view(), name='update'),
)
