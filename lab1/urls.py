from django.conf.urls import patterns, url
from lab1 import views

urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'edx.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    '',
    url(r'^albumdetails/$', views.album_details, name='album_details'),
)
