from django.contrib import admin





from project.models import Project, Payment

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'award_date', 'state']



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['project', 'payment_type', 'amount_paid_ngn', 'amount_paid_usd', 'when']