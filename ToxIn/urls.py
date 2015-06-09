from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.home),
    url('^login/$', views.login),
    url('^register/$', views.register),
    url('^getallusers/$', views.getallusers),
    url('^getallcontacts/$', views.getallcontacts),
    url('^addcontacttouser/$', views.addcontacttouser),
    url('^getuserprofile/$', views.getuserprofile),
    url('^setuserprofile/$', views.setuserprofile),
]