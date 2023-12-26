from django.contrib import admin
from .models import Company,Employee
# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_id','name', 'location','about','type','active']
    search_fields=('name',)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','phone','company']
    list_filter=('company',)

admin.site.register(Employee,EmployeeAdmin)