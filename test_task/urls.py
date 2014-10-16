from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('test_task.core.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
