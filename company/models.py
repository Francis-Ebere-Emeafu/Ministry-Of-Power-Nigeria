from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=200, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(max_length=200)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return "{}, {}, {}".format(self.company_name, self.phone, self.email)