from rest_framework import serializers

from .models import (
	AddClient,
	)

class AddClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddClient
        fields = '__all__'