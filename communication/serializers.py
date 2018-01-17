from rest_framework import serializers
from .models import ClientDetail, SalesStage, SalesSub


class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientDetail
        fields = '__all__'

class SalesStageSerializer(serializers.ModelSerializer):
	class Meta:
		model = SalesStage
		fields = '__all__'

class SalesSubSerializer(serializers.ModelSerializer):
	class Meta:
		model = SalesSub
		fields = '__all__'