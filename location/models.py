from django.db import models


ZONES = (
    ('NE', 'North East'),
    ('NW', 'North West'),
    ('NC', 'North Central'),
    ('SE', 'South East'),
    ('SW', 'South West'),
    ('SS', 'South South'),
)


class State(models.Model):
    name = models.CharField(max_length=50)
    zone = models.CharField(max_length=100, choices=ZONES)

    def __str__(self):
        return self.name


class LGA(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.state, self.name)
