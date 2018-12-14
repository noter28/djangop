from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url(r'^1$', views.post_list, name='index'),
#    url(r'^2$', views.post, name='index'),
]