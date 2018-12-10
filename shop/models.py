from django.db import models
from django.utils import timezone
from django.conf import settings

class Product(models.Model):
   #  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    print(settings.MEDIA_ROOT+"/456339.jpg")
    photo = models.ImageField(default=settings.MEDIA_ROOT+"/456339.jpg")
    description = models.TextField()
    dept = models.CharField(max_length = 50)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name