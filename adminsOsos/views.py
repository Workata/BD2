from django.shortcuts import render, redirect
from usersOsos.models import User
from mailboxOsos.models import Mail
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'adminHome.html')

def createAccount(request):

    if request.method == 'GET':
        return render(request, 'createAccount.html')

    else:   # request.method == 'POST'
        login = request.POST['login']
        password = request.POST['password']
        user_type = request.POST['userType']

        user = User()
        hashed_pass = make_password(password)

        user.login = login
        user.password = hashed_pass
        user.user_type = user_type

        user.save()

        messages.info(request,'User created successfully')
        return render(request, 'createAccount.html')

def createMail(request):

    if request.method == 'GET':
        return render(request, 'createMail.html')

    else:   # request.method == 'POST'
        mail = request.POST['mail']
        newMail = Mail()
        newMail.mail_id = mail
        newMail.save()

        messages.info(request,'Mail created successfully')
        return render(request, 'createMail.html')


def chooseUser(request):

    if request.method == 'GET':
        return render(request, 'chooseUser.html')

    else:   # request.method == 'POST'
        userLogin = request.POST['userLogin']
        user = User.objects.filter(login = userLogin).first()

        if user.user_type == "ADMIN":
            return redirect('/root/createAdmin?userLogin='+userLogin)
        if user.user_type == "STUDENT":
            return redirect('/root/createStudent?userLogin='+userLogin)
        if user.user_type == "TEACHER":
            return redirect('/root/createTeacher?userLogin='+userLogin)

        # ! user not found messages.info(request,'Mail created successfully')
        return render(request, 'chooseUser.html')


def createStudent(request):   #  , user

    if request.method == 'GET':
        userLogin = request.GET['userLogin']
        user = User.objects.filter(login = userLogin).first()
        return render(request, 'createStudent.html', {'user': user})
    else:                                           # request.method == 'POST'
        # receive data from form
        studentId        = request.POST['id']      # 248845
        name             = request.POST['name']
        lastName         = request.POST['lastName']
        phoneNumber      = request.POST['number']
        inaugurationDate = request.POST['ingDate']
        departmentName   = request.POST['department']
        fieldOfStudy     = request.POST['field']
        userLogin        = request.POST['userId']
        email            = request.POST['mail']

        # TODO check existence of email



        return render(request, 'createStudent.html', {'user': user})

def createTeacher(request):

    if request.method == 'GET':
        return render(request, 'createTeacher.html')

def createAdmin(request):

    if request.method == 'GET':
        return render(request, 'createAdmin.html')



