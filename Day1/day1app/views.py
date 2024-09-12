from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer

def home(request):
    return render(request,'home.html')

def newpage(request):
    customer1 =Customer(381,"Tazim","0176969690")
    customer2 = Customer(382,"Jakir", "0187823288")
    customer3 = Customer(320, "Rasel", "0197972397987")
    customer4 =Customer(381,"Tazim","0176969690")
    customer5 = Customer(382,"Jakir", "0187823288")
    customer6 = Customer(320, "Rasel", "0197972397987")
    customer7 =Customer(381,"Tazim","0176969690")
    customer8= Customer(382,"Jakir", "0187823288")
    customer9 = Customer(320, "Rasel", "0197972397987")
    customer10 =Customer(381,"Tazim","0176969690")
    customer11= Customer(382,"Jakir", "0187823288")
    customer12= Customer(320, "Rasel", "0197972397987")
    customers=[customer1,customer2,customer3,customer4,customer5,customer6,customer7,customer8,customer9,customer10,customer11,customer12]
    return render(request,"newpage.html",{'customers':customers})

def result(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1+num2
    re= {'result':result}
    return render(request, 'result.html',re)