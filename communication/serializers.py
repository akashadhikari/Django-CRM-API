from rest_framework import serializers
from .models import Clientlist


class ClientlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientlist
        fields = '__all__'