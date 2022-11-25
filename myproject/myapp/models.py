from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    fullname=models.CharField(max_length=200)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    mobile=models.IntegerField()




