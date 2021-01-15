from django.urls import path
from . import views

urlpatterns = [
   path('home', views.home, name= 'home'),

   # * Personal data
    path('yourPersonalData', views.seePersonalData, name= 'yourPersonalData'),

    # * Messages
    path('yourMessages', views.seeMessages, name= 'yourMessages'),

    # * Class panel
    path('manageClass', views.manageClass, name= 'manageClass'),

    path('classManager', views.classManager, name= 'classManager'),

]
