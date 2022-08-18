from turtle import update
from django.db import models
from django.contrib.auth.models import User
from account.models import profile
# Create your models here.

class category(models.Model):
    name_cat=models.CharField(max_length=25)
    img_cat =models.ImageField(upload_to="media")
    desc_cat=models.TextField()
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name_cat

class Councelingdet(models.Model):
    name=models.CharField(max_length=25)
    mobile=models.CharField(max_length=11)
    staff=models.ForeignKey(User, on_delete=models.CASCADE)
    topic=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Service(models.Model):
    cate=models.ForeignKey(category,default=1,on_delete=models.CASCADE)
    name_ser=models.CharField(max_length=25)
    desc_ser=models.TextField()
    price_ser=models.IntegerField()
    img_ser=models.ImageField(upload_to="media")
    updated_on=models.DateTimeField(auto_now=True)
    

class cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    quantity=models.IntegerField()
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True, null=True)
    updated_on=models.DateTimeField(auto_now=True, null=True)
    def _str_(self):
        return self.user.username

class videolecture(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    service=models.ForeignKey(Service, on_delete=models.CASCADE)
    nameofvideo=models.CharField(max_length=50)
    lecture=models.FileField(upload_to="lecture/nameofvideo")
    desc_videolecture=models.TextField()
    updated_on=models.DateTimeField(auto_now=True,null=True)
    def _str_(self):
        return self.nameofvideo

class mocktest(models.Model):
    course=models.ForeignKey(Service,on_delete=models.CASCADE)
    link=models.CharField(max_length=50) 
    updated_on=models.DateTimeField(auto_now=True,null=True)
    def _str_(self):
        return self.course

class Order(models.Model):
    cust_id = models.ForeignKey(User,on_delete=models.CASCADE)
    cart_ids = models.CharField(max_length=250)
    product_ids = models.CharField(max_length=250)
    invoice_id = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    processed_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.cust_id.username

class review(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    desc_feed=models.TextField()
    img_feed=models.ImageField(upload_to="media",default="default\z.jpeg")
    updated_on=models.DateTimeField(auto_now=True,null=True)
    def _str_(self):
        return self.username

class studymaterial(models.Model):
    bran=models.ForeignKey(Service, on_delete=models.CASCADE)
    matname=models.CharField(max_length=30)
    materials=models.FileField(upload_to='materials')
    added_on=models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.matname

class feedback(models.Model):
    fname=models.ForeignKey(User,on_delete=models.CASCADE)
    prf=models.ForeignKey(profile,on_delete=models.CASCADE)
    brn=models.ForeignKey(Service,on_delete=models.CASCADE)
    email=models.CharField(max_length=100)
    rating=models.IntegerField(max_length=5)
    message=models.TextField(max_length=1000)
    added_on=models.DateTimeField(auto_now=True)
    def _str_(self):
        return self.fname.username