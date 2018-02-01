from django.conf.urls import url

from .views import (

    UserViewSet,
    UserDetailsViewSet,

)

urlpatterns = [

    url(
        r'^api/v1/common/user/(?P<pk>[0-9]+)$',
        UserDetailsViewSet.as_view(),
        name='get_delete_update_user'
    ),

    url(
        r'^api/v1/common/user/$',
        UserViewSet.as_view(),
        name='get_post_user'
    ),

]