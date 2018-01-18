from rest_framework import serializers

from .models import (
	ClientDetail,
	SalesStage,
	SalesSub,
	Branch,
	BusinessOutflow,
	ListService
	)

class BranchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Branch
		fields = '__all__'

class BusinessOutflowSerializer(serializers.ModelSerializer):
	class Meta:
		model = BusinessOutflow
		fields = '__all__'
		
class ListServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = ListService
		fields = '__all__'

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