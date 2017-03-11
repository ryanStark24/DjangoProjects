
from college.models import College
from django.contrib.auth.models import User
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class College_Form(forms.ModelForm):
     
    class Meta:
        model = College
        fields = '__all__'
        widgets = {
            'cr_date': DateInput(),
        }
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        