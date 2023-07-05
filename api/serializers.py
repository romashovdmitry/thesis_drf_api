# DRF imports
from rest_framework import serializers

# Django imports
from django.utils import formats
from django.db.models import Count, Sum

# import models
from company.models.department import Department
from company.models.employee import Employee

# DRF imports
from rest_framework.serializers import ModelSerializer, SerializerMethodField, IntegerField, CharField


class DepartmentSerializer(ModelSerializer):

    employees_counter = serializers.SerializerMethodField()
    chief = SerializerMethodField()
    budget = SerializerMethodField()

    class Meta:
        model = Department
        fields = ['department_name', 'chief', 'employees_counter', 'budget']

    def get_chief(self, obj):

        if Employee.objects.filter(department=obj).filter(position='chief').exists():
            employees = Employee.objects.get(department=obj, position='chief')
            serializer = EmployeeSeializer(employees, many=False)
            return serializer.data
        else:
            return None

    def get_employees_counter(self, obj):

        return obj.employees_counter

    def get_budget(self, obj):

        return Employee.objects.filter(department=obj).aggregate(total_salary=Sum('salary'))['total_salary']


class EmployeeSeializer(ModelSerializer):

    photo = CharField(allow_null=True, required=False)
    position = CharField(allow_null=True, required=False)
    salary = IntegerField(allow_null=True, required=False)
    age = IntegerField(allow_null=True, required=False)

    class Meta:
        model = Employee
        fields = [
            'full_name',
            'position',
            'department',
            'photo',
            'position',
            'salary',
            'age'
        ]