from django.shortcuts import render,redirect 
from django.contrib import messages
from myapp.models import UserData 

def home(request):
    user_name = None
    user_mobile = None

    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_mobile = request.POST.get("user_mobile")

        if user_name and user_mobile:
            obj = UserData(
                user_name=user_name,
                user_mobile=user_mobile
            )
            obj.save()
        messages.success(request, "✅ Data saved successfully!")
        return redirect("home") 

    return render(request, "home.html",{"user_name":user_name,"user_mobile":user_mobile})


def about(request):
    return render(request, "about.html")


def data(request):
    users = UserData.objects.all()
    return render(request, "data.html", {"users": users})
