# default imports
from django.contrib import admin

# imports models
from company.models.department import Department
from company.models.employee import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)
