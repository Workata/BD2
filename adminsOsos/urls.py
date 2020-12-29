from django.urls import path
from . import views

urlpatterns = [
   path('home', views.home, name= 'home'),
   path('createAccount', views.createAccount, name= 'createAccount'),
   path('createMail', views.createMail, name= 'createMail'),
   path('chooseUser', views.chooseUser, name= 'chooseUser'),
   path('createStudent', views.createStudent, name = 'createStudent'),
   path('createTeacher', views.createTeacher, name = 'createTeacher'),
   path('createAdmin', views.createAdmin, name = 'createAdmin'),
]
