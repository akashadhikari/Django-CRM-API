from rest_framework import serializers
from .models import LeadProcess


class LeadProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadProcess
        fields = ('id', 'service', 'status', 'income', 'discount', 'unit', 'bulk', 'stage', 'created', 'tax_percent', 'user', 'username')

class StatsSerializer(serializers.ModelSerializer):

    hardware_count = serializers.ReadOnlyField()
    software_count = serializers.ReadOnlyField()

    class Meta:
        model = LeadProcess
        fields = ('hardware_count', 'software_count')