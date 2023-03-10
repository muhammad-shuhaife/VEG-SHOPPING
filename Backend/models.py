from django.db import models


class logindb(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    Password=models.CharField(max_length=30,null=True,blank=True)

class admindb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Email=models.EmailField(max_length=30,null=True,blank=True)
    Username=models.CharField(max_length=30,null=True,blank=True)
    Password=models.CharField(max_length=30,null=True,blank=True)
    Confirmpassword=models.CharField(max_length=30,null=True,blank=True)
    Image=models.ImageField(upload_to="admin",null=True,blank=True)

class categorydb(models.Model):
        Name = models.CharField(max_length=30, null=True, blank=True)
        Description = models.CharField(max_length=30, null=True, blank=True)
        Image = models.ImageField(upload_to="category", null=True, blank=True)

class productdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Category=models.CharField(max_length=30,null=True,blank=True)
    Description=models.CharField(max_length=30,null=True,blank=True)
    Price=models.CharField(max_length=30,null=True,blank=True)
    Quantity=models.CharField(max_length=30,null=True,blank=True)
    Image=models.ImageField(upload_to="product",null=True,blank=True)











# Create your models here.
