from collections import UserString
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import *


# Create your models here.
class User(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    img = models.ImageField()

    class Meta:
        ordering = ["-username"]

    def __str__(self):
        return self.username


class Brand(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f"{self.name}"

class Company(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f"{self.title}"

class Condition(models.Model):
    Condition = models.CharField(max_length=50)
    def __str__(self) -> str:
         return f"{self.Condition}"

class Size(models.Model):
    Size = models.CharField(max_length=30)
    def __str__(self) -> str:
         return f"{self.Size}"

# yangi
class Color(models.Model):
    Color = models.CharField(max_length=30)
    def __str__(self) -> str:
         return f"{self.Color}"


# yangi
class Country(models.Model):
    Country = models.CharField(max_length=30)
    def __str__(self) -> str:
         return f"{self.Country}"

# yangi
class Region(models.Model):
    Region = models.CharField(max_length=30)
    def __str__(self) -> str:
         return f"{self.Region}"

# yangi
class Features(models.Model):
    Features = models.CharField(max_length=30)
    def __str__(self) -> str:
         return f"{self.Features}"


class Material(models.Model):
    Material = models.CharField(max_length=30)
    def __str__(self) -> str:
         return f"{self.Material}"

class Technique(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.FloatField()
    abaut = models.CharField(max_length=500)
    img = models.ImageField(upload_to= 'static/images')
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    features = models.ForeignKey(Features,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} {self.company} {self.price} {self.brand} {self.img}  {self.color} "

class Aksiya_Code(models.Model):
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.date_from} {self.date_to}"

class Aksiya(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    old_price = models.FloatField()
    new_price = models.FloatField()
    abaut = models.CharField(max_length=500)
    img = models.ImageField(upload_to= 'static/images')
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    features = models.ForeignKey(Features,on_delete=models.CASCADE)
    code = models.ForeignKey(Aksiya_Code,on_delete=models.CASCADE)
    chegirma = models.IntegerField()    
    def __str__(self) -> str:
        return f"{self.name} {self.company}  {self.brand} {self.new_price} {self.old_price} {self.img}  {self.color} "



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    technique = models.ForeignKey(Technique, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.user} {self.technique}"



    def save(self):
        return super().save()
