from django.conf.urls import patterns, url
from lab3 import views

urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'edx.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    '',
    url(r'^modal/$', views.modal, name='modal'),
    url(r'^final/$', views.final, name='final'),
)
