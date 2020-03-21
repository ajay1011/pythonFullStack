from django.conf.urls import url
from app_two import views
urlpatterns = [
    url(r'^$',views.index_2,name='index_2'),
    url(r'^help/',views.help,name='help'),
]
