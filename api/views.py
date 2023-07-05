# DRF imports
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# import models
from company.models.department import Department
from company.models.employee import Employee

# import serialazers
from api.serializers import DepartmentSerializer, EmployeeSeializer

# Django imports
from django.db.models import Count

# import custom objects
from api.paginators import EmployessPagination

# JWT imports
from rest_framework_simplejwt.authentication import JWTAuthentication

# import custom filter
from api.filters import FullNameFilter

class DepartmentsViewSet(ModelViewSet):
    ''' To work with departments '''
    permission_classes = [AllowAny]
    queryset = Department.objects.annotate(employees_counter=Count('employees_of_department'))
    serializer_class = DepartmentSerializer
    http_method_names = ['post', 'get']


class EmployeesViewSet(ModelViewSet):
    ''' To work with employees '''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSeializer
    # SearchFilter is not suitable because of spaces,
    # that can't be processed correctly
    filter_backends = [DjangoFilterBackend, FullNameFilter, SearchFilter]
    search_fields = ['full_name']
    filterset_fields = ['department', 'position']
    pagination_class = EmployessPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get', 'delete']

    def create(self, request):
        ''' create new one employee '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def destroy(self, request, *args, **kwargs):
        ''' delete employee '''
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(f'Employee object {instance.full_name} is deleted', status=200)

    def list(self, request):
        ''' return list of employees '''
        queryset = self.filter_queryset(self.queryset)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(
            page, many=True) if page is not None else self.serializer_class(queryset, many=True)
        return self.get_paginated_response(serializer.data) if page is not None else Response(serializer.data)
