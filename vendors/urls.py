from django.conf.urls import patterns, include, url
from .views import TestList

urlpatterns = patterns('',
	url(r'^join/$', 'vendors.views.join'),
	url(r'^test/$', TestList.as_view()),


	)