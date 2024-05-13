from rest_framework.views import APIView
from CanalEticoApp.models import Comunicado
from CanalEticoApp.api.serializers import ComunicadoSerializer
from rest_framework.response import Response

class ComunicadoAPIView(APIView):
    
    def get(self, request):
        comunicados = Comunicado.objects.all().order_by('solucionado', 'fecha')
        comunicados_serializer = ComunicadoSerializer(comunicados, many=True)
        return Response(comunicados_serializer.data)