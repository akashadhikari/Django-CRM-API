from django.contrib.auth.models import User

import django_filters.rest_framework
from rest_framework import generics
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)
from rest_framework import filters

from .permissions import IsOwnerOrReadOnly, IsSameUser

from .serializers import (
	UserSerializer
	)

class UserViewSet(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAuthenticated,)

class UserDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAuthenticated, IsSameUser)
