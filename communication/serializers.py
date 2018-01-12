from rest_framework import serializers
from .models import Clientlist, SalesStage, SalesSub


class ClientlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientlist
        fields = '__all__'

class SalesStageSerializer(serializers.ModelSerializer):
	class Meta:
		model = SalesStage
		fields = '__all__'

class SalesSubSerializer(serializers.ModelSerializer):
	class Meta:
		model = SalesSub
		fields = '__all__'