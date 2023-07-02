from rest_framework.routers import DefaultRouter

from api.views import DepartmentsViewSet, EmployeesViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentsViewSet, basename='departments')
router.register(r'employees', EmployeesViewSet, basename='employees')