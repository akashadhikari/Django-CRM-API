from rest_framework import serializers

from .models import (
	AddCommunication,
	Suspecting,
	Prospecting,
	)

class AddCommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCommunication
        fields = '__all__'

class SuspectingSerializer(serializers.ModelSerializer):
	#communications = AddCommunicationSerializer(many=True)
	class Meta:
		model = Suspecting
		fields = ('user', 'client', 'contact_verification', 'communications')

		# def create(self, validated_data):
		# 	communications_data = validated_data.pop('communications')
		# 	suspecting = Suspecting.objects.create(**validated_data)
		# 	for client_data in communications_data:
		# 		AddCommunication.objects.create(suspecting=suspecting, **communications_data)
		# 	return suspecting

class ProspectingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Prospecting
		fields = '__all__'