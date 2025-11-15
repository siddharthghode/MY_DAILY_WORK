from django.http import HttpResponse
from django.shortcuts import render 
from myapp.models import UserData 

def home(request):
    uname = None  # default value

    if request.method == "POST":
        try:
            uname = request.POST.get("username")
        except:
            print("didn't get username")

    return render(request,"home.html",{"usname": uname})

def about(request):
    return render(request,"about.html",)

def data(request):
    users = UserData.objects.all()
    return render(request, "data.html", {"users": users})