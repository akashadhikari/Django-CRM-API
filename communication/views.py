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
from .models import (
	Branch,
	BusinessOutflow,
	ClientDetail,
	SalesStage,
	SalesSub,
	ListService
	)
from .serializers import (
	BranchSerializer,
	BusinessOutflowSerializer,
	ListServiceSerializer,
	ClientDetailSerializer,
	SalesStageSerializer,
	SalesSubSerializer
	)

class BranchViewSet(generics.ListCreateAPIView):
	queryset = Branch.objects.all()
	serializer_class = BranchSerializer
	#permission_classes = (IsAuthenticated,)

	filter_backends = (
		filters.SearchFilter, 
		filters.OrderingFilter, 
		django_filters.rest_framework.DjangoFilterBackend,
		)
	filter_fields = ('branch_incharge', 'branch_address')
	search_fields = ('branch_incharge', 'branch_address')


	def perform_create(self, serializer):
			serializer.save() # Adding owner=self.request.user

class BranchDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = Branch.objects.all()
	serializer_class = BranchSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class BusinessOutflowViewSet(generics.ListCreateAPIView):
	queryset = BusinessOutflow.objects.all()
	serializer_class = BusinessOutflowSerializer
	#permission_classes = (IsAuthenticated,)

	filter_backends = (
		filters.SearchFilter, 
		filters.OrderingFilter, 
		django_filters.rest_framework.DjangoFilterBackend,
		)
	filter_fields = ('outflowed_to', 'service_outflowed')
	search_fields = ('outflowed_to', 'service_outflowed')


	def perform_create(self, serializer):
			serializer.save() # Adding owner=self.request.user

class BusinessOutflowDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = BusinessOutflow.objects.all()
	serializer_class = BusinessOutflowSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class ListServiceViewSet(generics.ListCreateAPIView):
	queryset = ListService.objects.all()
	serializer_class = ListServiceSerializer
	#permission_classes = (IsAuthenticated,)

	filter_backends = (
		filters.SearchFilter, 
		filters.OrderingFilter, 
		django_filters.rest_framework.DjangoFilterBackend,
		)
	filter_fields = ('service_name', 'service_detail')
	search_fields = ('service_name', 'service_detail')


	def perform_create(self, serializer):
			serializer.save() # Adding owner=self.request.user

class ListServiceDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = ListService.objects.all()
	serializer_class = ListServiceSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class ClientDetailViewSet(generics.ListCreateAPIView):
	queryset = ClientDetail.objects.all()
	serializer_class = ClientDetailSerializer
	permission_classes = (IsAuthenticated,)

	filter_backends = (
		filters.SearchFilter, 
		filters.OrderingFilter, 
		django_filters.rest_framework.DjangoFilterBackend,
		)
	filter_fields = ('client_name', 'organisation_name')
	search_fields = ('client_name', 'organisation_name', 'user__username')


	def perform_create(self, serializer):
			serializer.save() # Adding owner=self.request.user

class ClientDetailDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = ClientDetail.objects.all()
	serializer_class = ClientDetailSerializer
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

