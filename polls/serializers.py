from rest_framework import serializers
from .models import Vendas

class VendasSerializer(serializers.ModelSerializer):

    class Meta:

        model = Vendas
        fields = '__all__'