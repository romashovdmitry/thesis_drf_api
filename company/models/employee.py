# Django imports
from django.db.models import Model, CharField, UUIDField, URLField, \
    PositiveBigIntegerField, PositiveSmallIntegerField, ForeignKey, Index, \
    CASCADE

# Python imports
from uuid import uuid4

# import models
from company.models.department import Department


class Employee(Model):
    ''''''
    class Meta:
        db_table = 'employees'
        indexes = [
            Index(fields=['full_name'])
        ]

    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    full_name = CharField(max_length=512, null=False)
    photo = URLField(max_length=1024, null=True)
    position = CharField(max_length=256, null=True)
    salary = PositiveBigIntegerField(null=True)
    age = PositiveSmallIntegerField(null=True)
    department = ForeignKey(
        Department,
        related_name='department_of_employee',
        on_delete=CASCADE
    )

    def __str__(self):
        return self.full_name