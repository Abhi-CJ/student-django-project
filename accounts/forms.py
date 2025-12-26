from django import forms
from django.contrib.auth.models import User
from .models import Student


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm_password')
        if password != confirm:
            raise forms.ValidationError("Password do not match")
        
        
class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['name', 'age', 'address', 'email']
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("Age must be greater than or equal to 18")
        return age
        
