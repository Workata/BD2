from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from usersOsos.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.sessions.backends.db import SessionStore

# Create your views here.

def home(request):
    if 'user' in request.session:
        del request.session['user']
    return render(request, 'login.html')

def login(request):

    login = request.POST['login']
    password = request.POST['password']

    user = User.objects.filter(login = login).first()
    if user != None:
        hash_correct = check_password(password, user.password)
        if hash_correct == True:
            if user.user_type == "ADMIN":
                request.session["user"] = user.login
                return redirect('/root/home')
            if user.user_type == "STUDENT":
                return redirect('/student/home')
            if user.user_type == "TEACHER":
                return redirect('/teacher/home')


    messages.info(request,'Invalid credentials')
    return render(request, 'login.html')