from rest_framework import serializers
from managedata.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(input_formats=['%d/%m/%y'])
    appointment_date = serializers.DateField(input_formats=['%d/%m/%y'])

    class Meta:
        model = Employee
        fields = ('name', 'employee_id', 'gender', 'dob', 'designation', 'department', 'appointment_date')
