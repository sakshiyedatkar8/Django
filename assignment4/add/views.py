from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
# Create your views here.

def addpage(request):
    return render(request,"add.html")

def getdata(request):
    user_name = request.GET['uname']
    password = request.GET['pass']
    phone = request.GET['phone']
    address = request.GET['address']
    database = models.Data(user_name = user_name, password = password, phone = phone,address = address)
    database.save()
    return render(request,"submit.html")  

def show_data(request):
    data = Data.objects.all()
    dat = {
        'all_data':data
    }
    return render(request,'show.html',dat)






