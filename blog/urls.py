from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^(?P<pkl>\d+)/$', views.post_detail),
]
