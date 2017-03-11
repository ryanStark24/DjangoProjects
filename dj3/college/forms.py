
from college.models import College
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import Widget



    
    
class College_Form(forms.ModelForm):
    
    class Meta:
        model = College
        fields = '__all__'
       
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        