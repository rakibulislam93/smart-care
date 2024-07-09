from django.contrib import admin
from .models import PatientModel
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','mobile_no','image']


    def first_name(self,obj):
        
        return obj.user.first_name
        
    def last_name(self,obj):
        return obj.user.last_name

admin.site.register(PatientModel,PatientAdmin)