from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from department.models import Department



class Account(models.Model):
    STAFF = 0
    EMIU = 1
    ERD = 2
    DSD = 3
    ISD = 4
    RRD = 5
    TSD = 6
    MANAGEMENT = 7
    USER_TYPE = enumerate((
        'Staff', 
        'EMIU Staff', 
        'Energy Resources Department', 
        'Distribution Services Department',
        'Investment & Sector Development',
        'Renewable Energy Department',
        'Transmission Department',
        'Management Staff'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=False, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    department = models.ForeignKey(Department, blank=True, on_delete=models.CASCADE)
    user_type = models.PositiveBigIntegerField(choices=USER_TYPE, default=STAFF)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {}, {}, {}".format(self.surname, self.first_name, self.phone, self.email)

    @property
    def full_name(self):
        if self.middle_name:
            return "{} {}. {}.".format(self.surname, self.first_name[0], self.middle_name[0])
        else:
            return "{} {}.".format(self.surname, self.first_name[0])
