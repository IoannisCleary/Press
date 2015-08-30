
from django.conf.urls import patterns, url
from rssSearcher import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^results/(?P<query_search>[\w\-]+)/$', views.results),	

]
