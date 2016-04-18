from django.conf.urls import include, url
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
        url(r'^$', views.PostList.as_view(),name='post_list'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(),name='post_detail'),
        url(r'^post/new/$',login_required(views.PostCreate,login_url='login'), name='post_new'),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.PostEdit.as_view(), name='post_edit'),
        url(r'^post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post_delete'),
    ]