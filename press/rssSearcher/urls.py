
from django.conf.urls import patterns, url
from rssSearcher import views

urlpatterns = [
	url(r'^$', views.home, name='home'),

]
