from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$',
        'goat.apps.lists.views.home_page',
        name='home_page'),
    url(r'^lists/(\d+)/$',
        'goat.apps.lists.views.view_list',
        name = 'view_list'),
    url(r'^lists/(\d+)/add_item$',
        'goat.apps.lists.views.add_item',
        name = 'add_item'),
    url(r'^lists/new$',
        'goat.apps.lists.views.new_list',
        name = 'new_list'),
    #url(r'^admin/', include(admin.site.urls)),
)
