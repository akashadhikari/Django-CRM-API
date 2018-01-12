from django.conf.urls import url
from .views import ClientlistViewSet, ClientlistDetailsViewSet


urlpatterns = [

    url(
        r'^api/communication/v1/clientinfo/(?P<pk>[0-9]+)$',
        ClientlistDetailsViewSet.as_view(),
        name='get_delete_update_clientlist'
    ),

    url(
        r'^api/communication/v1/clientinfo/$',
        ClientlistViewSet.as_view(),
        name='get_post_clientlist'
    ),
]