from rest_framework import serializers
from .models import Clientlist, SalesStage


class ClientlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientlist
        fields = '__all__'

class SalesStageSerializer(serializers.ModelSerializer):
	class Meta:
		model = SalesStage
		fields = '__all__'