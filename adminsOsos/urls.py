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
   # path('createUser', views.createUser, name= 'createUser'),
   # path('chooseUserToModify', views.chooseUserToModify, name= 'chooseUserToModify'),
   # path('modifyUser', views.modifyUser, name= 'modifyUser'),
   # path('chooseUserToDelete', views.chooseUserToDelete, name= 'chooseUserToDelete'),
   # path('deleteUser', views.deleteUser, name= 'deleteUser'),

   path('createStudent', views.createStudent, name = 'createStudent'),
   path('createTeacher', views.createTeacher, name = 'createTeacher'),
   path('createAdmin', views.createAdmin, name = 'createAdmin'),
   path('createCourse', views.createCourse, name = 'createCourse'),
   path('createClass', views.createClass, name = 'createClass'),
]
