from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from .permissions import IsOwnerOrReadOnly
from .models import Clientlist, SalesStage, SalesSub
from .serializers import ClientlistSerializer, SalesStageSerializer, SalesSubSerializer


class ClientlistViewSet(generics.ListCreateAPIView):
    queryset = Clientlist.objects.all()
    serializer_class = ClientlistSerializer
    permission_classes = (IsAuthenticated,)


    def perform_create(self, serializer):
            serializer.save() # Adding owner=self.request.user

class ClientlistDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clientlist.objects.all()
    serializer_class = ClientlistSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class SalesStageViewSet(generics.ListCreateAPIView):
	queryset = SalesStage.objects.all()
	serializer_class = SalesStageSerializer
	permission_classes = (IsAuthenticated,)

class SalesStageDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = SalesStage.objects.all()
	serializer_class = SalesStageSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class SalesSubViewSet(generics.ListCreateAPIView):
	queryset = SalesSub.objects.all()
	serializer_class = SalesSubSerializer
	permission_classes = (IsAuthenticated,)

class SalesSubDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = SalesSub.objects.all()
	serializer_class = SalesSubSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

