from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('',views.loginpage,name="loginpage"),
    path('registrationpage',views.registrationpage,name="registrationpage"),
    path('check',views.getdata,name="getdata"),
    path('after_login',views.result,name='result')
    
]
