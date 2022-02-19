from django.db import models



class Department(models.Model):
    dept_name = models.CharField(max_length=200, blank=False, null=True)
    alias = models.CharField(max_length=5, blank=False, null=True)
    room_number = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return "({}) - {} - {}".format(self.alias, self.room_number, self.dept_name)