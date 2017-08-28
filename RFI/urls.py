from django.conf.urls import url 
from . import views

app_name = 'RFI'

urlpatterns = [
	url(r'^$', views.Home, name='home'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^profile/$', views.update_profile),
    url(r'^account/logout/$', views.Logout),
]