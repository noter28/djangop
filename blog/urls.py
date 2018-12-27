from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url(r'^1$', views.post_list, name='index'),
    url(r'^post/(?P<pk>\d+)$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    #    url(r'^2$', views.post, name='index'),
]