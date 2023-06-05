from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'gender', 'dob', 'designation', 'department', 'appointment_date')
    list_filter = ('gender', 'designation', 'department')
    search_fields = ('name', 'employee_id')
    list_per_page = 10
    ordering = ('name',)
    actions = ['delete_selected']
    