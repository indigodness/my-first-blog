from django.db import models
from django.utils import timezone
from django.conf import settings
import os

class Product(models.Model):
   #  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    print("THIS IS PRINT",settings.MEDIA_ROOT+"/456339_XxqsMMx.jpg")
#    os.chdir(settings.MEDIA_ROOT)
    print(os.getcwd())
    photo = models.ImageField()
    description = models.TextField()
    dept = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
