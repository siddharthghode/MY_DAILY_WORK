from django.http import HttpResponse
from django.shortcuts import render
 
def home(request):
    addition=0
    try:
        num1=int(request.GET['number1'])
        num2=int(request.GET['number2'])
        addition=num1+num2
        # print(num1+num2)
    except:
        pass
    # return render(request,"home.html",{'plus_values':adition})
    return render(request,"home.html",{'value':addition})

def about(request):
    return render(request,"about.html")