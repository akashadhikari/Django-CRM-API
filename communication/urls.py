from django.conf.urls import url

from .views import (
    ClientDetailViewSet,
    ClientDetailDetailsViewSet,
    SalesStageViewSet,
    SalesStageDetailsViewSet,
    SalesSubViewSet,
    SalesSubDetailsViewSet
    )


urlpatterns = [

    url(
        r'^api/communication/v1/clientinfo/(?P<pk>[0-9]+)$',
        ClientDetailDetailsViewSet.as_view(),
        name='get_delete_update_clientdetail'
    ),

    url(
        r'^api/communication/v1/clientinfo/$',
        ClientDetailViewSet.as_view(),
        name='get_post_clientdetail'
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