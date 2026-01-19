from django.http import HttpResponse
from django.shortcuts import render 
from myapp.models import UserData 

def home(request):
    uname = '' # default value
    umobile = '' # default value
    

    if request.method == "POST":
        try:
            uname = request.POST.get("user_name")
            umobile = request.POST.get("user_mobile")
        except:
            print("didn't get username")

    return render(request,"home.html",{"usname": uname})
