from rest_framework.pagination import PageNumberPagination


class EmployessPagination(PageNumberPagination):
    page_size = 10
