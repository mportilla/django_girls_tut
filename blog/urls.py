from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.PostList),
        url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail),
        url(r'^post/new/$', views.PostCreate, name='post_new'),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.PostEdit, name='post_edit'),
        url(r'^post/(?P<pk>[0-9]+)/delete/$', views.PostDelete, name='post_delete'),
    ]