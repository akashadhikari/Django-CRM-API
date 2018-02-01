from datetime import date, timedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)
from rest_framework import filters
import django_filters.rest_framework

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


# Calculating Today's, Yesterday's, This Week's, This month's and This year's Client count.

class StatsViewSet(APIView):

	def get(self ,request, format=None):

		# count the number of entries since the given date -- in this case, yesterday to today
		today = date.today() - timedelta(1)
		ct_today = AddClient.objects.filter(created__gte=today).count()

		yesterday = date.today() - timedelta(1)
		day_before_yesterday = date.today() - timedelta(2)
		ct_yesterday = AddClient.objects.filter(created__range=(yesterday, day_before_yesterday)).count()

		week = date.today() - timedelta(7)
		ct_week = AddClient.objects.filter(created__gte=week).count()

		month = date.today() - timedelta(30)
		ct_month = AddClient.objects.filter(created__gte=month).count()

		year = date.today() - timedelta(365)
		ct_year = AddClient.objects.filter(created__gte=year).count()

		response_dict = {
			"Today" : ct_today,
			"Yesterday" : ct_yesterday,
			"This Week" : ct_week,
			"This Month" : ct_month,
			"This Year" : ct_year
		}

		return Response(response_dict)
