from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Name', 'Email', 'Password']
        labels = {'Email':'Email'}
        widgets = {
            'Password':forms.PasswordInput(attrs={'class':'form-control'}),
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.TextInput(attrs={'class':'form-control'})}