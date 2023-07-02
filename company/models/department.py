# Django imports
from django.db.models import Model, CharField


class Department(Model):

    class Meta:
        db_table = 'departments'

    department_name = CharField(max_length=256, null=False, primary_key=True)

    def __str__(self):

        return self.department_name
