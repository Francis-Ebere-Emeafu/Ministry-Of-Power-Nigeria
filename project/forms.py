from django import forms
from django.core.exceptions import ObjectDoesNotExist


from project.models import Project
from company.models import Company
from department.models import Department
from location.models import State, LGA


class ProjectForm(forms.ModelForm):
    # state = forms.ModelChoiceField(queryset=State.objects.all(), required=False, empty_label="Select state", widget=forms.Select(attrs={'class':'form-control'}))
    # lga = forms.ModelChoiceField(queryset=LGA.objects.none(), required=False, empty_label="Select LGA", widget=forms.Select(attrs={'class':'form-control', 'required': 'False'})) 
    # "Select LGA"
    # contractor = forms.ModelChoiceField(queryset=Company.objects.all(), required=False, empty_label="Contractor", widget=forms.Select(attrs={'class':'form-control', 'required': 'False'}))
    # department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False, empty_label="Department", widget=forms.Select(attrs={'class':'form-control', 'required': 'False'}))

    class Meta:
        model = Project
        # exclude = ['when']
        fields = ['title', 'award_date', 'proposed_completion_date', 'contract_sum_ngn', 'contract_sum_usd', 
        'state', 'contractor', 'consultant', 'department', 'description']
        

        def __init__(self, *args, **kwargs):
            # super(ProjectForm, self).__init__(*args, **kwargs)
            super().__init__(*args, **kwargs)
            print('******the INIT method******')
            # self.fields['lga'].queryset = LGA.objects.none()

            self.fields['proposed_completion_date'].required = False
            self.fields['contract_sum_ngn'].required = False
            self.fields['contract_sum_usd'].required = False
            self.fields['consultant'].required = False
            self.fields['description'].required = False
            self.fields['lga'].required = False

            if 'state' in self.data:
                state = self.cleaned_data['state']
                print('-----****-----')
                print(state)
                print('-----***-----')

                try:
                    state_id = self.data.get('state')
                    print(state_id)
                    print('***********state ID**********88')
                    self.fields['lga'].queryset = LGA.objects.filter(state_id=state_id).order_by('name')
                except(TypeError, ValueError):
                    pass
            elif self.instance.pk:
                # self.fields['lga'].queryset = LGA.objects.all()
                self.fields['lga'].queryset = self.instance.state.lga_set.order_by('name')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project title'}),
            'award_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'proposed_completion_date': forms.DateInput(attrs={'class': 'form-control', 'required': 'False', 'type': 'date'}),
            'contract_sum_ngn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NGN - contract sum'}),
            'contract_sum_usd': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'USD - contract sum'}),
            'state': forms.Select(attrs={'class': 'form-select', 'placeholder': ''}),
            'lga': forms.Select(attrs={'class': 'form-select', }),
            'contractor': forms.Select(attrs={'class': 'form-select'}),
            'consultant': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Consultant - Optional'}),
            'department': forms.Select(attrs={'class': 'form-select', 'required': 'False', 'placeholder': 'Select Supervision Department'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':5, 'placeholder': 'Project Summary -  Optional'}),
        }
        
        #     for visible in self.visible_fields():
        #         visible.field.widget.attrs['class'] = 'form-control'
                
            # super(ProjectForm, self).__init__(*args, **kwargs)
            # super().__init__(*args, **kwargs)
            # self.fields['lga'].queryset = LGA.objects.filter(state=state)
            # self.fields['state'].queryset = State.objects.none()
            # self.fields['state'].queryset = State.objects.none()
            # self.fields['consultant'].queryset = State.objects.none()
            # self.fields['state'].queryset = State.objects.none()

            #     super(ProjectForm, self).__init__(*args, **kwargs)
        #     self.fields['state'].empty_label = "Select State"

       

        
# class ThatForm(ModelForm):
#   class Meta:
    # widgets = {"text": Textarea(required=False)}



# class ThatForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     for field in self.Meta.required:
    #         self.fields[field].required = True

    # class Meta:
    #     model = User
    #     fields = (
    #         'email',
    #         'first_name',
    #         'last_name',
    #         'address',
    #         'postcode',
    #         'city',
    #         'state',
    #         'country',
    #         'company',
    #         'tax_id',
    #         'website',
    #         'service_notifications',
    #     )
    #     required = (
    #         'email',
    #         'first_name',
    #         'last_name',
    #         'address',
    #         'postcode',
    #         'city',
    #         'country',
    #     )


#     'website': forms.URLField(attrs={'class': 'form-control', 'required': 'False', 'placeholder': 'Website'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'False', 'placeholder': 'Email'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'False', 'placeholder': 'Phone Number'}),
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'False', 'required': 'False', 'placeholder': 'Contact Person'}),
        #     'logo': forms.ClearableFileInput(attrs={'class': 'form-control', 'required': 'False'}),