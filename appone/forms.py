from django import forms
from . models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'

class SignupForm(forms.ModelForm):
    class Meta:
        model=Signup
        fields='__all__'