from rest_framework import serializers
from .models import Cuerda
from .models import Percusion
from .models import Amplificador
from .models import Accesorio

class CuerdaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Cuerda
        fields = '__all__'


class PercusionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Percusion
        fields = '__all__'


class AmplificadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Amplificador
        fields = '__all__'


class AccesorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Accesorio
        fields = '__all__'