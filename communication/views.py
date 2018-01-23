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
	AddCommunication,
	Suspecting,
	Prospecting
	)
from .serializers import (
	AddCommunicationSerializer,
	SuspectingSerializer,
	ProspectingSerializer
	)

class AddCommunicationViewSet(generics.ListCreateAPIView):
	queryset = AddCommunication.objects.all()
	serializer_class = AddCommunicationSerializer
	permission_classes = (IsAuthenticated,)

	filter_backends = (
		filters.SearchFilter, 
		filters.OrderingFilter, 
		django_filters.rest_framework.DjangoFilterBackend,
		)
	filter_fields = ('medium', 'contact_person')
	search_fields = ('medium', 'contact_person')


	def perform_create(self, serializer):
			serializer.save() # Adding owner=self.request.user

class AddCommunicationDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = AddCommunication.objects.all()
	serializer_class = AddCommunicationSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class SuspectingViewSet(generics.ListCreateAPIView):
	queryset = Suspecting.objects.all()
	serializer_class = SuspectingSerializer
	permission_classes = (IsAuthenticated,)

	filter_backends = (
		filters.SearchFilter, 
		filters.OrderingFilter, 
		django_filters.rest_framework.DjangoFilterBackend,
		)
	# filter_fields = ('medium', 'contact_person')
	# search_fields = ('medium', 'contact_person')


	def perform_create(self, serializer):
			serializer.save() # Adding owner=self.request.user

class SuspectingDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = Suspecting.objects.all()
	serializer_class = SuspectingSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class ProspectingViewSet(generics.ListCreateAPIView):
	queryset = Prospecting.objects.all()
	serializer_class = ProspectingSerializer
	permission_classes = (IsAuthenticated,)

	filter_backends = (
		filters.SearchFilter, 
		filters.OrderingFilter, 
		django_filters.rest_framework.DjangoFilterBackend,
		)
	# filter_fields = ('medium', 'contact_person')
	# search_fields = ('medium', 'contact_person')


	def perform_create(self, serializer):
			serializer.save() # Adding owner=self.request.user

class ProspectingDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = Prospecting.objects.all()
	serializer_class = ProspectingSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)