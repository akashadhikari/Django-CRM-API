from django.conf.urls import url

from .views import (

    AlbumViewSet,
    AlbumDetailsViewSet,

    TrackViewSet,
    TrackDetailsViewSet,

)

urlpatterns = [

    url(
        r'^api/common/v1/album/(?P<pk>[0-9]+)$',
        AlbumDetailsViewSet.as_view(),
        name='get_delete_update_album'
    ),

    url(
        r'^api/common/v1/album/$',
        AlbumViewSet.as_view(),
        name='get_post_album'
    ),

    url(
        r'^api/common/v1/track/(?P<pk>[0-9]+)$',
        TrackDetailsViewSet.as_view(),
        name='get_delete_update_track'
    ),

    url(
        r'^api/common/v1/track/$',
        TrackViewSet.as_view(),
        name='get_post_track'
    ),

]