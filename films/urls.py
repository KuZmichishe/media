from django.conf.urls import url
from . import views


app_name = 'films'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<film_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^edit/(?P<film_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^download/(?P<film_id>[0-9]+)/$', views.download_film, name='download'),
]
