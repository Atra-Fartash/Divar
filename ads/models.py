from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)


class Category(models.Model):
    title = models.CharField(max_length=100)


class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)


class Area(models.Model):
    city = models.ForeignKey(to= City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)


class Ad(models.Model):
    user = models.ForeignKey(to= User, on_delete=models.CASCADE) 
    category = models.ForeignKey(to= Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    picture = models.ImageField(null=True, blank=True)
    attribute = models.CharField(max_length=100, null=True, blank=True)
    city = models.ForeignKey(to= City, on_delete=models.CASCADE)
    area = models.ForeignKey(to= Area, on_delete=models.CASCADE)


class Reports(models.Model):
    user = models.ForeignKey(to= User, on_delete=models.CASCADE)
    ad = models.ForeignKey(to= Ad, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)


class Message(models.Model):
    user = models.ForeignKey(to= User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

class Payment(models.Model):
    user = models.ForeignKey(to= User, on_delete=models.CASCADE)
    ad = models.ForeignKey(to= Ad, on_delete=models.CASCADE)
    amount = models.IntegerField()



