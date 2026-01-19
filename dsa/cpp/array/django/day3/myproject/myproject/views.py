from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def about_us(request):
    return HttpResponse("this about us page")