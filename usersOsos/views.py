from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from usersOsos.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.sessions.backends.db import SessionStore

# Create your views here.

def home(request):
    return redirect('/login')

def login(request):

    if 'user' in request.session:
        del request.session['user']
    if 'user_type' in request.session:
        del request.session['user_type']

    if request.method == 'GET':
        return render(request, 'login.html')
    else:       # request.method == 'POST'

        login = request.POST['login']
        password = request.POST['password']

        user = User.objects.filter(login = login).first()
        if user != None:
            hash_correct = check_password(password, user.password)
            if hash_correct:
                request.session["user"] = user.login
                if user.user_type == "ADMIN":
                    request.session["user_type"] = "ADMIN"
                    return redirect('/root/home')
                if user.user_type == "STUDENT":
                    request.session["user_type"] = "STUDENT"
                    return redirect('/student/home')
                if user.user_type == "TEACHER":
                    request.session["user_type"] = "TEACHER"
                    return redirect('/teacher/home')


        messages.info(request,'Invalid credentials')
        return render(request, 'login.html', {'invalid': True})