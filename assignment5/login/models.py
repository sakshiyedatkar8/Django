from django.db import models

# Create your models here.
class Register(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField( max_length=10)
    mail = models.CharField( max_length=150)