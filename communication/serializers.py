from rest_framework import serializers

from .models import (
	AddCommunication,
	)

class AddCommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCommunication
        fields = '__all__'