from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from .permissions import IsOwnerOrReadOnly
from .models import LeadProcess
from .serializers import LeadProcessSerializer, StatsSerializer


class LeadProcessViewSet(generics.ListCreateAPIView):
    queryset = LeadProcess.objects.all()
    serializer_class = LeadProcessSerializer
    permission_classes = (IsAuthenticated,)


    def perform_create(self, serializer):
            serializer.save() # Adding owner=self.request.user

class LeadProcessDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeadProcess.objects.all()
    serializer_class = LeadProcessSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class StatsViewSet(generics.ListCreateAPIView):
    queryset = LeadProcess.objects.all() # LeadProcess.objects.filter(service='Hardware').count()
    serializer_class = StatsSerializer
    permission_classes = (IsAuthenticated,)