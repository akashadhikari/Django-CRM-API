from rest_framework import serializers

from .models import (
	AddCommunication,
	Suspecting,
	Prospecting,
	Approaching,
	Negotiation
	)

class SuspectingSerializer(serializers.ModelSerializer):

	class Meta:
		model = Suspecting
		fields = (
			'user', 
			'client', 
			'contact_verification', 
			'communication'
			)

class ProspectingSerializer(serializers.ModelSerializer):

	class Meta:
		model = Prospecting
		fields = (
			'user',
			'client',
			'communication',
			'showed_interest_for_later',
			'preferred_competitors',
			'not_interested',
			'dont_call_again',
			'interest_in_other_HR',
			'remarks'
			)

class ApproachingSerializer(serializers.ModelSerializer):

	class Meta:
		model = Approaching
		fields = (
			'user',
			'communication',
			'service_introduction',
			'business_renewal',
			'submit_proposal',
			'presentation'
			)

class NegotiationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Negotiation
		fields = (
			'user',
			'service_discussion',
			'discount_discussion'
			)

class AddCommunicationSuspectingSerializer(serializers.ModelSerializer):

	communication_suspecting = SuspectingSerializer(many=True)

	class Meta:
		model = AddCommunication
		fields = (
			'user', 
			'client', 
			'contact_person', 
			'medium', 
			'sales_stage', 
			'communication_suspecting',
			)

	def create(self, validated_data):
		communication_suspecting_data = validated_data.pop('communication_suspecting')
		addcommunication = AddCommunication.objects.create(**validated_data)
		for each in communication_suspecting_data:
			Suspecting.objects.create(addcommunication=addcommunication, **each)
		return addcommunication

class AddCommunicationProspectingSerializer(serializers.ModelSerializer):

	communication_prospecting = ProspectingSerializer(many=True)

	class Meta:
		model = AddCommunication
		fields = (
			'user', 
			'client', 
			'contact_person', 
			'medium', 
			'sales_stage',
			'communication_prospecting'
			)	

	def create(self, validated_data):
		communication_prospecting_data = validated_data.pop('communication_prospecting')
		addcommunication = AddCommunication.objects.create(**validated_data)
		for each in communication_prospecting_data:
			prospecting.objects.create(addcommunication=addcommunication, **each)
		return addcommunication

class AddCommunicationApproachingSerializer(serializers.ModelSerializer):

	communication_approaching = ApproachingSerializer(many=True)

	class Meta:
		model = AddCommunication
		fields = (
			'user', 
			'client', 
			'contact_person', 
			'medium', 
			'sales_stage',
			'communication_approaching'
			)	

	def create(self, validated_data):
		communication_approaching_data = validated_data.pop('communication_approaching')
		addcommunication = AddCommunication.objects.create(**validated_data)
		for each in communication_approaching_data:
			approaching.objects.create(addcommunication=addcommunication, **each)
		return addcommunication

class AddCommunicationNegotiationSerializer(serializers.ModelSerializer):

	communication_negotiation = NegotiationSerializer(many=True)

	class Meta:
		model = AddCommunication
		fields = (
			'user', 
			'client', 
			'contact_person', 
			'medium', 
			'sales_stage',
			'communication_negotiation'
			)	

	def create(self, validated_data):
		communication_negotiation_data = validated_data.pop('communication_negotiation')
		addcommunication = AddCommunication.objects.create(**validated_data)
		for each in communication_negotiation_data:
			negotiation.objects.create(addcommunication=addcommunication, **each)
		return addcommunication
