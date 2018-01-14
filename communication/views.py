from rest_framework import generics
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from rest_framework import filters
import django_filters.rest_framework


from .permissions import IsOwnerOrReadOnly
from .models import Clientlist, SalesStage, SalesSub
from .serializers import ClientlistSerializer, SalesStageSerializer, SalesSubSerializer


class ClientlistViewSet(generics.ListCreateAPIView):
	queryset = Clientlist.objects.all()
	serializer_class = ClientlistSerializer
	permission_classes = (IsAuthenticated,)

	filter_backends = (
		filters.SearchFilter, 
		filters.OrderingFilter, 
		django_filters.rest_framework.DjangoFilterBackend,
		)
	filter_fields = ('client_name', 'medium')
	search_fields = ('client_name', 'medium', 'user__username')


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

	filter_backends = (
		filters.SearchFilter,
		filters.OrderingFilter, 
		django_filters.rest_framework.DjangoFilterBackend,
		)
	filter_fields = ('substage', 'sales_stage')
	search_fields = ('substage', 'sales_stage', 'client__client_name')

class SalesStageDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = SalesStage.objects.all()
	serializer_class = SalesStageSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class SalesSubViewSet(generics.ListCreateAPIView):
	queryset = SalesSub.objects.all()
	serializer_class = SalesSubSerializer
	permission_classes = (IsAuthenticated,)

	filter_backends = (
		filters.SearchFilter,
		filters.OrderingFilter,
		django_filters.rest_framework.DjangoFilterBackend,
		)
	filter_fields = ('sales_substage', 'substage__sales_stage')
	search_fields = ('sales_substage', 'substage__sales_stage')

class SalesSubDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = SalesSub.objects.all()
	serializer_class = SalesSubSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

