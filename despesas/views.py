from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import DespesasModel
from .despesa_serializer import DespesaSerializer


class Despesas(APIView):
    def get(self, request) -> Response:
        despesas = DespesasModel.objects.all()
        if len(despesas) >= 1:
            serializer = DespesaSerializer(despesas, many=True)
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        else: return Response(status=status.HTTP_400_BAD_REQUEST, 
                            data={"error": "Não há dados cadastrados!"})
        

    def post(self, request) -> Response:
        serializer = DespesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data={"message": "Dados inseridos com sucesso!"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "Dados não inseridos com sucesso!"})


class DespesasByID(APIView):
    def get(self, request, id):
        try:
            despesas = DespesasModel.objects.get(id=id)
            serializer = DespesaSerializer(despesas)
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        except: return Response(status=status.HTTP_400_BAD_REQUEST, 
                            data={"error": "Não há dados cadastrados para o id: {}!".format(id)})



    def delete(self, request, id):
        if len(DespesasModel.objects.filter(id=id)) is not 0:
            DespesasModel.objects.filter(id=id).delete()
            return Response({"message": "Dados deletados com sucesso!"})
        else:
            return Response({"error": "Dados não encontrados para id: {}!".format(id)})
        
    
    def put(self, request, id):
        despesas = DespesasModel.objects.get(id=id)
        if despesas is not None:
            despesas.id = request.data.get("id")
            despesas.descricao = request.data.get("delen(despesas)scricao")
            despesas.valor = request.data.get("valor")
            despesas.data = request.data.get("data")
            despesas.save()
            return Response({"message": "Dados atualizados com sucesso!"})
        else:
            return Response({"error": "Dados não encontrados para id: {}!".format(id)})
