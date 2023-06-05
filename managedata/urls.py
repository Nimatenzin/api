from django.urls import path
from django.shortcuts import redirect
from managedata.views import employeeApi


urlpatterns = [
    path('', lambda request: redirect('/employee/')),
    path('employee/', employeeApi),
    path('employee/<int:id>/', employeeApi),
]
