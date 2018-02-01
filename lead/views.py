import django_filters.rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

from rest_framework import filters

from common.filters import DateRangeFilter
from .permissions import IsOwnerOrReadOnly
from .models import LeadProcess
from .serializers import LeadProcessSerializer


class LeadProcessViewSet(generics.ListCreateAPIView):
    queryset = LeadProcess.objects.all()
    serializer_class = LeadProcessSerializer
    #authentication_classes = [TokenAuthentication]

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        django_filters.rest_framework.DjangoFilterBackend,
        DateRangeFilter,
        )
    
    filter_fields = ('employer_name', 'service_type', 'user__username')
    search_fields = ('employer_name', 'service_type', 'user__username')

    def perform_create(self, serializer):
        serializer.save() # Adding owner=self.request.user

class LeadProcessDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeadProcess.objects.all()
    serializer_class = LeadProcessSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    #authentication_classes = [TokenAuthentication]

class StatsViewSet(APIView):

    def get(self ,request, format=None):

        count_tj = LeadProcess.objects.filter(service_type='Top Jobs').count()
        count_hj = LeadProcess.objects.filter(service_type='Hot Jobs').count()
        count_fp = LeadProcess.objects.filter(service_type='F. Post').count()
        count_gp = LeadProcess.objects.filter(service_type='G. Post').count()

        response_dict = {
            "Top Jobs" : count_tj,
            "Hot Jobs" : count_hj,
            "F. Post" : count_fp,
            "G. Post" : count_gp
        }

        return Response(response_dict)
