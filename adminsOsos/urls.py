from django.urls import path
from . import views

urlpatterns = [
   path('home', views.home, name= 'home'),

   # * Manage account
   path('manageAccount', views.manageAccount, name= 'manageAccount'),
   path('createAccount', views.createAccount, name= 'createAccount'),
   path('chooseAccountToModify', views.chooseAccountToModify, name= 'chooseAccountToModify'),
   path('modifyAccount', views.modifyAccount, name= 'modifyAccount'),
   path('chooseAccountToDelete', views.chooseAccountToDelete, name= 'chooseAccountToDelete'),
   path('deleteAccount', views.deleteAccount, name= 'deleteAccount'),

   # * Manage mail
   path('manageMail', views.manageMail, name= 'manageMail'),
   path('createMail', views.createMail, name= 'createMail'),
   path('chooseMailToDelete', views.chooseMailToDelete, name= 'chooseMailToDelete'),
   path('deleteMail', views.deleteMail, name= 'deleteMail'),

   # * Manage user
   path('manageUser', views.manageUser, name= 'manageUser'),   
   path('chooseUserTypeToCreate', views.chooseUserTypeToCreate, name= 'chooseUserTypeToCreate'),                  # * Create user 
   path('chooseUntakenAdminAccount', views.chooseUntakenAdminAccount, name= 'chooseUntakenAdminAccount'),
   path('createAdmin', views.createAdmin, name = 'createAdmin'),
   path('chooseUntakenTeacherAccount', views.chooseUntakenTeacherAccount, name= 'chooseUntakenTeacherAccount'),
   path('createTeacher', views.createTeacher, name = 'createTeacher'),
   path('chooseUntakenStudentAccount', views.chooseUntakenStudentAccount, name= 'chooseUntakenStudentAccount'),
   path('createStudent', views.createStudent, name = 'createStudent'),   
   path('chooseUserToModify', views.chooseUserToModify, name= 'chooseUserToModify'),                              # * Modify user
   path('modifyUserAdmin', views.modifyUserAdmin, name= 'modifyUserAdmin'),
   path('modifyUserTeacher', views.modifyUserTeacher, name= 'modifyUserTeacher'),
   path('modifyUserStudent', views.modifyUserStudent, name= 'modifyUserStudent'),
   path('chooseUserToDelete', views.chooseUserToDelete, name= 'chooseUserToDelete'),                              # TODO Delete user
   path('deleteUser', views.deleteUser, name= 'deleteUser'),                                                      # TODO One page for all user types


   path('manageCourse', views.manageCourse, name= 'manageCourse'),
   path('createCourse', views.createCourse, name= 'createCourse'),
   path('chooseCourseToModify', views.chooseCourseToModify, name= 'chooseCourseToModify'),
   path('modifyCourse', views.modifyCourse, name= 'modifyCourse'),
   path('chooseCourseToDelete', views.chooseCourseToDelete, name= 'chooseCourseToDelete'),
   path('deleteCourse', views.deleteCourse, name= 'deleteCourse'),

   path('manageClass', views.manageClass, name= 'manageClass'),
   path('chooseCourseToClass', views.chooseCourseToClass, name= 'chooseCourseToClass'),
   path('chooseTeacherToClass', views.chooseTeacherToClass, name= 'chooseTeacherToClass'),
   path('createClass', views.createClass, name= 'createClass'),
   path('chooseClassToModify', views.chooseClassToModify, name= 'chooseClassToModify'),
   path('modifyClass', views.modifyClass, name= 'modifyClass'),
   path('chooseClassToDelete', views.chooseClassToDelete, name= 'chooseClassToDelete'),
   path('deleteClass', views.deleteClass, name= 'deleteClass'),

   # path('chooseUserToModify', views.chooseUserToModify, name= 'chooseUserToModify'),
   # path('modifyUser', views.modifyUser, name= 'modifyUser'),
   # path('chooseUserToDelete', views.chooseUserToDelete, name= 'chooseUserToDelete'),
   # path('deleteUser', views.deleteUser, name= 'deleteUser'),
   # path('createUser', views.createUser, name= 'createUser'),
   
   # path('createCourse', views.createCourse, name = 'createCourse'),
   # path('createClass', views.createClass, name = 'createClass'),
   # path('chooseUser', views.chooseUser, name= 'chooseUser'),
]

