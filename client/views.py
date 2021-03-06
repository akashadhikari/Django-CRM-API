import django_filters.rest_framework
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from rest_framework import filters

from .permissions import IsOwnerOrReadOnly
from .models import (
	AddClient,
	ListOfProduct,
	)
from .serializers import (
	AddClientSerializer,
	ListOfProductSerializer,
	StatsSerializer
	)

class AddClientViewSet(generics.ListCreateAPIView):
	queryset = AddClient.objects.all()
	serializer_class = AddClientSerializer
	permission_classes = (IsAuthenticated,)
	#authentication_classes = [TokenAuthentication]

	filter_backends = (
		filters.SearchFilter, 
		filters.OrderingFilter, 
		django_filters.rest_framework.DjangoFilterBackend,
		)
	filter_fields = ('client_name', 'organisation_name')
	search_fields = ('client_name', 'organisation_name', 'user__username')


	def perform_create(self, serializer):
			serializer.save() # Adding owner=self.request.user

class AddClientDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = AddClient.objects.all()
	serializer_class = AddClientSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class ListOfProductViewSet(generics.ListCreateAPIView):
	queryset = ListOfProduct.objects.all()
	serializer_class = ListOfProductSerializer
	permission_classes = (IsAuthenticated,)
	#authentication_classes = [TokenAuthentication]

	filter_backends = (
		filters.SearchFilter, 
		filters.OrderingFilter, 
		django_filters.rest_framework.DjangoFilterBackend,
		)
	filter_fields = ('client__client_name', 'service_name', 'service_detail')
	search_fields = ('client__client_name', 'service_name', 'service_detail', 'user__username')


	def perform_create(self, serializer):
			serializer.save() # Adding owner=self.request.user

class ListOfProductDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = ListOfProduct.objects.all()
	serializer_class = ListOfProductSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class StatsViewSet(generics.ListCreateAPIView):
    queryset = AddClient.objects.all() # LeadProcess.objects.filter(service_type='Hardware').count()
    serializer_class = StatsSerializer
