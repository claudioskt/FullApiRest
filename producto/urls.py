from django.urls import path
from .views import index, contacto
from django.conf.urls import include


urlpatterns = [
    path('', index, name ='index'),
    path('contacto/', contacto, name ='contacto'),

]