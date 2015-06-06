from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.home),
    url('^login/$', views.login),
    url('^register/$', views.register),
    url('^getallusers/$', views.getallusers),
]