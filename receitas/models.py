from django.db import models



class ReceitasModel(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255, null=False, unique_for_month="data")
    valor = models.FloatField(null=False)
    data = models.DateTimeField(null=False)
    
    
    class Meta:
        db_table = "receitas"
    
