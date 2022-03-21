from django.db import models

# Create your models here.

class User(models.Model):
    name= models.CharField(max_length=30)
    alias= models.CharField(max_length=30)
    email= models.EmailField(max_length=30)
    birthday= models.CharField(max_length=20)
    country= models.CharField(max_length=30)

    def __str__(self):
        return f'User: {self.alias}'

class Professional(models.Model):
    name= models.CharField(max_length=30)
    email= models.EmailField(max_length=30)
    ssn= models.IntegerField()
    area= models.CharField(max_length=20)
    
    def __str__(self):
        return f'Profesional: {self.name}, social security number {self.SSN} in {self.area}'
    
class Business(models.Model):
    business_name= models.CharField(max_length=30)
    tin= models.IntegerField()
    area= models.CharField(max_length=30)
    email= models.EmailField(max_length=30)
    
    
    def __str__(self):
        return f'Business: {self.business_name} of area {self.area}'