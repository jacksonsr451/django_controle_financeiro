from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import DespesasModel
from .despesa_serializer import DespesaSerializer


class Despesas(APIView):
    def get(self, request) -> Response:
        try:
            return Response(
                status=status.HTTP_200_OK,
                data=DespesaSerializer(data=DespesasModel.objects.all(), many=True).data
            )
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, 
                            data={"error": "Não há dados cadastrados!"})
        

    def post(self, request) -> Response:
        serializer = DespesaSerializer(data=request.data)
        if serializer.is_valid() and self.validate_post(request.data):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data={"message": "Dados inseridos com sucesso!"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "Dados não inseridos com sucesso!"})

    
    def validate_post(self, request) -> bool:
        despesas = DespesasModel.objects.all()
        for despesa in despesas:
            data_atual = despesa.data.__str__().split('-')
            if despesa.descricao.__eq__(request["descricao"]):
                if data_atual[1].__eq__(request["data"].split('-')[1])  \
                    and data_atual[0].__eq__(request["data"].split('-')[0]):
                    return False
        return True
