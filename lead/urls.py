from django.conf.urls import url
from .views import LeadProcessViewSet, LeadProcessDetailsViewSet, StatsViewSet


urlpatterns = [

    url(
        r'^api/lead/v1/leads/(?P<pk>[0-9]+)$',
        LeadProcessDetailsViewSet.as_view(),
        name='get_delete_update_leadprocess'
    ),

    url(
        r'^api/lead/v1/leads/$',
        LeadProcessViewSet.as_view(),
        name='get_post_leadprocess'
    ),

    url(
        r'^api/lead/v1/stats/$',
        StatsViewSet.as_view(),
        name='get_stats_leads'
    )

]