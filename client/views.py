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
	# Branch,
	# BusinessOutflow,
	# ListService
	)
from .serializers import (
	# BranchSerializer,
	# BusinessOutflowSerializer,
	# ListServiceSerializer,
	AddClientSerializer,
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

class StatsViewSet(generics.ListCreateAPIView):
    queryset = AddClient.objects.all() # LeadProcess.objects.filter(service_type='Hardware').count()
    serializer_class = StatsSerializer

# class BranchViewSet(generics.ListCreateAPIView):
# 	queryset = Branch.objects.all()
# 	serializer_class = BranchSerializer
# 	#permission_classes = (IsAuthenticated,)

# 	filter_backends = (
# 		filters.SearchFilter, 
# 		filters.OrderingFilter, 
# 		django_filters.rest_framework.DjangoFilterBackend,
# 		)
# 	filter_fields = ('branch_incharge', 'branch_address')
# 	search_fields = ('branch_incharge', 'branch_address')


# 	def perform_create(self, serializer):
# 			serializer.save() # Adding owner=self.request.user

# class BranchDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Branch.objects.all()
# 	serializer_class = BranchSerializer
# 	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

# class BusinessOutflowViewSet(generics.ListCreateAPIView):
# 	queryset = BusinessOutflow.objects.all()
# 	serializer_class = BusinessOutflowSerializer
# 	#permission_classes = (IsAuthenticated,)

# 	filter_backends = (
# 		filters.SearchFilter, 
# 		filters.OrderingFilter, 
# 		django_filters.rest_framework.DjangoFilterBackend,
# 		)
# 	filter_fields = ('outflowed_to', 'service_outflowed')
# 	search_fields = ('outflowed_to', 'service_outflowed')


# 	def perform_create(self, serializer):
# 			serializer.save() # Adding owner=self.request.user

# class BusinessOutflowDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = BusinessOutflow.objects.all()
# 	serializer_class = BusinessOutflowSerializer
# 	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

# class ListServiceViewSet(generics.ListCreateAPIView):
# 	queryset = ListService.objects.all()
# 	serializer_class = ListServiceSerializer
# 	#permission_classes = (IsAuthenticated,)

# 	filter_backends = (
# 		filters.SearchFilter, 
# 		filters.OrderingFilter, 
# 		django_filters.rest_framework.DjangoFilterBackend,
# 		)
# 	filter_fields = ('service_name', 'service_detail')
# 	search_fields = ('service_name', 'service_detail')


# 	def perform_create(self, serializer):
# 			serializer.save() # Adding owner=self.request.user

# class ListServiceDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = ListService.objects.all()
# 	serializer_class = ListServiceSerializer
# 	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
