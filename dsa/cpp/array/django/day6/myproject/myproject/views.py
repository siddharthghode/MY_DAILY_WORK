from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("this is the home page.")

def about(request):
    return render(request, "about.html")