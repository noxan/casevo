from django.conf.urls import patterns, include, url

from django.contrib import admin

from casevo.common.views import CasevoHomeView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', CasevoHomeView.as_view(), name='home'),

    url(r'^accounts/', include('casevo.accounts.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
