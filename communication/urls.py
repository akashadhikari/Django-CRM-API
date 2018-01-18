from django.conf.urls import url

from .views import (
    
    BranchViewSet,
    BranchDetailsViewSet,

    BusinessOutflowViewSet,
    BusinessOutflowDetailsViewSet,

    ListServiceViewSet,
    ListServiceDetailsViewSet,

    ClientDetailViewSet,
    ClientDetailDetailsViewSet,

    SalesStageViewSet,
    SalesStageDetailsViewSet,

    SalesSubViewSet,
    SalesSubDetailsViewSet
    )


urlpatterns = [

    url(
        r'^api/communication/v1/branch/(?P<pk>[0-9]+)$',
        BranchDetailsViewSet.as_view(),
        name='get_delete_update_branch'
    ),

    url(
        r'^api/communication/v1/branch/$',
        BranchViewSet.as_view(),
        name='get_post_branch'
    ),

    url(
        r'^api/communication/v1/businessoutflow/(?P<pk>[0-9]+)$',
        BusinessOutflowDetailsViewSet.as_view(),
        name='get_delete_update_businessoutflow'
    ),

    url(
        r'^api/communication/v1/businessoutflow/$',
        BusinessOutflowViewSet.as_view(),
        name='get_post_businessoutflow'
    ),

    url(
        r'^api/communication/v1/listservice/(?P<pk>[0-9]+)$',
        ListServiceDetailsViewSet.as_view(),
        name='get_delete_update_listservice'
    ),

    url(
        r'^api/communication/v1/listservice/$',
        ListServiceViewSet.as_view(),
        name='get_post_listservice'
    ),

    url(
        r'^api/communication/v1/clientdetail/(?P<pk>[0-9]+)$',
        ClientDetailDetailsViewSet.as_view(),
        name='get_delete_update_clientdetail'
    ),

    url(
        r'^api/communication/v1/clientdetail/$',
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