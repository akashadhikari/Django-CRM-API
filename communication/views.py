import django_filters.rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from rest_framework import filters

from common.filters import DateRangeFilter
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
	NegotiationSerializer,
	)
from django.contrib.auth.models import User
from django.db.models import Count


class AddCommunicationNegotiationViewSet(generics.ListCreateAPIView):
	queryset = AddCommunication.objects.all()
	serializer_class = AddCommunicationNegotiationSerializer
	permission_classes = (IsAuthenticated,)

	filter_backends = (
		filters.SearchFilter, 
		filters.OrderingFilter, 
		django_filters.rest_framework.DjangoFilterBackend,
		DateRangeFilter
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
		DateRangeFilter
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
		DateRangeFilter
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
		DateRangeFilter
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
		DateRangeFilter
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
		DateRangeFilter
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
		DateRangeFilter
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
		DateRangeFilter
		)
	# filter_fields = ('medium', 'contact_person')
	# search_fields = ('medium', 'contact_person')


	def perform_create(self, serializer):
			serializer.save() # Adding owner=self.request.user

class NegotiationDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = Negotiation.objects.all()
	serializer_class = NegotiationSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class StatsViewSet(APIView):

	def get(self ,request, format=None):

		call = AddCommunication.objects.filter(medium='Call').count()
		email = AddCommunication.objects.filter(medium='Email').count()
		sms = AddCommunication.objects.filter(medium='SMS').count()
		meeting = AddCommunication.objects.filter(medium='Meeting').count()

		response_dict = {
			"Call" : call,
			"Email" : email,
			"SMS" : sms,
			"Meeting" : meeting,
		}

		return Response(response_dict)


class CoreCRMViewset(APIView):

	#permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):

		usernames = [user.username for user in User.objects.all()]

		suspecting = [Suspecting.objects.all().aggregate(Count('suspecting_substages'))]

		prospecting = [Prospecting.objects.all().aggregate(Count('prospecting_substages'))]

		approaching = [Approaching.objects.all().aggregate(Count('approaching_substages'))]

		negotiation = [Negotiation.objects.all().aggregate(Count('negotiation_substages'))]

		response_dict = {

			"userlist" : usernames,

			"suspecting" : suspecting,

			"prospecting" : prospecting,

			"approaching" : approaching,

			"negotiation" : negotiation,


			}

		return Response(response_dict)

# mydict = {'carl':40,
#           'alan':2,
#           'bob':1,
#           'danny':3}

# for key in sorted(mydict.iterkeys()):
#     print "%s: %s" % (key, mydict[key])

# >>> from communication.models import AddCommunication, Suspecting, Prospecting, Negotiation
# >>> from django.db.models import Count
# >>> com = Suspecting.objects.annotate(num_clients=Count('client'))
# >>> com[0]
# <Suspecting: Apple>
# >>> com[0].num_clients
# 1
