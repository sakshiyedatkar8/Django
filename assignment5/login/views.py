from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Register

# Create your views here.
def loginpage(request):
    return render(request,"login.html")

    
def result(request):
    if request.method=='GET':
        user_name = request.GET['uname']
        password = request.GET['pass']
    try:
        result = Register.objects.get(user_name=user_name ,password=password)
    except Register.DoesNotExist:
        result = ''
    return render(request,'login1.html',{'Result':result})


def registrationpage(request):
    return render(request,"registration.html")

def getdata(request):
    user_name = request.GET['uname']
    password = request.GET['pass']
    phone = request.GET['phone']
    mail = request.GET['mail']
    database = Register(user_name = user_name, password = password, phone = phone, mail = mail)
    database.save()
    return render(request,"register.html")  





