from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # comes in with /lists/ prefixed
    url(r'^(\d+)/$',
        'goat.apps.lists.views.view_list',
        name = 'view_list'),
    url(r'^new$',
        'goat.apps.lists.views.new_list',
        name = 'new_list'),
    url(r'^colors$',
        'goat.apps.lists.views.bootstrap_customization',
        name = 'bootstrap_customization')
)
