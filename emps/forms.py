from django import forms
from .models import *


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'        

class RecruitmentForm(forms.ModelForm):
    class Meta:
        model=Recruitment
        fields='__all__'