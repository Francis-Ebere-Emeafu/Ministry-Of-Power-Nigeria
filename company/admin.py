from django.contrib import admin





from company.models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email', 'website']