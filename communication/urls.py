from django.conf.urls import url

from .views import (

    AddCommunicationViewSet,
    AddCommunicationDetailsViewSet,

    )


urlpatterns = [

    url(
        r'^api/v1/communication/new/(?P<pk>[0-9]+)$',
        AddCommunicationDetailsViewSet.as_view(),
        name='get_delete_update_communication'
    ),

    url(
        r'^api/v1/communication/new/$',
        AddCommunicationViewSet.as_view(),
        name='get_post_communication'
    ),
]