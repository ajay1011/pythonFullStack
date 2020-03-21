from django.conf.urls import url

from myapp import views

app_name = 'myapp'
urlpatterns = [

    url(r'^portfolio/$',views.portfolio,name='portfolio'),
    url(r'^contact/$',views.contact,name='contact'),


]
