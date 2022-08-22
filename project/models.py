from termios import N_SLIP
from django.db import models
from django.utils import timezone


from company.models import Company
from department.models import Department
from location.models import State, LGA


class Project(models.Model):
    ERD = 0
    DSD = 1
    ISD = 2
    RRD = 3
    TSD = 4
    DEPARTMENT = enumerate((
        'Energy Resources Department', 
        'Distribution Services Department',
        'Investment & Sector Development',
        'Renewable Energy Department',
        'Transmission Department'))

    title = models.CharField(max_length=500, blank=False, null=False)
    award_date = models.DateField()
    proposed_completion_date = models.DateField()
    contract_sum_ngn = models.DecimalField(null=True, blank=True, max_digits=50, decimal_places=5)
    contract_sum_usd = models.DecimalField(null=True, blank=True, max_digits=50, decimal_places=5)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE, blank=True, null=True)
    contractor = models.ForeignKey(Company, on_delete=models.CASCADE)
    consultant = models.CharField(max_length=200, null=True, blank=True)
    department = models.PositiveIntegerField(choices=DEPARTMENT)

    description = models.TextField(blank=True, null=True)
    when = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} - {} - {}".format(self.award_date, self.contract_sum_ngn, self.title)



class Payment(models.Model):
    PAYMENT = 0
    RETENTION = 1
    VARIATION = 2
    CONTINGENCY = 3
    PAYMENT_TYPE = enumerate((
        'Progress Payment - (IPC)',
        'Retention',
        'Contract Variation'
        'Contingency'))

    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    payment_type = models.PositiveBigIntegerField(choices=PAYMENT_TYPE, default=PAYMENT)
    amount_paid_ngn = models.DecimalField(max_digits=50, decimal_places=5)
    amount_paid_usd = models.DecimalField(null=True, blank=True, max_digits=50, decimal_places=5)
    amount_certified_ngn = models.DecimalField(max_digits=50, decimal_places=5)
    amount_certified_usd = models.DecimalField(null=True, blank=True, max_digits=50, decimal_places=5)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {} {}".format(self.amount_ngn, self.payment_type, self.project)