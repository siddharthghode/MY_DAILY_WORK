# from django.shortcuts import render 
# from django.http import HttpResponse

# def home(request):
#     addition=None
#     # try:
#     #     number_a = int(request.GET.get('number1'))
#     #     number_b = int(request.GET.get('number2'))
#     #     addition = number_a + number_b
#     # except:
#     #     pass
#     try:
#        if request.method=='POST':
#            n1=int(request.POST.get('number1'))
#            n2=int(request.POST.get('number2'))
#            addition=n1+n2
#     except:
#         pass       
#     return render(request,"home.html",{'add':addition})

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    addition = None  # Initialize variable
    
    if request.method == 'POST':   # Check request type first
        try:
            n1 = int(request.POST.get('number1', 0))
            n2 = int(request.POST.get('number2', 0))
            addition = n1 + n2
        except (TypeError, ValueError):
            addition = "Invalid input. Please enter numbers only."
    
    return render(request, "home.html", {'add': addition})
