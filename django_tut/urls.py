from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page': '/'}),
    url('^',include('django.contrib.auth.urls')),
    url(r'^sobre_mi/', TemplateView.as_view(template_name="sobre_mi.html", name =)),
    ]