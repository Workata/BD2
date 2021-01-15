from django.shortcuts import render, redirect
from usersOsos.models import User
from mailboxOsos.models import Mail
from studentsOsos.models import Student
from adminsOsos.models import Admin
from teachersOsos.models import Teacher
from classesOsos.models import Course, Class, ClassStudents
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
import re

def check_user_teacher_ok(request):
    if 'user_type' not in request.session or 'user' not in request.session:
        return redirect('/')

    user_type = request.session['user_type']
    if user_type == 'ADMIN':
        return redirect('/root/home')
    elif user_type == 'STUDENT':
        return redirect('/student/home')
    else:
        return True

# Create your views here.

def home(request):
    valid = check_user_teacher_ok(request)
    if valid != True:
        return valid

    return render(request, 'teacherHome.html')


def seePersonalData(request):
    return render(request, 'teacherPersonalData.html')


def seeMessages(request):
    return render(request, 'teacherMessages.html')


def manageClass(request):
    user_id = request.session['user']
    teacher = Teacher.objects.filter(user_id = user_id).first()
    teacher_classes = Class.objects.filter(teacher_id = teacher.teacher_id)

    return render(request, 'chooseClassToManage.html', {'classes': teacher_classes})

def classManager(request):  # To debugg

    class_id = request.GET['id']
    map_students_in_class = ClassStudents.objects.filter(classs_id=class_id)
    students_in_class = []
    for relation in map_students_in_class:
        student = Student.objects.filter(student_id=relation.student_id)
        students_in_class.append(student)


    return render(request, 'manageClassAsTeacher.html', {'students_in_class': students_in_class})