from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

from vendors import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'organisations', views.OraganisationViewSet)


from django.contrib import admin
admin.autodiscover()
from main.views import AddcontactView, ContactDetailView, AddOrganisationView
from main.models import Contact, Organisation

from vendors.views import AddOrganisationView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iboilerplate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^addbusiness/', AddcontactView.as_view()),

    url(r'^thanks/', TemplateView.as_view(template_name="contact/thanku.html")),
    url(r'^search/', include('search.urls')),
    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^join/', AddOrganisationView.as_view()),
    url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^', TemplateView.as_view(template_name="index.html")),

    url(r'^$', ListView.as_view(
    		model = Contact,
    		queryset = Contact.objects.all(),
    		context_object_name = "contacts",
    		template_name = 'contact/index.html')),
    
    #url(r'^addbusiness/', AddOrganisationView.as_view()),
    url(r'^(?P<slug>[-_\w]+)/$', ContactDetailView.as_view(), name='article-detail'),
    

)






