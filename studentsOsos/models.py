from django.db import models
from usersOsos.models import User
from mailboxOsos.models import Mail

class Student(models.Model):
    student_id          = models.IntegerField(primary_key = True, null = False)
    first_name          = models.CharField(max_length = 30, null = False)
    last_name           = models.CharField(max_length = 60, null = False)
    phone_number        = models.CharField(max_length = 13, null = True)
    inauguration_date   = models.DateField(null = False)
    department_name     = models.CharField(max_length = 45, null = False)
    field_of_study      = models.CharField(max_length = 45, null = False)
    user                = models.OneToOneField(User, on_delete = models.CASCADE)    # * OK
    mail                = models.OneToOneField(Mail, on_delete = models.CASCADE)    # * OK

class StudentLog(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length = 200, null = False)

# Create your models here.
