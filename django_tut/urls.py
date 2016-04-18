from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page': '/'}),
    url(r'^login/$','django.contrib.auth.views.login',{'template_name': 'base.html'}),
    url('^',include('django.contrib.auth.urls'))
]
