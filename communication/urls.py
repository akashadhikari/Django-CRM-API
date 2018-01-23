from django.conf.urls import url

from .views import (

    AddCommunicationViewSet,
    AddCommunicationDetailsViewSet,

    SuspectingViewSet,
    SuspectingDetailsViewSet,

    ProspectingViewSet,
    ProspectingDetailsViewSet,

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

    url(
        r'^api/v1/communication/suspecting/(?P<pk>[0-9]+)$',
        SuspectingDetailsViewSet.as_view(),
        name='get_delete_update_suspecting'
    ),

    url(
        r'^api/v1/communication/suspecting/$',
        SuspectingViewSet.as_view(),
        name='get_post_suspecting'
    ),

    url(
        r'^api/v1/communication/prospecting/(?P<pk>[0-9]+)$',
        ProspectingDetailsViewSet.as_view(),
        name='get_delete_update_prospecting'
    ),

    url(
        r'^api/v1/communication/prospecting/$',
        ProspectingViewSet.as_view(),
        name='get_post_prospecting'
    ),
]