from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages


from company.models import Company
from company.forms import CompanyForm


def register_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES or None)
        if form.is_valid():
            print(form)
            form.save(commit=True)
            messages.success(request, "New Company successfully registered")

            return redirect("register_company")
    else:
        form = CompanyForm()

    context = {
        "form": form,
    }
    return render(request, 'company/register_company.html', context)



def company_list(request):
    companies = Company.objects.all()
    context = {
        "companies": companies,
    }
    return render(request, 'company/company_list.html', context)

