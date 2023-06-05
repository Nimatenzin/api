from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from managedata.models import Employee
from managedata.serializers import EmployeeSerializer

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        print("Received data:", employee_data)  # Debugging statement
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            print("Data is valid")  # Debugging statement
            employee_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            print("Errors:", employee_serializer.errors)  # Debugging statement
            return JsonResponse("Failed to add", safe=False)
    
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        print("Received data:", employee_data)  # Debugging statement
        employee = get_object_or_404(Employee, employee_id=employee_data['employee_id'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            print("Data is valid")  # Debugging statement
            employee_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        else:
            print("Errors:", employee_serializer.errors)  # Debugging statement
            return JsonResponse("Failed to update", safe=False)
    
    elif request.method == 'DELETE':
        employee = Employee.objects.get(id=id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)
