from django.conf.urls import patterns, url

from casevo.statistics.views import StatisticHomeView


urlpatterns = patterns('',
    url(r'^$', StatisticHomeView.as_view(), name='home'),
)

