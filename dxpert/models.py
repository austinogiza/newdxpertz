from django.db import models
from datetime import datetime

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.BigIntegerField(blank=False)
    time = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=2000, blank=False)

    def __str__(self):
        return self.name
