from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import viewsets
from django.core.mail import send_mail




def index(request):
    return render(request, 'web/index.html')



def contacto(request):
    if request.method == 'POST':
        name = request.POST.get('nombre')
        subject = request.POST.get('asunto')
        email = request.POST.get('email')
        message = request.POST.get('mensaje')

        data = {
                'name': name,
                'subject': subject,
                'email':email,
                'message': message      
        }
        message= '''
        Nuevo mensaje: {}


        De: {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'], message,'',['djangoexamen@gmail.com'])
    return render(request, 'web/contacto.html')





