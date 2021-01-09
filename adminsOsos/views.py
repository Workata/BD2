from django.shortcuts import render, redirect
from usersOsos.models import User
from mailboxOsos.models import Mail
from studentsOsos.models import Student
from adminsOsos.models import Admin
from teachersOsos.models import Teacher
from classesOsos.models import Course, Class
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'adminHome.html')

def manageAccount(request):
    return render(request, 'manageAccount.html')

def createAccount(request):

    if request.method == 'GET':
        return render(request, 'createAccount.html')

    else:   # request.method == 'POST'
        login = request.POST['login']
        password = request.POST['password']
        user_type = request.POST['userType']    # TODO make repeat password field

        user = User()
        hashed_pass = make_password(password)

        user.login = login
        user.password = hashed_pass
        user.user_type = user_type

        user.save()

        messages.info(request,'User created successfully')
        return render(request, 'createAccount.html')
    
def chooseAccountToModify(request):
    all_accounts = User.objects.all().order_by("user_type")
    return render(request, 'chooseAccountToModify.html',{'accounts' : all_accounts})

def modifyAccount(request):

    if request.method == 'GET':
        user_login = request.GET['id']
        user = User.objects.filter(login = user_login).first()
        return render(request, 'modifyAccount.html', {'user': user})
    else:           # request.method == 'POST'
        user_login = request.GET['id']
        # user_login_new = request.POST['login']
        user_type_new      = request.POST['userType']
        user_password_new  = request.POST['pass']       # TODO make repeat password field
        user = User.objects.filter(login = user_login).first()

        # user.login = user_login_new
        user.user_type = user_type_new
        if user_password_new != '':                     # if password is blank dont update it -> dont hash it
            messages.info(request,'pass changed')
            hashed_pass = make_password(user_password_new)
            user.password = hashed_pass

        # ? https://docs.djangoproject.com/en/dev/ref/models/instances/?from=olddocs#how-django-knows-to-update-vs-insert
        user.save()        # Primary key has changed so I have to probably force an update (in other case it will insert)    
        #messages.info(request,'User updated successfully')
        return render(request, 'modifyAccount.html', {'user': user})

def chooseAccountToDelete(request):
    all_accounts = User.objects.all().order_by("user_type")
    return render(request, 'chooseAccountToDelete.html',{'accounts' : all_accounts})

def deleteAccount(request):
    if request.method == 'GET':
        user_login = request.GET['id']
        user = User.objects.filter(login = user_login).first()
        return render(request, 'deleteAccount.html', {'user': user})
    else:           # request.method == 'POST'
        user_login = request.GET['id']
        user = User.objects.filter(login = user_login).first()
        user.delete()
        messages.info(request,'User deleted successfully')
        return render(request, 'deleteAccount.html')

def manageMail(request):
    return render(request, 'manageMail.html')

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

def chooseMailToDelete(request):
    all_mails = Mail.objects.all().order_by("mail_id")
    return render(request, 'chooseMailToDelete.html',{'mails' : all_mails})

def deleteMail(request):
    if request.method == 'GET':
        mail_id = request.GET['id']
        mail = Mail.objects.filter(mail_id = mail_id).first()
        return render(request, 'deleteMail.html', {'mail': mail})
    else:           # request.method == 'POST'
        mail_id = request.GET['id']
        mail = Mail.objects.filter(mail_id = mail_id).first()
        mail.delete()
        messages.info(request,'Mail deleted successfully')
        return render(request, 'deleteMail.html')

def manageUser(request):
    return render(request, 'manageUser.html')

def chooseUserTypeToCreate(request):
    return render(request, 'chooseUserTypeToCreate.html')

def chooseUntakenAdminAccount(request):
    admins = Admin.objects.all()
    admins_user_id = []
    for admin in admins:
        admins_user_id.append(admin.user_id)


    admin_users = User.objects.filter(user_type="ADMIN").exclude(pk__in = admins_user_id).order_by("login")
    return render(request, 'chooseUntakenAdminAccount.html', {'admin_users': admin_users})

def chooseUntakenTeacherAccount(request):
    teachers = Teacher.objects.all()
    teachers_user_id = []
    for teacher in teachers:
        teachers_user_id.append(teacher.user_id)


    teacher_users = User.objects.filter(user_type="TEACHER").exclude(pk__in = teachers_user_id).order_by("login")
    return render(request, 'chooseUntakenTeacherAccount.html', {'teacher_users': teacher_users})


def createAdmin(request):

    if request.method == 'GET':
        userLogin = request.GET['userLogin']
        user = User.objects.filter(login = userLogin).first()
        return render(request, 'createAdmin.html', {'user': user})
    else:     # request.method == 'POST'
        # receive data from form
        name             = request.POST['name']
        lastName         = request.POST['lastName']
        phoneNumber      = request.POST['number']
        userLogin        = request.POST['userId']

        # TODO data validation

        # * get instances of foreign key attributes 
        user = User.objects.filter(login = userLogin).first()
        
        newAdmin               = Admin()
        newAdmin.first_name    = name
        newAdmin.last_name     = lastName
        newAdmin.phone_number  = '+48 ' + phoneNumber  # TODO change in data validation
        newAdmin.user          = user
        newAdmin.save()

        messages.info(request,'Admin created successfully')

        return render(request, 'createAdmin.html', {'user': user})   # ? maybe change page?

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
        mail             = request.POST['mail']

        # TODO data validation

        if Mail.objects.filter(mail_id = mail).exists() == False:    # if email doesnt exist then create new email
            newMail = Mail()
            newMail.mail_id = mail
            newMail.save()

        # * get instances of foreign key attributes 
        user = User.objects.filter(login = userLogin).first()
        email = Mail.objects.filter(mail_id = mail).first()
        
        newStudent                      = Student()
        newStudent.student_id           = studentId
        newStudent.first_name           = name
        newStudent.last_name            = lastName
        newStudent.phone_number         = '+48 ' + phoneNumber  # TODO change in data validation
        newStudent.inauguration_date    = inaugurationDate
        newStudent.department_name      = departmentName
        newStudent.field_of_study       = fieldOfStudy
        newStudent.user                 = user
        newStudent.mail                 = email
        newStudent.save()

        messages.info(request,'Student created successfully')

        return render(request, 'createStudent.html', {'user': user})   # ? maybe change page?

def createTeacher(request):

    if request.method == 'GET':
        userLogin = request.GET['userLogin']
        user = User.objects.filter(login = userLogin).first()
        return render(request, 'createTeacher.html', {'user': user})
    else:                                           # request.method == 'POST'         
        # receive data from form
        name             = request.POST['name']
        lastName         = request.POST['lastName']
        phoneNumber      = request.POST['number']
        departmentName   = request.POST['department']
        userLogin        = request.POST['userId']
        mail             = request.POST['mail']

        # TODO data validation

        if Mail.objects.filter(mail_id = mail).exists() == False:    # if email doesnt exist then create new email
            newMail = Mail()
            newMail.mail_id = mail
            newMail.save()

        # * get instances of foreign key attributes 
        user = User.objects.filter(login = userLogin).first()
        email = Mail.objects.filter(mail_id = mail).first()
        
        newTeacher                      = Teacher()
        newTeacher.first_name           = name
        newTeacher.last_name            = lastName
        newTeacher.phone_number         = '+48 ' + phoneNumber  # TODO change in data validation
        newTeacher.department_name      = departmentName
        newTeacher.user                 = user
        newTeacher.mail                 = email
        newTeacher.save()

        messages.info(request,'Teacher created successfully')

        return render(request, 'createTeacher.html', {'user': user})   # ? maybe change page?


def createCourse(request):
    if request.method == 'GET':
        return render(request, 'createCourse.html')
    else:        # request.method == 'POST'
        course_name  = request.POST['name']
        course_type  = request.POST['type']

        # TODO data validation
        # TODO check if course exists

        new_course = Course()
        new_course.course_name = course_name
        new_course.course_type = course_type
        new_course.save()

        messages.info(request,'Course created successfully')

        return render(request, 'createCourse.html')   # ? maybe change page?

def createClass(request):
    if request.method == 'GET':
        return render(request, 'createClass.html')
    else:        # request.method == 'POST'
        course_name  = request.POST['name']
        course_type  = request.POST['type']

        # TODO data validation
        # TODO check if course exists

        new_course = Course()
        new_course.course_name = course_name
        new_course.course_type = course_type
        new_course.save()

        messages.info(request,'Class created successfully')

        return render(request, 'createClass.html')   # ? maybe change page?