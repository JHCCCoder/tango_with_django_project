from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest):
    context_dict = {
        "boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"
    }

    return render(request, 'rango/index.html', context=context_dict)

def about(request: HttpRequest):
    return render(request, 'rango/about.html')