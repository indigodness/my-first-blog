from django.db import models
from django.utils import timezone


class Product(models.Model):
   #  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    photo = models.ImageField()
    description = models.TextField()
    dept = models.CharField(max_length = 50)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name