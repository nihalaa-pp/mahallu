from django import forms
from .models import Household, HouseholdMember
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class HouseholdForm(forms.ModelForm):
    class Meta:
        model = Household
        fields = ['panchayath', 'ward', 'house_number', 'mahallu_number', 'mahallu_area', 'standard_of_living', 'head_of_household']

class HouseholdMemberForm(forms.ModelForm):
    class Meta:
        model = HouseholdMember
        fields = [
            'name', 'relationship_to_head', 'phone_number', 'whatsapp_number', 
            'age', 'is_married', 'studying_course', 'institution', 
            'education_qualification', 'job', 'country_of_job', 'place_of_job', 
            'job_sector', 'job_experience', 'is_government_employee', 
            'is_expat', 'is_entrepreneur', 'is_business_owner', 
            'is_looking_for_job', 'is_chronic_patient', 'chronic_disease_info', 
            'is_differently_abled'
        ]
        widgets = {
            'phone_number': forms.NumberInput(attrs={'type': 'tel', 'inputmode': 'numeric', 'pattern': '[0-9]+'}),
            'whatsapp_number': forms.NumberInput(attrs={'type': 'tel', 'inputmode': 'numeric', 'pattern': '[0-9]+'}),
            'age': forms.NumberInput(attrs={'type': 'number', 'min': 0, 'step': 1}),
            'job_experience': forms.NumberInput(attrs={'type': 'number', 'min': 0, 'step': 1})
        }