from django.db import models
from studentsOsos.models import Student
from teachersOsos.models import Teacher

# Create your models here.
# * e.g. E06-47 -> 1, 2, 3, 4... , C1-216, pon tp 13-15
class Class(models.Model):
    class_id            = models.AutoField(primary_key=True)
    class_location      = models.CharField(max_length = 45, null = True)
    class_term          = models.CharField(max_length = 50, null = False)

    teacher             = models.ForeignKey('teachersOsos.Teacher', on_delete = models.CASCADE)    # ! OK but insert default teacher with id = 0
    course              = models.ForeignKey('Course', on_delete = models.CASCADE)                    # * OK
    # student             = models.ForeignKey('studentsOsos.Student', on_delete = models.CASCADE)      # * OK

# list of students in different classes
class ClassStudents(models.Model):
    class_students_id   = models.AutoField(primary_key=True)                             # autoincremented
    classs              = models.ForeignKey('Class', on_delete = models.CASCADE) 
    student             = models.ForeignKey('studentsOsos.Student', on_delete = models.CASCADE)

# ! AK2
class Course(models.Model):
    CourseEnum          = models.TextChoices('CourseEnum', 'LABORATORY LECTURE PROJECT SEMINARY PRACTICALS')

    course_id           = models.AutoField(primary_key=True)
    course_name         = models.CharField(max_length = 100, null = True)
    course_type         = models.CharField(blank = False, choices = CourseEnum.choices, max_length = 10)

class Grade(models.Model):
    ValueEnum            = models.TextChoices('ValueEnum', '2.0 3.0 3.5 4.0 4.5 5.0 5.5')
    TypeEnum             = models.TextChoices('TypeEnum', 'PARTIAL FINAL')

    grade_id             = models.AutoField(primary_key=True)
    value                = models.CharField(blank = False, choices = ValueEnum.choices, max_length = 10)
    grade_type           = models.CharField(blank = False, choices = TypeEnum.choices, max_length = 10)
    date_of_approval     = models.DateField(null = True)

    teacher              = models.ForeignKey('teachersOsos.Teacher', on_delete = models.SET_DEFAULT, default=0)      # ! OK but insert default teacher with id = 0
    classs               = models.ForeignKey('Class', on_delete = models.CASCADE)                                    # * OK
    student              = models.ForeignKey('studentsOsos.Student', on_delete = models.CASCADE)                     # * OK

# py manage.py makemigrations
# py manage.py sqlmigrate travello 0001
# 			<app name> <number of migration file>
# py manage.py migrate
