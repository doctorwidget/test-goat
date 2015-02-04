from django.conf.urls import patterns, url

urlpatterns = patterns('',
   # comes in with /accounts/ prefixed
   url(r'^login$',
       'goat.apps.accounts.views.persona_login',
       name='persona_login'),
)