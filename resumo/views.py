from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from receitas.models import ReceitasModel

from despesas.models import DespesasModel



class Resumo(APIView):
    def get(self, request, ano, mes):
        total_receitas = self.get_total_receitas(ano, mes)
        total_despesas = self.get_total_despesas(ano, mes)
        print(total_receitas, total_despesas)
        saldo_final = total_receitas - total_despesas
        total_gasto_por_categoria = self.get_total_gasto_por_categoria(ano, mes); 
        return Response(data={
            "total receitas": total_receitas,
            "total despesas": total_despesas,
            "saldo final": saldo_final,
            "total gasto por categoria": total_gasto_por_categoria
        }, status=status.HTTP_200_OK)
    
    
    def get_total_despesas(self, ano, mes):
        despesas = DespesasModel.objects.filter(data__contains="{}-{}".format(ano, mes))
        value: float = 0
        for row in despesas:
            value += row.valor
        return value
    
    
    def get_total_receitas(self, ano, mes):
        receitas = ReceitasModel.objects.filter(data__contains="{}-{}".format(ano, mes))
        value: float = 0
        for row in receitas:
            value += row.valor
        return value
    
    
    def get_total_gasto_por_categoria(self, ano, mes):
        despesas = DespesasModel.objects.filter(data__contains="{}-{}".format(ano, mes))
        dict_categorias = self.get_dict_categorias()
        for row in despesas:
            dict_categorias[row.categoria] += row.valor
        return dict_categorias
    
    
    def get_dict_categorias(self) -> dict:
        return {
            "Alimentação": 0.00,
            "Saúde": 0.00,
            "Moradia": 0.00,
            "Transporte": 0.00,
            "Educação": 0.00,
            "Lazer": 0.00,
            "Imprevistos": 0.00,
            "Outras": 0.00
        }
