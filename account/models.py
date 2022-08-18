from django.db import models
from django.contrib.auth.models import User

from home.models import*
# Create your models here.
class profile(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    img_pro=models.ImageField(upload_to="media", default="default\default-user.png")
    addr_pro=models.TextField(default="lko")
    ph_pro=models.IntegerField(default="0213456782")
    updated_on=models.DateTimeField(auto_now=True)
    substatus=models.BooleanField(default=False)
    def __str__(self):
        return self.usr.username