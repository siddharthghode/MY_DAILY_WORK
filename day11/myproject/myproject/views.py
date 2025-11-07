from django.shortcuts import render 
from django.http import HttpResponse

def home(request):
    try:
        number1=int(request.GET["num1"])
        number2=int(request.GET["num2"])
        print(number1+number2)
        number_add=number1+number2
    except:
        pass
    return render(request,"home.html",{"result":number_add})

def about(request):
    return render(request,"about.html")