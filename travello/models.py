from django.db import models


class Destination(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField()
    img = models.ImageField(upload_to='pics')
    price= models.IntegerField()
    offer= models.BooleanField(default=False)