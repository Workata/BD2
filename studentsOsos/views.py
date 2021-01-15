from django.shortcuts import render, redirect
from usersOsos.models import User
from mailboxOsos.models import Mail
from studentsOsos.models import Student
from adminsOsos.models import Admin
from teachersOsos.models import Teacher
from classesOsos.models import Course, Class
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
import re

# Create your views here.

def check_user_student_ok(request):
    if 'user_type' not in request.session or 'user' not in request.session:
        return redirect('/')

    user_type = request.session['user_type']
    if user_type == 'ADMIN':
        return redirect('/root/home')
    elif user_type == 'TEACHER':
        return redirect('/teacher/home')
    else:
        return True

def home(request):
    valid = check_user_student_ok(request)
    if valid != True:
        return valid

    return render(request, 'studentHome.html')


def seePersonalData(request):
    valid = check_user_student_ok(request)
    if valid != True:
        return valid

    user_id = request.session['user']
    student = Student.objects.filter(user_id = user_id).first()
    return render(request, 'studentPersonalData.html', {'student': student})


def seeMessages(request):
    return render(request, 'studentMessages.html')


def seeGrades(request):
    return render(request, 'studentGrades.html')