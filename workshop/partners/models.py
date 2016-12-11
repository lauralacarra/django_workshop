from django.db import models
from django.utils import timezone

# Create your models here.
class Partner(models.Model):
    email = models.EmailField(max_length=200, null=False)
    name = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=50, null=False)
    created_date = models.DateTimeField(default=timezone.now)
