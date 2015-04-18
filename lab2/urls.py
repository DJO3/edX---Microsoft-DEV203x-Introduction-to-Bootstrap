from django.conf.urls import patterns, url
from lab2 import views

urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'edx.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    '',
    url(r'^submitalbum/$', views.submit_album, name='submit_album'),
)
