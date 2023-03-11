from django.db import models

from django.contrib.auth.models  import  AbstractUser
from django.core.validators import MaxValueValidator ,MinValueValidator ,MinLengthValidator,MaxLengthValidator



# Create your models here.
# class Profile(models.models):
#     user=




class User(AbstractUser):
    email=models.EmailField(null=True)
    bio=models.TextField(null=True)
    avatar=models.ImageField(null=True,default="avatar.svg")

    
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    # email=models.EmailField(null=True)
    # bio=models.TextField(null=True)
    # avatar=models.ImageField(null=True,default="avatar.svg")



class Shop(models.Model):
    item=models.ForeignKey("Items", blank=True,on_delete=models.SET_NULL,null=True, related_name="items")
    shop_name=models.CharField(max_length=100 ,blank=True,unique=True)
    phone=models.TextField(validators=[MinLengthValidator(10),MaxLengthValidator(10)],null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    shop_host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    description=models.TextField(max_length=200,null=True)
    location=models.TextField(max_length=100,null=True)
    updated =models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['shop_name']


    def __str__(self):
        return self.shop_name

class Items(models.Model):
    name=models.CharField(max_length=100,null=True)
    price=models.PositiveIntegerField(validators=[MinValueValidator(1)],null=True)
    shop=models.ForeignKey(Shop,on_delete=models.SET_NULL,null=True)
    updated =models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    items_image=models.ImageField(null=True,default="base1items.jpg")

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name



class Ratings(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    shopname=models.ForeignKey(Shop,on_delete=models.CASCADE,related_name="shopname",null=True)
    stars=models.PositiveIntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(1)] )
    updated =models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
 



    class Meta:
        ordering=['-updated','-created']

    def __int__(self):
        return self.stars




class Message(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE)
    body=models.TextField(null=True,blank=True)
    updated =models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.body[0:50]



