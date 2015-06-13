from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mineral_list, name='list'),
    url(r'^(?P<mineral_id>[0-9]+)/$', views.mineral_detail, name='detail'),
]
