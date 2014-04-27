from django.conf.urls import patterns, url

from munger import views

urlpatterns = patterns(
    '',
    url(r'^$', views.munge, name='munge')
)
