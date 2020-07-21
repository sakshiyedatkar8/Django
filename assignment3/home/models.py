from django.db import models

# Create your models here.
class Data(models.Model):
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phone=models.CharField( max_length=10)
    address=models.CharField( max_length=150)