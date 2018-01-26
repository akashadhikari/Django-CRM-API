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
			'user_name',
			'client',
			'client_name',
			'contact_person', 
			'medium',
			'medium_direction',
			'medium_status',
			'sales_stage', 
			'communication_suspecting',
			)

		# if fields contain communication_suspecting, then sales_stages can only be Suspecting
		# else, create a validation error

	def create(self, validated_data):
		communication_suspecting_data = validated_data.pop('communication_suspecting')
		addcommunication = AddCommunication.objects.create(**validated_data)
		for each in communication_suspecting_data:
			Suspecting.objects.create(addcommunication=addcommunication, **each)
		return addcommunication

	def update(self, instance, validated_data):

		# get native fields of the same model (exclusion of ForeignKey)

		instance.contact_person = validated_data.get('contact_person', instance.contact_person)
		instance.medium = validated_data.get('medium', instance.medium)
		instance.medium_direction = validated_data.get('medium_direction', instance.medium_direction)
		instance.medium_status = validated_data.get('medium_status', instance.medium_status)
		instance.sales_stage = validated_data.get('sales_stage', instance.sales_stage)
		instance.save()

		communication_suspecting = validated_data.get('communication_suspecting')

		if communication_suspecting:
			for each in communication_suspecting:
				comm_id = each.get('id', None)
				if comm_id:
					# get native fields + linked foreign field of the model to be nested
					comm_susp = Suspecting.objects.get(id=comm_id, communication=instance)
					comm_susp.communication = each.get('communication', comm_susp.communication)
					comm_susp.contact_verification = each.get('contact_verification', comm_susp.contact_verification)

					comm_susp.save()
				else:
					Suspecting.objects.create(account=instance, **each)

		return instance

class AddCommunicationProspectingSerializer(serializers.ModelSerializer):

	communication_prospecting = ProspectingSerializer(many=True)

	class Meta:
		model = AddCommunication
		fields = (
			'user',
			'user_name',
			'client',
			'client_name',
			'contact_person', 
			'medium',
			'medium_status', 
			'sales_stage',
			'communication_prospecting'
			)

	def create(self, validated_data):
		communication_prospecting_data = validated_data.pop('communication_prospecting')
		addcommunication = AddCommunication.objects.create(**validated_data)
		for each in communication_prospecting_data:
			prospecting.objects.create(addcommunication=addcommunication, **each)
		return addcommunication

	def update(self, instance, validated_data):

		# get native fields of the same model (exclusion of ForeignKey)

		instance.contact_person = validated_data.get('contact_person', instance.contact_person)
		instance.medium = validated_data.get('medium', instance.medium)
		instance.medium_direction = validated_data.get('medium_direction', instance.medium_direction)
		instance.medium_status = validated_data.get('medium_status', instance.medium_status)
		instance.sales_stage = validated_data.get('sales_stage', instance.sales_stage)
		instance.save()

		communication_prospecting = validated_data.get('communication_prospecting')

		if communication_prospecting:
			for each in communication_prospecting:
				comm_id = each.get('id', None)
				if comm_id:
					# get native fields + linked foreign field of the model to be nested
					comm_prosp = Prospecting.objects.get(id=comm_id, communication=instance)
					comm_prosp.communication = each.get('communication', comm_prosp.communication)
					comm_prosp.showed_interest_for_later = each.get('showed_interest_for_later', comm_prosp.showed_interest_for_later)
					comm_prosp.preferred_competitors = each.get('preferred_competitors', comm_prosp.preferred_competitors)
					comm_prosp.not_interested = each.get('not_interested', comm_prosp.not_interested)
					comm_prosp.dont_call_again = each.get('dont_call_again', comm_prosp.dont_call_again)
					comm_prosp.interest_in_other_HR = each.get('interest_in_other_HR', comm_prosp.interest_in_other_HR)
					comm_prosp.remarks = each.get('remarks', comm_prosp.remarks)
					comm_prosp.save()
				else:
					Prospecting.objects.create(account=instance, **each)

		return instance

class AddCommunicationApproachingSerializer(serializers.ModelSerializer):

	communication_approaching = ApproachingSerializer(many=True)

	class Meta:
		model = AddCommunication
		fields = (
			'user',
			'user_name',
			'client',
			'client_name',
			'contact_person', 
			'medium',
			'medium_status',
			'sales_stage',
			'communication_approaching'
			)	

	def create(self, validated_data):
		communication_approaching_data = validated_data.pop('communication_approaching')
		addcommunication = AddCommunication.objects.create(**validated_data)
		for each in communication_approaching_data:
			approaching.objects.create(addcommunication=addcommunication, **each)
		return addcommunication

	def update(self, instance, validated_data):

		# get native fields of the same model (exclusion of ForeignKey)

		instance.contact_person = validated_data.get('contact_person', instance.contact_person)
		instance.medium = validated_data.get('medium', instance.medium)
		instance.medium_direction = validated_data.get('medium_direction', instance.medium_direction)
		instance.medium_status = validated_data.get('medium', instance.medium_status)
		instance.sales_stage = validated_data.get('sales_stage', instance.sales_stage)
		instance.save()

		communication_approaching = validated_data.get('communication_approaching')

		if communication_approaching:
			for each in communication_approaching:
				comm_id = each.get('id', None)
				if comm_id:
					# get native fields + linked foreign field of the model to be nested
					comm_appr = Approaching.objects.get(id=comm_id, communication=instance)
					comm_appr.communication = each.get('communication', comm_appr.communication)
					comm_appr.service_introduction = each.get('service_introduction', comm_appr.service_introduction)
					comm_appr.business_renewal = each.get('business_renewal', comm_appr.business_renewal)
					comm_appr.submit_proposal = each.get('submit_proposal', comm_appr.submit_proposal)
					comm_appr.presentation = each.get('presentation', comm_appr.presentation)
					comm_appr.save()
				else:
					Approaching.objects.create(account=instance, **each)

		return instance

class AddCommunicationNegotiationSerializer(serializers.ModelSerializer):

	communication_negotiation = NegotiationSerializer(many=True)

	class Meta:
		model = AddCommunication
		fields = (
			'user',
			'user_name',
			'client',
			'client_name',
			'contact_person', 
			'medium',
			'medium_status',
			'sales_stage',
			'communication_negotiation'
			)	

	def create(self, validated_data):
		communication_negotiation_data = validated_data.pop('communication_negotiation')
		addcommunication = AddCommunication.objects.create(**validated_data)
		for each in communication_negotiation_data:
			negotiation.objects.create(addcommunication=addcommunication, **each)
		return addcommunication

	def update(self, instance, validated_data):

		# get native fields of the same model (exclusion of ForeignKey)

		instance.contact_person = validated_data.get('contact_person', instance.contact_person)
		instance.medium = validated_data.get('medium', instance.medium)
		instance.medium_direction = validated_data.get('medium_direction', instance.medium_direction)
		instance.medium_status = validated_data.get('medium_status', instance.medium_status)
		instance.sales_stage = validated_data.get('sales_stage', instance.sales_stage)
		instance.save()

		communication_negotiation = validated_data.get('communication_negotiation')

		if communication_negotiation:
			for each in communication_negotiation:
				comm_id = each.get('id', None)
				if comm_id:
					# get native fields + linked foreign field of the model to be nested
					comm_neg = Negotiation.objects.get(id=comm_id, communication=instance)
					comm_neg.communication = each.get('communication', comm_neg.communication)
					comm_neg.service_introduction = each.get('service_introduction', comm_neg.service_introduction)
					comm_neg.business_renewal = each.get('business_renewal', comm_neg.business_renewal)
					comm_neg.submit_proposal = each.get('submit_proposal', comm_neg.submit_proposal)
					comm_neg.presentation = each.get('presentation', comm_neg.presentation)
					comm_neg.save()
				else:
					Negotiation.objects.create(account=instance, **each)

		return instance

class StatsSerializer(serializers.ModelSerializer):

    inbound_call = serializers.ReadOnlyField()
    outbound_call = serializers.ReadOnlyField()
    inbound_email = serializers.ReadOnlyField()
    outbound_email = serializers.ReadOnlyField()
    sms = serializers.ReadOnlyField()
    meeting = serializers.ReadOnlyField()


    class Meta:
        model = AddCommunication
        fields = ('inbound_call', 'outbound_call', 'inbound_email', 'outbound_email', 'sms', 'meeting')
