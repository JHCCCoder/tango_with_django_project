from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest):
    context_dict = {
        "boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"
    }

    return render(request, 'rango/index.html', context=context_dict)


def about(request: HttpResponse):
    return HttpResponse('Rango says here is the about page.<a href="/rango/">Index</a>')