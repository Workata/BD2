from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name= 'home'),

    # * Personal data
    path('yourPersonalData', views.seePersonalData, name= 'yourPersonalData'),

    # * Messages
    path('yourMessages', views.seeMessages, name= 'yourMessages'),

    # * Grades
    path('yourGrades', views.seeGrades, name= 'yourGrades'),

]
