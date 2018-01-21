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
	Album,
	Track,
	)
from .serializers import (
	AlbumSerializer,
	TrackSerializer,
	)

class AlbumViewSet(generics.ListCreateAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
	#permission_classes = (IsAuthenticated,)

	filter_backends = (
		filters.SearchFilter,
		filters.OrderingFilter,
		django_filters.rest_framework.DjangoFilterBackend,
		)
	# filter_fields = ('album_incharge', 'Album_address')
	# search_fields = ('album_incharge', 'Album_address')


	def perform_create(self, serializer):
			serializer.save() # Adding owner=self.request.user

class AlbumDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

class TrackViewSet(generics.ListCreateAPIView):
	queryset = Track.objects.all()
	serializer_class = TrackSerializer
	#permission_classes = (IsAuthenticated,)

	filter_backends = (
		filters.SearchFilter,
		filters.OrderingFilter,
		django_filters.rest_framework.DjangoFilterBackend,
		)
	# filter_fields = ('outflowed_to', 'service_outflowed')
	# search_fields = ('outflowed_to', 'service_outflowed')


	def perform_create(self, serializer):
			serializer.save() # Adding owner=self.request.user

class TrackDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = Track.objects.all()
	serializer_class = TrackSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)