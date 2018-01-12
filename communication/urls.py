from django.conf.urls import url

from .views import (
    ClientlistViewSet,
    ClientlistDetailsViewSet,
    SalesStageViewSet,
    SalesStageDetailsViewSet,
    SalesSubViewSet,
    SalesSubDetailsViewSet
    )


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

    url(
        r'^api/communication/v1/salesstage/(?P<pk>[0-9]+)$',
        SalesStageDetailsViewSet.as_view(),
        name='get_delete_update_salesstage'
    ),

    url(
        r'^api/communication/v1/salesstage/$',
        SalesStageViewSet.as_view(),
        name='get_post_salesstage'
    ),

    url(
        r'^api/communication/v1/salessubstage/(?P<pk>[0-9]+)$',
        SalesSubDetailsViewSet.as_view(),
        name='get_delete_update_salessubstage'
    ),

    url(
        r'^api/communication/v1/salessubstage/$',
        SalesSubViewSet.as_view(),
        name='get_post_salessubstage'
    ),
]