from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def newpage(request):
    return HttpResponse("This is new page")

def result(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1+num2
    re= {'result':result}
    return render(request, 'result.html',re)