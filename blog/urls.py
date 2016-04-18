from django.conf.urls import include, url
from . import views
from contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
        url(r'^$', views.PostList.as_View()),
        url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_View()),
        url(r'^post/new/$',login_required(views.PostCreate,login_url='login'), name='post_new'),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.PostEdit.as_View(), name='post_edit'),
        url(r'^post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_View(), name='post_delete'),
    ]