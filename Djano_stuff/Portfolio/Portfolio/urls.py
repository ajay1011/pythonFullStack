from django.conf.urls import include, url
from django.contrib import admin
from myapp import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'Portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index,name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/',include('myapp.urls',namespace="myapp")),
]
