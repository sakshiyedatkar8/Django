from django.shortcuts import render

from django.http import HttpResponse
from . import models
# Create your views here.
def homepage(request):
    
    return render(request,"home.html")

def getdata(request):
    user_name = request.GET['uname']
    password = request.GET['pass']
    phone = request.GET['phone']
    address = request.GET['address']
    database = models.Data(user_name = user_name, password = password, phone = phone,address = address)
    database.save()
    return render(request,"submit.html")  