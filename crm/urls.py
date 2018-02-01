from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.authtoken import views

urlpatterns = [

    url(r'^', include('lead.urls')),

    url(r'^', include('communication.urls')),

	url(r'^', include('client.urls')),    

    url(r'^', include('common.urls')),

    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),

    url(r'^api-token-auth/', views.obtain_auth_token),
    
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns