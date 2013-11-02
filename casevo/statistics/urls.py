from django.conf.urls import patterns, url

from casevo.statistics.views import StatisticHomeView, StatisticAccountsPieView


urlpatterns = patterns('',
    url(r'^$', StatisticHomeView.as_view(), name='home'),
    url(r'^accounts/pie/$', StatisticAccountsPieView.as_view(), name='accounts-pie'),
)

