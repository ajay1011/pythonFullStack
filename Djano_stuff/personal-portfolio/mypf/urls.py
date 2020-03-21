from django.conf.urls import url
from . import views #import views


# adding url
urlpatterns = [
    url('', views.index, name='home'), #home
    url('portfolio', views.portfolio, name='portfolio'), #portfolio
    url('contact', views.contact, name='contact'), #contact
]
