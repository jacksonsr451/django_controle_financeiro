from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK



@api_view(['GET'])
def index(request):
    return Response(status=HTTP_200_OK, data={"message": "ok"})
