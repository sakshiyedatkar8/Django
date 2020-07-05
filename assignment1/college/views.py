from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

def cse(request):
    res=JsonResponse({'name':'Welcome on CSE page'})
    return res

def etc(request):
    return HttpResponse("Welcome on ETC page")

def mech(request):
    return HttpResponse("Welcome on Mech page")
   
def civil(request):
    return HttpResponse("Welcome on CIVIL page")   