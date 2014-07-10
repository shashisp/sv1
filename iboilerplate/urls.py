from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView





from vendors import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'organisations', views.OraganisationViewSet)


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iboilerplate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^join/$', 'vendors.views.join'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    (r'^', TemplateView.as_view(template_name="index.html")),

)
