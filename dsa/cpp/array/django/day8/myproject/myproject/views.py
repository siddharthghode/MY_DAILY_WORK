from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
    data={
        "title":"Home Page",
        "heading":"Passing data form views to template",
        "languages":["Python","JavaScript","Java","C++","Ruby"],
        "numbers": [1,2,3,4,5,6,7,8,9,10],
        "student_details":[
            {
                'name':'pradeep','phone':12345678
            },
            {
                'name':'siddharth','phone':87654321
            }
        ]
        
    }
    return render(request,"home.html",data)