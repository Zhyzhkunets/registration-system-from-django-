from django.conf.urls import patterns, url
from test_task.core import views

urlpatterns = patterns('',
    url(r'^$', views.home_view, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),  
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^registrate/$', views.registrate_view, name='registrate'),
)
