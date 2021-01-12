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


        # login validation
        if len(login) < 5:
           messages.error(request, 'This login must contain at least 5 characters.')
           return render(request, 'createAccount.html', {"invalid": True})
        elif len(login) > 20:
           messages.error(request, 'This login  may contain up to 45 characters.')
           return render(request, 'createAccount.html', {"invalid": True})

        # password validation  
        if len(password) < 5:
           messages.error(request, 'This password must contain at least 5 characters.')
           return render(request, 'createAccount.html', {"invalid": True})
        elif len(password) > 20:
           messages.error(request, 'This password may contain up to 128 characters.')
           return render(request, 'createAccount.html', {"invalid": True})


        user = User()
        hashed_pass = make_password(password)

        user.login = login
        user.password = hashed_pass
        user.user_type = user_type

        messages.info(request,'User has been created successfully')
        user.save()

        #messages.info(request,'User created successfully')
        return render(request, 'createAccount.html', {"created": True})
    
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
            messages.info(request,'Password has been changed') 
            hashed_pass = make_password(user_password_new)
            user.password = hashed_pass

        # ? https://docs.djangoproject.com/en/dev/ref/models/instances/?from=olddocs#how-django-knows-to-update-vs-insert
        user.save()        # Primary key has changed so I have to probably force an update (in other case it will insert)    
        # messages.info(request,'User has been updated successfully')
        return render(request, 'modifyAccount.html', {'user': user, "created": True })

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
        messages.info(request,'User has been deleted successfully')
        return render(request, 'deleteAccount.html', {"created": True})

def manageMail(request):
    return render(request, 'manageMail.html')

def createMail(request):

    if request.method == 'GET':
        return render(request, 'createMail.html')

    else:   # request.method == 'POST'
        mail = request.POST['mail']

        # e-mail validation
        regex = "^\d{6}@student.pwr.edu.pl|[a-z]{2,20}.[a-z]{2,20}@pwr.edu.pl$"

        if re.match(regex, mail):

            newMail = Mail()
            newMail.mail_id = mail
            newMail.save()

            messages.info(request,'Mail has been created successfully')
            return render(request, 'createMail.html', {"created": True})
        else: 
            messages.error(request,'Invalid e-mail address')
            return render(request, 'createMail.html', {"invalid": True})

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
        messages.info(request,'Mail has been deleted successfully')
        return render(request, 'deleteMail.html', {"created": True})

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

def chooseUntakenStudentAccount(request):
    students = Student.objects.all()
    students_user_id = []
    for student in students:
        students_user_id.append(student.user_id)

    student_users = User.objects.filter(user_type="STUDENT").exclude(pk__in = students_user_id).order_by("login")
    return render(request, 'chooseUntakenStudentAccount.html', {'student_users': student_users})

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


        # phone number validation
        #regex = "^[0-9]{9}$"

        #if re.match(regex, phoneNumber) == False:
        #   messages.error(request, 'Invalid phone number')
        #   return render(request, 'createStudent.html', {"invalid": True})


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
        newStudent.phone_number         = '+48 ' + phoneNumber
        newStudent.inauguration_date    = inaugurationDate
        newStudent.department_name      = departmentName
        newStudent.field_of_study       = fieldOfStudy
        newStudent.user                 = user
        newStudent.mail                 = email
        newStudent.save()

        messages.info(request,'Student has been created successfully')

        return render(request, 'createStudent.html', {'user': user, "created": True})   # ? maybe change page?

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


        # phone number validation
        #regex = "^[0-9]{9}$"

        #if re.match(regex, phoneNumber) == None:
        #   messages.error(request, 'Invalid phone number')
        #   return render(request, 'createAdmin.html', {"invalid": True})

        # * get instances of foreign key attributes 
        user = User.objects.filter(login = userLogin).first()
        
        newAdmin               = Admin()
        newAdmin.first_name    = name
        newAdmin.last_name     = lastName
        newAdmin.phone_number  = '+48 ' + phoneNumber
        newAdmin.user          = user
        newAdmin.save()

        messages.info(request,'Admin has been created successfully')

        return render(request, 'createAdmin.html', {'user': user, "created": True})   # ? maybe change page?

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

def chooseUserToModify(request):

    if request.method == 'GET':
        all_students = Student.objects.all()
        all_admins = Admin.objects.all()
        all_teachers = Teacher.objects.all()

        return render(request, 'chooseUserToModify.html', {'all_students': all_students, 'all_admins': all_admins, 'all_teachers': all_teachers})

def modifyUserAdmin(request):
    if request.method == 'GET':

        admin_id = request.GET['id']
        admin = Admin.objects.filter(admin_id = admin_id).first()

        return render(request, 'modifyUserAdmin.html', {'admin': admin})

    else:  # request.method == 'POST
        # receive data from form
        admin_id = request.GET['id']
        admin = Admin.objects.filter(admin_id = admin_id).first()

        name             = request.POST['name']
        lastName         = request.POST['lastName']
        phoneNumber      = request.POST['number']
        #userLogin        = request.POST['userId']

        # phone number validation
        #regex = "^[0-9]{9}$"

        #if re.match(regex, phoneNumber) == None:
        #  messages.error(request, 'Invalid phone number')
        #   return render(request, 'modifyUserAdmin.html', {"invalid": True})

        # * get instances of foreign key attributes 
        #user = User.objects.filter(login = userLogin).first()
        
        adminModified               = admin
        adminModified.first_name    = name
        adminModified.last_name     = lastName
        adminModified.phone_number  = phoneNumber  
        #adminModified.user          = user
        adminModified.save()

        messages.info(request,'Admin has been updated successfully')

        return render(request, 'modifyUserAdmin.html', {'admin': adminModified, "created": True})   # ? maybe change page?

    

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

        # phone number validation
        #regex = "^[0-9]{9}$"
        #
        #if re.match(regex, phoneNumber) == False:
        #   messages.error(request, 'Invalid phone number')
        #   return render(request, 'createTeacher.html', {'user': user, "invalid": True})
        

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
        newTeacher.phone_number         = '+48 ' + phoneNumber  
        newTeacher.department_name      = departmentName
        newTeacher.user                 = user
        newTeacher.mail                 = email
        newTeacher.save()

        messages.info(request,'Teacher has been created successfully')

        return render(request, 'createTeacher.html', {'user': user, "created": True})   # ? maybe change page?


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

        messages.info(request,'Course has been created successfully')

        return render(request, 'createCourse.html', {"created": True})   # ? maybe change page?

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

        messages.info(request,'Class has been created successfully')

        return render(request, 'createClass.html', {"created": True})   # ? maybe change page?