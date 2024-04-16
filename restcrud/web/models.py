from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=250)
    created_time=models.DateTimeField(auto_now_add=True)