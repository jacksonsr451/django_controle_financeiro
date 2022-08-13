from rest_framework import serializers

from .models import ReceitasModel


class ReceitasSerializer(serializers.ModelSerializer):
    descricao = serializers.CharField(required=True)
    valor = serializers.FloatField(required=True)
    data = serializers.DateTimeField(required=True)
    
    class Meta:
        model = ReceitasModel
        fields = ["id", "descricao", "valor", "data"]
        