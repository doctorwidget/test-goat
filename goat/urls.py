from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$',
        'goat.apps.lists.views.home_page',
        name='home_page'),
    url(r'^lists/', include('goat.apps.lists.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
