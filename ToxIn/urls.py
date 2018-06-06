from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.HomeView.as_view()),
    url('^login/$', views.SignInView.as_view()),
    url('^register/$', views.SignUpView.as_view()),
    url('^getallusers/$', views.getallusers),
    url('^getallcontacts/$', views.getallcontacts),
    url('^addcontacttouser/$', views.addcontacttouser),
    url('^getuserprofile/$', views.getuserprofile),
    url('^setuserprofile/$', views.setuserprofile),
]