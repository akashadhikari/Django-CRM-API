from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.authtoken import views

urlpatterns = [
    url(r'^', include('lead.urls')),

    url(r'^', include('communication.urls')),

    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),

    url(r'^api-token-auth/', views.obtain_auth_token),
    
    url(r'^admin/', admin.site.urls),
]
