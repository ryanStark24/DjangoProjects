from django import forms
from college.models import College

class noticeForm(forms.ModelForm):
    
    class Meta:
        model=College
        fields = '__all__' 