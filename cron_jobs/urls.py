from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register_files/$', views.register_files, name='register'),
    url(r'^update_video_data/$', views.update_video_data, name='update_video_data'),
]
