from django.conf.urls import url

from .views import (
    
    AddClientViewSet,
    AddClientDetailsViewSet,

    StatsViewSet,

    )


urlpatterns = [

    url(
        r'^api/v1/client/addclient/(?P<pk>[0-9]+)$',
        AddClientDetailsViewSet.as_view(),
        name='get_delete_update_addclient'
    ),

    url(
        r'^api/v1/client/addclient/$',
        AddClientViewSet.as_view(),
        name='get_post_addclient'
    ),

    url(
        r'^api/v1/client/stats/$',
        StatsViewSet.as_view(),
        name='get_stats_client'
    )
]