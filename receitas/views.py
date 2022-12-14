from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ReceitasModel
from .receitas_serializer import ReceitasSerializer


class Receitas(APIView):
    def get(self, request) -> Response:
        if request.GET.get("descricao") is not None:
            receitas = ReceitasModel.objects.filter(descricao__contains=request.GET.get("descricao"))
            return Response(data=ReceitasSerializer(receitas, many=True).data)
        else:
            receitas = ReceitasModel.objects.all()
            if len(receitas) >= 1:
                serializer = ReceitasSerializer(receitas, many=True)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
            else: return Response(status=status.HTTP_400_BAD_REQUEST, 
                                data={"error": "Não há dados cadastrados!"})
        

    def post(self, request) -> Response:
        serializer = ReceitasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data={"message": "Dados inseridos com sucesso!"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "Dados não inseridos com sucesso!"})


class ReceitasByID(APIView):
    def get(self, request, id):
        try:
            receitas = ReceitasModel.objects.get(id=id)
            serializer = ReceitasSerializer(receitas)
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        except: return Response(status=status.HTTP_400_BAD_REQUEST, 
                            data={"error": "Não há dados cadastrados para o id: {}!".format(id)})



    def delete(self, request, id):
        if len(ReceitasModel.objects.filter(id=id)) != 0:
            ReceitasModel.objects.filter(id=id).delete()
            return Response({"message": "Dados deletados com sucesso!"})
        else:
            return Response({"error": "Dados não encontrados para id: {}!".format(id)})
        
    
    def put(self, request, id):
        try:
            receita = ReceitasModel.objects.get(id=id)
            receita.id = request.data.get("id")
            receita.descricao = request.data.get("descricao")
            receita.valor = request.data.get("valor")
            receita.data = request.data.get("data")
            receita.save()
            return Response({"message": "Dados atualizados com sucesso!"})
        except ReceitasModel.DoesNotExist:
            return Response({"error": "Dados não encontrados para id: {}!".format(id)})


class ReceitasByAnoAndMes(APIView):
    def get(self, request, ano, mes):
        receitas = ReceitasModel.objects.filter(data__contains="{}-{}".format(ano, mes))
        if receitas.count() != 0:
            return Response(data=ReceitasSerializer(receitas, many=True).data)
        else: return Response({"error": "Não há dados neste periodo de ano: {} e mês: {}.".format(ano, mes)})
