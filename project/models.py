from django.db import models
from django.utils import timezone


from company.models import Company
from department.models import Department
from location.models import State, LGA


class Project(models.Model):
    title = models.CharField(max_length=500, blank=False, null=False)
    award_date = models.DateField()
    proposed_completion_date = models.DateField()
    contract_sum_ngn = models.DecimalField(null=True, blank=True, max_digits=25,decimal_places=3)
    contract_sum_usd = models.DecimalField(null=True, blank=True, max_digits=25,decimal_places=3)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE, blank=True, null=True)
    contractor = models.ForeignKey(Company, on_delete=models.CASCADE)
    consultant = models.CharField(max_length=200, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    description = models.TextField(blank=True, null=True)
    when = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} - {} - {}".format(self.award_date, self.contract_sum_ngn, self.title)