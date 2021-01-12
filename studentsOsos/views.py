from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'studentHome.html')


def seePersonalData(request):
    return render(request, 'studentPersonalData.html')


def seeMessages(request):
    return render(request, 'studentMessages.html')


def seeGrades(request):
    return render(request, 'studentGrades.html')