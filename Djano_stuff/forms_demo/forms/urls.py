from django.conf.urls import url
from forms import views
urlpatterns = [
    url(r'^$',views.form_page_view,name='form_page'),
    url(r'^users/',views.users,name='users')

]
