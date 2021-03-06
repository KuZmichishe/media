from django.conf.urls import url
from . import views


app_name = 'tvshows'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<show_id>[0-9]+)/$', views.show_detail, name='show_detail'),
    url(r'^(?P<show_id>[0-9]+)/season/(?P<season_id>[0-9]+)/$', views.season_detail, name='season_detail'),
]
