from .models import Cuerda
from .models import Percusion
from .models import Amplificador
from .models import Accesorio
from .serializers import PercusionSerializer
from .serializers import AmplificadorSerializer
from .serializers import AccesorioSerializer
from .serializers import CuerdaSerializer
from rest_framework import viewsets


class CuerdaViewset(viewsets.ModelViewSet):
    queryset = Cuerda.objects.all()
    serializer_class = CuerdaSerializer



class PercusionViewset(viewsets.ModelViewSet):
    queryset = Percusion.objects.all()
    serializer_class = PercusionSerializer


class AmplificadorViewset(viewsets.ModelViewSet):
    queryset = Amplificador.objects.all()
    serializer_class = AmplificadorSerializer


class AccesorioViewset(viewsets.ModelViewSet):
    queryset = Accesorio.objects.all()
    serializer_class = AccesorioSerializer