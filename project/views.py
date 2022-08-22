from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy


from project.models import Project, Payment
from project.forms import ProjectForm, PaymentForm
from location.models import *


def add_new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            lga_id = request.POST.get('lga')
            lga = LGA.objects.get(id=lga_id)
            contract_sum_ngn = form.cleaned_data['contract_sum_ngn']
            contract_sum_usd = form.cleaned_data['contract_sum_usd']
            print("\n***********")
            print(lga.name)
            print(contract_sum_usd)
            print(contract_sum_ngn)

            print(project)
            print("***********")
            project.lga = lga
            project.contract_sum_ngn = contract_sum_ngn
            project.contract_sum_usd = contract_sum_usd
            project.save()
            messages.info(request, 'New Project Save Successfully')
            return redirect('new_project')
    else:
        form = ProjectForm()
    return render(request, 'project/new_project2.html', {'form':form})


def project_list(request):
    projects = Project.objects.all()
    for i in projects:
        print(i)
    context = {
        "projects": projects,
    }
    return render(request, 'project/project_list.html', context)


def load_lgas(request):
    state_id = request.GET.get('state')
    print('--Ajax load_lgas View--')
    print(state_id)
    lgas = LGA.objects.filter(state_id=state_id).order_by('name')
    for lga in lgas:
        print(lga)
    return render(request, 'project/lga_dropdown_list.html', {'lgas': lgas})



def add_project_payment(request, project_id=None):
    
    context = {}
    return render(request, 'project/add_project_payment.html', context)


class ProjectCreateView(CreateView):
    model = Project
    fields = ('title', 'award_date', 'proposed_completion_date', 'contract_sum_ngn', 'contract_sum_usd', 
        'state', 'lga', 'contractor', 'consultant', 'department', 'description')
        
    # fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('project_test_list')


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ('title', 'award_date', 'proposed_completion_date', 'contract_sum_ngn', 'contract_sum_usd', 
        'state', 'lga', 'contractor', 'consultant', 'department', 'description')
        
    # fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('project_test_list')