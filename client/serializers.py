from rest_framework import serializers

from .models import (
    AddClient,
    ListOfProduct
    )

class ListOfProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfProduct
        fields = '__all__'

class AddClientSerializer(serializers.ModelSerializer):

    #client_listofproduct = ListOfProductSerializer

    class Meta:
        model = AddClient
        fields = '__all__'

class StatsSerializer(serializers.ModelSerializer):

    today_created = serializers.ReadOnlyField()
    yesterday_created = serializers.ReadOnlyField()
    this_week_created = serializers.ReadOnlyField()
    this_month_created = serializers.ReadOnlyField()
    this_year_created = serializers.ReadOnlyField()

    class Meta:
        model = AddClient
        fields = ('today_created', 'yesterday_created', 'this_week_created', 'this_month_created', 'this_year_created')
