from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data={
        'title_name':'home page site',
        'heading':'welcome to home page'
    }
    return render(request, 'home.html',data)