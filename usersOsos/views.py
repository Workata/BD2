from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from usersOsos.models import User
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'login.html')

def login(request):

    login = request.POST['login']
    password = request.POST['password']

    user = User.objects.filter(login = login).first()
    if user != None:
        hash_correct = check_password(password, user.password)
        if hash_correct == True:
            if user.user_type == "ADMIN":
                return redirect('/root/home')
            if user.user_type == "STUDENT":
                return redirect('/student/home')
            if user.user_type == "TEACHER":
                return redirect('/teacher/home')


    messages.info(request,'Invalid credentials')
    return render(request, 'login.html')

    # login = "workata"
    # password = "1234"
    # hashed_pass = make_password(password)
    # user = User()
    # user.login = login
    # user.password = hashed_pass
    # user.user_type = "ADMIN"
    # user.save()
    #return render(request, 'login.html')