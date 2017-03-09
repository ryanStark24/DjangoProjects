from django.contrib import admin
from .models import College

# Register your models here.
class CollegeAdmin(admin.ModelAdmin):
    
    list_display=['subject','cr_date']
    list_filter=['cr_date','subject']
    search_fields=['subject','message']
    
    
admin.site.register(College,CollegeAdmin)   
    