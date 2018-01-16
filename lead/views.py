import django_filters.rest_framework

from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

from rest_framework import filters

from .permissions import IsOwnerOrReadOnly
from .models import LeadProcess
from .serializers import LeadProcessSerializer, StatsSerializer


class LeadProcessViewSet(generics.ListCreateAPIView):
    queryset = LeadProcess.objects.all()
    serializer_class = LeadProcessSerializer
    permission_classes = (IsAuthenticated,)

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        django_filters.rest_framework.DjangoFilterBackend,
        )
    filter_fields = ('employer_name', 'service_type', 'user__username')
    search_fields = ('employer_name', 'service_type', 'user__username')

    def perform_create(self, serializer):
        serializer.save() # Adding owner=self.request.user

class LeadProcessDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeadProcess.objects.all()
    serializer_class = LeadProcessSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class StatsViewSet(generics.ListCreateAPIView):
    queryset = LeadProcess.objects.all() # LeadProcess.objects.filter(service_type='Hardware').count()
    serializer_class = StatsSerializer
    permission_classes = (IsAuthenticated,)