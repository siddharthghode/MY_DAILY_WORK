from django.shortcuts import render 
from myapp.models import UserData 

def home(request):
    uname = None

    if request.method == "POST":
        uname = request.POST.get("username")

        if uname:
            obj = UserData(username=uname)
            obj.save()

    return render(request, "home.html", {"usname": uname})


def about(request):
    return render(request, "about.html")


def data(request):
    users = UserData.objects.all()
    return render(request, "data.html", {"users": users})
