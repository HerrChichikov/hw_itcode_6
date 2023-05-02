from django.db import models


# Create your models here.
class Worker(models.Model):
    photo = models.ImageField(upload_to="photos/")
    fio = models.CharField(max_length=255)
    position = models.CharField(max_length=50)
    home_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)
    mail = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)

