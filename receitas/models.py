from django.db import models



class Receitas(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField(null=False)
    valor = models.FloatField(null=False)
    data = models.DateTimeField(null=False)
    
    
    class Meta:
        ordering = ['id', 'descricao', 'valor', 'data']
    
    
    def __init__(self, descricao=None, valor=None, data=None, *args, **kwargs) -> None:
        self.descricao = descricao
        self.valor = valor
        self.data = data
