from django.db import models


class CategoriasEnum(models.TextChoices):
    ALIMENTACAO = "Alimentação"
    SAUDE = "Saúde"
    MORADIA = "Moradia"
    TRANSPORTE = "Transporte"
    EDUCACAO = "Educação"
    LAZER = "Lazer"
    IMPREVISTOS = "Imprevistos"
    OUTRAS = "Outras"


class DespesasModel(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=11, 
                                choices=CategoriasEnum.choices,
                                default=CategoriasEnum.OUTRAS)
    descricao = models.CharField(max_length=255, null=False, unique_for_month="data")
    valor = models.FloatField(null=False)
    data = models.DateTimeField(null=False)
    
    
    class Meta:
        db_table = "despesas"
    
    