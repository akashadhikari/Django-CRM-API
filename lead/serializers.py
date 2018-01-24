from rest_framework import serializers
from .models import LeadProcess


class LeadProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadProcess
        fields = (
			'id',
        	'user',
        	'username',
            'client',
        	'employer_name',
        	'client_value',
        	'client_address',
        	'contact_person',
        	'pan_no',
        	'billing_name',
        	'service_type',
            'stages',
        	'bulk',
        	'amount', 
        	'discount_entry', 
        	'discount', 
        	'vat_percent', 
        	'total_amount', 
        	'total_invoicing_amount',
        	'last_communicated',
        	'last_status',
        	'last_service_taken',
        	'last_service_name',
        	'created',
        )

class StatsSerializer(serializers.ModelSerializer):

    top_job = serializers.ReadOnlyField()
    hot_job = serializers.ReadOnlyField()
    f_post = serializers.ReadOnlyField()
    g_post = serializers.ReadOnlyField()

    class Meta:
        model = LeadProcess
        fields = ('top_job', 'hot_job', 'f_post', 'g_post')