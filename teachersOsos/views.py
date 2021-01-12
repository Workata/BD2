from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'teacherHome.html')


def seePersonalData(request):
    return render(request, 'teacherPersonalData.html')


def seeMessages(request):
    return render(request, 'teacherMessages.html')


def manageClass(request):
    return render(request, 'manageTeacherClass.html')