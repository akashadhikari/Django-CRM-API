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
	Prospecting,
	Approaching,
	Negotiation
	)
from .serializers import (
	AddCommunicationSuspectingSerializer,
	AddCommunicationProspectingSerializer,
	AddCommunicationApproachingSerializer,
	AddCommunicationNegotiationSerializer,
	SuspectingSerializer,
	ProspectingSerializer,
	ApproachingSerializer,
	NegotiationSerializer
	)

class AddCommunicationNegotiationViewSet(generics.ListCreateAPIView):
	queryset = AddCommunication.objects.all()
	serializer_class = AddCommunicationNegotiationSerializer
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

class AddCommunicationNegotiationDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = AddCommunication.objects.all()
	serializer_class = AddCommunicationNegotiationSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class AddCommunicationApproachingViewSet(generics.ListCreateAPIView):
	queryset = AddCommunication.objects.all()
	serializer_class = AddCommunicationApproachingSerializer
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

class AddCommunicationApproachingDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = AddCommunication.objects.all()
	serializer_class = AddCommunicationApproachingSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class AddCommunicationProspectingViewSet(generics.ListCreateAPIView):
	queryset = AddCommunication.objects.all()
	serializer_class = AddCommunicationProspectingSerializer
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

class AddCommunicationProspectingDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = AddCommunication.objects.all()
	serializer_class = AddCommunicationProspectingSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class AddCommunicationSuspectingViewSet(generics.ListCreateAPIView):
	queryset = AddCommunication.objects.all()
	serializer_class = AddCommunicationSuspectingSerializer
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

class AddCommunicationSuspectingDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = AddCommunication.objects.all()
	serializer_class = AddCommunicationSuspectingSerializer
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

class ApproachingViewSet(generics.ListCreateAPIView):
	queryset = Approaching.objects.all()
	serializer_class = ApproachingSerializer
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

class ApproachingDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = Approaching.objects.all()
	serializer_class = ApproachingSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class NegotiationViewSet(generics.ListCreateAPIView):
	queryset = Negotiation.objects.all()
	serializer_class = NegotiationSerializer
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

class NegotiationDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = Negotiation.objects.all()
	serializer_class = NegotiationSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)