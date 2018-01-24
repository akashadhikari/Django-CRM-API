from django.conf.urls import url

from .views import (

    AddCommunicationSuspectingViewSet,
    AddCommunicationSuspectingDetailsViewSet,

    AddCommunicationProspectingViewSet,
    AddCommunicationProspectingDetailsViewSet,

    AddCommunicationApproachingViewSet,
    AddCommunicationApproachingDetailsViewSet,

    AddCommunicationNegotiationViewSet,
    AddCommunicationNegotiationDetailsViewSet,

    SuspectingViewSet,
    SuspectingDetailsViewSet,

    ProspectingViewSet,
    ProspectingDetailsViewSet,

    ApproachingViewSet,
    ApproachingDetailsViewSet,

    NegotiationViewSet,
    NegotiationDetailsViewSet,

    StatsViewSet

    )


urlpatterns = [

    url(
        r'^api/v1/communication/susp/(?P<pk>[0-9]+)$',
        AddCommunicationSuspectingDetailsViewSet.as_view(),
        name='get_delete_update_communication_suspecting'
    ),

    url(
        r'^api/v1/communication/susp/$',
        AddCommunicationSuspectingViewSet.as_view(),
        name='get_post_communication_suspecting'
    ),

    url(
        r'^api/v1/communication/prosp/(?P<pk>[0-9]+)$',
        AddCommunicationProspectingDetailsViewSet.as_view(),
        name='get_delete_update_communication_prospecting'
    ),

    url(
        r'^api/v1/communication/prosp/$',
        AddCommunicationProspectingViewSet.as_view(),
        name='get_post_communication_prospecting'
    ),

    url(
        r'^api/v1/communication/appr/(?P<pk>[0-9]+)$',
        AddCommunicationApproachingDetailsViewSet.as_view(),
        name='get_delete_update_communication_approaching'
    ),

    url(
        r'^api/v1/communication/appr/$',
        AddCommunicationApproachingViewSet.as_view(),
        name='get_post_communication_approaching'
    ),

    url(
        r'^api/v1/communication/neg/(?P<pk>[0-9]+)$',
        AddCommunicationNegotiationDetailsViewSet.as_view(),
        name='get_delete_update_communication_negotiation'
    ),

    url(
        r'^api/v1/communication/neg/$',
        AddCommunicationNegotiationViewSet.as_view(),
        name='get_post_communication_negotiation'
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

    url(
        r'^api/v1/communication/approaching/(?P<pk>[0-9]+)$',
        ApproachingDetailsViewSet.as_view(),
        name='get_delete_update_approaching'
    ),

    url(
        r'^api/v1/communication/approaching/$',
        ApproachingViewSet.as_view(),
        name='get_post_approaching'
    ),

    url(
        r'^api/v1/communication/negotiation/(?P<pk>[0-9]+)$',
        NegotiationDetailsViewSet.as_view(),
        name='get_delete_update_negotiation'
    ),

    url(
        r'^api/v1/communication/negotiation/$',
        NegotiationViewSet.as_view(),
        name='get_post_negotiation'
    ),

    url(
        r'^api/v1/communication/stats/$',
        StatsViewSet.as_view(),
        name='get_stats_communication'
    )
]