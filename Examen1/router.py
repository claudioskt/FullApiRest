from producto.viewsets import CuerdaViewset
from producto.viewsets import PercusionViewset
from producto.viewsets import AmplificadorViewset
from producto.viewsets import AccesorioViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cuerda',CuerdaViewset)
router.register('percusion',PercusionViewset)
router.register('amplificador',AmplificadorViewset)
router.register('accesrorio',AccesorioViewset)