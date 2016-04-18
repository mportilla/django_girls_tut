from django.conf.urls import include, url
from django.contrib import admin
<<<<<<< HEAD
from django.views.generic import TemplateView
=======
from django.contrib.auth.views import login,logout

>>>>>>> dev

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page': '/'}),
<<<<<<< HEAD
    url('^',include('django.contrib.auth.urls')),
    url(r'^sobre_mi/', TemplateView.as_view(template_name="sobre_mi.html", name =)),
    ]
=======
    url(r'^login/$','django.contrib.auth.views.login',{'template_name': 'base.html'}),
    url('^',include('django.contrib.auth.urls'))
]
>>>>>>> dev
