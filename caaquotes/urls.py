from caaquotes.quotes import views
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.ListQuotes.as_view(), name='quotes'),
    url(r'^(?P<pk>\d+)/$', views.QuoteDetail.as_view(), name='quote'),
    url(r'^search/$', views.QuoteSearch.as_view(), name='quote_search'),
    # Examples:
    # url(r'^$', 'caaquotes.views.home', name='home'),
    # url(r'^caaquotes/', include('caaquotes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
