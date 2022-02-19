from django.shortcuts import render


from company.models import Company
from company.forms import CompanyForm


def register_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = CompanyForm()

    context = {
        "form": form,
    }
    return render(request, 'company/register_company.html', context)