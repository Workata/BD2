from django.db import models

# Create your models here.

class User(models.Model):

    UsersEnum        = models.TextChoices('UsersEnum','TEACHER STUDENT ADMIN')

    id               = models.AutoField(primary_key=True)
    login            = models.CharField(max_length = 45, null = False)
    password         = models.CharField(max_length = 128, null = False)                                   # https://stackoverflow.com/questions/25098466/how-to-store-django-hashed-password-without-the-user-object
    user_type        = models.CharField(blank = False, choices = UsersEnum.choices, max_length = 10)


class UserLog(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length = 200, null = False)