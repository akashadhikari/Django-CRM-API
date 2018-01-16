from rest_framework import serializers
from .models import LeadProcess


class LeadProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadProcess
        fields = (
        	'user',
        	'username',
        	'employer_name',
        	'client_value',
        	'client_address',
        	'contact_person',
        	'pan_no',
        	'billing_name',
        	'service_type',
        	'post_type',
        	'bulk',
        	'post_choice',
        	'amount', 
        	'discount_entry', 
        	'discount', 
        	'vat_percent', 
        	'total_amount', 
        	#'total_invoicing_amount',
        	'last_communicated',
        	'last_status',
        	'last_service_taken',
        	'last_service_name',
        	'created',
        )

class StatsSerializer(serializers.ModelSerializer):

    hardware_count = serializers.ReadOnlyField()
    software_count = serializers.ReadOnlyField()

    class Meta:
        model = LeadProcess
        fields = ('hardware_count', 'software_count')