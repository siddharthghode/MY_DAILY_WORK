from django.http import HttpResponse

def home(requeest):
    return HttpResponse("Welcome to the Home Page")