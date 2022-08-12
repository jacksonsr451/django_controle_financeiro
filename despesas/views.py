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
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, 
                            data={"error": "Não há dados cadastrados!"})
        

    def post(self, request) -> Response:
        serializer = DespesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data={"message": "Dados inseridos com sucesso!"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "Dados não inseridos com sucesso!"})

