from django import forms
from college.models import College

class noticeForm(forms.ModelForm):
    
    class Meta:
        model=College
        fields = '__all__' 
    def __init__(self, *args, **kwargs):
        super(noticeForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            
            })
            self.fields[field].widget.attrs['cols'] = 10
            self.fields[field].widget.attrs['rows'] = 4