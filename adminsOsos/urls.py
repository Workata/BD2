from django.urls import path
from . import views

urlpatterns = [
   path('home', views.home, name= 'home'),

   path('manageAccount', views.manageAccount, name= 'manageAccount'),
   path('createAccount', views.createAccount, name= 'createAccount'),
   path('chooseAccountToModify', views.chooseAccountToModify, name= 'chooseAccountToModify'),
   path('modifyAccount', views.modifyAccount, name= 'modifyAccount'),
   path('chooseAccountToDelete', views.chooseAccountToDelete, name= 'chooseAccountToDelete'),
   path('deleteAccount', views.deleteAccount, name= 'deleteAccount'),

   path('manageMail', views.manageMail, name= 'manageMail'),
   path('createMail', views.createMail, name= 'createMail'),
   path('chooseMailToDelete', views.chooseMailToDelete, name= 'chooseMailToDelete'),
   path('deleteMail', views.deleteMail, name= 'deleteMail'),

   
   path('chooseUser', views.chooseUser, name= 'chooseUser'),
   path('manageUser', views.manageUser, name= 'manageUser'),

   # * Create user 
   path('chooseUserTypeToCreate', views.chooseUserTypeToCreate, name= 'chooseUserTypeToCreate'),
   path('chooseUntakenAdminAccount', views.chooseUntakenAdminAccount, name= 'chooseUntakenAdminAccount'),
   path('createAdmin', views.createAdmin, name = 'createAdmin'),
   path('chooseUntakenTeacherAccount', views.chooseUntakenTeacherAccount, name= 'chooseUntakenTeacherAccount'),
   path('createTeacher', views.createTeacher, name = 'createTeacher'),
   path('chooseUntakenStudentAccount', views.chooseUntakenStudentAccount, name= 'chooseUntakenStudentAccount'),
   path('createStudent', views.createStudent, name = 'createStudent'),

   # * Modify user
   path('chooseUserToModify', views.chooseUserToModify, name= 'chooseUserToModify'),
   path('modifyUserAdmin', views.modifyUserAdmin, name= 'modifyUserAdmin'),


   # path('chooseUserToModify', views.chooseUserToModify, name= 'chooseUserToModify'),
   # path('modifyUser', views.modifyUser, name= 'modifyUser'),
   # path('chooseUserToDelete', views.chooseUserToDelete, name= 'chooseUserToDelete'),
   # path('deleteUser', views.deleteUser, name= 'deleteUser'),
   # path('createUser', views.createUser, name= 'createUser'),
   
   path('createCourse', views.createCourse, name = 'createCourse'),
   path('createClass', views.createClass, name = 'createClass'),
]

