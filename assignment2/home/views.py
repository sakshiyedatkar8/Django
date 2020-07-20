from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request,"home.html")

def getdata(request):
    w=float(request.GET['weight'])    
    h=float(request.GET['height'])
    res = w/(h*h)

    return render(request,"result.html", {'result':res})
    