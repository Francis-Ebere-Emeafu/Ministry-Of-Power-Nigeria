from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from department.models import Department



class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=False, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {}, {}, {}".format(self.surname, self.first_name, self.phone, self.email)
