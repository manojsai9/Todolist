from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class List(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    phone_number = models.IntegerField()
    def __str__(self):
        return self.name