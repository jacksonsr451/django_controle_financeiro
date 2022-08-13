from rest_framework import serializers

from .models import DespesasModel


class DespesaSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(required=False)
    descricao = serializers.CharField(required=True)
    valor = serializers.FloatField(required=True)
    data = serializers.DateTimeField(required=True)
    
    class Meta:
        model = DespesasModel
        fields = ["id", "categoria", "descricao", "valor", "data"]
        