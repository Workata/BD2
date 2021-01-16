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

def check_user_admin_ok(request):
    if 'user_type' not in request.session or 'user' not in request.session:
        return redirect('/')

    user_type = request.session['user_type']
    if user_type == 'STUDENT':
        return redirect('/student/home')
    elif user_type == 'TEACHER':
        return redirect('/teacher/home')
    else:
        return True

def home(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    return render(request, 'adminHome.html')


def manageAccount(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    return render(request, 'manageAccount.html')
 
def createAccount(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    if request.method == 'GET':
        return render(request, 'createAccount.html')

    else:   # request.method == 'POST'
        login = request.POST['login']
        password = request.POST['password']
        user_type = request.POST['userType']  


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
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    all_accounts = User.objects.all().order_by("user_type")
    return render(request, 'chooseAccountToModify.html',{'accounts' : all_accounts})

def modifyAccount(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

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
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    all_accounts = User.objects.all().order_by("user_type")
    return render(request, 'chooseAccountToDelete.html',{'accounts' : all_accounts})

def deleteAccount(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

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
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    return render(request, 'manageMail.html')

def createMail(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

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
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    all_mails = Mail.objects.all().order_by("mail_id")
    return render(request, 'chooseMailToDelete.html',{'mails' : all_mails})

def deleteMail(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

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
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    return render(request, 'manageUser.html')

def chooseUserTypeToCreate(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    return render(request, 'chooseUserTypeToCreate.html')

def chooseUntakenAdminAccount(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    admins = Admin.objects.all()
    admins_user_id = []
    for admin in admins:
        admins_user_id.append(admin.user_id)


    admin_users = User.objects.filter(user_type="ADMIN").exclude(pk__in = admins_user_id).order_by("login")
    return render(request, 'chooseUntakenAdminAccount.html', {'admin_users': admin_users})

def chooseUntakenTeacherAccount(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    teachers = Teacher.objects.all()
    teachers_user_id = []
    for teacher in teachers:
        teachers_user_id.append(teacher.user_id)


    teacher_users = User.objects.filter(user_type="TEACHER").exclude(pk__in = teachers_user_id).order_by("login")
    return render(request, 'chooseUntakenTeacherAccount.html', {'teacher_users': teacher_users})

def chooseUntakenStudentAccount(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    students = Student.objects.all()
    students_user_id = []
    for student in students:
        students_user_id.append(student.user_id)

    student_users = User.objects.filter(user_type="STUDENT").exclude(pk__in = students_user_id).order_by("login")
    return render(request, 'chooseUntakenStudentAccount.html', {'student_users': student_users})

def createStudent(request):   #  , user
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid


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

        # * get instances of foreign key attributes 
        user = User.objects.filter(login = userLogin).first()

        # phone number validation
        regex = "^[0-9]{9}$"

        if re.match(regex, phoneNumber) is None:
           messages.error(request, 'Invalid phone number')
           return render(request, 'createStudent.html', {'user': user,"invalid": True})


        if Mail.objects.filter(mail_id = mail).exists() == False:    # if email doesnt exist then create new email
            newMail = Mail()
            newMail.mail_id = mail
            newMail.save()

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
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

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

        # * get instances of foreign key attributes 
        user = User.objects.filter(login = userLogin).first()

        # phone number validation
        regex = "^[0-9]{9}$"

        if re.match(regex, phoneNumber) is None:
           messages.error(request, 'Invalid phone number')
           return render(request, 'createAdmin.html', {'user': user,"invalid": True})
        
        newAdmin               = Admin()
        newAdmin.first_name    = name
        newAdmin.last_name     = lastName
        newAdmin.phone_number  = '+48 ' + phoneNumber
        newAdmin.user          = user
        newAdmin.save()

        messages.info(request,'Admin has been created successfully')

        return render(request, 'createAdmin.html', {'user': user, "created": True})   # ? maybe change page?

def chooseUser(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

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
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    if request.method == 'GET':
        all_students = Student.objects.all()
        all_admins = Admin.objects.all()
        all_teachers = Teacher.objects.all()

        return render(request, 'chooseUserToModify.html', {'all_students': all_students, 'all_admins': all_admins, 'all_teachers': all_teachers})

def modifyUserAdmin(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

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
        regex = "^\+48\s[0-9]{9}$"

        if re.match(regex, phoneNumber) is None:
            messages.error(request, 'Invalid phone number')
            return render(request, 'modifyUserAdmin.html', {"invalid": True})

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

def modifyUserTeacher(request):         # change for teacher
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    if request.method == 'GET':

        teacher_id = request.GET['id']
        teacher = Teacher.objects.filter(teacher_id = teacher_id).first()

        return render(request, 'modifyUserTeacher.html', {'teacher': teacher})

    else:  # request.method == 'POST
        # receive data from form
        teacher_id = request.GET['id']
        teacher = Teacher.objects.filter(teacher_id = teacher_id).first()

        name             = request.POST['name']
        lastName         = request.POST['lastName']
        phoneNumber      = request.POST['number']
        department_name  = request.POST['department']


        # TODO data validation

        # * get instances of foreign key attributes 
        #user = User.objects.filter(login = userLogin).first()
        
        teacherModified                  = teacher
        teacherModified.first_name       = name
        teacherModified.last_name        = lastName
        teacherModified.phone_number     = phoneNumber  # TODO change in data validation
        teacherModified.department_name  = department_name
        teacherModified.save()

        messages.info(request,'Teacher updated successfully')

        return render(request, 'modifyUserTeacher.html', {'teacher': teacherModified, "created": True})   # ? maybe change page?

def modifyUserStudent(request):         # change for student
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    if request.method == 'GET':

        student_id = request.GET['id']
        student = Student.objects.filter(student_id = student_id).first()

        return render(request, 'modifyUserStudent.html', {'student': student})

    else:  # request.method == 'POST
        # receive data from form
        student_id = request.GET['id']
        student = Student.objects.filter(student_id = student_id).first()

        name             = request.POST['name']
        lastName         = request.POST['lastName']
        phoneNumber      = request.POST['number']
        ingDate          = request.POST['ingDate']
        department_name  = request.POST['department']
        field_of_study   = request.POST['field']

        # TODO data validation
        
        studentModified               = student
        studentModified.first_name    = name
        studentModified.last_name     = lastName
        studentModified.phone_number  = phoneNumber  # TODO change in data validation
        studentModified.inauguration_date  = ingDate
        studentModified.department_name  = department_name
        studentModified.field_of_study  = field_of_study
  
        studentModified.save()

        messages.info(request,'Student updated successfully')

        return render(request, 'modifyUserStudent.html', {'student': studentModified, "created": True})   # ? maybe change page?

def chooseUserToDelete(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    all_students = Student.objects.all()
    all_admins = Admin.objects.all()
    all_teachers = Teacher.objects.all()

    return render(request, 'chooseUserToDelete.html', {'all_students': all_students, 'all_admins': all_admins, 'all_teachers': all_teachers})

def deleteUser(request):    # one page for all user types   (show only name/last name etc.)
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    if request.method == 'GET':
        user_type_id = request.GET['id']
        user_type = request.GET['type']

        if user_type == 'admin':
            user_type_obj = Admin.objects.filter(admin_id=user_type_id).first()
        elif user_type == 'teacher':
            user_type_obj = Teacher.objects.filter(teacher_id=user_type_id).first()
        else:
            user_type_obj = Student.objects.filter(student_id=user_type_id).first()

        return render(request, 'deleteUser.html', {'userType': user_type_obj, 'userTypeName': user_type})
    else:           # request.method == 'POST'
        user_type_id = request.GET['id']
        user_type = request.GET['type']

        if user_type == 'admin':
            user_type_obj = Admin.objects.filter(admin_id=user_type_id).first()
        elif user_type == 'teacher':
            user_type_obj = Teacher.objects.filter(teacher_id=user_type_id).first()
        else:
            user_type_obj = Student.objects.filter(student_id=user_type_id).first()

        user_type_obj.delete()
        messages.info(request,'User type deleted successfully')
        return render(request, 'deleteUser.html', {'created': True})

def manageCourse(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    return render(request, 'manageCourse.html')

def createTeacher(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

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

        # * get instances of foreign key attributes 
        user = User.objects.filter(login = userLogin).first()

        # phone number validation
        regex = "^[0-9]{9}$"
        
        if re.match(regex, phoneNumber) is None:
           messages.error(request, 'Invalid phone number')
           return render(request, 'createTeacher.html', {'user': user, "invalid": True})
        

        if Mail.objects.filter(mail_id = mail).exists() == False:    # if email doesnt exist then create new email
            newMail = Mail()
            newMail.mail_id = mail
            newMail.save()


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
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

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

def chooseCourseToModify(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    all_courses = Course.objects.all()
    return render(request, 'chooseCourseToModify.html',{'courses':all_courses})

def modifyCourse(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid


    if request.method == 'GET':

        course_id = request.GET['id']
        course = Course.objects.filter(course_id = course_id).first()

        return render(request, 'modifyCourse.html', {'course': course})

    else:  # request.method == 'POST
        # receive data from form
        course_id = request.GET['id']
        course = Course.objects.filter(course_id = course_id).first()

        course_name      = request.POST['name']
        course_type      = request.POST['type']

        # TODO data validation
        
        courseModified               = course
        courseModified.course_name   = course_name
        courseModified.course_type   = course_type
  
        courseModified.save()

        messages.info(request,'Course updated successfully')

        return render(request, 'modifyCourse.html', {'course': courseModified, 'created': True})  

def chooseCourseToDelete(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    all_courses = Course.objects.all()
    return render(request, 'chooseCourseToDelete.html',{'courses':all_courses})

def deleteCourse(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid
        
    if request.method == 'GET':

        course_id = request.GET['id']
        course = Course.objects.filter(course_id = course_id).first()

        return render(request, 'deleteCourse.html', {'course': course})

    else:  # request.method == 'POST
        # receive data from form
        course_id = request.GET['id']
        course = Course.objects.filter(course_id = course_id).first()
        course.save()

        messages.info(request,'Course deleted successfully')

        return render(request, 'deleteCourse.html', {'created': True})  

def manageClass(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    return render(request, 'manageClass.html')

def chooseCourseToClass(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid
        
    all_courses = Course.objects.all()
    return render(request, 'chooseCourseToClass.html', {'courses':all_courses})

def chooseTeacherToClass(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    course_id = request.GET['course_id']
    all_teachers = Teacher.objects.all()
    return render(request, 'chooseTeacherToClass.html', {'all_teachers':all_teachers, 'course_id': course_id})

def createClass(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    if request.method == 'GET':

        course_id = request.GET['course_id']
        teacher_id = request.GET['teacher_id']

        course = Course.objects.filter(course_id = course_id).first()
        teacher = Teacher.objects.filter(teacher_id = teacher_id).first()
        return render(request, 'createClass.html', {'course':course, 'teacher':teacher})

    else:        # request.method == 'POST'
        course_id = request.GET['course_id']
        teacher_id = request.GET['teacher_id']
        course = Course.objects.filter(course_id = course_id).first()
        teacher = Teacher.objects.filter(teacher_id = teacher_id).first()

        class_location  = request.POST['location']
        class_term      = request.POST['term']

        new_class = Class()
        new_class.class_location = class_location
        new_class.class_term = class_term
        new_class.course = course
        new_class.teacher = teacher
        new_class.save()

        messages.info(request,'Class has been created successfully')

        return render(request, 'createClass.html', {'course':course, 'teacher':teacher, "created": True})   # ? maybe change page?

def chooseClassToModify(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    all_classes = Class.objects.all()
    return render(request, 'chooseClassToModify.html', {"classes": all_classes})   # ? maybe change page?

def modifyClass(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    if request.method == 'GET':

        class_id = request.GET['id']
        classs = Class.objects.filter(class_id=class_id).first()
        course = Course.objects.filter(course_id = classs.course_id).first()
        teacher = Teacher.objects.filter(teacher_id = classs.teacher_id).first()

        return render(request, 'modifyClass.html', {'class': classs, 'course': course, 'teacher': teacher})

    else:  # request.method == 'POST
        # receive data from form
        class_id = request.GET['id']
        classs = Class.objects.filter(class_id = class_id).first()
        course = Course.objects.filter(course_id = classs.course_id).first()
        teacher = Teacher.objects.filter(teacher_id = classs.teacher_id).first()

        class_location  = request.POST['location']
        class_term      = request.POST['term']



        # TODO data validation
        
        classModified                 = classs
        classModified.class_location  = class_location
        classModified.class_term      = class_term
  
        classModified.save()

        messages.info(request,'Class updated successfully')

        return render(request, 'modifyClass.html', {'class': classModified,'course': course, 'teacher': teacher, 'created': True})  




def chooseClassToDelete(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    all_classes = Class.objects.all()
    return render(request, 'chooseClassToDelete.html', {"classes": all_classes})   # ? maybe change page?  

def deleteClass(request):
    valid = check_user_admin_ok(request)
    if valid != True:
        return valid

    if request.method == 'GET':

        class_id = request.GET['id']
        classs = Class.objects.filter(class_id=class_id).first()
        course = Course.objects.filter(course_id = classs.course_id).first()
        teacher = Teacher.objects.filter(teacher_id = classs.teacher_id).first()

        return render(request, 'deleteClass.html', {'class': classs, 'course': course, 'teacher': teacher})

    else:  # request.method == 'POST
        # receive data from form
        class_id = request.GET['id']
        classs = Class.objects.filter(class_id=class_id).first()
        classs.delete()

        messages.info(request,'Class deleted successfully')

        return render(request, 'deleteClass.html', {'created': True})  